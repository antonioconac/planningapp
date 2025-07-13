import streamlit as st
from backend import functions as f

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Full Weekly Schedule</h1>", unsafe_allow_html=True)
st.markdown("---")

planner_dict = f.get_planner()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
periods = ['Morning', 'Afternoon', 'Evening']

# Start HTML table
html = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        text-align: center;
    }
    th, td {
        border: 1px solid #ccc;
        padding: 8px;
        vertical-align: top;
    }
    th {
        background-color: #f4f4f4;
    }
    td {
        white-space: pre-line;
    }
</style>

<table>
    <tr>
        <th></th>
"""

# Table header (days)
for day in days:
    html += f"<th>{day}</th>"
html += "</tr>"

# Table rows (periods)
for period in periods:
    html += f"<tr><th>{period}</th>"
    for day in days:
        tasks = planner_dict.get(day.lower(), {}).get(period.lower(), [])
        cell = "<br>".join(tasks) if tasks else ""
        html += f"<td>{cell}</td>"
    html += "</tr>"

html += "</table>"

# Render the HTML
st.markdown(html, unsafe_allow_html=True)