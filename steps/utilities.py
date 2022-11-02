import os
from datetime import datetime
import pandas as pd

output_path = "../test_data/output_errors.csv"
now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")


def output_details(errors):
    if os.path.isfile(output_path):
        pd.DataFrame({"TEST EXECUTION ON: " + time + " - ERRORS FOUND IN THE FOLLOWING RECORDS:": errors}).to_csv\
            (output_path, mode="a", index=False, header=True)
    else:
        pd.DataFrame({"TEST EXECUTION ON: " + time + " - ERRORS FOUND IN THE FOLLOWING RECORDS:": errors}).to_csv\
            (output_path, sep="|", index=False)
