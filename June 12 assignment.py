#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
def L(x):
    return x[1:]+x[0]
def R(x):
    return x[len(x)-1]+x[0:len(x)-1]
t=int(input())
list1=[input() for i in range(t)]
for i in list1:
    print("YES") if L(i) == R(i) else print("NO")


# In[ ]:


#2

i,j,k=map(int,input().split())
c=0
for n in range(i,j+1):
    if((n-int(str(n)[::-1]))%2==0):
        c+=1
print(c)


# In[4]:


#3

import itertools as it
a=list(map(str,input().split(',')))
p = it.permutations(a, 3)
x = list(set(p))               
l = []
for i in x:                          
    p = ''.join(i)                   
    l.append(int(p))
l.sort()
print(str(l[-1])+','+str(len(l)))


# In[ ]:


#4
n=int(input())
while(True):
    n=str(n)
    if(n ==n[::-1]):
        print(n)
        break
    else:
        n=int(n)+int(n[::-1])


# In[ ]:


#5

t=int(input())
while(t>0):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    gre=0
    l=0
    pos=-1
    long=0
    for i in range(n):
        if a[i]>k and gre!=0 and a[i]!=gre:
            gre = a[i]
            if long<l:
                long=l
            l = i - pos
            pos=i
            continue
        elif a[i]>k:
            gre = a[i]
            pos=i
        l+=1
    if long<l:
        long=l
    t-=1
    print("output:\n",long,"\n")


# In[ ]:


#6

s=input()
num=[]
dict1={}
a=list(s.split(","))
for i in a:
    n=int(i[i.index(':')+1:])
    while True:
        if(str(n)==str(n)[::-1]):
            num.append(n)
            dict1[n]=i[:i.index(':')]
            break
        else:
            n=int(str(n))+int(str(n)[::-1])
print(a[num.index(max(num))][0:a[num.index(max(num))].index(':')])
print(dict1)


# In[ ]:


#7
import json
s=input()
s=json.loads(s)
s1={}
s2=[]
for i,j in s.items():
    for k in j:
        s1[k]=[]
for i,j in s.items():
    for k in j:
        s1[k].append(i)    

print(s1)


# In[ ]:


#8
s=input()
s1=s.split(',')
print(s1)
a={}
b={}
al=[]
bl=[]
for i in s1:
    a1=list(i.split())
    a[a1[0]]=int(a1[1])
    b[a1[0]]=int(a1[2])
a1 = sorted(a.items(), key=lambda x: x[1],reverse=True)
b1 = sorted(b.items(), key=lambda x: x[1])
for i in a1:
    al.append(i[0])
for i in b1:
    bl.append(i[0])
for i in range(0,len(a1)):
    if(al[i]==bl[i]):
        print(al[i],end=" ")


# In[ ]:


#9
capacity=(8,5,3)
x = capacity[0]
y = capacity[1]
z = capacity[2]
memory = {}
ans = []

def get_all_states(state):
  a = state[0]
  b = state[1]
  c = state[2]

  if(a==4 and b==4):
      ans.append(state)
      return True

  if((a,b,c) in memory):
      return False

  memory[(a,b,c)] = 1
  if(a>0):
      if(a+b<=y):
          if( get_all_states((0,a+b,c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a-(y-b), y, c)) ):
              ans.append(state)
              return True
      if(a+c<=z):
          if( get_all_states((0,b,a+c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a-(z-c), b, z)) ):
              ans.append(state)
              return True
  if(b>0):
      if(a+b<=x):
          if( get_all_states((a+b, 0, c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((x, b-(x-a), c)) ):
              ans.append(state)
              return True
      if(b+c<=z):
          if( get_all_states((a, 0, b+c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a, b-(z-c), z)) ):
              ans.append(state)
              return True
  if(c>0):
      if(a+c<=x):
          if( get_all_states((a+c, b, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((x, b, c-(x-a))) ):
              ans.append(state)
              return True
      if(b+c<=y):
          if( get_all_states((a, b+c, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a, y, c-(y-b))) ):
              ans.append(state)
              return True

  return False

initial_state = (8,0,0)
get_all_states(initial_state)
ans.reverse()
print(ans)
print(len(ans))

