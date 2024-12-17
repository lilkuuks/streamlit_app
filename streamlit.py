import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app title
st.title("CSV File Viewer & Analyzer")

# Sidebar for file upload
st.sidebar.header("Upload your CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the DataFrame
    st.subheader("Your Uploaded Data")
    st.write(df.head())

    # Show basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Allow the user to choose a column for visualization
    st.subheader("Visualization")
    column = st.selectbox("Select a column to plot", df.columns)

    if pd.api.types.is_numeric_dtype(df[column]):
        fig, ax = plt.subplots()
        ax.hist(df[column], bins=20, color='skyblue', edgecolor='black')
        st.pyplot(fig)
    else:
        st.warning("Please select a numeric column to visualize.")
else:
    st.info("Please upload a CSV file to proceed.")

st.sidebar.write("---")
st.sidebar.info("This simple app was created using Streamlit!")
