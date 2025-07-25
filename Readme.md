AI Face Blur Web App 🤖 A simple web application built with Python and Flask that uses the AI for Thai API to automatically detect and blur faces in an uploaded image. Users can upload a JPG or PNG file, and the app will return a new image with the detected faces blurred.

📸 Screenshot (You should replace placeholder.png with a real screenshot of your application.)

✨ Features Simple Web UI: Clean and modern interface for uploading images.

Responsive Design: Works on desktop, tablets, and mobile devices.

AI-Powered: Uses a robust API for accurate face detection and blurring.

Loading Indicator: Shows a spinner while the image is being processed.

File Handling: Accepts .jpg and .png formats and saves results with a unique filename.

💻 Technologies Used Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

API: AI for Thai - Face Blur

🚀 Getting Started Follow these instructions to get the project running on your local machine.

Clone the Repository First, clone the repository to your local machine.
Bash

git clone https://github.com/your-username/your-repository-name.git cd your-repository-name 2. Install Dependencies It is highly recommended to use a virtual environment.

Bash

Create and activate a virtual environment
python -m venv venv source venv/bin/activate # On Windows, use: venv\Scripts\activate

Install the required packages
pip install Flask requests 3. Configure Your API Key You need an API key from AI for Thai to use the service.

Register and get your key from the AI for Thai website.

Open the app.py file.

Find this line and replace the placeholder with your actual key:

Python

AI_API_KEY = 'YOUR_API_KEY_HERE' 4. Run the Application Execute the following command in your terminal:

Bash

python app.py The application will start, and you can access it by opening your web browser and navigating to http://127.0.0.1:5000.

📂 Project Structure . ├── app.py # Main Flask application ├── static/ │ └── results/ # Stores the blurred images ├── templates/ │ └── index.html # Frontend HTML and CSS └── uploads/ # Stores original uploaded images 📄 License This project is licensed under the MIT License. See the LICENSE file for details.