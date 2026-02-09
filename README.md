# CSV Data Cleaner & Analyzer

##  Overview
CSV Data Cleaner & Analyzer is a Python-based utility that automates the process of **cleaning, validating, and analyzing CSV files** from a directory.  
It is designed to handle common real-world data issues such as extra index columns, missing values, inconsistent formatting, and duplicate records.

The tool processes multiple CSV files at once and generates **cleaned datasets and a consolidated analysis report**.

---

##  Features
- Reads **multiple CSV files** from an input directory
- Automatically removes unwanted index columns (e.g. `Unnamed: 0`)
- Standardizes column names
- Handles missing values intelligently  
  - Numeric columns → filled with median  
  - Non-numeric columns → filled with mode or `"Unknown"`
- Removes duplicate rows
- Generates:
  - Cleaned CSV files
  - A summary report with dataset statistics
- Organized output structure for easy reuse

---

##  Technologies Used
- Python
- Pandas
- NumPy
- OS / File System handling
- Pathlib

---

##  Project Structure

csv_data_cleaner_analyzer/
├── src/
│ ├── main.py # Entry point
│ ├── cleaner.py # Data cleaning logic
│ ├── analyzer.py # Data analysis & reporting
│ └── utils.py # Helper functions
│
├── data/
│ ├── input/ # Raw CSV files
│ └── output/
│ ├── cleaned/ # Cleaned CSVs
│ └── reports/ # Summary report
│
├── README.md
├── requirements.txt
└── .gitignore


---

##  How to Run

###  Clone the repository
```bash
git clone <your-github-repo-url>
cd csv_data_cleaner_analyzer
```
### Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Add CSV Files
```bash
data/input/
```
### Run the project
```bash
python src/main.py
```

## Output
After execution, the following files are generated:
### Cleaned CSV files
# Need to add some screenshots here
```bash
data/output/cleaned/
```
### Analysis report
```bash
data/output/reports/report.csv
```
## Use Cases
Data cleaning before analysis or ML pipelines.

Preparing API or log data for further processing.

Automating repetitive CSV cleanup tasks.
## Author
Ujjwal Dahiya