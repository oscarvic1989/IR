# IR


## Lab machines installation

- Install virtualenv: ```easy_install --user virtualenv```.
- Create a virtual environment: ```~/.local/bin/virtualenv ir_venv```.
- Activate the virtual environment (if you are in csh use activate.csh instead): ```source ir_venv/bin/activate```.
- Go to the directory where you cloned the poject: ```cd <your-project-dir>```.
- Install the required python libraries to the virtual environment: ```pip install -r requirements.txt```.


## Fetching the html files

Run fetch script to download all the department html files (this will take a very long time!): ```python fetch_all_departments.py```.


## Building the index

Build the index by running: ```python get_index.py```.

Compute the term frequency by running: ```python GetTerm.py```.

Calculate tf-idf by running: ```python tf-idf.py```.


## Running the analysis

Run the analysis script: ```python run_analysis.py```.

The output will be stored in ```analysis.log```.
