import streamlit as st  # For creating web interface
import pandas as pd  # For data manipulation
import datetime  # For handling dates
import csv  # For reading and writing CSV file
import os  # For file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create empty DataFrame with columns
        return pd.DataFrame(columns=["Date", "Mood"])
    # Read and return existing mood data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:
        # Create CSV writer
        writer = csv.writer(file)
        # Add new mood entry
        writer.writerow([date, mood])

# Custom CSS for background and text styles
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #f7cac9, #92a8d1); /* Gradient Background */
    }
    .title {
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 32px;
    }
    .success-message {
        text-align: center;
        background-color: black;
        color: white;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        color: white;
        background-color: #FF5733;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title with emoji
st.title("🌟 Mood Tracker 😊")

# Get today's date
today = datetime.date.today()

# Display "Select your mood" as a heading
st.markdown("## Select Your Mood")

# Create dropdown for mood selection with emojis
mood_options = {
    "😊 Happy": "Happy",
    "😢 Sad": "Sad",
    "😡 Angry": "Angry",
    "😐 Neutral": "Neutral"
}

mood_choice = st.selectbox("", list(mood_options.keys()))
selected_mood = mood_options[mood_choice]  # Extract mood without emoji

# Create button to save mood
if st.button("Log Mood  🔒"):
    # Save mood when button is clicked
    save_mood_data(today, selected_mood)

    # Show success message with black background and centered text
    st.markdown(f"<div class='success-message'>✅ Mood Logged Successfully: {selected_mood}!</div>", unsafe_allow_html=True)

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:
    # Create section for Visualization
    st.subheader("📊 Mood Trends Over Time")

    # Convert date strings to datetime objects
    data["Date"] = pd.to_datetime(data["Date"])

    # Count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)

# Add footer with color
st.markdown("<div class='footer'>Built with by Dua Shakir</div>", unsafe_allow_html=True)
