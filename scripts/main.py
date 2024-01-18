import requests
import toml
import numpy as np
import pandas as pd
import boto3
import os
from dotenv import load_dotenv


def read_api(url):
    """
    Reads the API and returns the response
    """
    print("Reading the API...")
    response = requests.get(url)
    return response

def process_response(response, output_file_path):
    print("processing response")
    json_response = response.json()

    company_list = []
    location_list = []
    job_list = []
    job_type_list = []
    publication_date_list = []

    for i in range(len(json_response["results"])):
        company_list.append(json_response["results"][i]["company"]["name"])
        location_list.append(json_response["results"][i]["locations"][0]["name"])
        job_list.append(json_response["results"][i]["name"])
        job_type_list.append(json_response["results"][i]["type"])
        publication_date_list.append(json_response["results"][i]["publication_date"][:10])

    my_array = np.array([company_list,location_list,job_list,job_type_list,publication_date_list])


    df = pd.DataFrame({'company': my_array[0], 'location': my_array[1],'job': my_array[2],'job_type': my_array[3],'publication_date': my_array[4] })
    df["city"] = df["location"].str.split(",").str[0]
    df["country"] = df["location"].str.split(",").str[1]
    df.drop("location", axis=1, inplace=True)

    # save the dataframe to a csv file locally first
    df.to_csv(output_file_path, index=False)


def upload_to_s3(source, bucket, destination):
    print("uploading to AWS S3...")
    load_dotenv()
    access_key = os.getenv("access_key")
    secret_access_key = os.getenv("secret_access_key")

    s3_client = boto3.client(
        "s3", aws_access_key_id=access_key, aws_secret_access_key=secret_access_key
    )
    s3_client.upload_file(source, bucket, destination)
    print("File uploading Done!")


# main function
if __name__ == "__main__":
    file_path = "../data/output_jobs.csv"
    app_config = toml.load("../config/config.toml")
    url = app_config["api"]["url"]
    bucket = app_config["aws"]["bucket"]
    folder = app_config["aws"]["folder"]
    output_file_path = app_config["aws"]["output_file_path"]
    
    response = read_api(url=url)
    process_response(response=response,output_file_path=file_path )
    upload_to_s3(source = file_path, bucket = bucket,destination = folder+output_file_path)
