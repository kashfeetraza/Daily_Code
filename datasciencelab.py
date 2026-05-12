# ================================
# Assignment #01 - Python + NumPy
# ================================

import numpy as np

# ================================
# Task 1: Generate Student Dataset
# ================================

np.random.seed(42)  # for reproducibility

# Student IDs
student_ids = np.arange(1001, 1061)

# Marks (60 students, 4 subjects)
marks = np.random.randint(0, 101, size=(60, 4))

print("Student IDs:\n", student_ids)
print("\nMarks Matrix:\n", marks)
print("\nShape:", marks.shape)
print("Data Type:", marks.dtype)


# ================================
# Task 2: Basic Statistical Analysis
# ================================

print("\n--- Statistical Analysis ---")

# Average per subject
avg_subject = np.mean(marks, axis=0)
print("Average per subject:", avg_subject)

# Overall class average
overall_avg = np.mean(marks)
print("Overall class average:", overall_avg)

# Standard deviation
std_dev = np.std(marks, axis=0)
print("Standard deviation per subject:", std_dev)

# Max per subject
max_marks = np.max(marks, axis=0)
print("Maximum per subject:", max_marks)

# Min per subject
min_marks = np.min(marks, axis=0)
print("Minimum per subject:", min_marks)


# ================================
# Task 3: Student Performance Report
# ================================

print("\n--- Performance Report ---")

# Total marks
total_marks = np.sum(marks, axis=1)

# Categories
excellent = total_marks >= 320
good = (total_marks >= 250) & (total_marks < 320)
average = (total_marks >= 200) & (total_marks < 250)
poor = total_marks < 200

print("Excellent students:", np.sum(excellent))
print("Good students:", np.sum(good))
print("Average students:", np.sum(average))
print("Poor students:", np.sum(poor))

print("\nExcellent Student IDs:", student_ids[excellent])
print("Poor Student IDs:", student_ids[poor])


# ================================
# Task 4: Find Top Students
# ================================

print("\n--- Top 5 Students ---")

# Get indices of top 5
top_indices = np.argsort(total_marks)[-5:][::-1]

for i in top_indices:
    print(f"\nStudent ID: {student_ids[i]}")
    print("Total Marks:", total_marks[i])
    print("Subject Marks:", marks[i])


# ================================
# Task 5: Subject Improvement Simulation
# ================================

print("\n--- Programming Marks Improvement ---")

# Copy marks
updated_marks = marks.copy()

# Before
before_prog = marks[:, 1]

# Add 5 to programming (column index 1)
updated_marks[:, 1] = np.minimum(updated_marks[:, 1] + 5, 100)

after_prog = updated_marks[:, 1]

print("Before:", before_prog)
print("After :", after_prog)


# ================================
# Task 6: Identify Weak Students
# ================================

print("\n--- Weak Students ---")

# Count subjects < 40
weak_condition = np.sum(marks < 40, axis=1) >= 2

weak_students_ids = student_ids[weak_condition]
weak_students_marks = marks[weak_condition]

print("Weak Student IDs:", weak_students_ids)
print("Their Marks:\n", weak_students_marks)


# ================================
# Task 7: Reshape + Aggregation
# ================================

print("\n--- Group Analysis ---")

# Reshape
reshaped = marks.reshape(20, 3, 4)

# Total per student in each group
group_totals = np.sum(reshaped, axis=2)

# Average per group
group_avg = np.mean(group_totals, axis=1)

best_group = np.argmax(group_avg)

print("Group Averages:", group_avg)
print("Best Group Index:", best_group)
print("Best Group Average:", group_avg[best_group])


# ================================
# Task 8: Custom Function
# ================================

def student_report(student_id, ids, marks):
    index = np.where(ids == student_id)[0][0]
    
    student_marks = marks[index]
    total = np.sum(student_marks)
    percentage = total / 4
    
    # Grade
    if percentage >= 85:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
    
    return {
        "Marks": student_marks,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }


# Example usage
print("\n--- Student Report Example ---")
report = student_report(1005, student_ids, marks)

print(report)