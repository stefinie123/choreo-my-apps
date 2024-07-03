
## Requirements

- Python 3.x
- Flask
- A web browser or API testing tool (e.g., Postman, curl)

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Create a virtual environment:

python -m venv venv


4. Activate the virtual environment:

- On Windows:

  ```
  .\venv\Scripts\activate
  ```

- On Unix or MacOS:

  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:

pip install -r requirements.txt

## Running the API

1. Start the Flask application:

python app.py

2. The API is now running on `http://localhost:5000`.

## Using the API

Example using curl:

curl "http://localhost:5000/stream"

Response:

```json

```