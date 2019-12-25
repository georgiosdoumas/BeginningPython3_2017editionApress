#!/usr/local/bin/python3

def process(inpstring, comment_char = '#', value_seperator = ','):
    inpstring = inpstring.strip()
    clearedstring, _, _ = inpstring.partition(comment_char)
    clearedstring = clearedstring.rstrip()
    if clearedstring is '':
        return
    name, _, value = clearedstring.partition(value_seperator)
    name = name.strip()
    value = value.strip()
    print(name, ':', value)

filesharp = 'page250.txt'
filesemicol = 'page250b.txt'
try:
    with open(filesharp) as f:
        for line in f.readlines():
        # for line in f:  ## another way to read it line-by-line
            process(line)
except Exception as e:
    print("Something went wrong while opening the file:", e)

print("Now we will read the other file all at once")
try:  
    with open(filesemicol) as f:
        whole_text = f.read()
        f.close()
        text_lines = whole_text.split('\n')
        for line in text_lines:
            process(line, ';', '=')
except Exception as e:
    print("Something went worng:", e)
