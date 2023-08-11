#!/usr/bin/env python
# coding: utf-8

# In[2]:


#palindrome string
def palin(m):
    s=m.replace(" ","")
    l=s[-1:]
    if s==l:
        return print("palindrome")
    else:
        return print("no")
m="malayalam"
palin(m)


# In[3]:


def ispalindrome(s):
    
    def palindrome(l,r,s):
        if l>=r:
            return True
        if s[l]!=s[r]:
            return False
        return palindrome(l+1,r-1,s)
    charstr=""
    for char in s:
        if char.isalnum()==False:
            continue
        if char==" ":
            continue
        if char.isupper():
            char=char.lower()
        charstr+=char
        ans=palindrome(0,len(charstr)-1,charstr)
    return ans
s="A man, a plan, a canal: Panama"
ispalindrome(s)


# In[4]:


#Given an integer array nums of unique elements, return all possible 
#subsets
 #(the power set).
def subsets(nums):
    def helper(i,subset,nums,ans):
        if i==len(nums):
            ans.append(subset.copy())
            return
        subset.append(nums[i])
        helper(i+1,subset,nums,ans)
        subset.pop()
        helper(i+1, subset, nums, ans)
            
        return
    ans=[]
    subset=[]
    helper(0,subset,nums,ans)
    return ans

nums = [1,2,3]   
subsets(nums)    


# In[5]:


#subsets with duplicate
def subsets(nums):
    def helper(i,subset,nums,ans):
        if i==len(nums):
            ans.append(subset.copy())
            return
        subset.append(nums[i])
        helper(i+1,subset,nums,ans)
        subset.pop()
        while i+1<len(nums)and nums[i]==nums[i+1]:
            i+=1
            
        helper(i+1, subset, nums, ans)
            
        return
    nums.sort()
    ans=[]
    subset=[]
    helper(0,subset,nums,ans)
    
    return ans

nums = [0]   
subsets(nums)  


# In[6]:


#combine
def combine(n,k):
    def helper(i,n,k):
        if k==0:
            ans.append(subset.copy())
            return
        if k>n-i+1:
            return
        if n<i:
            return
        
        
        subset.append(i)
        helper(i+1,n,k-1)
        subset.pop()
        helper(i+1,n,k)
    ans=[]
    subset=[]
    helper(1,n,k)
    
    return ans

 
combine(4,2) 


# In[7]:


#phone number to letter mapping
def phonechar(digits):
    def helper(i):
        if i==len(digits):
            new=""
            for j in comb:
                new+=j
            ans.append(new)
            return
        for j in range(len(numchar[digits[i]])):
            comb.append(numchar[digits[i]][j])
            helper(i+1)
            comb.pop()
    if not digits:
        return []
                       
    numchar = {  "2" : "abc", "3" : "def", "4" : "ghi","5" : "jkl", "6" : "mno","7" : "pqrs","8" : "tuv","9" : "wxyz"}                   
    ans = []
    comb = []
        
    helper(0)
        
    return ans
                       
digits = "23"
phonechar(digits)                       
            


# In[8]:


#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

def longestprefix(a):
    if a==0:
        return ""
    if len(a)==1:
        return a[0]
    size=len(a)
    minimum=min(a)
    for i, char in enumerate(minimum):
        for j in a:
            if j[i]!=char:
                return minimum[:i]
            
    return minimum
a=["flower","flow","flight"]
longestprefix(a)
            


# In[9]:


#Given a string s, return true if the s can be palindrome after deleting at most one character from it.



def validpal(a):
    def palindrome(a,left,right):
        while left<right:
            if a[left]!=a[right]:
                return False
            left+=1
            right-=1
        return True
    left=0
    right=len(a)-1
    while left<right:
        if a[left]!=a[right]:
            if palindrome(a,left+1,right):
                return True
            if palindrome(a,left,right-1):
                return True
            return False
        left+=1
        right-=1
        return True
    
    
    
        
        
  
            
    
a="abc"
validpal(a)


# In[10]:


#roman to number
def convert_roman(a):
    symbol={"I":1,"V":5,"X":10,"L": 50,"C":100,"D":500,"M" :1000}
    prev_val=0
    result=0
    for j in range(len(a)-1,-1,-1):
        current_val=symbol[a[j]]
        if current_val>=prev_val:
            result+=current_val
        else:
            result-=current_val
        prev_val=current_val
    return result
a="XI"
convert_roman(a)


# In[11]:


#longest subsequence
def longestsubstring(a):
    l=[]
    n=len(a)
    j=0
    while j<n:
        if a[j] not in l:
            l.append(a[j])
        j+=1    
    return len(l)
a="pwwkew"
longestsubstring(a)


# In[12]:


#longest substring
def longest_substring(word):
    n=len(word)
    if n<=1:
        return n
   
    start=0
    char_index={}
    max_length=0
    for end in range(n):
        if s[end] in char_index and start<=char_index[s[end]]:
            start=char_index[s[end]]+1
        else:
            max_length=max(max_length,end-start+1)
            
        char_index[s[end]]=end
    return max_length
s = "abcabcbb"
longest_substring(s)


# In[13]:


#valid parenthesis
def remove_paranthesis(s):
    stack=[]
    indices_to_remove=set()
    for i,char in enumerate(s):
        if char=='(':
            stack.append(s[i])
        if char==')':
            if stack:
                stack.pop()
            else:
                indices_to_remove.add(i)
    indices_to_remove=indices_to_remove.union(set(stack))
    result=[]
    for i,char in enumerate(s):
        if i not in indices_to_remove:
            result.append(char)
            
    return ''.join(result)
s="lee(t(c)o)de)"
remove_paranthesis(s)


# In[14]:


#longest substring
def longest_substring(a):
    k=[]
    an=[]
    max_count=0
    n=len(a)
    i=0
    while(i<n):
        if a[i] not in k:
            k.append(a[i])
        if a[i]==a[i-1]:
            an=k.copy()
            del k[:]
            #k.remove(a[i-2])
            k.append(a[i])
                
        i+=1
    return max(len(k),len(an))
a="aabbcc"
longest_substring(a)


# In[ ]:


from typing import List, Tuple
def create_duplicate_array(wordAr: List[str]) -> List[Tuple[str, int]]:
    dup_array = []
    # Iterate through the original list of words
    for i, word in enumerate(wordAr):
        # Append each word along with its index in the original list to the duplicate array
        dup_array.append((word, i))
    return dup_array
 
# Function to print out all the words that are anagrams of each other next to each other
def print_anagrams_together(wordArr: List[str]):
    # Create a duplicate array containing the words and their indices
    dup_array = create_duplicate_array(wordArr)
 
    # Iterate through the duplicate array and sort each word alphabetically
    for i in range(len(wordArr)):
        dup_array[i] = (sorted(dup_array[i][0]), dup_array[i][1])
    # Sort the duplicate array based on the sorted words
    dup_array.sort()
 
    # Iterate through the sorted duplicate array and print out the original words using their indices
    for i in range(len(wordArr)):
        print(wordArr[dup_array[i][1]], end=' ')
 
# Test the function with an example list of words
wordArr = ["cat", "dog", "tac", "god", "act"]
print_anagrams_together(wordArr)
 


# In[ ]:




