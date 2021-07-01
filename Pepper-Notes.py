#!/usr/bin/env python3

list = [1,2,3,4,5]

for index in range(len(list)):
    list[index] = list[index]**2

print(list)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
same_letter_count = 0
temp_sentence = sentence.split()

for index in temp_sentence:
    if index[0] == index[-1]:
        same_letter_count += 1

same_letter_count = sum(index[0] == index[-1] for index in sentence.split())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#acro = ''
#for words in org.split():
#    if words not in stopwords:
#        acro = acro + words[:1]
#        list_org = org.split()
acro = ''
for words in list_org:
    if words not in stopwords:
        acro = acro + words[:1]
#acro = acro.upper()
accum
acro = acro.upper()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
acro = ''
for words in org.split():
    if words not in stopwords:
        acro += words[0].upper()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
acro = '. '.join(word[:2].upper() for word in sent.split() if word not in stopwords)

acro = []
for word in sent.split():
    if word not in stopwords
        acro.append(word[:2].upper())
acro = '. '.join(acro)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for item in inventory:
    item_desc, quantity, price = item.split(', ')
    print('The store has {} {}, each for {} USD.'.format(quantity, item_desc, price))

for record in inventory
    fields = record.split(', ')
    print('The store has {} {}, each for {} USD.'.format(fields[1], fields [0], fields[2]))

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def stop_at_four(user_list):
    temp_list = []
    i = 0
    while i < len(user_list):
        if temp_list[i] != 4:
            temp_list.append(user_list[i])
            i += 1
        else:
            break
    return temp_list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sublist(lst):
    newl = []
    for item in lst:
        if item == 5:
            break
        newl.append(item)
    return newl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sublists(lst):
    index = 0
    while index < len(lst)
        if lst[index] == 5:
            break
        newl.append(lst[index])
        index += 1
    return newl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_nums(lst):
    newl = []
    index = 0
    for item in lst:
        if lst[index] == 7:
            break
        newl.append(lst[index])
        index += 1
    return newl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def stop_at_z(lst):
    index = 0
    newl = []
    while index < len(lst):
        if lst[index] == 'z':
            break
        newl.append(lst[index])
        index += 1
    return newl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
index = 0
sum2 = 0
while index < len(lst):
    sum2 += lst[index]
    index += 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def beginning(lst):
    newl = []
    index = 0

    while index < len(lst):
        if lst[index] == 'bye':
            break
        newl.append(lst[index])
        index += 1

    return newl[:10]

def beginning(lst):
    newl = []
    index = 0

    while index < len(lst):
        if len(newl) == 10 or lst[index] == 'bye':
            break
        newl.append(lst[index])
        index += 1

    return newl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def q1(sentence):
    rev_sen = []

#    for each word in sentence.split():
#       rev_sen = word[i:-1]

    rev_sen = ' '.join(reversed(word))





~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


pe1 part1

def invert(l):
    index = 0
    l = [int(i) for i in l]
    for nums in l:
        l[index] = 255 - l[index]
        index += 1
    l = [str(i) for i in l]

#invert(['100','200','250'])

def inverted(l):
    index = 0
    newl = [int(i) for i in l]
    for nums in newl:
        newl[index] = 255 - newl[index]
        index += 1
    newl = [str(i) for i in newl]
    return newl

#inverted(['100','200','250'])

if __name__ == '__main__':
    pass


for index in range(len(l)):
    l[index] = str(255 - int(l[index]))

newl = []
for pixel in l:
    newl.append(str(255 - int(pixel)))


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    num_words = len(fp.read().split())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

pe1 part2

#'{:08b}'.format()
#or format(x, '0>8b')



int('{:08b}'.format(cover[1])[:-1] + msgbin[1],2)


num_words = len(fp.read().split())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
str1 = "peter piper picked a peck of pickled peppers"

freq = {}

#for word in str1:
#    if word in freq:
#        freq[word] += 1
#    else:
#        freq[word] = 1

#freq = {i:}


for word in str1:
    freq[word] = freq.get(word,0)

from collections import Counter
freq = Counter(str1)

s1 = "hello"

counts = {}
for letter in s1:
    counts[letter] = counts.get(letter,0) + 1

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sally = "sally sells sea shells by the sea shore"

characters = {}

for chars in sally:
    characters[chars] = characters.get(chars,0) + 1

best_char = max(characters, key=characters.get)
best_char = sorted(characters.items(), key=lambda elem: elem[1])[-1][0]
best_char = sorted(characters, key=characters.get)[-1][0]


currentMax = -1
for k,v in characters.items():
    if v > currentMax:
        currentMax = v
        best_char = k
