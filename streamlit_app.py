import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("ICSSR Project Analysis and Trends")
uploaded_file = st.file_uploader("Choose a CSV file: ", type="CSV")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Plot Data")

    # Ask user if they want to use a single column or multiple columns
    graph_type = st.radio("Do you want to plot a graph with a single column or multiple columns?", ('Single Column', 'Multiple Columns'))

    def plot_bar_chart(counts, title, x_label):
        # Define new colors for each bar
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']  # Custom colors for variety
        
        # Plot the bar chart
        plt.figure(figsize=(12, 6))
        bars = plt.bar(counts.index, counts.values, color=colors[:len(counts.index)])

        # Add count labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
        
        plt.xlabel(x_label)
        plt.ylabel('Count')
        plt.title(title)
        st.pyplot(plt)

    if graph_type == 'Single Column':
        # Single column selected
        column = st.selectbox("Select the column to plot", df.columns)
        
        if st.button("Generate Plot"):
            # Categorize the values as 'Yes', 'No', or 'Other'
            counts = df[column].apply(lambda x: 'Yes' if x == 1 else ('No' if x == 0 else 'Other')).value_counts()

            # Plot the graph with customizations
            plot_bar_chart(counts, f'Distribution of Values in {column}', column)

    elif graph_type == 'Multiple Columns':
        # Multiple columns selected
        selected_columns = st.multiselect("Select columns to include in the plot", df.columns)
        
        if st.button("Generate Plot"):
            # Initialize a dictionary to hold the counts for each column
            column_counts = {}

            for col in selected_columns:
                # Count the number of 1s in the column
                count_ones = (df[col] == 1).sum()
                # Use the column name as the key
                column_counts[col] = count_ones

            # Convert column_counts to a pandas Series to plot
            counts_series = pd.Series(column_counts)

            # Plot the graph with customizations
            plt.figure(figsize=(12, 6))
            bars = plt.bar(counts_series.index, counts_series.values, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'][:len(counts_series.index)])

            # Add count labels on top of each bar
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

            plt.xlabel('Columns')
            plt.ylabel('Count of 1s')
            plt.title('Count of 1s in Selected Columns')

            # Split column names by '/' and use the part after '/'
            new_labels = [name.split('/')[-1] for name in counts_series.index]
            plt.xticks(ticks=range(len(new_labels)), labels=new_labels, rotation=45)

            st.pyplot(plt)
            st.subheader("Created by Utkarsh Shukla")

else:
    st.write("Waiting for file to upload...")
