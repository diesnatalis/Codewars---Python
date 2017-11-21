def friend(x):
  new_list = []
  for y in range(len(x)):
      if len(x[y])==4:
        new_list.append(x[y])
  return new_list
