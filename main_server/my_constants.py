from flask import Flask

UPLOAD_FOLDER = r"C:\Users\Nijat\Desktop\diplomishi\main\upload"
DOWNLOAD_FOLDER = r"C:\Users\Nijat\Desktop\diplomishi\main\download"

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['BUFFER_SIZE'] = 64 * 1024
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
