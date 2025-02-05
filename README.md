# hng-stage1-task
# Number Classification API

A RESTful API that takes an integer as input and returns interesting mathematical properties along with a fun fact. It checks if the number is prime, perfect, Armstrong (narcissistic), determines its parity, calculates the digit sum, and fetches a math-related fun fact.

## API Specification

### Endpoint

GET `/api/classify-number?number=<integer>`

### Success Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)

Example: GET `/api/classify-number?number=alphabet`

```json
{
    "number": "alphabet",
    "error": true
}
```

## Technology Stack

- Programming Language: Python
- Framework: Flask
- Dependencies: Flask, flask-CORS, requests
- External API: Numbers API (for fun facts)

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/hng-stage1-task.git
   cd hng-stage1-task
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *(Alternatively: pip install Flask flask-CORS requests)*

4. Run the application locally:

   ```bash
   python main.py
   ```

5. The API will be accessible at:
   [http://127.0.0.1:5000/api/classify-number?number=371](http://127.0.0.1:5000/api/classify-number?number=371)

## Configuration

Set configuration constants in `app.py`:

- `NUMBERS_API_BASE_URL`: Base URL for the Numbers API.
- `DEBUG_MODE`: Controlled by the `DEBUG` environment variable (default is True).

## Deployment

Consider deploying on platforms such as Heroku, Render, or AWS Elastic Beanstalk. Ensure proper environment variable handling and debug mode settings.

## Testing

- Valid Input: Confirm that valid integers return the correct JSON response.
- Invalid Input: Verify that non-integer values return a 400 error with the appropriate message.
- Performance: Ensure response times remain under 500ms under normal conditions.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Numbers API for providing fun math facts.
- Flask and flask-CORS for enabling fast API development.

---

### Notes

- Replace `<your-username>` and `<your-domain.com>` with your actual details.
- Run `pip freeze > requirements.txt` to update dependencies if needed.
