# Test functions created in main.py script

import zipfile

from mylib.lib import (
    read_csv_ncvoterdata,
)
from test_lib import (
    test_generate_histogram_age,
    test_generate_age_gender_pyramid,
    recode_age_groups,
    make_categorical_agecat,
)


def test_main():
    file_zip = "ncvoter32.zip"
    file_txt = "ncvoter32.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            df = read_csv_ncvoterdata(f)
    # test_generate_histogram()
    df["Age Group"] = df["age_at_year_end"].apply(recode_age_groups)
    make_categorical_agecat(df)
    test_generate_histogram_age()
    test_generate_age_gender_pyramid()


test_main()
