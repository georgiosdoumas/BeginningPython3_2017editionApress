#!/usr/bin/python3
def process(inpstring, comment_char = '#', value_seperator = ',', output_sep = ':'):
    inpstring = inpstring.strip()
    clearedstring, _, _ = inpstring.partition(comment_char)
    clearedstring = clearedstring.rstrip()
    if clearedstring is '':
        return
    name, _, value = clearedstring.partition(value_seperator)
    name = name.strip()
    value = value.strip()
    print(name, output_sep, value)
