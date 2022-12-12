## Local Setup

1. `pip install poetry`
1. `cd` into the directory where the `pyproject.toml` is located then `poetry install`
1. Run the DB migrations via poetry `poetry run python app/prestart.py`
1. [UNIX]: Run the FastAPI server via poetry with the bash script: `poetry run ./run.sh`
1. [WINDOWS]: Run the FastAPI server via poetry with the Python command: `poetry run python app/main.py`
1. Go to http://localhost:8001/
