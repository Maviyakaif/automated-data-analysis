import streamlit as st
import matplotlib.pyplot as plt
from backend import filereader

file = st.file_uploader("Upload your file here")
st.set_option('deprecation.showPyplotGlobalUse', False)

if file:
    try:
        # Display summary statistics
        data = filereader(file)

        data.fillna(0)
        st.subheader("Summary Statistics")
        st.write(data.describe(), unsafe_allow_html=True)

        # Visualizing data
        st.subheader("Data Visualization:")
        var_col1 = st.selectbox("Select 1st variable:", data.columns)
        var_col2 = st.selectbox("Select 2nd variable:", data.columns)
        plots = ["Line", "Bar", "Pie", "Scatter"]
        regression = ["Linear Regression"]
        reg = st.selectbox("Select Regression type", regression)
        plot_var = st.selectbox("Select type of plot/chart", plots)

        match plot_var:
            case "Line":
                plt.plot(data[var_col1], data[var_col2], linestyle="dashed")
                plt.xlabel(var_col1)
                plt.ylabel(var_col2)
                st.pyplot()

            case "Bar":
                plt.bar(data[var_col1], data[var_col2])
                plt.xlabel(var_col1)
                plt.ylabel(var_col2)
                st.pyplot()

            # case "Pie":
            #     plt.pie(data, labels=data.columns)
            #     st.pyplot()

            case "Scatter":
                plt.scatter(data[var_col1], data[var_col2])
                plt.xlabel(var_col1)
                plt.ylabel(var_col2)
                st.pyplot()
            case "Linear Regression":
                import pandas as pd
                import numpy as np
                import matplotlib.pyplot as plt
                from sklearn.model_selection import train_test_split
                from sklearn.linear_model import LinearRegression
                from sklearn.metrics import mean_squared_error


                # Assuming your CSV file has columns named 'X' and 'y' for the independent and dependent variables
                X = data[var_col1].values.reshape(-1, 1)
                y = data[var_col2].values

                # Split the data into training and testing sets
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Create a Linear Regression model
                model = LinearRegression()

                # Train the model on the training set
                model.fit(X_train, y_train)

                # Make predictions on the test set
                y_pred = model.predict(X_test)

                # Calculate the mean squared error
                mse = mean_squared_error(y_test, y_pred)
                st.write(f'Mean Squared Error: {mse}')

                # Plot the original data and the regression line
                plt.scatter(X_test, y_test, color='black', label='Actual data')
                plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regression line')
                plt.xlabel('Independent Variable')
                plt.ylabel('Dependent Variable')
                plt.legend()
                st.pyplot()



except AttributeError:

        pass
