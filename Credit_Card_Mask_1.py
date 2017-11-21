def maskify(cc):
    if len(cc)<=4:
       return cc
    else:
        return (cc[-4:]).rjust(len(cc),"#")
        
# rjust This method returns the string right justified in a string of length width. 
# Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s).
