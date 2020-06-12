#!/usr/bin/env python
# coding: utf-8

# In[1]:



s1=input("enter the string")
s2='Good Morning'
print(type(s1),type(s2))


# In[2]:


#operators : +,*(repitition),[](slice),[:](slice range)
print(s1 + s2)#Concatenation
print(s1 * 3)#Repitition
print(s1[4])#slicing
print(s1[-1])#slicing
print(s1[2:])


# In[3]:


print(s1[0:5])
print(s1[:])


# In[4]:


#Alternate characters
print(s1[::2])


# In[5]:



#Accept string from the user and check wheather it is pallimdrome or not
s3=input("enter the string")
if(s3==s3[::-1]):
    print("Pallindrome")
else:
    print("Not Pallindrome")


# In[6]:



n=int(input("enter the number"))
if str(n)==str(n)[::-1] :
    print("Pallindrome")
else:
    print("Not Pallindrome")


# In[7]:


s4="python"
print("on" in s4)
print("xyz" in s4)
print("on" not in s4)
print("xyz" not in s4)


# In[8]:


s="hello"
s1="abc123"
print(len(s))
print(max(s))
print(min(s))
print(len(s1))
print(max(s1))
print(min(s1))


# In[9]:


print(ord("1"),ord('a'))


# In[10]:



s="hello"
print(len(s))
print(s.capitalize())
print(s)
s=s.capitalize()
print(s)


# In[11]:


s1="hello"
s2="abc123"
s3="123"
print(s1.isalpha(),s2.isalpha(),s3.isalpha())
print(s1.isdigit(),s2.isdigit(),s3.isdigit())
print(s1.isalnum(),s2.isalnum(),s3.isalnum())


# In[12]:


s1="python"
s2="PYTHON"
s3="Python"
print(s1.isupper(),s2.isupper(),s3.isupper())
print(s1.islower(),s2.islower(),s3.islower())


# In[13]:


s1="python"
s2="PYTHON"
s3="Python"
print(s1.upper(),s2.upper(),s3.upper())
print(s1.lower(),s2.lower(),s3.lower())
print(s1.swapcase(),s2.swapcase(),s3.swapcase())


# In[14]:



s="abc abc abc"
print(s.count('abc'))


# In[15]:


s="abc abc abc"
print(s.split())
s1="a,b,c,d"
print(s1.split(","))
s2="hello"
print(s2.split())


# In[16]:


#replace
s="abc"
print(s.replace("b","z"))
print(s)


# In[17]:


# accept a number(n) from the user and remove nth position
#character from the string
n=int(input())
s=input()
#print(s[:n]+s[n+1:])
print(s.replace(s[n-1],"",1))


# In[18]:


#print 1-n numbers on the screen
n=10
for i in range(1,n+1):
    print(i,end=" ")
print()

i=1
while(i<=n):
    print(i,end=" ")
    i+=1


# In[19]:


s= "python"
for i in s:
    print(i)
print()
for i in s[::-1]:
    print(i)
print()


# In[20]:


#using while loop to print all character of your string
s="python"
i=0
while(i<len(s)):
    print(s[i])
    i+=1


# In[21]:


#using for loop but not iterable object
s="python"
for i in range(0,len(s)):
    print(s[i])


# In[23]:


#accept a string from user and count no of vowels,consonants and special charcters available in the string
s=input()
v=0
c=0
sp=0
for i in s:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
        v+=1
    elif(i=='!' or i=='@' or i=='#' or i=='$' or i=='&' or i=='"' or i=='.' or i=='-'):
        sp+=1
    else:
        c+=1
print("no of vowels",v)
print("no of consonants",c)
print("no of special characters",sp)


# In[24]:



c=0
s="abbaaccbbaaa"
for i in range(0,len(s)-1):
    if(s[i:i+2]=='aa'):
        c+=1
print(c)


# In[25]:


b=input()
c=0
stack=[]
for i in b:
    if(i=='('):
        stack.append('(')
    elif(i==')'):
        stack.remove('(')
        c+=1
print(c)


# In[ ]:




