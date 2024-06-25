from flask import Flask
from aws.aws_handler import aws_work


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

@app.route('/demo', methods=['GET'])
def demo_func():
    return aws_work()


@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404

if __name__ == '__main__':
    app.run(debug=True)