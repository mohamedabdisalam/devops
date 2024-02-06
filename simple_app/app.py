# file: app.py
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
import os


app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads') # Constructs path to the folder needed, joins the path using os.path.join
app.config['UPLOAD_FOLDER'] = upload_folder # Sets configuration variable for Upload_folder in flask app 

@app.route('/', methods=['GET']) # For home route
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST']) # For uploading files
def upload_file():
    if request.method == 'POST':
        file = request.files['img'] # Retrieves file from POST request - ORIGINAL FILE
        if file:
            filename = secure_filename(file.filename) # Secures filename to prevent directory attacks   
            file_path = os.path.join(upload_folder, filename) # Construct full file path static/uploads/<image name>
            file.save(file_path) # Saves file to correct filepath
            img = file_path # Constructs URL for image file 
            return render_template('index.html', img=img)
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    app.run(host='0.0.0.0', debug=True)
    # need to set host so other IPs addresses can access
    #default port is 5000. Otherwise need to specify it