import os
import json
import requests
import time
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# --- Configuration ---
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'static/results'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
AI_API_URL = 'https://api.aiforthai.in.th/face-blur'
AI_API_KEY = 'YOUR_API_KEY_HERE'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_and_blur_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file selected.")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected.")

        if file and allowed_file(file.filename):
            original_filename = secure_filename(file.filename)
            original_filepath = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
            file.save(original_filepath)

            try:
                if original_filename.lower().endswith(('.jpg', '.jpeg')):
                    mime_type = 'image/jpeg'
                else:
                    mime_type = 'image/png'

                with open(original_filepath, 'rb') as image_file:
                    files = {'file': (original_filename, image_file, mime_type)}
                    headers = {'Apikey': AI_API_KEY}
                    response = requests.post(AI_API_URL, headers=headers, files=files)

                if response.status_code == 200:
                    api_data = response.json()
                    blurred_url = api_data.get('URL')
                    
                    image_response = requests.get(blurred_url)
                    if image_response.status_code == 200:
                        timestamp = str(int(time.time()))
                        unique_filename = f"{timestamp}_{original_filename}"
                        result_filepath = os.path.join(app.config['RESULT_FOLDER'], unique_filename)
                        
                        with open(result_filepath, 'wb') as f:
                            f.write(image_response.content)
                        
                        # The line below that deletes the file is now removed.
                        # os.remove(original_filepath) # <-- CHANGE
                        
                        return render_template('index.html', blurred_image=unique_filename)

            except Exception as e:
                print(f"An error occurred: {e}")
                # Also removed the delete command from the error section.
                # if os.path.exists(original_filepath):
                #     os.remove(original_filepath) # <-- CHANGE
                return render_template('index.html', error="An API error occurred.")
    
    return render_template('index.html', blurred_image=None)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(RESULT_FOLDER, exist_ok=True)
    app.run(debug=True)