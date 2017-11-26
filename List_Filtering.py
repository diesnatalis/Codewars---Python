def filter_list(l):
  list = []
  for x in range(len(l)):
    if type(l[x]) != str:
      list.append(l[x])
  return list
  
  # In this kata you will create a function that takes a list of non-negative
  # integers and strings and returns a new list with the strings filtered out.
