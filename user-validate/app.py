from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/validate-user', methods=['GET'])
def validate_phone_number():
    # Extract phone number from query parameters
    phone_number = request.args.get('phone_number', '')

    # Regular expression to match Sri Lankan phone numbers
    pattern = r'^0\d{9}$'
    if re.match(pattern, phone_number):
        result = {"valid": True, "message": "Valid Sri Lankan phone number."}
    else:
        result = {"valid": False, "message": "Invalid Sri Lankan phone number."}
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()
