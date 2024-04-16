import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def q1(df, sample_df):
    # Calculate the mean and maximum glucose levels in the sample
    sample_mean_glucose = sample_df['Glucose'].mean()
    sample_max_glucose = sample_df['Glucose'].max()

    # Calculate the population mean and maximum glucose levels
    population_mean_glucose = df['Glucose'].mean()
    population_max_glucose = df['Glucose'].max()

    # Create bar charts to compare the sample and population statistics
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    axs[0].bar(['Sample', 'Population'], [sample_mean_glucose, population_mean_glucose])
    axs[0].set_title('Mean Glucose Comparison')

    axs[1].bar(['Sample', 'Population'], [sample_max_glucose, population_max_glucose])
    axs[1].set_title('Maximum Glucose Comparison')

    plt.tight_layout()
    plt.savefig('../result/01.mean_max_glucose_comparison.png', format='png', dpi=300)
    plt.show()


def q2(df, sample_df):
    # Calculate the 98th percentile of BMI in the sample and population
    sample_98th_bmi = np.percentile(sample_df['BMI'], 98)
    population_98th_bmi = np.percentile(df['BMI'], 98)

    # Create bar charts to compare the sample and population statistics
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.bar(['Sample', 'Population'], [sample_98th_bmi, population_98th_bmi])
    ax.set_title('98th Percentile BMI Comparison')

    plt.tight_layout()
    plt.savefig('../result/02.98th_percentile_bmi_comparison.png', format='png', dpi=300)
    plt.show()


def q3(df):
    # Create an empty DataFrame to store the bootstrap statistics
    bootstrap_stats = pd.DataFrame(columns=['Sample', 'Mean_BP', 'Std_BP', 'Percentile_BP'])

    # generate 500 bootstrap samples
    for i in range(500):
        # Take a random sample of 150 observations with replacement
        sample_df = df.sample(n=150, replace=True)

        # Calculate the mean, standard deviation and 98th percentile of BloodPressure in the sample
        sample_mean_bp = sample_df['BloodPressure'].mean()
        sample_std_bp = sample_df['BloodPressure'].std()
        sample_98th_bp = np.percentile(sample_df['BloodPressure'], 98)

        # Store the bootstrap statistics in the DataFrame
        bootstrap_stats.loc[i] = [i + 1, sample_mean_bp, sample_std_bp, sample_98th_bp]


    # Calculate the population mean, standard deviation and 98th percentile of BloodPressure
    population_mean_bp = df['BloodPressure'].mean()
    population_std_bp = df['BloodPressure'].std()
    population_98th_bp = np.percentile(df['BloodPressure'], 98)

    # Create bar charts to compare the sample and population statistics
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].bar(['Sample', 'Population'], [bootstrap_stats['Mean_BP'].mean(), population_mean_bp])
    axs[0].set_title('Mean BloodPressure Comparison')

    axs[1].bar(['Sample', 'Population'], [bootstrap_stats['Std_BP'].mean(), population_std_bp])
    axs[1].set_title('Standard Deviation BloodPressure Comparison')

    axs[2].bar(['Sample', 'Population'], [bootstrap_stats['Percentile_BP'].mean(), population_98th_bp])
    axs[2].set_title('98th Percentile BloodPressure Comparison')

    plt.tight_layout()
    plt.savefig('../result/03.mean_standard_deviation_98th_percentile_comparison.png', format='png', dpi=300)
    plt.show()


def analysis():
    df = pd.read_csv('../data_clean/diabetes.csv')

    # Set a seed for reproducibility
    np.random.seed(27)

    # Take a random sample of 25 observations
    sample_df = df.sample(n=25)

    q1(df, sample_df)
    q2(df, sample_df)
    q3(df, )



analysis()
