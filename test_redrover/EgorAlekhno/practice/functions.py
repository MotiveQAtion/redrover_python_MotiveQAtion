import os


def get_root_path(file_path):
    root_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root_path, file_path)

print(get_root_path(""))
