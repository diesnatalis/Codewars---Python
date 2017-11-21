def is_isogram(string):
    return len(string) == len(set(string.lower()))
    
# set() -> https://docs.python.org/3/tutorial/datastructures.html
