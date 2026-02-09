from __future__ import annotations
from pathlib import Path
import pandas as pd
from cleaner import clean_dataframe
from analyzer import build_report_row

INPUT_DIR = Path("data/input")
OUTPUT_DIR = Path("data/output")
CLEANED_DIR = OUTPUT_DIR / "cleaned"
REPORT_DIR = OUTPUT_DIR / "reports"
REPORTS_PATH = REPORT_DIR / "report.csv"
COMBINED_PATH = OUTPUT_DIR / "combined.csv"
print("This is main")
def main(): # returns nothing
    # ensure input exists
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    csv_files = sorted(INPUT_DIR.glob("*.csv")) # sorted keeps order stable (good for predictable output).
    if not csv_files:
        print("No csv files found in input directory")
        return
    report_rows = []
    cleaned_dfs = []
    for csv_file in csv_files:
        print(f"Processing {csv_file.name}")
        df_raw = pd.read_csv(csv_file) # reading csv data
        before = { # before cleaning metrics
            "rows":int (df_raw.shape[0]),
            "columns":int (df_raw.shape[1]),
            "missing_cells":int (df_raw.isna().sum().sum()),
            "duplicate_rows":int (df_raw.duplicated().sum()),
        }
        df_cleaned = clean_dataframe(df_raw)
        after ={ # after cleaning metrecs
            "rows":int (df_cleaned.shape[0]),
            "columns":int (df_cleaned.shape[1]),
            "missing_cells":int (df_cleaned.isna().sum().sum()),
            "duplicate_rows":int (df_cleaned.duplicated().sum())
        }
        cleaned_path = CLEANED_DIR / f"{csv_file.name}-cleaned.csv"
        df_cleaned.to_csv(cleaned_path, index=False)
        report_rows.append(build_report_row(csv_file.name,before,after))
        cleaned_dfs.append(df_cleaned)
    report_df = pd.DataFrame(report_rows)
    report_df.to_csv(REPORTS_PATH, index=False)
    combined_df = pd.concat(cleaned_dfs,ignore_index=True,sort=False)
    combined_df.to_csv(COMBINED_PATH, index=False)
    print("Done")
    print(f"Cleaned files: {CLEANED_DIR.resolve()}")
    print(f"Report files: {REPORT_DIR.resolve()}")
    print(f"Combined files: {COMBINED_PATH.resolve()}")
if __name__ == "__main__":
    main()