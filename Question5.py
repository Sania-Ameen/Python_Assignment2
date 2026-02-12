# create a new categorical variable and generate a grouped summary table

# import pandas library
import pandas as pd

# load student.csv dataset into a dataframe
student_dataset_to_dataframe = pd.read_csv("student.csv")

# fence the grades using 'bins' --> low, medium and high
new_grade_column_boundaries = [0, 9, 14, float("inf")]

# label the grade band by defining the names
new_grade_column_labels = ["Low (0 to 9)", "Medium (10-14)", "High (15 and above)"]

# look at each student's grade, decide the range and corresponding label then save it in the grade_band column
student_dataset_to_dataframe["grade_band"] = pd.cut(student_dataset_to_dataframe["grade"], bins = new_grade_column_boundaries, labels= new_grade_column_labels, right = True)

# group the students based on grade_band (low, medium, high)
groups = student_dataset_to_dataframe.groupby("grade_band", observed=False) # using observed will allow program to conclude without any errors should a category have no students

# calculate the information for the summary table (number of students, average absences, percentage of students with internet access)
total_number_of_students = groups["grade"].count()
average_number_of_absences = groups["absences"].sum() / groups["absences"].count()
percentage_of_students_with_internet_access = (groups["internet"].sum() / groups["internet"].count()) * 100

# combine all previous information into one single table
final_summary_table = pd.DataFrame({
    "total_number_of_students": total_number_of_students,
    "average_number_of_students": average_number_of_absences,
    "percentage_of_student_with_internet_access": percentage_of_students_with_internet_access
})

# save new dataset (summary) into a separate csv file
final_summary_table.to_csv("student_bands.csv")

# print final csv
print(final_summary_table)
