def is_isogram(string):
  if string == "":
    return True
  else:
    string = string.lower()
    for char in string:
      if string.count(char) > 1:
        return False
    return True
