"""
Transform and load with SQlite3 database
"""

import sqlite3
import csv


def load(dataset="pollingplaces_2020.csv"):
    payload = csv.reader(open(dataset, newline="", encoding="utf-8"), delimiter=",")
    conn = sqlite3.connect("pollingplaces_2020.db")
    c = conn.cursor()
    # generate new table for the database
    c.execute("DROP TABLE IF EXISTS pollingplaces_2020")
    c.execute(
        """
            CREATE TABLE pollingplaces_2020 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            election_dt DATE,
            county_name, 
            polling_place_id,
            polling_place_name,
            precinct_name,
            house_num,
            street_name, 
            city,
            state,
            zip,
            )
            """
    )
    # insert values
    c.executemany(
        """
            INSERT INTO pollingplaces_2020
            # col names
            # Values
            """,
        payload,
    )
    conn.commit()
    conn.close()
    return "pollingplaces_2020.db"


if __name__ == "__main__":
    load()
