Description of Files 

# Question 1 
In this program, the file 'sample-file.txt' is read and split into tokens or words. All words must meet the given requirements (lowercase, punctuation and alphabetic characters).
Words are then counted in terms of their frequency and the top 10 most frequenct words in decending order are printed. 

# Question 2
This program imports the library 're' while spliting and reading a sample file (sample-file.txt) into tokens. 
Tokens must meet the given requirements (punctuation, alphabetic characters and lower case). 
The program then constructs bigrams and counts their frquency, essentially outputting the 5 most frequent bigrams in decending order. 

# Question 3


# Question 4 
This program takes the dataset of a given .csv file (student.csv) and turns it into a DataFrame using adequate libraries. The porgram then filters through the datset and finds the students for which the criteria is met. 
This new dataset is then stored into a new .csv file (high_engagement.csv) and an output of the number of students as well as their average grade is printed. 

# Question 5 
This program takes an already created .csv file (student.csv) and creates a new categorical variable and generates a grouped summary table. 
The grouped summary table for each nand shows the number of students, average absences and percentage of students with internet access. 
The new table is then saved into a new .csv file (student_bands.csv). 

# Question 6 
This program takes a fiven .csv file (crime.csv), loads it into a DataFrame and creates a new column using the information based on other columns in dataset. 
The data is then grouped via the column and an average is calculated (PctUnemployed). 
Adequate information is then printed out. 

# Question 7 
Using external libraries, this program scarpes a webpage, extracts and prints a page title, then extracts the first paragraph of the main article content of that page. 
Then, using a for loop, the program loops through the paragraphs and matches one that meants the requirements (at least 50 characters after stripping whitespace). 

# Question 8 
Similar to the previous program, this program takes the same webpage, scrpaes it, this time extracting all 'h2' section heading then filters words and text in accordance to the question. 
The new headings are then saved to a .txt file (headings.txt) with each heading in order and on their own line. 

# Question 9 
This program uses external libraries to scrape a webpage and locate the first table inside of the main content area that meets the requirements for the number of data rows (3). 
It then extracts table headers if they are present, or creates automatic header titles. If rows are fewer than columns, empty strings are created. 
New table data is stroed to wiki_table.csv file. 

# Question 10 
Using a function, this program takes a given file with a given keyword, loops through the file contents while counting the number of matching lines in the file, 
then prints out the number of matching lines as well as the first 3 matching lines. 
