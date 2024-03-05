import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

all_df = pd.read_csv("main_data.csv")

grouped_data = pd.DataFrame({'month': ['Jan', 'Feb', 'Mar'],
                             'weathersit': [1, 2, 3],
                             'day_type': ['Weekday', 'Weekend', 'Weekday'],
                             'cnt': [100, 200, 300]})

seasonal_rental_count = pd.Series({'Spring': 500, 'Summer': 600, 'Fall': 700, 'Winter': 800})
# Define Streamlit app layout
def main():
    st.title('Bike Rental Analysis')

    # Plot 1: Line plot with Seaborn
    st.subheader('Bike Rental Count by Month, Weather Condition, and Day Type')
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=grouped_data, x='month', y='cnt', hue='weathersit', hue_order=[1, 2, 3, 4], style='day_type', markers=True)
    plt.title('Bike Rental Count by Month, Weather Condition, and Day Type')
    plt.xlabel('Month')
    plt.ylabel('Total Rental Count')
    plt.xticks(rotation=45)
    plt.legend(title='Weather Condition')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Plot 2: Bar plot with Matplotlib
    st.subheader('Total Bike Rental Count by Season')
    plt.figure(figsize=(10, 6))
    seasonal_rental_count.plot(kind='bar', color='skyblue')
    plt.title('Total Bike Rental Count by Season')
    plt.xlabel('Season')
    plt.ylabel('Total Rental Count')
    plt.xticks(rotation=0)
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
    main()
