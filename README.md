# IR


## Lab machines installation

```easy_install --user virtualenv```
```virtualenv ~/ir_venv```
```source ~/ir_venv/bin/activate``` (if you are in csh use activate.csh instead)

```cd <your-project-dir>```
```pip install -r requirements.txt```

## Running the analysis

Run the ```fetch_all_departments.py``` script to download all the department html files.

Then run the analysis script: ```python run_analysis.py```.

The output will be stored in ```analysis.log```.
