# Testing Created Functions with Dataset
# Import Packages
import pandas as pd
import zipfile
import os

from mylib.lib import (
    mean_age,
    median_age,
    std_age,
    recode_age_groups,
    make_categorical_agecat,
    generate_histogram_age,
    generate_age_gender_pyramid,
)

# Declaring Standard Columns for NC voter file data:
List_Match = [
    "county_id",
    "county_desc",
    "voter_reg_num",
    "ncid",
    "last_name",
    "first_name",
    "middle_name",
    "name_suffix_lbl",
    "status_cd",
    "voter_status_desc",
    "reason_cd",
    "voter_status_reason_desc",
    "res_street_address",
    "res_city_desc",
    "state_cd",
    "zip_code",
    "mail_addr1",
    "mail_addr2",
    "mail_addr3",
    "mail_addr4",
    "mail_city",
    "mail_state",
    "mail_zipcode",
    "full_phone_number",
    "confidential_ind",
    "registr_dt",
    "race_code",
    "ethnic_code",
    "party_cd",
    "gender_code",
    "birth_year",
    "age_at_year_end",
    "birth_state",
    "drivers_lic",
    "precinct_abbrv",
    "precinct_desc",
    "municipality_abbrv",
    "municipality_desc",
    "ward_abbrv",
    "ward_desc",
    "cong_dist_abbrv",
    "super_court_abbrv",
    "judic_dist_abbrv",
    "nc_senate_abbrv",
    "nc_house_abbrv",
    "county_commiss_abbrv",
    "county_commiss_desc",
    "township_abbrv",
    "township_desc",
    "school_dist_abbrv",
    "school_dist_desc",
    "fire_dist_abbrv",
    "fire_dist_desc",
    "water_dist_abbrv",
    "water_dist_desc",
    "sewer_dist_abbrv",
    "sewer_dist_desc",
    "sanit_dist_abbrv",
    "sanit_dist_desc",
    "rescue_dist_abbrv",
    "rescue_dist_desc",
    "munic_dist_abbrv",
    "munic_dist_desc",
    "dist_1_abbrv",
    "dist_1_desc",
    "vtd_abbrv",
    "vtd_desc",
]


# Test Data is Tyrell County, NC Voter File Data, which has been independently analyzed
# to verify summary statistics and age distribution.


### Loading Data
### Testing that there are a standard number of columns for NC voter file data
def test_read_csv_ncvoterdata():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    assert test_df is not None
    assert all([col in test_df.columns for col in List_Match])


# Test Analysis Functions
def test_mean_age():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    mean_test = mean_age(test_df)
    assert mean_test == 57.30544090056285


def test_median_age():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    median_test = median_age(test_df)
    assert median_test == 60.0


def test_std_age():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    std_test = std_age(test_df)
    assert std_test == 19.8996673571703


# Test Recoding Functions
def test_recode_age_groups():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    test_df["Age Group"] = test_df["age_at_year_end"].apply(recode_age_groups)
    age_cat = [
        "18-24 yrs",
        "25-29 yrs",
        "30-34 yrs",
        "35-39 yrs",
        "40-44 yrs",
        "45-49 yrs",
        "50-54 yrs",
        "55-59 yrs",
        "60-64 yrs",
        "65+ yrs",
    ]
    unique_values = test_df["Age Group"].unique()
    all_in_list = all(value in age_cat for value in unique_values)
    print(
        "All unique values in the series are in list of Age Group categories:",
        all_in_list,
    )


def test_make_categorical_agecat():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    test_df["Age Group"] = test_df["age_at_year_end"].apply(recode_age_groups)
    agecat_order = [
        "18-24 yrs",
        "25-29 yrs",
        "30-34 yrs",
        "35-39 yrs",
        "40-44 yrs",
        "45-49 yrs",
        "50-54 yrs",
        "55-59 yrs",
        "60-64 yrs",
        "65+ yrs",
    ]
    make_categorical_agecat(test_df)
    # Check if the actual order matches the expected order
    actual_order = test_df["Age Group"].cat.categories.tolist()

    # Output the result
    if actual_order == agecat_order:
        print("The categorical variable order matches the expected order.")
    else:
        print(f"Expected order: {agecat_order}, but got: {actual_order}")


# Test Visualization Functions
def test_generate_histogram_age():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    plot_name = "test_histogram.png"
    generate_histogram_age(test_df, plot_name)
    file_path = os.path.join("Output Images", plot_name)
    if os.path.exists(file_path):
        print("File exists.")
    else:
        print("File does not exist.")


def test_generate_age_gender_pyramid():
    file_zip = "ncvoter89.zip"
    file_txt = "ncvoter89.txt"
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            test_df = pd.read_csv(
                f,
                sep="\t",
                header=0,
                encoding="unicode_escape",
                low_memory=False,
            )
    test_df["Age Group"] = test_df["age_at_year_end"].apply(recode_age_groups)
    make_categorical_agecat(test_df)
    plot_name = "test_populationpyramid.png"
    generate_age_gender_pyramid(test_df, plot_name)
    file_path = os.path.join("Output Images", plot_name)
    if os.path.exists(file_path):
        print("File exists.")
    else:
        print("File does not exist.")


if __name__ == "__main__":
    # file_zip = "ncvoter89.zip"
    # file_txt = "ncvoter89.txt"
    # setup_tests()
    test_mean_age()
    test_median_age()
    test_std_age()
    test_make_categorical_agecat()
