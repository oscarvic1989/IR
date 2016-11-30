# IR


## Lab machines installation

Install virtualenv: ```easy_install --user virtualenv```.
Create a virtual environment: ```~/.local/bin/virtualenv ir_venv```.
Activate the virtual environment: ```source ir_venv/bin/activate``` (if you are in csh use activate.csh instead)

Go to the directory where you cloned the poject: ```cd <your-project-dir>```.
Install the required python libraries to the virtual environment: ```pip install -r requirements.txt```.

## Running the analysis

Run fetch script to download all the department html files (this will take a very long time!): ```python fetch_all_departments.py```.

Then run the analysis script: ```python run_analysis.py```.

The output will be stored in ```analysis.log```.
