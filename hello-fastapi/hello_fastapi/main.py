from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/customer/{customer_id}/info")
def read_item(customer_id: str):
    return {"customer_id": customer_id}
