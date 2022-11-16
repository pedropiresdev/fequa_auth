import json
import logging


def log(message: str):
    payload = {
        "service_name": "processor_apolice",
        "message": message,
    }
    logging.info(message, extra={"processor_apolice": json.dumps(payload)})


def save_credentials(user_credentials: dict):
    print(user_credentials)
    breakpoint()
    return True
