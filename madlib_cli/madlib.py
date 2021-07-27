import re
from typing import Tuple
print("""=== Welcome to our game ===
=== in this game you will be asked to entet some names,adjectives and verbs ===
=== and at the end a statment will be shown to you ===
""")

values=[]

def read_template(file_path):
    
    file=open(file_path,'r')
    return file.read().strip()
      
   


def get_inputs(list):
    for x in list:
        values.append(input(f'please enter a {x} :< '))

def remove_words(list,string):
    for x in list:
        string=string.replace(x,'',1)
    print (string)
    
    return string

def parse_template(string):
    inputs=tuple(re.findall("{(.*?)}",string))
    
    
    return (remove_words(inputs,string),inputs)

def merge(string,tuple):
    string=string.format(*tuple)
    print (string)
    return string


if __name__ == "__main__":
    statment=read_template("assets/madlib.txt")
    strip_statment,variables=parse_template(statment)
    print(strip_statment)
    get_inputs(variables)
    print(tuple(values))
    merge(strip_statment,tuple(values))



# merge(parse_template(read_template("assets/dark_and_stormy_night_template.txt")),get_inputs(variables))



