# jupyterlab-dir
Script for build JupyterLab project directories tree

After run this script will create directories, then will delete `.git` folder (if exists) and self.

The directories structure will looks like this:

```
├── data
│   ├── features
│   │   └── .gitignore
│   ├── processed
│   │   └── .gitignore
│   └── raw
│       └── .gitignore
├── docs
├── main.py
├── models
│   └── .gitignore
├── notebooks
├── reports
│   └── .gitignore
└── src
```
Run this command for quick start:
```bash
curl -s https://raw.githubusercontent.com/Woit/jupyterlab-dir/main/starter.py | python
```

Or clone repo and run script (assume that your folder should named "some_dir"):
```bash
git clone https://github.com/Woit/jupyterlab-dir

mv jupyterlab-dir some_dir && cd some_dir && python starter.py
```
