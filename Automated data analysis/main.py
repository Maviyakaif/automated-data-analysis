import streamlit as st
import plotly.express as px
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
        var_col3 = st.selectbox("Select 3rd variable:", data.columns)

        plots = ["Line", "Bar", "Scatter", "Pie Chart", "Donut Chart", "Clustered Column Chart"]
        plot_var = st.selectbox("Select type of plot/chart", plots, key='plot_var')

        st.markdown("---")  # Add a horizontal line for better separation

        match plot_var:
            case "Line":
                # Create a line chart using Plotly Express
                fig = px.line(data, x=var_col1, y=var_col2, color=var_col3, title="Line Chart")
                st.plotly_chart(fig)

            case "Bar":
                # Create a bar chart using Plotly Express with a colorful continuous color scale
                fig = px.bar(data, x=var_col1, y=var_col2, color=var_col3, title="Bar Chart", color_continuous_scale="Viridis")
                st.plotly_chart(fig)

            case "Scatter":
                # Create a scatter plot using Plotly Express with a colorful continuous color scale
                fig = px.scatter(data, x=var_col1, y=var_col2, color=var_col3, title="Scatter Plot", color_continuous_scale="Viridis")
                st.plotly_chart(fig)

            case "Pie Chart":
                # Create a pie chart using Plotly Express
                fig = px.pie(data, names=var_col1, title="Pie Chart", color=var_col3)
                st.plotly_chart(fig)

            case "Donut Chart":
                st.subheader("Donut Chart:")
                # Create a donut chart using Plotly Express
                fig = px.sunburst(data, path=[var_col1, var_col2, var_col3], title="Donut Chart", color=var_col3)
                fig.update_layout(margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig)

            case "Clustered Column Chart":
                st.subheader("Clustered Column Chart:")
                # Create a clustered column chart using Plotly Express
                fig = px.bar(data, x=var_col1, y=var_col2, color=var_col3, barmode="group", title="Clustered Column Chart", color_continuous_scale="YlOrBr")
                st.plotly_chart(fig)

    except AttributeError:
        pass
