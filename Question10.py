# design a reusable function for searching within text files

def find_lines_containing(filename,keyword):
   matching_lines_in_text_file = []
   # handle case-insensitive searches
   keyword_lower = keyword.lower()

   # open a file and find all matc
   with open(filename, "r", encoding="utf-8") as file:
       for i, line in enumerate(file, start=1):
        # check if keyword is already existing in the line
           if keyword_lower in line.lower():
        # if it is save the line number with the text
               matching_lines_in_text_file.append((i, line.strip()))

   return matching_lines_in_text_file

# assign a filename and keyword
filename = "sample-file.txt"
keyword = "lorem"

matching_lines = find_lines_containing(filename, keyword)

# print the amount of matching lines
print(f"The number of matching lines are:", {len(matching_lines)})

# print the first 3 matching lines
print("The first 3 matching lines:")
for line in matching_lines[:3]:
    print(f"Line {line[0]}: {line[1]}")
