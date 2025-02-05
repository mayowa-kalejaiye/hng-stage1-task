import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

# Configuration Constants
NUMBERS_API_BASE_URL = "http://numbersapi.com"
DEBUG_MODE = os.environ.get('DEBUG', 'True') == 'True'

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Utility Functions

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if n is a perfect number."""
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if n is an Armstrong (narcissistic) number."""
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)

def get_custom_armstrong_fact(n):
    """
    Generate a custom fun fact for Armstrong numbers.
    Example: '371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371'
    """
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    fact_parts = " + ".join(f"{d}^{power}" for d in digits)
    return f"{n} is an Armstrong number because {fact_parts} = {n}"

def get_fun_fact(n):
    """
    Retrieve a fun fact for the number n.
    For Armstrong numbers, a custom fun fact is generated.
    Otherwise, the fun fact is fetched from the Numbers API (using the math type).
    """
    if is_armstrong(n):
        return get_custom_armstrong_fact(n)
    try:
        response = requests.get(f"{NUMBERS_API_BASE_URL}/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "")
        return ""
    except requests.RequestException:
        return ""

# API Route

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """
    GET /api/classify-number?number=<number>
    
    Returns a JSON object with the following properties if the number is valid:
    {
        "number": <number>,
        "is_prime": <boolean>,
        "is_perfect": <boolean>,
        "properties": ["armstrong", "odd"] or ["armstrong", "even"] or ["odd"] or ["even"],
        "digit_sum": <sum of digits>,
        "fun_fact": <fun fact string>
    }
    
    For invalid inputs, returns:
    {
        "number": <input>,
        "error": true
    } with HTTP 400.
    """
    num_str = request.args.get('number')

    # Input validation: try converting input to integer.
    try:
        num = int(num_str)
    except (ValueError, TypeError):
        return jsonify({
            "number": num_str,
            "error": True
        }), 400

    # Determine the properties.
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 else "even")

    # Calculate the digit sum (using absolute value to ignore any '-' sign).
    digit_sum = sum(int(d) for d in str(abs(num)))

    # Build the JSON response.
    response_data = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": get_fun_fact(num)
    }
    return jsonify(response_data), 200

# Entry point
# if __name__ == '__main__':
#     app.run(debug=DEBUG_MODE)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=DEBUG_MODE)

