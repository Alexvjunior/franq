# Franq leads Project

This is a Django project for the Franq Leads.

## **Setup**

1. Clone the repository:
```bash
git clone https://github.com/Alexvjunior/franq.git
```

2. Navigate to the project directory:
```bash
cd franq
```

3. Build the Docker images:
```bash
make run 
```


## **Running the Tests**

To run the tests, use the following command:
```bash
make test
```


## **Code Quality and Security**

To ensure code quality and enhance security, the following tools are integrated into the project:

### isort

[isort](https://pycqa.github.io/isort/) is a Python utility that sorts imports alphabetically and automatically separates them into sections.

To run isort and automatically format your imports, use the following command:

```bash
isort 
or
make format
```


### flake8

flake8 is a code linter that checks Python code for style and programming errors.

To run flake8 and check your code, use the following command:
```bash
flake8 apps
or 
make lint
```

### safety

safety is a command-line tool that checks your Python dependencies for known security vulnerabilities.

To run safety and check for vulnerabilities, use the following command:
```bash
safety check
or
make security
```


## **Available Makefile Commands**
The project includes a Makefile with several useful commands:

- make lint: Run flake8 for linting the code.
- make test: Run pytest for running tests.
- make security: Perform a security check on the project dependencies using Safety.
- make run: Run the application using docker compose.
- make run-postgres: Run the postgres application using docker
- make run-redis: Run the redis application using docker
- make clean: Clean up the project by removing the virtual environment and cached files.


## **License**

This project is licensed under the [MIT License](LICENSE).