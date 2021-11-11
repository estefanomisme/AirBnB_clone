import re
line = input()
m = re.search('[^\(\)\.\s]+\.[^\(\)\.\s]+\([^\(\)\.]*\)', line)
if m is None:
    print('No matches')
else:
    print(m.group(0))