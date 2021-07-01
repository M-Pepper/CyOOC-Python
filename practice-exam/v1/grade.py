#!/usr/bin/env python3

import unittest
import unittest.mock
import importlib
import sys
import random
import itertools
import os
import string
import io
import contextlib
import re
from pathlib import Path


import exam as student
__unittest = True

class Q1(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q1'

    def shortDescription(self):
        return 'q1'

    def setUp(self):
        self.numFloats = int(random.randint(1,100))
        self.floatList = [float(random.randrange(1,100)) for x in range(self.numFloats)]
        self.floatStr = ','.join([str(x) for x in self.floatList])
        
    '''
    def q1(floatstr):
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the 
    argument as elements in the list.
    
    newlist = []
    for y in floatstr.split():
        newlist.append(float(y))
    return newlist
    '''
 
    def test_q1(self):
        submitted = student.q1(self.floatStr)
        
        with self.subTest(points=2):
            self.assertIsNotNone(submitted)
       
        with self.subTest(points=8):
            self.assertEqual(submitted,self.floatList)
        
class Q2(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q2'

    def shortDescription(self):
        return 'q2'

    def setUp(self):
        self.numFloats = int(random.randint(1,100))
        self.arglist = [1,2,3,4,5]
        self.dynlist = [float(random.randrange(1,100)) for x in range(self.numFloats)]
    '''
    def q2(*args):
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''

    def test_q2(self):
        submitted = student.q2(*self.arglist)
        answer = sum(self.arglist)/len(self.arglist)
        
        with self.subTest(points=2):
            self.assertIsNotNone(submitted)
       
        with self.subTest(points=4):
            self.assertEqual(submitted,answer)
       
        with self.subTest(points=4):
            submitted = student.q2(*self.dynlist)
            answer = sum(self.dynlist)/len(self.dynlist)
            self.assertEqual(submitted,answer)

class Q3(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q3'

    def shortDescription(self):
        return 'q3'
    '''
    def q3(lst, n):
    Given a list (lst) and a number of items (n), return a new 
    list containing the last n entries in lst.
    '''

    def setUp(self):
        self.arglist = [1,2,3,4,5]
        self.staticn = 2
        self.dynlist = [int(random.randint(1,100)) for x in range(random.randint(10,100))]
        self.dynn = random.randint(5,len(self.dynlist) - 3)
        
    def test_q3(self):
        submitted = student.q3(self.arglist, self.staticn)
        answer = self.arglist[-1 * self.staticn:]
        
        with self.subTest(points=2):
            self.assertIsNotNone(submitted)
       
        with self.subTest(points=4):    #Static Test
            self.assertEqual(submitted,answer)

        with self.subTest(points=4):    #Dynamic Test
            submitted = student.q3(self.dynlist, self.dynn)
            answer = self.dynlist[-1 * self.dynn:]
            self.assertEqual(submitted,answer)


class Q4(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q4'

    def shortDescription(self):
        return 'q4'
    '''
    def q4(strng):
    Given an input string, return a list containing the ordinal numbers of 
    each character in the string in the order found in the input string.
    '''

    def setUp(self):
        self.argstr = 'hello'
        self.content = ' '.join([''.join(random.sample(string.ascii_lowercase,k=random.randint(5,15))) for _ in range(5,random.randint(10,25))])
 
    def test_q4(self):
        submitted = student.q4(self.argstr)
        answer = [ord(x) for x in list(self.argstr)]
        
        with self.subTest(points=2):
            self.assertIsNotNone(submitted)
       
        with self.subTest(points=4):    #Static Test
            self.assertEqual(submitted,answer)
        
        with self.subTest(points=4):    #Dynamic Test
            submitted = student.q4(self.content)
            answer = [ord(x) for x in list(self.content)]
            self.assertEqual(submitted,answer)



class Q5(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q5'

    def shortDescription(self):
        return 'q5'
    '''
    def q5(strng):
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''

    def setUp(self):
        self.argstr = "Long sentence to test the function's capabilities"
        self.content = ' '.join([''.join(random.sample(string.ascii_lowercase,k=random.randint(5,15))) for _ in range(5,random.randint(10,25))])
 
    def test_q5(self):
        submitted = student.q5(self.argstr)
        answer = tuple(list(self.argstr.split(' ')))
        
        with self.subTest(points=2):
            self.assertIsNotNone(submitted)
       
        with self.subTest(points=4):    #Static Test
            self.assertEqual(submitted,answer)
        
        with self.subTest(points=4):    #Dynamic Test
            submitted = student.q5(self.content)
            answer = tuple(list(self.content.split(' ')))
            self.assertEqual(submitted,answer)


class Q6(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q6'

    def shortDescription(self):
        return 'q6'
    '''
    def q6():
    Given an input string similar to the below, craft a regular expression  
    pattern to match and extract the date, time, and temperature in groups  
    and return this pattern. Samples given below.
    Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
    Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C
    '''

    def setUp(self):
        self.goodpat = r"Date:\s+([0-9]+/[0-9]+/[0-9]+)\s+Time:\s+([0-9]+:[0-9]+\s[a|p]\.m\.)\s+Temperature:\s+([0-9.]+\s[KkFfCc])"
        #self.goodpat = r"Date: (\d+/\d+/\d+) Time: (\d+:\d+ .\.m\.) Temperature: ([\d\.]+ [FfCc])"
        self.testlogs = ["Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F", 
                         "Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C"]
        self.testlogs.append("Date: {:02d}/{:02d}/{:04d} Time: {:01d}:{:02d} {!s}.m. Temperature: {:0>.1f} {!s}".format(random.randint(1,12), random.randint(1,28), random.randint(1900,2019), random.randint(1,12), random.randint(0,59), 'p' if random.randint(0,1)==0 else 'a', random.randint(10,14000)/100, 'C' if random.randint(0,1)==0 else 'F'))
 
    def test_q6(self):
        submitted = student.q6()
        
        with self.subTest(points=1):
            self.assertIsNotNone(submitted)
       
        for stng in self.testlogs:
            with self.subTest(points=3):
                studentFound = re.findall(submitted, stng)
                knownFound = re.findall(self.goodpat, stng)
                self.assertEqual(knownFound, studentFound)
                    

class Q7(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)

    def id(self):
        return 'q7'

    def shortDescription(self):
        return 'q7'

    def setUp(self):
        self.filename = ''.join(random.sample(string.ascii_lowercase, k=random.randint(5,15)))
        self.content = '\n'.join([''.join(random.sample(string.ascii_lowercase,k=random.randint(5,15))) for _ in range(5,random.randint(10,25))])
    
    '''
    def q7(filename):
    Given a filename, open the file and return the length of the first line 
    in the file excluding the line terminator.
    '''

    def test_q7(self):
        fp = io.StringIO(self.content)
        with unittest.mock.patch('builtins.open',return_value=fp):
            submitted = student.q7(self.filename)
        answer = len(self.content.split('\n')[0])
        
        with self.subTest(points=2):
            self.assertIsNotNone(submitted)

        with self.subTest(points=8):
            self.assertEqual(submitted,answer)



class Q8(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)

    def id(self):
        return 'q8'

    def shortDescription(self):
        return 'q8'
    
    def getStopList(self, wordlist):
        lst = []
        for word in wordlist:
            pass
            if word.lower() == 'stop':
                break
            lst.append(word)
        return lst

    def setUp(self):
        self.filename = ''.join(random.sample(string.ascii_lowercase,
            k=random.randint(5,15)))
        #Generate a list with 'stop' in the list
        self.wordsstop = [''.join(random.sample(string.ascii_lowercase,
            k=random.randint(1,9))) for _ in range(6,20)]
        self.wordsstop.append('stop')
        self.wordsstop.extend([''.join(random.sample(string.ascii_lowercase,
            k=random.randint(1,9))) for _ in range(6,20)])
        self.wordsstoplist = self.getStopList(self.wordsstop)
        


    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    '''
    def q8(filename,lst):
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in 
    the list. If "stop" is not found in the list, write the entire list to 
    the file on separate lines.
    '''

    def test_q8(self):
        student.q8(self.filename,self.wordsstop)
        
        with self.subTest(points=2):
            self.assertTrue(os.path.isfile(self.filename), 'File does not exist')    
        with self.subTest(points=8):
            self.assertTrue(os.path.isfile(self.filename), 'File does not exist')
            with open(self.filename) as fp:
                alllines = fp.readlines()
                self.assertEqual(len(alllines), len(self.wordsstoplist), 'Number of lines is invalid')
                for stud,ans in itertools.zip_longest(alllines, self.wordsstoplist, fillvalue='stop'):
                    self.assertEqual(stud.strip(), ans.strip(), 'Line in file is not correct')
            

class Q9(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q9'

    def shortDescription(self):
        return 'q9'
    
    def correct(self, miltime):
        if miltime >= 300 and miltime < 1200:
            return "Good Morning"
        elif miltime >= 1200 and miltime < 1600:
            return "Good Afternoon"
        elif miltime >= 1600 and miltime < 2100:
            return "Good Evening"
        elif miltime >= 2100 or miltime < 300:
            return "Good Night"
    
    '''
    def q9(miltime):
    Given the military time in the argument miltime, return a string 
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''

    def setUp(self):
        randTime = int(random.randint(0,23)) * 100 + int(random.randint(0,59))
        self.timeTest = randTime
        self.argval = self.correct(randTime)
 
    def test_q9(self):
        submitted = student.q9(self.timeTest)
        
        with self.subTest(points=2):
            self.assertIsNotNone(submitted)
       
        with self.subTest(points=8):
            self.assertEqual(self.argval, submitted)


class Q10(unittest.TestCase):
    POINTS=10

    def __str__(self):
        return "%s " % (self._testMethodName)
 
    def id(self):
        return 'q10'

    def shortDescription(self):
        return 'q10'

    def correct(self, numlist):
        for i in numlist:
            if i < 0:
                return False
        return True

    '''
    def q10(numlist):
    Given the argument numlist as a list of numbers, return True if all 
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''

    def setUp(self):
        self.argdict = [ [int(random.randint(1,100))] * int(random.randint(5,100)) ,
                         [int(random.randint(-100,-1))] * int(random.randint(5,100)) ,
                         [int(random.randint(-100,100))] * int(random.randint(5,100)) ,
                         [int(random.randint(-100,100))] * int(random.randint(5,100)) ,
                         [int(random.randint(0,100))] * int(random.randint(5,100)) ]

    def test_q10(self):
        
        for numlst in self.argdict:
            with self.subTest(points=2):
                answer = self.correct(numlst)
                submitted = student.q10(numlst)
                self.assertEqual(submitted,answer)
        

class GradeTestResult(unittest.TextTestResult):

    def __init__(self,stream,descriptions,verbosity):
        self.successes = 0
        self.grade = 0
        self.possible = 0
        unittest.TextTestResult.__init__(self,stream,descriptions,verbosity)

    def startTest(self,test):
        self.possible += test.POINTS
        unittest.TextTestResult.startTest(self,test)

    def addSubTest(self,test,subtest,outcome):
        if outcome == None:
            self.successes += subtest.params['points']
        self.grade = self.successes/self.possible*100
        unittest.TextTestResult.addSubTest(self,test,subtest,outcome)

    def addFailure(self,test,err):
        pass

    def __str__(self):
        return '{}/{} points earned ({:.2f}%)'.format(self.successes,self.possible,self.grade)

class GradeTestRunner(unittest.TextTestRunner):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def run(self, test):
        result = super().run(test)
        #self.report(result)
        return result

    def report(self, result):
        #result_bytes = pickle.dumps(result.grade)
        result_bytes = pickle.dumps(result)
        result_msg = struct.pack('!H{}s'.format(len(result_bytes)),len(result_bytes),result_bytes)

        s = socket.socket()
        context = ssl.SSLContext()
        context.verify_mode = ssl.CERT_NONE
        context.check_hostname = False
        context.load_cert_chain(**configure.NetworkConfiguration.identity)
        s = context.wrap_socket(s,server_side = False)
        
        s.connect(configure.NetworkConfiguration.endpoint)
        s.sendall(result_msg)
        s.close()


if __name__ == '__main__':
    for i in range(len(sys.argv)):
        sys.argv[i] = 'Q'+sys.argv[i]

    runner = GradeTestRunner(resultclass = GradeTestResult)
    test = unittest.main(exit=False,verbosity=9,failfast=False,testRunner=runner,argv=sys.argv)
    print(test.result)


