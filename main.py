# import matplotlib.pyplot as plt
# import pandas as pd
# import streamlit as st
# st.title("ICSSR Project Analysis and Trends")
# uploaded_file = st.file_uploader("Choose a CSV file: ",type="CSV")
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Data Preview")
#     st.write(df.head())

#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.write("Filter Data")
#     columns = df.columns.tolist()
#     selected_columns = st.selectbox("Select columns to filter by",columns)
#     unique_values = df[selected_columns].unique()
#     selected_values = st.selectbox("Select value",unique_values)

#     filtered_df = df[df[selected_columns]== selected_values]
#     st.write(filtered_df)

#     st.subheader("Plot Data")
#     x_column = st.selectbox("Select x-axis column", columns)
#     y_column = st.selectbox("Select y-axis column", columns)

#     if st.button("Generate Plot"):
#         st.line_chart(filtered_df.set_index(x_column)[y_column])
# else:
#     st.write("Waiting for file to upload...") 


# import matplotlib.pyplot as plt
# import pandas as pd
# import streamlit as st

# st.title("ICSSR Project Analysis and Trends")
# uploaded_file = st.file_uploader("Choose a CSV file: ", type="CSV")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Data Preview")
#     st.write(df.head())

#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.write("Filter Data")
#     columns = df.columns.tolist()
#     selected_columns = st.selectbox("Select columns to filter by", columns)
#     unique_values = df[selected_columns].unique()
#     selected_values = st.selectbox("Select value", unique_values)

#     filtered_df = df[df[selected_columns] == selected_values]
#     st.write(filtered_df)

#     st.subheader("Plot Data")

#     if st.button("Generate Plot"):
#         # Calculate the count of 1s for each column
#         count_of_ones = (df == 1).sum()

#         # Plotting the graph
#         plt.figure(figsize=(10, 6))
#         plt.bar(count_of_ones.index, count_of_ones.values)
#         plt.xlabel('Column Names')
#         plt.ylabel('Count of 1s')
#         plt.title('Count of 1s in Each Column')
#         plt.xticks(rotation=90)
#         st.pyplot(plt)

# else:
#     st.write("Waiting for file to upload...")







# import matplotlib.pyplot as plt
# import pandas as pd
# import streamlit as st

# st.title("ICSSR Project Analysis and Trends")
# uploaded_file = st.file_uploader("Choose a CSV file: ", type="CSV")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Data Preview")
#     st.write(df.head())

#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.subheader("Plot Data")

#     # Ask user if they want to use a single column or multiple columns
#     graph_type = st.radio("Do you want to plot a graph with a single column or multiple columns?", ('Single Column', 'Multiple Columns'))

#     if graph_type == 'Single Column':
#         # Single column selected
#         column = st.selectbox("Select the column to plot", df.columns)
#         x_column = st.selectbox("Select the x-axis column", df.columns)
        
#         if st.button("Generate Plot"):
#             count_of_ones = df[column].value_counts().get(1, 0)
            
#             # Plot the graph
#             plt.figure(figsize=(10, 6))
#             plt.bar([column], [count_of_ones])
#             plt.xlabel(x_column)
#             plt.ylabel('Count of 1s')
#             plt.title(f'Count of 1s in {column}')
#             st.pyplot(plt)

#     elif graph_type == 'Multiple Columns':
#         # Multiple columns selected
#         selected_columns = st.multiselect("Select columns to include in the plot", df.columns)
#         x_column = st.selectbox("Select the x-axis column", df.columns)
        
#         if st.button("Generate Plot"):
#             # Calculate the count of 1s for selected columns
#             count_of_ones = (df[selected_columns] == 1).sum()

#             # Plot the graph
#             plt.figure(figsize=(10, 6))
#             plt.bar(count_of_ones.index, count_of_ones.values)
#             plt.xlabel(x_column)
#             plt.ylabel('Count of 1s')
#             plt.title('Count of 1s in Selected Columns')
#             plt.xticks(rotation=90)
#             st.pyplot(plt)

# else:
#     st.write("Waiting for file to upload...")








# import matplotlib.pyplot as plt
# import pandas as pd
# import streamlit as st

# st.title("ICSSR Project Analysis and Trends")
# uploaded_file = st.file_uploader("Choose a CSV file: ", type="CSV")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Data Preview")
#     st.write(df.head())

#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.subheader("Plot Data")

#     # Ask user if they want to use a single column or multiple columns
#     graph_type = st.radio("Do you want to plot a graph with a single column or multiple columns?", ('Single Column', 'Multiple Columns'))

#     if graph_type == 'Single Column':
#         # Single column selected
#         column = st.selectbox("Select the column to plot", df.columns)
        
#         if st.button("Generate Plot"):
#             # Categorize the values as 'Yes', 'No', or 'Other'
#             counts = df[column].apply(lambda x: 'Yes' if x == 1 else ('No' if x == 0 else 'Other')).value_counts()

#             # Plot the graph
#             plt.figure(figsize=(10, 6))
#             plt.bar(counts.index, counts.values)
#             plt.xlabel(column)
#             plt.ylabel('Count')
#             plt.title(f'Distribution of Values in {column}')
#             st.pyplot(plt)

#     elif graph_type == 'Multiple Columns':
#         # Multiple columns selected
#         selected_columns = st.multiselect("Select columns to include in the plot", df.columns)
        
#         if st.button("Generate Plot"):
#             # Initialize a dictionary to hold the counts for each category across all selected columns
#             combined_counts = {'Yes': 0, 'No': 0, 'Other': 0}

#             for col in selected_columns:
#                 counts = df[col].apply(lambda x: 'Yes' if x == 1 else ('No' if x == 0 else 'Other')).value_counts()
#                 for category in ['Yes', 'No', 'Other']:
#                     combined_counts[category] += counts.get(category, 0)

#             # Plot the graph
#             plt.figure(figsize=(10, 6))
#             plt.bar(combined_counts.keys(), combined_counts.values())
#             plt.xlabel('Categories')
#             plt.ylabel('Count')
#             plt.title('Combined Distribution of Values in Selected Columns')
#             st.pyplot(plt)

# else:
#     st.write("Waiting for file to upload...")







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
        # Define colors for each category
        colors = ['green', 'blue', 'orange']  # Yes -> Green, No -> Blue, Other -> Orange
        
        # Plot the bar chart
        plt.figure(figsize=(10, 6))
        bars = plt.bar(counts.index, counts.values, color=colors)

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
            # Initialize a dictionary to hold the counts for each category across all selected columns
            combined_counts = {'Yes': 0, 'No': 0, 'Other': 0}

            for col in selected_columns:
                counts = df[col].apply(lambda x: 'Yes' if x == 1 else ('No' if x == 0 else 'Other')).value_counts()
                for category in ['Yes', 'No', 'Other']:
                    combined_counts[category] += counts.get(category, 0)

            # Convert combined_counts to a pandas Series to plot
            counts_series = pd.Series(combined_counts)

            # Plot the graph with customizations
            plot_bar_chart(counts_series, 'Combined Distribution of Values in Selected Columns', 'Categories')

else:
    st.write("Waiting for file to upload...")
