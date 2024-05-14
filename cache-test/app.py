from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/data')
def get_data():
    # Simulate fetching data (e.g., from a database or external service)
    data = {"message": "This is cached data"}

    # Create a response object from the data
    response = make_response(jsonify(data))
    
    # Set cache control headers
    response.headers['Cache-Control'] = 'public, max-age=300'  # Cache for 5 minutes
    response.headers['Expires'] = 'Sun, 17 Jul 2022 23:00:00 GMT'  # Example static expiration date

    return response

if __name__ == '__main__':
    app.run(debug=True)