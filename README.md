# prog-5-ussd Project

## Overview
The `prog-5-ussd` project is a USSD application that provides users with access to account information and services through a simple menu-driven interface. The application is designed to be user-friendly and efficient, allowing users to quickly navigate through options to manage their accounts.

## Setup Instructions
To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/prog-5-ussd.git
   cd prog-5-ussd
   ```

2. **Create a Virtual Environment**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guidelines
To run the application, execute the following command:
```bash
python src/main.py
```
Follow the prompts in the terminal to navigate through the menus and access account information or services.

## Linting
This project uses Flake8 for linting. To run the linter manually, use the following command:
```bash
flake8 src/
```
Ensure that your code adheres to the style guidelines specified in the `.flake8` configuration file.

## Continuous Integration
The project is configured with GitHub Actions to automatically run the linter on each push. If any linting errors are detected, the job will fail, ensuring code quality is maintained.

## Documentation
For detailed information on the naming conventions used in this project, please refer to the `docs/NAMING_CONVENTIONS.md` file.