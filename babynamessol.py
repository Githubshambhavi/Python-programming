
# coding: utf-8

# In[1]:


import sys
import re


# In[39]:


def extract_names(filename):
    """['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]"""
    #extract year
    #extract name and rank and print them
    
    name=[]
    f=open(filename,'r')
    text=f.read()
    #get the year
    year_match=re.search(r'Popularity\sin\s(\d\d\d\d)',text)
    #print(year_match)
    if not year_match:
        sys.stderr.write('Couldn\'t find the year!\n')
        sys.exit(1)
    year = year_match.group(1)
    #print(year)
    name.append(year)
    #find all data using findall()
    #tuples=(rank,boyname,girlname)
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
    #print(tuples)
    #extract data into dict with each name as a key and rank as value
    names_to_rank ={}
    for rank_tuples in tuples:
        (rank,boy_name,girl_name)=rank_tuples #unpack tuples in 3 vars
        if boy_name not in names_to_rank:
            names_to_rank[boy_name]=rank
        if girl_name not in names_to_rank:
            names_to_rank[girl_name]=rank
    print(names_to_rank)      
    sorted_names=sorted(names_to_rank.keys())
    print(sorted_names)
    
    for names in sorted_names:
        print(names_to_rank[names])
        name.append(names+" " + names_to_rank[names])
    return name


# In[40]:


extract_names("/Users/shambhavi.srivastava/Desktop/google-python-exercises/babynames/baby1990.html")

