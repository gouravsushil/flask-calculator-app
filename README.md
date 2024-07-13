# Flask Calculator Project

## Description

This is a web application built using Flask and Bootstrap that provides two calculators: a simple calculator and an advanced calculator. The simple calculator supports basic arithmetic operations like addition, subtraction, multiplication, and division. The advanced calculator offers trigonometric functions, logarithmic functions, and a square root function. The application features multiple routes to the home page, the simple calculator page, and the advanced calculator page.

## Installation Instructions

1. **Clone the repository or extract the provided zip file**:
  
   git clone https://github.com/gouravsushil/flask-calculator-app.git
   cd flask-calculator-app
 

2. **Create a virtual environment (optional but recommended)**:
   python -m venv .venv
  

3. **Activate the virtual environment**:
   - On Windows:
     .venv\Scripts\activate
    
   - On macOS/Linux:
     source .venv/bin/activate

4. **Install the dependencies**:
   pip install -r requirements.txt

## Usage Instructions

1. **Run the Flask application**:
   python index.py

2. **Open your web browser and go to `http://127.0.0.1:8000`**.

3. **Use the calculator**:
   - Navigate to the simple calculator: `http://127.0.0.1:8000/simple`
   - Navigate to the advanced calculator: `http://127.0.0.1:8000/advanced`

## Project Structure


flask_calculator/
├── index.py                # Main Flask application script
├── templates/
│   ├── index.html        # base html
│   ├── home.html        # Home page
│   ├── simple.html       # Simple calculator page
│   ├── advanced.html     # Advanced calculator page
├── static
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
├── vercel.json           
└── .venv/                # Virtual environment (optional, if included)


## Routes

- `/home`: Home page with links to both calculators.
- `/simple`: Simple calculator page.
- `/advanced`: Advanced calculator page.

## Features

- **Simple Calculator**: 
  - Addition
  - Subtraction
  - Multiplication
  - Division

- **Advanced Calculator**:
  - Trigonometric functions (sin, cos, tan)
  - Logarithmic function
  - Exponential function
  - Square root function

