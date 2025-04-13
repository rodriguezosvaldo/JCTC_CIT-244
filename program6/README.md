# Payroll Management System

This is a Python web application built with the `Bottle` framework and styled with Bootstrap. It allows users to manage payroll data, including viewing employee details by department and editing employee hours. The application uses an SQLite database (`payroll.db`) to store employee and payroll data.

## Features
- **Home Page**: 
  - A simple landing page that assumes the user is already logged in for educational purposes.
- **View Payroll by Department**: 
  - Users can select a department to view employee details, including ID, name, wage, hours worked, and weekly pay.
  - Weekly pay is calculated dynamically, including overtime pay for hours worked over 40.
- **Edit Employee Hours**: 
  - Users can update the hours worked for a specific employee by providing their ID and the new hours worked.
- **Request Status**: 
  - Displays a confirmation message after successfully updating an employee's hours.

## Dependencies
- Python 3.x
- `Bottle` framework
- SQLite database (`payroll.db`)

## How to Run the Application
1. **Clone the Repository**: 
   Clone this repository to your local machine using Git or download it as a ZIP file.
2. **Install Dependencies**: 
   Make sure you have Python installed. You can install the required dependencies using pip:
   ```bash
   pip install bottle
   ```
3. **Run the Application**: 
   Navigate to the directory where the application files are located and run the following command:
   ```bash
   python bottle_app.py
   ```
4. **Access the Application**: 
   Open your web browser and go to `http://localhost:8080` to access the application.

## Notes:
- The application assumes that the user is already logged in for educational purposes. 
