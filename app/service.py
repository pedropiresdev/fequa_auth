import json
import logging
import uuid
import subprocess
from datetime import datetime

from nameko.rpc import rpc


class TaskService:
    name = "user_auth"
    target_path = "app/go_auth.py"

    @staticmethod
    def auth_log(process: dict):
        data = json.dumps(process)
        logging.info(data, extra={"auth_process": data})

    @rpc
    def start_task(self, user_credentials: dict):
        task_id = user_credentials.get("task_id") or uuid.uuid4().hex
        command_args = ["python", self.target_path]
        command_args += [f"{key}={value}" for key, value in user_credentials.items()]
        pid = subprocess.Popen(command_args).pid
        start_at = datetime.timestamp(datetime.now())
        user_credentials.update({
            "task_id": task_id,
            "start_at": start_at
        })

        self.auth_log({
            "pid": pid,
            "spider": self.target_path,
            "action": user_credentials["action"],
            "start_at": datetime.timestamp(datetime.now()),
            "task_id": task_id,
        })

        return user_credentials
