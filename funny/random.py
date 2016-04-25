#coding:utf-8
import random

# http://code.activestate.com/recipes/410692/
# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def print_header():
    print '************************'
    print '** A Simple Math Quiz **'
    print '************************'
    print '1.Addition'
    print '2.Subtraction'
    print '3.Multiplication'
    print '4.Interger Division'
    print '5.Exit'
    print '-----------------------'

def get_random():
    v1 = random.randint(1, 20)
    v2 = random.randint(1, 20)
    return [v1,v2]

def calc(questions,correct,error,mark):
    numbers = get_random()
    print 'Enter your answer' 
    questions += 1
    student_answer =raw_input(mark.join(map(str,numbers))+' = ')
    answer = 0
    for mark in switch(mark):
        if mark(' + '):
            answer = numbers[0] + numbers[1]
            break
        if mark(' - '):
            answer = numbers[0] - numbers[1]
            break
        if mark(' * '):
            answer = numbers[0] * numbers[1]
            break
        if mark(' // '):
            answer = numbers[0] // numbers[1]
            break
    #print answer,student_answer
    if str(answer) == student_answer:
        correct += 1
        print 'Correct.'
    else:
        error += 1
        print 'Incorrect.'
    print_choice_option(questions,correct,error)

def print_choice_option(questions = 0,correct = 0,error = 0):
    option = raw_input('Enter your choice:')
    for option in switch(option):
        if option('1'):
            calc(questions,correct,error,' + ')
            break
        if option('2'):
            calc(questions,correct,error,' - ')
            break
        if option('3'):
            calc(questions,correct,error,' * ')
            break
        if option('4'):
            calc(questions,correct,error,' // ')
            break
        if option('5'):
            print 'Exit the Quiz'
            print '-----------------------'
            print 'You answered %d questions with %d correct'%(questions,correct)
            print 'Your score is %2.1f%%.Thank you.'%((float(correct)/questions)*100)
            return
        if option():
            print 'error numbers input!'
            break
    
if __name__=='__main__':
    print_header()
    print_choice_option()
