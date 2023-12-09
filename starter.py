import os
import shutil

data_folders = ["raw", "processed", "features"]
main_content = """import os

if __name__ == "__main__":
    print("hello world")
"""

if __name__ == "__main__":
    # create data folder and subfolders
    if not os.path.exists("data"):
        os.mkdir("data")
        for folder in data_folders:
            os.mkdir(f"data/{folder}")
            with open(f"data/{folder}/.gitignore", "w") as f:
                f.write("*\n")

    # create folders which content wil store in git
    for folder in ["docs", "notebooks", "src"]:
        if not os.path.exists(folder):
            os.mkdir(folder)

    # create folders with gitignore
    for folder in ["models", "reports"]:
        if not os.path.exists(folder):
            os.mkdir(folder)
            with open(f"{folder}/.gitignore", "w") as f:
                f.write("*\n")

    # create python main file
    if not os.path.exists("main.py"):
        with open("main.py", "w") as f:
            f.write(main_content)

    # delete git folder if exists and subfolders
    if os.path.exists(".git"):
        shutil.rmtree(".git")
    os.remove(__file__)
