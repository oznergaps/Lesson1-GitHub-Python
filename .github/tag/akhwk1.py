import pickle
import numpy as np

with open('Hwk1Data.pkl','rb')as f:datadict=pickle.load(f)
s2='i would like to be uppercase';piStr='%5.3e'%(np.pi**datadict['nPower'])
myDict={datadict['Student_IDs'][i]:datadict['Student_names'][i]for i in range(len(datadict['Student_names']))}
cA={'q1':'Hello my name is Name','q2':s2.upper(),'q3':f"I bought {datadict['number']} {datadict['fruit']} on {datadict['day']}.",'q4':datadict['string_4'].count('a'),'q5':''.join(datadict['string_5'].split(' ')),'q6':len(datadict['string_6']),'q7':piStr,'q8':sum(datadict['xData'])/len(datadict['xData']),'q9':datadict['xData'][-1],'q10':list(set(datadict['List10'])),'q11':myDict,'q12':datadict['List12'][::2]}
with open('Hwk1Answers.pkl','rb')as f:adt=pickle.load(f)
def f(v):return isinstance(v,(int,float,complex))
def c(a,b):return abs(a-b)/abs(b)<=0.05
def t(q):return c(adt[q],cA[q])if f(cA[q])else adt[q].lower()==cA[q].lower()
def l(q):a,b=adt[q],cA[q];return len(a)==len(b)and all(a[i]==b[i]for i in range(len(b)))
def u(q):a,b=adt[q],cA[q];return len(a)==len(b)and a.sort()==b.sort()
def d(q):a,b=adt[q],cA[q];return len(a)==len(b)and all(a[k]==b[k]for k in b)
def testQ001():assert t('q1')
def testQ002():assert adt['q2']==cA['q2']
def testQ003():assert adt['q3']==cA['q3']
def testQ004():assert adt['q4']==cA['q4']
def testQ005():assert adt['q5']==cA['q5']
def testQ006():assert adt['q6']==cA['q6']
def testQ007():assert adt['q7']==cA['q7']
def testQ008():assert t('q8')
def testQ009():assert adt['q9']==cA['q9']
def testQ010():assert u('q10')
def testQ011():assert d('q11')
def testQ012():assert l('q12')