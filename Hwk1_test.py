#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 07:37:22 2023

@author: munsky
"""

import pickle
import numpy as np


 # Read the lines and store numbers as floats and strings as strings
fn = 'Hwk1Data.pkl'
    #Read and print 
with open(fn, 'rb') as file:
    datadict = pickle.load(file)
    
string_2 = 'i would like to be uppercase'
piStr ='%5.3e'%(np.pi**datadict['nPower'])
myDict = {datadict['Student_IDs'][i]:datadict['Student_names'][i] for i in range(len(datadict['Student_names']))}

correctAnswers = {'q1':'Hello my name is Name',
    'q2':string_2.upper(),
    'q3':f"I bought {datadict['number']} {datadict['fruit']} on {datadict['day']}.",
    'q4':datadict['string_4'].count('a'),
    'q5':datadict['string_5'][datadict['string_5']!=' '],
    'q6':len(datadict['string_6']),
    'q7':piStr,
    'q8':sum(datadict['xData'])/len(datadict['xData']),
    'q9':datadict['xData'][-1],
    'q10':list(set(datadict['List10'])),
    'q11':myDict,
    'q12':datadict['List12'][::2]}
  
fn = 'Hwk1Answers.pkl'
    #Read and print 
with open(fn, 'rb') as file:
    answerdict = pickle.load(file)
  
def is_numeric(var):
    return isinstance(var, (int, float, complex))

def checkTolerance(a,b):
    relAbsDiff = abs(a-b)/abs(b)
    print(f'relAbsDiff = {relAbsDiff}')
    return relAbsDiff<=0.05

def runTest(q):  # Test for floats and simple strings
    if is_numeric(correctAnswers[q]):
        return checkTolerance(answerdict[q],correctAnswers[q])
    else:
        return answerdict[q].lower() == correctAnswers[q].lower()

def runListTest(q):
    answerList = answerdict[q]
    correctList = correctAnswers[q]
    if len(answerList)!=len(correctList):
        return False
    else:
        for i in range(len(correctList)):
            if answerList[i]!=correctList[i]:
                return False
    return True
        
def runDictTest(q):
    answerList = answerdict[q]
    correctList = correctAnswers[q]
    if len(answerList)!=len(correctList):
        return False
    else:
        for key in correctList:
            if answerList[key]!=correctList[key]:
                return False
    return True


def test_Q1():
    assert runTest('q1')

def test_Q2():
    assert answerdict['q2'] == correctAnswers['q2']
    
def test_Q3():
    assert answerdict['q3'] == correctAnswers['q3']
    
def test_Q4():
    assert answerdict['q4'] == correctAnswers['q4']
    
def test_Q5():
    assert answerdict['q5'] == correctAnswers['q5']
    
def test_Q6():
    assert answerdict['q6'] == correctAnswers['q6']

def test_Q7():
    assert answerdict['q7'] == correctAnswers['q7']

def test_Q8():
    assert runTest('q8')

def test_Q9():
    assert answerdict['q9'] == correctAnswers['q9']

def test_Q10():
    assert runListTest('q10')
    
def test_Q11():
    assert runDictTest('q11')


