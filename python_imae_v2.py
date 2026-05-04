import webview
import time

TARGET_URL = 'https://njk122.github.io/exam_portal/'

# A simple, clean loading screen
LOADING_HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            background-color: #ffffff; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            height: 100vh; 
            margin: 0; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .loader {
            border: 8px solid #f3f3f3;
            border-top: 8px solid #3498db;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        h2 { color: #333; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="loader"></div>
    <h2>Exam portal is loading...</h2>
    <p>Please wait while we secure your environment.</p>
</body>
</html>
"""

def load_logic(window):
    # Give the user a second to actually see the loading screen
    time.sleep(4) 
    # Redirect to the actual exam
    window.load_url(TARGET_URL)

def start_portal():
    # Start the window with the local HTML instead of the URL
    window = webview.create_window(
        title='Exam portal by Nilav',
        html=LOADING_HTML, # Initialize with the loader
        fullscreen=True,
        on_top=False,
        confirm_close=True,
        background_color='#ffffff'
    )
    
    # Use the 'start' function to trigger the redirect logic
    webview.start(load_logic, window)

if __name__ == '__main__':
    start_portal()