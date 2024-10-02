import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

# Data Loading


def read_csv_ncvoterdata(voterdata):
    df = pd.read_csv(
        voterdata, sep="\t", header=0, encoding="unicode_escape", low_memory=False
    )
    return df


# Descriptive Statistics
def mean_age(df):
    # calculate mean of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].mean()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def median_age(df):
    # calculate median of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].median()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def std_age(df):
    # calculate standard deviation of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].std()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


# Data Processing
def recode_age_groups(series):
    if 18 <= series <= 24:
        return "18-24 yrs"
    elif 25 <= series <= 29:
        return "25-29 yrs"
    elif 30 <= series <= 34:
        return "30-34 yrs"
    elif 35 <= series <= 39:
        return "35-39 yrs"
    elif 40 <= series <= 44:
        return "40-44 yrs"
    elif 45 <= series <= 49:
        return "45-49 yrs"
    elif 50 <= series <= 54:
        return "50-54 yrs"
    elif 55 <= series <= 59:
        return "55-59 yrs"
    elif 60 <= series <= 64:
        return "60-64 yrs"
    elif 65 <= series:
        return "65+ yrs"


def make_categorical_agecat(df):
    df["Age Group"] = pd.Categorical(
        df["Age Group"],
        categories=[
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
        ],
        ordered=True,
    )
    return df


# Data Visualization
def generate_histogram_age(df, plot_name):
    age_column = [col for col in df.columns if "age" in col]
    plt.figure(figsize=(10, 6))
    bins = 6
    plt.hist(df[age_column], color="orange", bins=bins, edgecolor="black")
    plt.title("Age Distribution for Registered Voters in Durham County, NC")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{int(x):,}")
    )
    x_ticks = np.arange(0, 110, 10)
    plt.xticks(x_ticks)
    subfolder = "Output Images"
    file_path = os.path.join(subfolder, plot_name)
    plt.savefig(file_path)


def generate_age_gender_pyramid(df, plot_name):
    # Prepare data for plotting
    df = pd.DataFrame(df)
    age_gender_counts = (
        df.groupby(["Age Group", "gender_code"], observed=False)
        .size()
        .unstack(fill_value=0)
    )
    age_groups = age_gender_counts.index
    males = age_gender_counts["M"]
    females = age_gender_counts["F"]
    print(age_gender_counts)
    # Convert males to negative values for plotting
    males_negative = -males

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the population pyramid
    ax.barh(
        age_groups,
        males_negative,
        color="cornflowerblue",
        label="Male",
        edgecolor="black",
    )
    ax.barh(age_groups, females, color="salmon", label="Female", edgecolor="black")

    # Set labels and title
    ax.set_xlabel("Number of Observations")
    ax.set_ylabel("Age Groups")
    ax.set_title("Registered Voters of Durham County, NC by Gender and Age Group")
    ax.legend()

    # Add grid for better readability
    ax.grid(True)
    subfolder = "Output Images"
    file_path = os.path.join(subfolder, plot_name)
    plt.savefig(file_path)
