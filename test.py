import requests


base_url = "http://127.0.0.1:8000"


def call_execute_method_a():
    response = requests.post(f"{base_url}/execute-method-a")
    if response.status_code == 200:
        print("Method A:", response.json())
    else:
        print("Method A: Error", response.status_code, response.text)


def call_execute_method_b():
    response = requests.post(f"{base_url}/execute-method-b")
    if response.status_code == 200:
        print("Method B:", response.json())
    else:
        print("Method B: Error", response.status_code, response.text)


if __name__ == "__main__":
    call_execute_method_a()
    call_execute_method_b()
