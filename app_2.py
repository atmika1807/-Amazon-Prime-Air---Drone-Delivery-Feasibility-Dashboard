# Generating a complete Streamlit app.py content with integrated visualizations

import streamlit as st
import pandas as pd
import plotly.express as px

# Set up page
st.set_page_config(page_title="Amazon Prime Air Dashboard", layout="wide")
st.title("📦 Amazon Prime Air - Drone Delivery Feasibility Dashboard")

# Load datasets
df_items = pd.read_csv(r"C:\Users\atpt1\amazon prime air\dataset\drone_items.csv")
df_counties = pd.read_csv(r"C:\Users\atpt1\amazon prime air\dataset\massachusetts_counties.csv")
df_emissions = pd.read_csv(r"C:\Users\atpt1\amazon prime air\dataset\emissions_data.csv")

# Summary section
st.subheader("📈 Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Deliverable %", f"{df_items['Deliverable_Percentage'].mean():.1f}%")
col2.metric("Top County", df_counties.sort_values(by='Suitability_Score', ascending=False).iloc[0]['County'])
col3.metric("Lowest CO2 Mode", df_emissions.sort_values(by='CO2_grams').iloc[0]['Mode'])

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🚁 Drone-Compatible Items",
    "🗺️ Delivery Zones in MA",
    "⏱️ Delivery Time Simulator",
    "🌱 Environmental Impact"
])

# Tab 1: Drone-Compatible Product Categories
with tab1:
    st.header("📦 Drone-Compatible Product Categories")
    fig1 = px.pie(df_items, names='Category', values='Deliverable_Percentage',
                  title="Drone-Compatible Product Categories")
    st.plotly_chart(fig1, use_container_width=True)
    st.dataframe(df_items)

# Tab 2: Massachusetts Delivery Zones
with tab2:
    st.header("📍 County Suitability Scores")
    fig2 = px.bar(df_counties, x='County', y='Suitability_Score',
                  title="Suitability Score by County for Drone Delivery")
    st.plotly_chart(fig2, use_container_width=True)
    st.dataframe(df_counties)

# Tab 3: Delivery Time Simulation
with tab3:
    st.header("⏱️ Delivery Time Calculator")
    distance = st.slider("Distance to Customer (miles)", 1, 10, 5)
    drone_speed = st.slider("Drone Speed (mph)", 30, 60, 45)
    delivery_time = (distance / drone_speed) * 60
    st.metric("Estimated Delivery Time", f"{delivery_time:.2f} minutes")

# Tab 4: Environmental Impact Comparison
with tab4:
    st.header("🌱 CO2 Emissions by Delivery Mode")
    fig4 = px.bar(df_emissions, x="Mode", y="CO2_grams", color="Mode",
                  title="Estimated CO2 Emissions per Delivery")
    st.plotly_chart(fig4, use_container_width=True)
    st.dataframe(df_emissions)
