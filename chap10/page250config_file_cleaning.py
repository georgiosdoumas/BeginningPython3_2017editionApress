#!/usr/local/bin/python3

def process(inpstring):
    inpstring = inpstring.strip()
    clearedstring, _, _ = inpstring.partition('#')
    clearedstring = clearedstring.rstrip()
    if clearedstring is '':
        return
    name, _, value = clearedstring.partition(',')
    name = name.strip()
    value = value.strip()
    print(name, ':', value)
    
with open('page250.txt') as f:
    for line in f.readlines():  # for line in f:  is also good
        process(line)

print("Now we will read the whole file at once")
with open('page250.txt') as f:
    whole_text = f.read()
    f.close()
    text_lines = whole_text.split('\n')
    for line in text_lines:
        process(line)
