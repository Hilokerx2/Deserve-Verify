from flask import Flask, jsonify

app = Flask(__name__)

# เส้นทางหลัก
@app.route('/')
def home():
    return "Welcome to the Flask server!"

# เส้นทาง server_on
@app.route('/server_on')
def server_on():
    return jsonify({"status": "Server is running!"})

if __name__ == '__main__':
    app.run(debug=True)
