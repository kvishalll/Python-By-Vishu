# 5.	Write a Python program to copy the contents of a file to another file

# open the input file in read mode
with open('F:\Py By Vishu\Worksheet_3.3_py\input.txt', 'r') as input_file:
    # read the contents of the input file
    contents = input_file.read()

# open the output file in write mode
with open('F:\Py By Vishu\Worksheet_3.3_py\output.txt', 'w') as output_file:
    # write the contents to the output file
    output_file.write(contents)
