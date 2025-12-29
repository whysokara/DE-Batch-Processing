import boto3
import os

## Config
BUCKET_NAME = "s3kara-batch"
S3_FOLDER = "bronze"
LOCAL_FILE_PATH = "/Users/kara/Desktop/batch/data/behaviour_metrics.csv"

## Extract file name
file_name = os.path.basename(LOCAL_FILE_PATH)
s3_key = f"{S3_FOLDER}/{file_name}"

# Create s3 client
s3 = boto3.client("s3")

# Upload file
s3.upload_file(
    Filename=LOCAL_FILE_PATH,
    Bucket=BUCKET_NAME,
    Key=s3_key
)

print(f"Uploaded {LOCAL_FILE_PATH} to s3://{BUCKET_NAME}/{s3_key}")