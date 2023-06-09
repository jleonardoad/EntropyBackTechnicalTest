# Task Manager API

This is an API for managing tasks using the FastAPI framework and PostgreSQL database.

## Requirements

Make sure you have the following installed:

- Python 3.8 or higher
- PostgreSQL
- Project dependencies (see `requirements.txt` file)

## Installation

1. Clone the repository:

git clone <git@github.com:jleonardoad/EntropyBackTechnicalTest.git>

2. Create and activate a virtual environment:

python3 -m venv api_env
source api_env/bin/activate (Linux/Mac)
api_env\Scripts\activate (Windows)


3. Install the project dependencies:

pip install -r requirements.txt


4. Start the development server:

docker-compose up

uvicorn main:app --reload

## Usage

The API provides the following endpoints:

- `GET /tasks`: Get all tasks.
- `GET /tasks/{task_id}`: Get a specific task.
- `POST /tasks`: Create a new task.
- `PUT /tasks/{task_id}`: Update an existing task.
- `DELETE /tasks/{task_id}`: Delete an existing task.

The API expects and returns data in JSON format.

## Contribution

Contributions are welcome! If you find any issues, have ideas for improvements, or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
