def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
  
def longest(a1, a2):
    newl = set()
    for i in a1:
        if i not in newl:
            newl.add(i)
    for j in a2:
        if j not in newl:
            newl.add(j)
    
    return ''.join(sorted(newl))
