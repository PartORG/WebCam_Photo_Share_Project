import os


class FileShare:
    """Dummy class for FileStack"""

    def __init__(self, filepath):
        self.filepath = filepath

    def share(self):
        return f"{os.getcwd()}/{self.filepath}"
