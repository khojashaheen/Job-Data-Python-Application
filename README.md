1. This Project retrieves job data from the following API web page  (https://www.themuse.com/developers/api/v2)
2. It then processes by extracting relevant information and transforms the json data into a pandas dataframe
3. Finally, it uploads the csv data into Amazon S3 Bucket using Boto3 (AWS SDK for Python) and AWS credentials, stored in the .env file
