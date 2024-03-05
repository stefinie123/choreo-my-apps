from flask import Flask, Response, render_template
import time
import json

app = Flask(__name__)

def generate_random_data():
    """
    This function simulates real-time data.
    It could be replaced with actual logic to fetch or stream real-time data.
    """
    while True:
        json_data = json.dumps({'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'value': time.time()})
        yield f"data:{json_data}\n\n"
        time.sleep(1)  # Simulate real-time delay

@app.route('/stream')
def stream():
    """
    This route streams the data to the client using SSE.
    """
    return Response(generate_random_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
