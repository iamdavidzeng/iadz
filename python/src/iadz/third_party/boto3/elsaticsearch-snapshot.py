import boto3
import requests
from requests_aws4auth import AWS4Auth

host = ""  # e.g. your amazon aws service url
region = ""  # e.g. ap-southeast-1
service = "es"
credentials = boto3.Session().get_credentials()
aws_auth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    region,
    service,
    session_token=credentials.token,
)

# Register repository
path = "_snapshot/{your-snapshot-repo}"  # e.g. s3_repository
url = host + path

payload = {
    "type": "s3",
    "settings": {
        "bucket": "{your-s3-bucket}",
        "region": "{your-region}",
        "role_arn": "{your-role-arn}",
    },
}

headers = {"Content-Type": "application/json"}

response = requests.put(url, auth=aws_auth, json=payload, headers=headers)

print(response.status_code)
print(response.text)
