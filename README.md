Simple Cloud-Based File Uploader

📁 Project Overview

This project is a simple yet powerful web application that allows users to upload files through a clean web interface, with secure storage on AWS S3 Cloud.
It is built with Python (Flask) for the backend and uses boto3 for AWS integration.

✅ Key Features

Upload files from your local system via a simple web form
Automatically store uploaded files in AWS S3
Real-time success confirmation
Clean, responsive front-end design

🛠️ Technologies Used

Python (Flask) — for backend development
HTML & CSS — for the front-end
AWS S3 — for cloud storage
boto3 — Python SDK for AWS
Git & GitHub — for version control

🌐 Project Structure

FileUploader/
│
├── app.py
├── config.py (not included in repo)
├── static/
│   └── style.css
└── templates/
    └── index.html
    
⚙️ Setup Instructions

1. Clone the repository
git clone https://github.com/shivangi-5057/simple-file-uploader.git
cd simple-file-uploader
2. Install required packages
pip install flask boto3
3. Add your AWS credentials in a config.py file (not included in the repository)
AWS_ACCESS_KEY = 'your-aws-access-key'
AWS_SECRET_KEY = 'your-aws-secret-key'
BUCKET_NAME = 'your-s3-bucket-name'
REGION = 'your-region'  # Example: 'ap-south-1'
4. Run the application
python app.py
5. Open your browser
Visit http://127.0.0.1:5000/ and upload a file!

💡 Future Improvements (Optional)

Add file type restrictions and size limits
Display uploaded files list
Deploy the app using Render or Heroku for live demonstration
🔒 Security Notice

This project uses a config.py file to securely store AWS keys and bucket information. Please make sure this file is never pushed to GitHub or exposed publicly.

⭐ Conclusion

This project demonstrates cloud integration with AWS S3, backend handling with Flask, and a simple UI for file uploads. It’s a great showcase of backend-cloud communication and secure file handling for beginner to intermediate-level portfolios.
