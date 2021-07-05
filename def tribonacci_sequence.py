def tribonacci(signature, n):
    tribonacci_list = []
    if n == 0:
        return tribonacci_list
    
    if n == 1:
        tribonacci_list.append(signature[n-1])
        return tribonacci_list
    elif n == 2:
        for i in range(len(signature)-1):
            tribonacci_list.append(signature[i])
        return tribonacci_list
        
        for i in range(0,1):
            tribonacci_list.append(tribonacci_list[i] + tribonacci_list[i-1])
        return tribonacci_list
    else:
        for i in range(len(signature)):
            tribonacci_list.append(signature[i])

        for i in range(3,n):
            tribonacci_list.append(tribonacci_list[i-1] + tribonacci_list[i-2] + tribonacci_list[i-3])
        return tribonacci_list
 
