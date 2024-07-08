from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded."}), 400

    file = request.files['image']

    # Read the file and convert it to a base64 string
    file_content = file.read()
    base64_image = base64.b64encode(file_content).decode('utf-8')

    # Log the base64 encoded string
    print(base64_image)

    return jsonify({"message": "Image received and logged."})

if __name__ == '__main__':
    app.run(port=3000)
