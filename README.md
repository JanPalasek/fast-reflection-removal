# Python Data Science Template
## How to install

**Prerequisities**
- Python: 3.8

1. Clone the project and go to its root directory.
2. Create and activate the virtual environment:
    ```bash
    # create the environment
    python3 -m venv "venv"
    # activate the environment
    source venv/bin/activate # on Windows ./venv/Scripts/activate.ps1 in Powershell
    ```
3. Install the necessary packages:
    ```bash
    python -m pip install --upgrade pip
    python -m pip install --upgrade wheel setuptools pip-tools
    ```
4. Install the packages from requirements and the project:
    ```bash
    # install from 'requirements.txt'
    python -m piptools sync
    # install the current modules
    python -m pip install -e .
    ```

## How to work with pip-tools
Pip-tools has 2 operations: *compile* and *sync*.

1. **compile**: Generates *requirements.in* into *requirements.txt*. Do not modify requirements.txt manually, it must be generated.
```bash
python -m piptools compile
```

2. **sync**: Based on *requirements.txt*, updates the installed packages of the virtual environment. If you keep your local packages of the project (installed by pip install -e .) separately, after this step you need to install them again with the same command. If you add them to *requirements.in*, then it is generated as an absolute path into *requirements.txt* and the project is not well distributable.
```bash
python -m piptools sync
# (optionally) python -m pip install -e .
```

## Project structure
Folders:
- *bin*: executable python files. They should be included into the root namespace by setup.py scripts.
- *config*: configuration files, usually in yaml or ini.
- *docs*: documentation.
- *notebooks*: jupyter notebooks for analysis etc.
- *src*: contains list of folders for sources, e.g. python.
- *tests*: follows the structure of src/python.
