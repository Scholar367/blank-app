import requests
# app.py
import streamlit as st

st.title("Prayer Time Predictor 📿")
city = st.text_input("Enter City", "Wesley Chapel")
country = st.text_input("Enter Country", "United States")

def get_prayer_times(city, country, method=2):
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and data["code"] == 200:
        timings = data["data"]["timings"]
        for prayer, time in timings.items():
            print(f"{prayer}: {time}")
    else:
        print("Error fetching prayer times:", data.get("data", "Unknown error"))

    if st.button("Get Prayer Times"):
        for prayer, time in timings.items():
            st.write(f"{prayer}: {time}")



# Example usage
get_prayer_times("Wesley Chapel", "United States")
