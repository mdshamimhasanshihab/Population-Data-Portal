import streamlit as st
import pandas as pd

# Static population data
population_data = {
    "Age group": ["0-14", "15-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "Rural Male": [18.74, 10.01, 8.28, 8.26, 6.25, 4.69, 3.85],
    "Rural Female": [17.57, 10.41, 9.92, 8.60, 6.17, 4.32, 2.74],
    "Urban Male": [7.25, 4.17, 3.86, 4.03, 2.72, 1.79, 1.20],
    "Urban Female": [6.91, 4.83, 4.79, 3.90, 2.37, 1.40, 0.84],
}

df = pd.DataFrame(population_data)
df.set_index("Age group", inplace=True)

# Additional educational data
education_data = {
    "Education Level": ["None", "Primary", "Secondary", "Higher Secondary", "Tertiary", "Others", "Total"],
    "Rural Male": [1.61, 32.27, 51.77, 7.12, 6.07, 1.16, 100.00],
    "Rural Female": [1.68, 36.36, 51.53, 6.16, 3.29, 0.98, 100.00],
    "Urban Male": [0.68, 26.05, 40.88, 13.26, 18.32, 0.81, 100.00],
    "Urban Female": [0.68, 25.23, 50.68, 11.87, 11.02, 0.52, 100.00],
    "Bangladesh Male": [1.35, 30.50, 48.69, 8.86, 9.54, 1.06, 100.00],
    "Bangladesh Female": [1.36, 32.77, 51.25, 8.01, 5.78, 0.83, 100.00],
    "Bangladesh Total": [1.35, 31.56, 49.88, 8.46, 7.79, 0.95, 100.00],
}
education_df = pd.DataFrame(education_data)
education_df.set_index("Education Level", inplace=True)

employment_percentage_data = {
    "Sector": ["Agriculture", "Industry", "Service", "Total"],
    "Rural Male": [39.3, 19.2, 41.5, 100],
    "Rural Female": [85.1, 4.7, 10.2, 100],

    "Urban Male": [7.0, 27.0, 66.0, 100],
    "Urban Female": [16.8, 29.4, 53.8, 100],

    "Bangladesh Male": [29.7, 21.5, 48.8, 100],
    "Bangladesh Female": [74.1, 8.7, 17.2, 100],
    "Bangladesh Total": [45.4, 17.0, 37.6, 100],
}

df_employment_percentage = pd.DataFrame(employment_percentage_data)
df_employment_percentage.set_index("Sector", inplace=True)


occupation_percentage_data = {
    "Occupation": [
        "Managers",
        "Professionals",
        "Technicians and associate professionals",
        "Clerical support workers",
        "Service and Sales Workers",
        "Skilled agricultural, forestry and fishery workers",
        "Craft and related trades workers",
        "Plant and machine operators, and assemblers",
        "Elementary occupations",
        "Others",
        "Total",
    ],
    "Rural Male": [1.1, 4.1, 4.2, 1.1, 16.2, 34.0, 15.3, 11.1, 12.5, 0.3, 100.0],
    "Rural Female": [0.1, 2.1, 0.4, 0.2, 1.2, 85.8, 5.9, 0.6, 3.6, 0.0, 100.0],

    "Urban Male": [3.6, 7.6, 8.2, 2.5, 28.5, 7.6, 19.3, 11.4, 10.9, 0.3, 100.0],
    "Urban Female": [1.1, 13.9, 3.3, 1.8, 8.0, 18.6, 30.7, 2.9, 19.7, 0.0, 100.0],

    "Bangladesh Male": [1.9, 5.2, 5.4, 1.6, 19.9, 26.1, 16.5, 11.2, 12.0, 0.3, 100.0],
    "Bangladesh Female": [0.3, 4.0, 0.9, 0.5, 2.3, 75.0, 9.8, 1.0, 6.2, 0.0, 100.0],
    "Bangladesh Total": [1.3, 4.8, 3.8, 1.2, 13.7, 43.4, 14.2, 7.6, 10.0, 0.2, 100.0],
}

df_occupation_percentage = pd.DataFrame(occupation_percentage_data)
df_occupation_percentage.set_index("Occupation", inplace=True)

industry_percentage_data = {
    "Industry Sector": [
        "Agriculture, forestry and fishing",
        "Mining and quarrying",
        "Manufacturing",
        "Electricity, gas, steam and air conditioning supply",
        "Water supply, sewerage, waste management",
        "Construction",
        "Wholesale and retail trade, repair of motor vehicles",
        "Transportation and storage",
        "Accommodation and food service activities",
        "Information and communication",
        "Financial and insurance activities",
        "Real estate activities",
        "Professional, scientific and technical activities",
        "Administrative and support service activities",
        "Public administration and defence",
        "Education",
        "Human health and social work activities",
        "Arts, entertainment and recreation",
        "Other service activities",
        "Activities of households as employers",
        "Activities of extraterritorial organizations",
        "Total",
    ],
    "Rural Male": [39.35, 0.15, 10.52, 0.2, 0.03, 8.27, 15.54, 11.78, 2.73, 0.33, 0.64, 0.08, 0.64, 0.71, 1.18, 2.52, 0.57, 1.44, 1.51, 1.79, 0.01,  100],
    "Rural Female": [85.03, 0, 4.43, 0, 0, 0.32, 1.19, 0.09, 0.35, 0.02, 0.15, 0.01, 0.11, 0.14, 0.08, 1.62, 0.38, 2.45, 0.19, 3.43, 0,  100],

    "Urban Male": [7.03, 0.07, 18.44, 0.41, 0.08, 7.98, 26.85, 14.13, 4.12, 0.98, 1.89, 0.37, 1.46, 1.72, 2.73, 3.24, 1.27, 2.06, 1.83, 3.07, 0,  100],
    "Urban Female": [16.72, 0.04, 28.45, 0.09, 0.02, 0.8, 5.21, 0.75, 2.38, 0.35, 1.38, 0.04, 0.59, 0.99, 8.74, 3.46, 8.92, 0.75, 1.97, 18.07, 0.03,100],

    "Bangladesh Male": [29.71, 0.13, 12.89, 0.26, 0.04, 8.18, 18.91, 12.48, 3.15, 0.52, 1.02, 0.17, 0.89, 1.02, 1.72, 2.74, 0.78, 2.28, 1.21, 3.44, 0.01,  100],
    "Bangladesh Female": [74.09, 0.01, 8.28, 0.02, 0.01, 0.4, 1.83, 0.2, 0.68, 0.07, 0.35, 0.01, 0.19, 0.28, 0.23, 2.76, 0.87, 3.49, 0.48, 5.77, 0,  100],
    "Bangladesh Total": [45.36, 0.09, 11.26, 0.18, 0.03, 5.44, 12.89, 8.15, 2.28, 0.36, 0.78, 0.11, 0.64, 0.75, 1.19, 2.74, 0.81, 2.28, 1.21, 3.44, 0.01,  100],
}

df_industry_percentage = pd.DataFrame(industry_percentage_data)
df_industry_percentage.set_index("Industry Sector", inplace=True)



employment_data = {
    "Age group": ["0-14","15-24",  "25-34",  "35-44",  "45-54", "55-64", "65+"],
    "Rural Male": [0,4827, 7432, 7917, 5892, 3923, 2009],
    "Rural Female": [0,6204, 8963, 2758, 1818, 906, 227],
    "Urban Male": [0,1867, 3462,3861, 2529, 1390, 503],
    "Urban Female": [0,806, 1231, 1116, 566, 202, 59]
}
employment_df=pd.DataFrame(employment_data)
employment_df.set_index("Age group", inplace=True)

# Streamlit app
st.title("Population Data Portal")

# Filter options
all_age_groups_option = "All"
labor_force_option=st.checkbox("Labor force Distribution", value=False)
if labor_force_option:
    selected_age_groups = st.multiselect("Select Age Groups", [all_age_groups_option] + df.index.tolist(),default=["15-24", "25-34","35-44","45-54","55-64",'65+'])
else:
    selected_age_groups = st.multiselect("Select Age Groups", [all_age_groups_option] + df.index.tolist(), default=[all_age_groups_option])
selected_genders = st.multiselect("Select Genders", ["Male", "Female"])
selected_locations = st.multiselect("Select Locations", ["Rural", "Urban"])

further_options=st.checkbox("Select if you want more specific value",value=False)
if further_options:
    selected_option = st.radio("Select Option", ["Educational Level", "Employment Status","Employment distribution by economic sectors","Employment distribution by occupations",
                                                 "Employment distribution by industries"])
else:
    selected_option=""
# educational_level_option = st.checkbox("Select Educational Level", value=False)
# employment_status_option=st.checkbox("Select Employment Status", value=False)
#

# Filter the data
if all_age_groups_option in selected_age_groups:
    selected_age_groups = df.index.tolist()  # Select all age groups
if not selected_genders:
    selected_genders = ["Male", "Female"]  # Select both genders if none are selected
if not selected_locations:
    selected_locations = ["Rural", "Urban"]  # Select all locations if none are selected

base_value=df.loc[selected_age_groups, [f"{loc} {gender}" for loc in selected_locations for gender in selected_genders]].sum().sum() * 1_000_000
# if educational_level_option:
#     selected_educational_levels = st.multiselect("Select Educational Levels", education_df.index.tolist())
#     filtered_education_data = education_df.loc[selected_educational_levels, [f"{loc} {gender}" for loc in selected_locations for gender in selected_genders]].sum().sum()
#     st.write(f"Population for Educational Levels: {', '.join(selected_educational_levels)} in {', '.join(selected_genders)}, {', '.join(selected_locations)}: {filtered_education_data:.2f}%")
if selected_option == "Educational Level":
    if len(selected_locations)>1:
        loc="Bangladesh"
    else:
        loc=selected_locations[0]

    gender=selected_genders[0]
    selected_educational_levels = st.multiselect("Select Educational Levels", education_df.index.tolist(),default="Total")
    filtered_data = ((education_df.loc[selected_educational_levels, [f"{loc} {gender}"]].sum())/100)*base_value

elif selected_option=="Employment Status":
    base_value = employment_df.loc[selected_age_groups, [f"{loc} {gender}" for loc in selected_locations for gender in
                                              selected_genders]].sum().sum()*1000
    filtered_data = base_value
elif selected_option=="Employment distribution by economic sectors":
    if len(selected_locations)>1:
        loc="Bangladesh"
    else:
        loc=selected_locations[0]

    gender=selected_genders[0]
    selected_employment_levels = st.multiselect("Select Employment Sectors: ", df_employment_percentage.index.tolist(),default="Total")
    filtered_data = ((df_employment_percentage.loc[selected_employment_levels, [f"{loc} {gender}"]].sum())/100)*70468000

elif selected_option=="Employment distribution by occupations":
    if len(selected_locations)>1:
        loc="Bangladesh"
    else:
        loc=selected_locations[0]

    gender=selected_genders[0]
    selected_occupation_levels = st.multiselect("Select Employment Sectors: ", df_occupation_percentage.index.tolist(),default="Total")
    filtered_data = ((df_occupation_percentage.loc[selected_occupation_levels, [f"{loc} {gender}"]].sum())/100)*70468000

elif selected_option=="Employment distribution by industries":
    if len(selected_locations)>1:
        loc="Bangladesh"
    else:
        loc=selected_locations[0]

    gender=selected_genders[0]
    selected_industry_levels = st.multiselect("Select Employment Sectors: ", df_industry_percentage.index.tolist(),default="Total")
    filtered_data = ((df_industry_percentage.loc[selected_industry_levels, [f"{loc} {gender}"]].sum())/100)*70468000

else:
    filtered_data = base_value



st.write(f"Population: {int(filtered_data)}")