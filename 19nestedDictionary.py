students = {
    "Guru": {
        "Math": 85,
        "Science": 90,
        "English": 88
    },
    "Lucky": {
        "Math": 78,
        "Science": 82,
        "English": 80
    },
    "Adya": {
        "Math": 92,
        "Science": 95,
        "English": 94
    }
}

def average_grade(students, name):
    if name not in students:
        return f"{name} not found"

    grades = students[name].values()
    return sum(grades) / len(grades)

print(average_grade(students, "Guru"))
