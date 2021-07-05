def find_short(s):
    l= (sorted(s.split(), key=len))
    return len(l[0])
  
def find_short(s):
    return min(len(x) for x in s.split())
