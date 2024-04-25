import streamlit as st
import pandas as pd
import numpy as np
from pickle import load

# Set Streamlit page configuration
st.set_page_config(
    page_title="World Development Measurement",
    page_icon="🌍",
)

# Define custom CSS styles
st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f4f4f4;
}

h1 {
    color: #0074E4;
    text-align: center;
}

h2 {
    color: #0074E4;
}

.subheader {
    font-size: 16px;
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# Main title and subheader
st.header("World Development Measurement")
st.subheader("Enter Data")

# Function to show input fields
def show_page():
    Birth_Rate = st.sidebar.number_input("Birth Rate")
    Business_Tax_Rate = st.sidebar.number_input("Business Tax Rate")
    Co2_Emissions = st.sidebar.number_input("Co2 Emissions")
    Days_to_start_Business = st.sidebar.number_input("Days to Start Business")
    Ease_of_Business = st.sidebar.number_input("Ease of Business")
    Energy_Usage = st.sidebar.number_input("Energy Usage")
    Gross_Domestic_Product = st.sidebar.number_input("Gross Domestic Product")
    Health_Exp_percent_GDP = st.sidebar.number_input("Health Expenditure percent of GDP")
    Health_Exp_or_Capita = st.sidebar.number_input("Health Expenditure per Capita")
    Hours_to_do_Tax = st.sidebar.number_input("Hours to do Tax")
    Infant_Mortality_Rate = st.sidebar.number_input("Infant Mortality Rate")
    Internet_Usage = st.sidebar.number_input("Internet Usage")
    Lending_Interest = st.sidebar.number_input("Lending Interest")
    Life_Expectancy_Female = st.sidebar.slider("Select Female Life Expectancy", min_value=0, max_value=100, key="unique_key_female_age")
    Life_Expectancy_Male = st.sidebar.slider("Select Male Life Expectancy", min_value=0, max_value=100, key="unique_key_male_age")
    Mobile_Phone_Usage = st.sidebar.number_input("Mobile Phone Usage")
    Population_0_14 = st.sidebar.number_input("Population 0-14 Rate")
    Population_15_64 = st.sidebar.number_input("Population 15-64 Rate")
    Population_65plus = st.sidebar.number_input("Population 65plus Rate")
    Population_Total = st.sidebar.number_input("Population Total")
    Population_Urban = st.sidebar.number_input("Urban Population Rate")
    Tourism_Inbound = st.sidebar.number_input("Tourism Inbound")
    Tourism_Outbound = st.sidebar.number_input("Tourism Outbound")
    return [Birth_Rate, Business_Tax_Rate, Co2_Emissions, Days_to_start_Business, Ease_of_Business,
            Energy_Usage, Gross_Domestic_Product, Health_Exp_percent_GDP, Health_Exp_or_Capita, Hours_to_do_Tax,
            Infant_Mortality_Rate, Internet_Usage, Lending_Interest, Life_Expectancy_Female, Life_Expectancy_Male,
            Mobile_Phone_Usage, Population_0_14, Population_15_64, Population_65plus, Population_Total,
            Population_Urban, Tourism_Inbound, Tourism_Outbound]

x = show_page()

# Button to trigger prediction
if st.button("Predict"):
    if all(x):
        x = np.array(x).reshape(1, -1)

        # Load the model
        model = load(open('wdm.pkl', 'rb'))

        # Make a prediction
        prediction = model.predict(x)[0]

        # Define result categories and corresponding images
        result_categories = [
            "Underdeveloped Country",
            "Developing Country",
            "Developing Country with Improving Conditions",
            "Developed Country with Continued Growth",
            "Developed Country with Stable Conditions",
            "Highly Developed Country",
            "Unknown or Invalid Category"
        ]
        result_images = [
            "underdeveloped.jpg",
            "developing.jpg",
            "developing_improving.jpg",
            "developed_growth.jpg",
            "developed_stable.jpg",
            "highly_developed.jpg",
            "unknown.jpg"
        ]

        # Determine the result text and image
        if 0 <= prediction < len(result_categories):
            result_text = result_categories[prediction]
            result_image = result_images[prediction]
        else:
            result_text = result_categories[-1]
            result_image = result_images[-1]

        # Display the prediction result
        st.subheader("Prediction Result:")
        st.header(result_text)
        st.image(result_image, use_column_width=True)
    else:
        st.error("Please provide all required inputs.")
    
    