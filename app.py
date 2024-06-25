# import os
from flask import Flask
# import boto3
# from dotenv import load_dotenv

app = Flask(__name__)

# load_dotenv()

# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
# AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
# AWS_REGION = os.getenv('AWS_REGION')

# LOCAL_FILE = './images/dummy_img.png'
# S3_NAME = os.getenv('dummy.png')

@app.route('/', methods=['GET'])
def func_1():
    return "hello"

# @app.route('/demo', methods=['GET'])
# def demo_func():
#     s3_client = boto3.client(
#         service_name = 's3',
#         region_name = AWS_REGION,
#         aws_access_key_id = AWS_ACCESS_KEY,
#         aws_secret_access_key = AWS_SECRET_KEY
#     )

#     response = s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET_NAME, S3_NAME)

#     return f"Img Upload Successful with response: {response}"


@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404

if __name__ == '__main__':
    app.run(debug=True)