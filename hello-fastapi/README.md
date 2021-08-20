# Hello FastAPI

Setup environment
```sh
python3 -m venv .venv
. .venv/bin/activate
pip install --editable .[test,run]
```

Run the server
```sh
cd hello_fastapi/
uvicorn main:app --reload
```
