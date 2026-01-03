## Authentication System

### Features
- User Registration
- User Login
- User Logout
- Profile Management (username & email)

### How It Works
- Django built-in authentication handles login/logout securely.
- Custom registration form extends UserCreationForm.
- Profile page allows authenticated users to update their details.

### URLs
- /login/ – Login page
- /logout/ – Logout page
- /register/ – Registration page
- /profile/ – Profile management

### Testing Instructions
1. Register a new user.
2. Log in using the created credentials.
3. Access /profile/ and update user info.
4. Log out and confirm session ends.
