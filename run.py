from waitress import serve
from app import app

print("Starting Arthsanchay Growth Fund website on http://127.0.0.1:8080 ...")
serve(app, host='0.0.0.0', port=8080)
