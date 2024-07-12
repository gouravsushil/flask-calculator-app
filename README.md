# Flask Calculator App

Welcome to the Flask Calculator App! This application is designed to provide two types of calculators: a Simple Calculator for basic arithmetic operations and an Advanced Calculator with trigonometric, square root, logarithmic, and exponential functions. The app also features seamless navigation between the home page, simple calculator page, and advanced calculator page, utilizing Bootstrap for a responsive and user-friendly interface.

## Features

### Simple Calculator
- Addition
- Subtraction
- Multiplication
- Division

### Advanced Calculator
- Trigonometric functions (sine, cosine, tangent, etc.)
- Square root function
- Logarithmic functions
- Exponential functions

### Navigation
- Home Page
- Simple Calculator Page
- Advanced Calculator Page

## Technologies Used
- Flask: A micro web framework for Python.
- Bootstrap: A front-end framework for responsive and modern web design.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gouravsushil/flask-calculator-app.git
   cd flask-calculator-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   flask run
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## File Structure

```
flask-calculator-app/
│
├── index.py                # Main application file
├── templates/
│   ├── index.html         # Base template
│   ├── home.html        # Home page template
│   ├── simple.html      # Simple calculator page template
│   ├── advanced.html     # Advanced calculator page template
├── requirements.txt      # List of dependencies
└── README.md             # This README file
```

## Usage

1. **Home Page:**
   - Provides links to both the Simple Calculator and Advanced Calculator.

2. **Simple Calculator:**
   - Perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

3. **Advanced Calculator:**
   - Access a variety of advanced mathematical functions including trigonometric, square root, logarithmic, and exponential functions.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Calculating! If you have any questions or feedback, feel free to reach out.