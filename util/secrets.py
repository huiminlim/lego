import json


class KaggleSecrets:
    def __init__(self, path: str) -> None:
        secrets = json.load(open(path))

        self.username = secrets["username"]
        self.key = secrets["key"]
