# Django Employee Management System

Django Employee Management System is a web application built with Django that allows organizations to manage their employee information. It provides a centralized platform for HR teams to keep track of employee details, including personal information, job roles, salary, department, hiring date and contact information.

## Features

- **User Authentication:** Secure login and registration system for authorized access.
- **Employee CRUD Operations:** Create, Read, Update, and Delete employee records.
- **Role-based Access Control:** Different roles such as Admin and HR with specific permissions.
- **Responsive Design:** Ensures a consistent user experience across different devices.

## Prerequisites

Make sure you have the following installed before running the application:

- Python 3.x
- Django (latest version)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Prasad981998/EmployeeManagementSystem.git
    ```

2. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Create a superuser for initial access:

    ```bash
    python manage.py createsuperuser
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to log in with the superuser credentials and manage employees.

## Usage

- Log in with the superuser credentials to access the admin dashboard.
- Navigate to the "Employees" section to manage employee records.
- Use the search and filter options to find specific employees.
- Add, update, or delete employee records as needed.

## Contributing

If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the Django community for their amazing framework.
- Icons used in the project are provided by [FontAwesome](https://fontawesome.com/).
- apecial thanks to bootstrap.

## NOTE
- This project is in development phase many functionalities are in process to update.
