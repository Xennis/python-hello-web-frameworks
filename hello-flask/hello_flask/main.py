from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return {"Hello": "World"}


@app.route("/customer/<string:customer_id>/info")
def customer_info(customer_id: str):
    return {"customer_id": customer_id}


if __name__ == "__main__":
    app.run()
