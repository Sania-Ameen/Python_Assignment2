# filtering data and saving results to a new file

# import the pandas library
import pandas as pd

# load the dataset into a DataFrame
# read the student.csv file
student_dataset_to_dataframe = pd.read_csv("student.csv")

# filter student where studytime >= 3, internet = 1, and absences <= 5
filtered_student_dataset = student_dataset_to_dataframe[
    (student_dataset_to_dataframe["studytime"] >= 3) &
    (student_dataset_to_dataframe["internet"] == 1) &
    (student_dataset_to_dataframe["absences"] <= 5)
]

# save filtered data to a new csv (high_engagement.csv)
filtered_student_dataset.to_csv("high_engagement.csv", index = False)

# get the number of saved students from filtered_student_dataset and their average grade
number_of_students_saved_in_filtered_dataset = len(filtered_student_dataset)
average_grade_of_students_in_filtered_dataset = filtered_student_dataset["grade"].sum() / len(filtered_student_dataset) # you can also use .mean()

print(f"The number of students in the filtered dataset are: {number_of_students_saved_in_filtered_dataset}")
print(f"The average grade of the students are: {average_grade_of_students_in_filtered_dataset:.2f}") # rounded to two decimal places