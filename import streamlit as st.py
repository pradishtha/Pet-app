import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Function to simulate deep learning model for dietary needs
def simulate_dietary_needs(weight, age):
    return "Recommended diet: High protein and low carbs."

# Function to detect anomalies in weight data
def detect_anomalies(weights):
    z_scores = np.abs(stats.zscore(weights))
    return z_scores > 2  # Anomaly threshold

# Title of the app
st.title("Pet Health Monitoring App")

# User Inputs
pet_name = st.text_input("Enter your pet's name:")
pet_age = st.number_input("Enter your pet's age (in years):", min_value=0)
pet_weight = st.number_input("Enter your pet's weight (in kg):", min_value=0.0, format="%.2f")
vaccination_dates = st.text_area("Enter vaccination dates (comma-separated):", "2023-01-01, 2023-06-01")
dietary_needs = st.text_input("Enter dietary needs (optional):")

# Initialize session state for weights
if 'weights' not in st.session_state:
    st.session_state.weights = []

# Button to add current weight
if st.button("Add Weight"):
    st.session_state.weights.append(pet_weight)
    st.success(f"Weight for {pet_name} added successfully!")

# Display the collected data
st.subheader("Pet Information")
st.write(f"**Name**: {pet_name}")
st.write(f"**Age**: {pet_age} years")
st.write(f"**Current Weight**: {pet_weight} kg")
st.write(f"**Vaccination Dates**: {vaccination_dates}")
st.write(f"**Dietary Needs**: {dietary_needs}")

# Anomaly Detection
if st.session_state.weights:
    anomalies = detect_anomalies(st.session_state.weights)
    
    st.subheader("Weight Tracking")
    st.write("Weights recorded:", st.session_state.weights)
    st.write("Anomalies detected:", [weight for weight, is_anomaly in zip(st.session_state.weights, anomalies) if is_anomaly])

    # Plotting the weight data
    plt.figure(figsize=(10, 5))
    plt.plot(st.session_state.weights, marker='o', label='Weight')
    plt.scatter(np.where(anomalies)[0], np.array(st.session_state.weights)[anomalies], color='red', label='Anomalies', zorder=5)
    plt.title(f"{pet_name}'s Weight Over Time")
    plt.xlabel('Entry Number')
    plt.ylabel('Weight (kg)')
    plt.axhline(y=np.mean(st.session_state.weights), color='gray', linestyle='--', label='Average Weight')
    plt.legend()
    st.pyplot(plt)

# Dietary Recommendation
if st.button("Get Dietary Recommendation"):
    recommendation = simulate_dietary_needs(pet_weight, pet_age)
    st.write(recommendation)

# Reminder Section
if st.button("Show Vaccination Reminders"):
    dates = vaccination_dates.split(',')
    reminders = [f"Reminder: Vaccination due on {date.strip()}" for date in dates]
    st.write("\n".join(reminders))
