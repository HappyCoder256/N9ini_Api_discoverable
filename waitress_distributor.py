from waitress import serve
from n9ini_api import app  # Your Flask app

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000, threads=100)
