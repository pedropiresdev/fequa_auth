import sys
from ast import literal_eval
from multiprocessing import Process

from get_auth import save_credentials


def main(user_credentials):
    actions = {
            "save_credentials": save_credentials
    }
    process = Process(target=actions[user_credentials["action"]], args=(user_credentials,))
    process.start()


if __name__ == "__main__":
    credentials = {item[0]: literal_eval(item[1]) if item[1].startswith("[") else item[1] for item in
                [arg.split("=") for arg in sys.argv[1:]]}

    main(credentials)
