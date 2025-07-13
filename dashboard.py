import streamlit as st
from backend import functions as f

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Weekly Planner</h1>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

planner_dict = f.get_planner()

left_column, middle_column, right_column = st.columns(3)

with left_column.form("planner"):
    st.write("Pick the day and the day period.")
    day = st.selectbox(
        "What day do you prefer?",
        ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    )
    dayPeriod = st.selectbox(
        "What period of the day do you prefer?",
        ('Morning', 'Afternoon', 'Evening')
    )
    new_activity = st.text_input("Type in the activity you want to do.")
    submitted = st.form_submit_button("Submit my choices.")

    if submitted and new_activity.strip():
        f.add_task_to_specific_day(planner_dict, day, dayPeriod, new_activity)
        f.save_planner(planner_dict)
        st.success(f"Task '{new_activity}' added to {day} {dayPeriod}")

with middle_column:
    st.markdown("<h2 style='text-align: center;'>Overview</h2>", unsafe_allow_html=True)
    st.markdown(
        "This weekly planner helps the user organize and manage the tasks across the week.<br>"
        "<h4>To add a new activity, an user must:</h4>"
        "• Select a day and a day period<br>"
        "• Write the new activity and click 'Submit my choices.'<br><br>"
        "<h4>To see the activities, an user must:</h4>"
        "• Select a day and a day period<br><br>"
        "<h4>To clear an activity, an user must:</h4>"
        "• Check the checkbox for the specific activity that needs to be cleared.",
        unsafe_allow_html=True
    )

with right_column:
    # These dropdowns work immediately because they're not inside a form
    dayToGet = st.selectbox("Pick a day to display the planner:",
                            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                            key="display_day")
    dayPeriodToGet = st.selectbox("Pick a day period to display the planner:",
                                  ['Morning', 'Afternoon', 'Evening'],
                                  key="display_period")

    tasks = f.access_specific_todos(planner_dict, dayToGet, dayPeriodToGet)

    # Display tasks and allow instant removal when checkbox is ticked
    for task in tasks.copy():
        if st.checkbox(task, key=f"{dayToGet}_{dayPeriodToGet}_{task}"):
            f.remove_task(planner_dict, dayToGet, dayPeriodToGet, task)
            f.save_planner(planner_dict)
            st.success(f"Task '{task}' removed.")
            st.rerun()