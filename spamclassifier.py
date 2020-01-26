from sklearn.model_selection import train_test_split as tts
from sklearn.naive_bayes import MultinomialNB as mb
from sklearn.naive_bayes import BernoulliNB as bb
from sklearn.naive_bayes import GaussianNB as gb
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score
import os
from collections import Counter
print("Enter path of the folder where training email data store :".title())
print("it can predict according to email data ".title())
path=input("path > ")
def makeword():
    file=path
    mail=os.listdir(file)
    email=[file+"//"+x for x in mail]
    word=[]
    for x in email:
       f=open(x)
       blob=f.read()
       word+=blob.split(" ")
       f.close()
    for i in range(len(word)):
        if not word[i].isalpha():
            word[i]=""
    diction=Counter(word)
    del diction[""]
    return diction.most_common(3000)
def makedataset(diction):
    file=path
    mail=os.listdir(file)
    email=[file+"//"+x for x in mail]
    feature=[]
    label=[]
    c=len(email)
    print('creating feature and labels')
    m=1
    for x in email:
        data=[] 
        f=open(x)
        word=f.read().split(' ')
        for entry in diction:
             data.append(word.count(entry[0]))
        feature.append(data)
        if "ham" in x:
             label.append(0)
        if "spam" in x:
             label.append(1)
        if type(int(((m)/(c))*100))==int:
            print("|",end='')
        f.close()    
        m+=1    
    print("Complete")    
    return feature,label
k=makeword()
xtr,ytr=makedataset(k)
print("there are three algorithum which will you select for train")
print("1.MultinomailNB")
print("2.BernoulliNB")
print("3.GaussianNB")
i=int(input("enter your choice > "))
if i==1:
    mul=mb()
    mul.fit(xtr,ytr)
    n=list(confusion_matrix(mul.predict(xtr),ytr))
    print("training data ")
    print("your ",n[0][0]+n[1][1]," value is right predicted out of ",len(xtr))
    print("your ",n[0][1]+n[1][0]," value is worng predicted out of ",len(xtr))
    print("accuracy",accuracy_score(mul.predict(xtr),ytr))
elif i==2:
    mul=gb()
    mul.fit(xtr,ytr)
    n=list(confusion_matrix(mul.predict(xtr),ytr))
    print("training data ")
    print("your ",n[0][0]+n[1][1]," value is right predicted out of ",len(xtr))
    print("your ",n[0][1]+n[1][0]," value is worng predicted out of ",len(xtr))
    print("accuracy",accuracy_score(mul.predict(xtr),ytr)) 
elif i==3:    
    mul=bb()
    mul.fit(xtr,ytr)
    n=list(confusion_matrix(mul.predict(xtr),ytr))
    print("training data ")
    print("your ",n[0][0]+n[1][1]," value is right predicted out of ",len(xtr))
    print("your ",n[0][1]+n[1][0]," value is worng predicted out of ",len(xtr))
    print("accuracy",accuracy_score(mul.predict(xtr),ytr))  
print("For exiting [Press exit]")
print("Enter some text for classifing weather its spam or not")
while True:
     p=makeword()
     b=[]
     it=input("enter text > ").split(" ")
     if "Exit" or "exit" in it:
         break
     for x in range(len(it)):
          if it[x].isalpha():
              b.append(it[x])
     feature=[]
     for x in p:
          feature.append(b.count(x[0]))
     c=mul.predict([feature])
     if c==[0]:
          print("Not Spam")
     if c==[1]:
          print("Spam")    
