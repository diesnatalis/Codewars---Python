def square_digits(num):
    #num = str(num)
    list = []
    for char in str(num):
      list.append(int(char)**2)
    s = ''.join(map(str, list))
    return(int(s))
 
 
# In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out.
# Note: The function accepts an integer and returns an integer
