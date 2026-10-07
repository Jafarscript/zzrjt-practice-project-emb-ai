from flask import Flask
print("Python is reading this file!")

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!"

if __name__ == "__main__":
    print("Launching test server...")
    app.run(port=5001, debug=True)
