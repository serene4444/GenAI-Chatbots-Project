"""
Created on 07/09/2025

@author: Serene Plummer
"""
import dash
from dash import html, dash_table

students = {
    1: {"name": "Liam", "surname": "Johnson", "age": 17, "grade": 88},
    2: {"name": "Emma", "surname": "Smith", "age": 16, "grade": 92},
    3: {"name": "Noah", "surname": "Williams", "age": 18, "grade": 75},
    4: {"name": "Olivia", "surname": "Brown", "age": 17, "grade": 85},
    5: {"name": "Elijah", "surname": "Jones", "age": 17, "grade": 90},
    6: {"name": "Ava", "surname": "Garcia", "age": 16, "grade": 95},
    7: {"name": "James", "surname": "Martinez", "age": 18, "grade": 81},
    8: {"name": "Sophia", "surname": "Rodriguez", "age": 17, "grade": 87},
    9: {"name": "Benjamin", "surname": "Lee", "age": 16, "grade": 78},
    10: {"name": "Isabella", "surname": "Hernandez", "age": 18, "grade": 93},
    11: {"name": "Lucas", "surname": "Lopez", "age": 17, "grade": 86},
    12: {"name": "Mia", "surname": "Gonzalez", "age": 16, "grade": 89},
    13: {"name": "Henry", "surname": "Wilson", "age": 17, "grade": 84},
    14: {"name": "Charlotte", "surname": "Anderson", "age": 16, "grade": 91},
    15: {"name": "Alexander", "surname": "Thomas", "age": 18, "grade": 82},
    16: {"name": "Amelia", "surname": "Taylor", "age": 17, "grade": 94},
    17: {"name": "William", "surname": "Moore", "age": 16, "grade": 77},
    18: {"name": "Harper", "surname": "Jackson", "age": 17, "grade": 88},
    19: {"name": "Ethan", "surname": "Martin", "age": 18, "grade": 80},
    20: {"name": "Evelyn", "surname": "White", "age": 17, "grade": 96}
}

student_data = [
    {"id": key, **value} for key, value in students.items()
]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Student Data", style = {"color": "#8d68ad"}),
    dash_table.DataTable(
        data = student_data,
        page_size = 5,
        columns=[
            {"name": "ID", "id": "id"},
            {"name": "Name", "id": "name"},
            {"name": "Surname", "id": "surname"},
            {"name": "Age", "id": "age"},
            {"name": "Grade", "id": "grade"}
        ],
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "left"}
        )
    ])

if __name__ == "__main__":
    app.run(debug = True)