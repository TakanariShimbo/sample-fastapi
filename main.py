from fastapi import FastAPI

from algo import execute_a, execute_b


app = FastAPI()


@app.post("/execute-method-a")
def execute_method_a():
    is_success = execute_a()
    if not is_success:
        raise Exception("something error...")
    return {"message": "Success!"}


@app.post("/execute-method-b")
def execute_method_b():
    is_success = execute_b()
    if not is_success:
        raise Exception("something error...")
    return {"message": "Success!"}
