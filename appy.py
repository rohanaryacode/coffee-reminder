import streamlit as st
import random
import time

st.set_page_config(page_title="Muma's Coffee Companion", layout="centered")

QUOTES = [
    "Coffee is a hug in a mug.",
    "But first, coffee.",
    "Life begins after coffee.",
    "Espresso yourself!",
    "Coffee: because adulting is hard.",
    "Coffee is life."
]

routine_tasks = [
    "Make Coffee",
    "Wake up Rohan",
    "Wake up Riya",
    "Check Email",
    "Eat Breakfast",
    "Water the Plants"
]

st.title("☕ Muma's Coffee Companion")
st.write("I coded this all by myself, except that I had to translate it into a different programming language last minute!")
st.write("Welcome to your smart coffee and reminder hub!")

if st.button("Show Me a Coffee Quote"):
    st.success(random.choice(QUOTES))

brew_time = st.number_input("Set a Brew Reminder (minutes)", min_value=1, step=1)
if st.button("Start Brew Timer"):
    st.info(f"Reminder set for {brew_time} minutes!")
    st.toast("Timer started (simulated)")

reminder_name = st.text_input("Reminder For:")
custom_time = st.number_input("Custom Reminder Time (minutes)", min_value=1, step=1)
if st.button("Set Custom Reminder"):
    if reminder_name:
        st.info(f"Reminder set for {reminder_name} in {custom_time} minute(s)")
    else:
        st.error("Please enter a name for the reminder")

st.write("### Current Time")
st.markdown(f"⏰ **{time.strftime('%H:%M:%S')}**")

st.write("### Daily Routine Checklist")
completed = {}
for task in routine_tasks:
    completed[task] = st.checkbox(task)

new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    if new_task:
        routine_tasks.append(new_task)
        st.success(f"Added task: {new_task}")
    else:
        st.error("Please enter a task name.")
