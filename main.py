import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader(
    "Choose a CSV file", type="csv"
)
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     df= pd.read_csv(uploaded_files)
    # st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)

if uploaded_file is not None:
   df= pd.read_csv(uploaded_file)
   st.subheader("Data Preview")
   st.write(df.head())

   st.subheader("Data Summary")
   st.write(df.describe())

   st.subheader("Filter Data")
   columns=df.columns.tolist()
   selected_column = st.selectbox("Select column to filter by", columns)
   uniqe_values=df[selected_column].unique()
   selected_value= st.selectbox("Select Value", uniqe_values)

   filtered_df=df[df[selected_column]==selected_value]
   st.write(filtered_df)

   st.subheader("Plot Data")
   x_column=st.selectbox("Select x-axis column", columns)
   y_column=st.selectbox("Select y-axis column", columns)

   if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")
