def high_and_low(numbers):
    newl = numbers.split()
    numbers = sorted([int(newl[i]) for i in range(len(newl))], reverse=True)
    return ' '.join([str(numbers[0]), str(numbers[-1])])

def high_and_low(numbers):
    n = map(int, numbers.split(''))
    return str(max(n)) + ' ' + str(min(n))

def high_and_low(numbers):
    new_num = [int(i) for i in numbers.split()]
    return '{} {}'.format(max(new_num), min(new_num))

high_and_low=lambda x:max(x.split(' '),key=int)+' '+min(x.split(' '),key=int)
