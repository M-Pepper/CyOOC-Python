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

import exam as student
#import solution2 as student

class Q1(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.given = ' '.join([''.join(
	    random.sample(string.ascii_lowercase,k=random.randint(3,9)))
	    for w in range(random.randint(3,9))])

    def correct(self):
        return ' '.join(reversed(self.given.split()))

    def test_q1(self):
        with self.subTest(points=10):
            self.assertEqual(student.q1(self.given),self.correct())

class Q2(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.given = random.randint(1000,50000000)

    def correct(self):
        return '{:,}'.format(self.given)

    def test_q2(self):
        with self.subTest(points=10):
            self.assertEqual(student.q2(self.given),self.correct())

class Q3(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.a = [random.randint(-100,100) for _ in range(30,70)]
        self.b = [random.randint(-100,100) for _ in range(30,70)]

    def correct(self):
        return list(reversed(sorted(self.a + self.b)))

    def test_q3(self):
        with self.subTest(points=5):
            # Give partial credit if WE have convert to a list
            self.assertEqual(list(student.q3(self.a,self.b)),self.correct())
        with self.subTest(points=5):
            # Give remaining points if THEY converted to a list
            self.assertEqual(student.q3(self.a,self.b),self.correct())

class Q4(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.go_scores = [random.randint(51,100) for _ in range(3)]
        self.no_scores = [random.randint(0,50) for _ in range(3)]

    def correct(self,*scores):
        return 'GO' if (sum(scores)/3.0) > 50.0 else 'NOGO'

    def test_q4(self):
        with self.subTest(points=5):
            self.assertEqual(student.q4(*self.go_scores[:]),self.correct(*self.go_scores))
        with self.subTest(points=5):
            self.assertEqual(student.q4(*self.no_scores[:]),self.correct(*self.no_scores))

class Q5(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.i = random.randint(3,15)
        self.limit = random.randint(30,60)

    def correct(self):
        return [n for n in range(self.limit+1) if ((n%self.i==0) and (n%2==0))]

    def test_q5(self):
        with self.subTest(points=10):
            self.assertEqual(student.q5(self.i,self.limit),self.correct())

class Q6(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.content0 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.'''
        self.content1 = [list(l) for l in self.content0.splitlines()]

        linenumbers = [n for n in range(len(self.content1))]
        random.shuffle(linenumbers)
        self.correct = set(linenumbers[:3])
        for _ in range(3):
            linenumber = linenumbers.pop(0)
            del self.content1[linenumber][random.randint(0,len(self.content1[linenumber])-1)]
        self.content1 = '\n'.join([''.join(w) for w in self.content1])
        self.filenames = ('a.txt','b.txt')

    def test_q6(self):
        f0 = io.StringIO(self.content0)
        f1 = io.StringIO(self.content1)
       
        def side_effect(filename,mode='r',**kwargs):
            if filename == self.filenames[0]:
                return f0
            elif filename == self.filenames[1]:
                return f1
            else:
                raise FileNotFoundError

        with unittest.mock.patch('builtins.open',side_effect=side_effect) as m:
            with self.subTest(points=10):
                submitted = set(student.q6(*self.filenames))
                self.assertEqual(submitted,self.correct)
                

class Q7(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.lst = [random.randint(0,100) for _ in range(50)]
        self.lst.insert(random.randint(25,49),self.lst[random.randint(0,25)])

    def correct(self):
        seen = set()
        for i in self.lst:
            if i in seen:
                return i
            else:
                seen.add(i)

    def test_q7(self):
        with self.subTest(points=10):
            self.assertEqual(student.q7(self.lst),self.correct())

class Q8(unittest.TestCase):
    POINTS=10

    def setUp(self):
        words = []
        for _ in range(10,random.randint(15,30)):
            words.append(''.join([random.choice(string.ascii_lowercase) for _ in range(1,random.randint(2,30))]))
        self.sentence = ' '.join(words)

    def correct(self):
        return len(min(self.sentence.split(),key=len))

    def test_q8(self):
        with self.subTest(points=10):
            self.assertEqual(student.q8(self.sentence),self.correct())

class Q9(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.staticword = 'hell9oworld7'
        self.dynamicword = [random.choice(string.ascii_lowercase) for _ in range(10,random.randint(20,30))]
        self.dynamicnum = random.randint(65,90)
        self.dynamicword.insert(random.randint(0,len(self.dynamicword)//2), str(self.dynamicnum)[0])
        self.dynamicword.insert(random.randint(len(self.dynamicword)//2,len(self.dynamicword)-1),str(self.dynamicnum)[1])
        self.dynamicword = ''.join(self.dynamicword)

    def correct(self,strng):
        chars = []
        for c in strng:
            if c in string.digits:
                chars.append(c)
        return chr(int(''.join(chars)))

    def test_q9(self):
        with self.subTest(points=5):
            self.assertEqual(student.q9(self.staticword),self.correct(self.staticword))
        with self.subTest(points=5):
            self.assertEqual(student.q9(self.dynamicword),self.correct(self.dynamicword))

class Q10(unittest.TestCase):
    POINTS=10

    def setUp(self):
        self.lst = list(range(100))
        del self.lst[random.randint(1,98)]

    def correct(self,strng):
        for i in range(len(self.lst)-1):
            if (self.lst[i+1] - self.lst[i]) != 1:
                return self.lst[i+1]

    def test_q10(self):
        with self.subTest(points=10):
            self.assertEqual(student.q10(self.lst),self.correct(self.lst))

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
