# Movie Management System

This is a Python web application built with the `Bottle` framework. It allows users to manage a collection of movies, including viewing, adding, and deleting films. The application uses an SQLite database (`movies5.db`) to store movie data and user credentials.

## Features
- **User Authentication**: 
  - Users can log in with a username and password.
  - Session management is implemented using cookies to track the user's login status.
- **Add Movies**: Allows users to add new movies to the database, including details such as title, description, release year, length, and category.
- **Delete Movies**: Enables users to delete movies from the database by providing the movie's ID.
- **Logout**: Users can log out, which clears their session cookies.

## Dependencies
- Python 3.x
- `Bottle` framework
- SQLite database (`movies5.db`)

## How to Run the Application
1. **Clone the Repository**: 
Clone this repository to your local machine using Git or download it as a ZIP file.
2. **Install Dependencies**: 
Make sure you have Python installed. You can install the required dependencies using pip:
   ```bash
   pip install bottle
   ```
3. **Set Up the Database**: 
Ensure that the SQLite database file (`movies5.db`) is present in the same directory as the application. If not, you may need to create it or copy it from another location.
4. **Run the Application**: 
Open a terminal or command prompt, navigate to the directory where the application is located, and run the following command:
   ```bash
   python bottle_app.py
   ```
5. **Access the Application**:
Open a web browser and navigate to `http://localhost:8080`.
    The application will be running on port 8080 by default.

