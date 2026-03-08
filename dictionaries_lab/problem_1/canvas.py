import course_data
data = course_data.actual_data

student = input("Enter the student's name: ")

total = 0
if student in data["roster"]:
    for person in data["assignments"]:
        score = data["assignments"][person]["submissions"].get(student, 0)
        print(f"{person}: {score}%")
        total += score * (data["assignments"][person]["weight"] / 100)
    print(f"Total grade: {total:.2f}%")
else:
    print("Student not found.")


