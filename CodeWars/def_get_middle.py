def get_middle(s):
    length = len(s)
    middle = int(length // 2)
    
    if length % 2 == 0:
        #return "".join(s[(middle-1):(middle+1)])
        return s[middle - 1:middle + 1]
    else:
        return s[middle]
      
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
