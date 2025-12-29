import os
import boto3

BUCKET_NAME = "s3kara-batch"
LOCAL_DATA_DIR = "../data"
BRONZE_PREFIX = "bronze"

s3 = boto3.client("s3")

for file in os.listdir(LOCAL_DATA_DIR):
    if not file.endswith(".csv"):
        continue

    local_file_path = os.path.join(LOCAL_DATA_DIR, file)
    s3_key = f"{BRONZE_PREFIX}/{file}"

    s3.upload_file(
        Filename=local_file_path,
        Bucket=BUCKET_NAME,
        Key=s3_key
    )

    print(f"Uploaded {file} → s3://{BUCKET_NAME}/{s3_key}")
