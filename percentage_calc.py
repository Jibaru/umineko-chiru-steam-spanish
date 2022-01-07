import sys

start_line = 4_483
end_line = 264_452

total_lines = end_line - start_line

current_line = int(sys.argv[1]) - start_line

current_percentage = (current_line * 100) / total_lines

print("{:0.2f}".format(current_percentage))
