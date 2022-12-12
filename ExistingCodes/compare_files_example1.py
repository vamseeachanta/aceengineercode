# import difflib
# from difflib_data import *
#
#
# d = difflib.Differ()
# diff = d.compare(text1_lines, text2_lines)
# print '\n'.join(diff)

file1 = 'K:/aceengineer/tests/cfg/results/app_vertical_riser_vertical_riser_py_west_boreas.yml'
file2 = 'C:/Users/vamsee.achanta/OneDrive - Occidental Petroleum Corporation/Temp/CN/Ref/BOP_Wellhead.yml'
outputfile = 'cfg/results/outfile.txt'

# Method 1, no output
with open(file1) as f1, open(file2) as f2, open(outputfile, 'w') as outfile:
    for line1, line2 in zip(f1, f2):
        if line1 == line2:
            print(line1, end='', file=outfile)


# Method 2, no output
with open(file1, 'r') as file1:
    with open(file2, 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open(outputfile, 'w') as file_out:
    for line in same:
        file_out.write(line)