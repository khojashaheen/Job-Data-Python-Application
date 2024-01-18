1. This Project retrieves job data from the following API web page  (https://www.themuse.com/developers/api/v2)
2. It then transforms the json data into a pandas dataframe
3. Finally, it uploads the csv data into Amazon S3 Bucket using boto3 library and AWS credentials, stored in the .env file

