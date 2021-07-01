#!/usr/bin/env python3

def q1(sentence):
    '''
    Given a string of multiple words separated by single spaces,
    return a new string with the sentence reversed. The words
    themselves should remain as they are. For example, given
    'it is accepted as a masterpiece on strategy', the returned
    string should be 'strategy on masterpiece a as accepted is it'.
    '''
    return ' '.join(reversed(sentence.split()))
    pass

def q2(n):
    '''
    Given a positive integer, return its string representation with
    commas seperating groups of 3 digits. For example, given 65535
    the returned string should be '65,535'.
    '''
    return '{:,}'.format(n)
    pass

def q3(lst0, lst1):
    '''
    Given two lists of integers, return a sorted list that contains
    all integers from both lists in descending order. For example,
    given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1].
    The returned list may contain duplicates.
    '''
    return sorted(lst0 + lst1, reverse=True)
    pass

def q4(s1,s2,s3):
    '''
    Given 3 scores in the range [0-100] inclusive, return 'GO' if
    the average score is greater than 50. Otherwise return 'NOGO'.
    '''

    return 'GO' if (s1+s2+s3) / 3 >= 50 else 'NOGO'
    pass

def q5(integer, limit):
    '''
    Given an integer and limit, return a list of even multiples of the
    integer up to and including the limit. For example, if integer==3 and
    limit==30, the returned list should be [0,6,12,18,24,30]. Note, 0 is
    a multiple of any integer except 0 itself.
    '''
    #newl = []
    #for i in range(limit + 1):
    #    if (i%integer == 0) and (i%2 == 0):
    #        newl.append(i)
    #return(newl)
    return [i for i in range((limit+1)) if (i%integer == 0) and (i%2 == 0)]
    pass

def q6(f0, f1):
    '''
    Given two filenames, return a list whose elements consist of line numbers
    for which the two files differ. The first line is considered line 0.
    '''
    #diff_list = []
    #with open(f0, 'r') as fp0, open(f1, 'r') as fp1:
    #    fp0, fp1 = fp0.read().splitlines(), fp1.read().splitlines()
    #for lines in range(len(fp0)):
    #    if fp0[lines] != fp1[lines]:
    #            diff_list.append(lines)
    #return [lines for lines in range(len(fp0)) if fp0[lines] != fp1[lines]]

    #linenumber = 0
    #result = []
    #with open(f0) as file0, open(f1) as file1:
    #    for line0 in file0:
    #        line1 = file1.readline():
    #        if line0 != line1:
    #            result.append(linenumber)
    #        linenumber += 1
    #return result
    return [item[0] for item in enumerate(zip(open(f0),open(f1))) if item[1][0] != item[1][1]]
    pass

def q7(lst):
    '''
    Return the first duplicate value in the given list.
    For example, if given [5,7,9,1,3,7,9,5], the returned value should
    be 7.
    '''
    seen = set()
    #for i in lst:
    #    if i in seen:
    #        return i
    #    else:
    #        seen.add(i)
    #print([seen.add(i) if i not in seen else i for i in lst])[]
    return [j for j in [i if i in seen else seen.add(i) for i in lst] if j is not None][0]
    pass

def q8(strng):
    '''
    Given a sentence as a string with words being separated by a single space,
    return the length of the shortest word.
    '''
    return len(min(strng.split(), key=len))
    pass

def q9(strng):
    '''
    Given an alphanumeric string, return the character whose ascii value
    is that of the integer represenation of all of the digits in the string
    concatenated in the order in which they appear. For example, given
    'hell9oworld7', the returned character should be 'a' which has
    the ascii value of 97.
    '''
    #newl = []
    #for char in strng:
    #    if char.isnumeric() == True:
    #       newl.append(char)
    #[newl.append(char) for char in strng if char.isnumeric() == True]
    return chr(int(''.join([char for char in strng if char.isnumeric() == True])))
    pass

def q10(arr):
    '''
    Given a list of positive integers sorted in ascending order, return
    the first non-consecutive value. If all values are consecutive, return
    None. For example, given [1,2,3,4,6,7], the returned value should be 6. 
    '''
    #for i in range(len(arr)-1):
    #   if arr[i+1] - arr[i] != 1:
    #        return arr[i+1]
    #return int(''.join([str(arr[i+1]) for i in range(len(arr)-1) if arr[i+1] - arr[i] != 1]))
    return [arr[i+1] for i in range(len(arr)-1) if arr[i+1] - arr[i] != 1][0]
    pass