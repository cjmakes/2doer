import sys
import re

todo_line = re.compile(r"^((\#)|(\/{2}))([ ]){0,1}(TODO).*$")
todo_check = re.compile(r"(TODO).*$")
line_number = 0

print("TODO")
print("====")

for line in sys.stdin:
    match = todo_line.match(line)
    if match:
        print("- [  ] %d:%s" %
                (line_number , re.search(todo_check, line).group()[4:]))
    line_number += 1
