import streamlit as st
import pandas as pd

st.title("Sebastian's Workout Generator")

exercises = pd.read_csv("exercises.csv")

workout_group = st.selectbox(
    "Select Workout Day",
    [
        "Chest + Triceps",
        "Back + Biceps",
        "Legs + Abs",
        "Accessories"
    ]
)

workout_location = st.radio(
    "Select Workout Location",
    [
        "Home",
        "Gym"
    ]
)

number_of_exercises = st.selectbox(
    "Number of Exercises",
    [3, 4, 5, 6]
)

filtered = exercises[exercises["group"] == workout_group]

if workout_location == "Home":
    home_equipment = [
        "Barbell",
        "Dumbbells",
        "Bodyweight",
        "Bench",
        "Cable",
        "Plate"
    ]

    filtered = filtered[filtered["equipment"].isin(home_equipment)]

if st.button("Generate Workout"):
    workout = filtered.sample(
        n=min(number_of_exercises, len(filtered))
    )

    st.write("Your Workout")

    st.dataframe(
        workout[["name", "muscle", "equipment", "type"]]
    )