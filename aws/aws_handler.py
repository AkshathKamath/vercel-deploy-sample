import boto3
from dotenv import load_dotenv
import os
import io
import matplotlib.pyplot as plt

def aws_work():
    load_dotenv()

    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY_ID')
    AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME_ID')
    AWS_REGION = os.getenv('AWS_REGION_ID')

    S3_NAME = 'dummy.png'

    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.title('Sample Plot')
    # Save plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)  # Rewind the buffer

    s3_client = boto3.client(
        service_name = 's3',
        region_name = AWS_REGION,
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_KEY
    )

    response = s3_client.upload_fileobj(buf, AWS_S3_BUCKET_NAME, S3_NAME)

    return f"Img Upload Successful with response: {response}"