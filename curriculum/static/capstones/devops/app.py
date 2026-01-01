from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Use an Environment Variable (Best Practice)
    target = os.environ.get('TARGET', 'World')
    return f'Hello {target}! This is Version 1.0 (Deployed via Cloud Build)'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
