# Login System Simulation

This project simulates a basic login system, demonstrating core concepts such as user registration, authentication, and session management. It is intended for educational purposes and is not recommended for production use without further security enhancements.

## Features

- **User Registration:** New users can sign up with a username and password.
- **User Authentication:** Registered users can log in with their credentials.
- **Session Simulation:** System tracks logged-in users (session handling may be in-memory or cookie-based).
- **Password Security:** Passwords are hashed before storage (for demonstration, uses a simple hash).
- **Error Handling:** Basic feedback for invalid login attempts or duplicate registrations.

## Technologies Used

- Programming Language: Python
- 
### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) 
- Install dependencies:
  ```bash
  pip install flask bcrypt
  # or
  npm install express bcryptjs
  ```

### Running the Simulation

1. Clone this repository:
   ```bash
   git clone https://github.com/malish-web/login-system-simulation.git
   cd login-system-simulation
   ```
2. Start the server:
   - **Python (Flask):**
     ```bash
     python app.py
     ```
   - **Node.js (Express):**
     ```bash
     node app.js
     ```
3. Open your browser and visit [http://localhost:5000](http://localhost:5000) 

### Usage

- Register a new account on the Registration page.
- Log in using your credentials.
- See login success/failure messages.
- Log out to end the session.

## Security Notice

This simulation is for educational purposes only:
- Passwords are not stored securely enough for real-world use.
- No protection against brute force attacks or common vulnerabilities.
- Sessions may be handled in-memory, which is reset on server restart.

## License

[MIT License](LICENSE)

## Author

[MALISH EMMANUEL ABUI](https://github.com/malish-web)
