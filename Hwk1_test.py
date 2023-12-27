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
    'q5':''.join(datadict['string_4'].split(' ')),
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


def test_Q001():
    assert runTest('q1')

def test_Q002():
    assert answerdict['q2'] == correctAnswers['q2']
    
def test_Q003():
    assert answerdict['q3'] == correctAnswers['q3']
    
def test_Q004():
    assert answerdict['q4'] == correctAnswers['q4']
    
def test_Q005():
    assert answerdict['q5'] == correctAnswers['q5']
    
def test_Q006():
    assert answerdict['q6'] == correctAnswers['q6']

def test_Q007():
    assert answerdict['q7'] == correctAnswers['q7']

def test_Q008():
    assert runTest('q8')

def test_Q009():
    assert answerdict['q9'] == correctAnswers['q9']

def test_Q010():
    assert runListTest('q10')
    
def test_Q011():
    assert runDictTest('q11')


