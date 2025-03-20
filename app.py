from flask import Flask, request, render_template
import boto3
import config

app = Flask(__name__)

# Add your AWS credentials and bucket details here:
AWS_ACCESS_KEY = config.AWS_ACCESS_KEY
AWS_SECRET_KEY = config.AWS_SECRET_KEY
BUCKET_NAME = config.BUCKET_NAME
REGION = config.REGION  # Example: 'ap-south-1'

# Create an S3 client using boto3
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        return f"File '{file.filename}' uploaded successfully to AWS S3!"
    return "No file selected."

if __name__ == '__main__':
    app.run(debug=True)
