"""
Extracting dataset from CSV hosted online
"""

import requests
import os


def extract(
    url="https://s3.amazonaws.com/dl.ncsbe.gov/ENRS/2020_11_03/polling_place_20201103.csv",
    filepath="data/pollingplaces_2020.csv",
    directory="data",
):
    """Extract to file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url, timeout=5) as r:
        with open(filepath, "wb") as f:
            f.write(r.content)
    return filepath


if __name__ == "__main__":
    if os.path.exists("/Users/pdeguz01/Documents/git/PeterdeGuzman_Mini5"):
        os.chdir("/Users/pdeguz01/Documents/git/PeterdeGuzman_Mini5")
    else:
        print("Directory does not exist.")

    extract()
