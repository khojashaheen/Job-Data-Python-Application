# Job-Data-Python-Application

## Overview
1. This application retrieves job data from the following API web page  (https://www.themuse.com/developers/api/v2)
2. It then processes by extracting relevant information, transforms the json data into a pandas dataframe, and stores it as csv file locally
3. Finally, it uploads the csv data into Amazon S3 Bucket using Boto3 (AWS SDK for Python) and AWS credentials



![WeCloudDataProjectsJobData](https://github.com/khojashaheen/job-data-to-s3-python-project/assets/132402838/56c2581c-6099-41e5-9a76-c9ebfde8fa45)


## Pre-requisites:
- AWS Account: Sign up for an [AWS Account](https://aws.amazon.com/)
- Python 3.7+: Download and install Python 3.7+

## Installation:
### 1. Clone the Repository:
	Use git clone https://github.com/khojashaheen/Job-Data-Python-Application to clone this repository to your local machine.

### 2. Complete Pre-requisites Steps

### 3. Create .env file to store AWS credentials, as follows:
    access_key=<Your ACCESS KEY>
    secret_access_key=<Your SECRET ACCESS KEY>

### 4. Create a virtual environmment:
    pip install virtualenv
    python<version> -m venv <virtual-environment-name>
    source <virtual-environment-name>/bin/activate
        
### 5 Install packages and dependencies: 
    pip install -r requirements.txt

### 6. Run the application:
    python main.py
