import re
import sys
with open(sys.argv[1], "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        cleaned_line = re.sub(r'-{2,}', '-', line)  # Replace 2 or more dashes with a single dash
        if(cleaned_line[0]=="-"):
            cleaned_line = cleaned_line[1:]
        if (cleaned_line[-1]=="-"):
            cleaned_line = cleaned_line[0:-1]
        outfile.write(cleaned_line)
