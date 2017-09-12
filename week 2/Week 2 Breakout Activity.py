
# coding: utf-8

# ## Activity 1
#
# ### Part A
#
# You work for a Python consulting company. One of your clients is really bad at math, and comes to you with an important task: to create a "calculator" program.
#
# We're going to build your first tool using Python code! Create a calculator tool that prompts a user for two numbers and an operator. Then, print out the result of that equation to the screen.
#
# Your calculator should work for addition, subtraction, multiplication and division. If the user enters anything else as the operator, tell the user they picked an invalid operator.
#
#
# #### Helpful functions
# - input()
# - float()
# - if, elif, else
# - print()
#
# #### Sample output
# Enter first number: 3 <br>
# Enter second number: 5.5 <br>
# Enter an operator: \* <br>
# 3.0 \* 5.5 = 16.5 <br>

# In[ ]:

f_n = float(input("Enter first number: "))
s_n = float(input("Enter second number: "))
o = input("Enter an operator: ")
if o == "+":
    ans = f_n + s_n
elif o == "-":
    ans = f_n + s_n
elif o == "*":
    ans = f_n * s_n
elif o == "-":
    ans = f_n / s_n
elif:
    print("operator is invalid")
print(ans)


# In[6]:

type('+)


# ### Part B
#
# Your client does not have access to Jupyter Notebook. Save your code as a .py file and run it from the command line a few times. Make sure all of your operators still work.

# ### Part C
#
# Your client is bored of simple equations, and would like to be able to use some of Python's advanced operators. Update your program to allow exponents, modular division, and integer division.
#
# #### Helpful Functions
# - \**
# - %
# - //
#
# #### Sample Output
# Enter first number: 7 <br>
# Enter second number: 4 <br>
# Enter an operator: % <br>
# 7.0 % 4.0 = 3.0

# In[ ]:

# Insert your code here


# ## Activity 2
#
# ### Part A
#
# Now, we will work with lists and while loops to solve one of the most popular "introduction to data analysis" problems - counting the words in a document. To start, let's write a simple while loop that will iterate through a Python list and will print the length of each word. Fill in the missing part of the code below to complete this.
#
# You will want to use the following functions:
# - list_variable.pop()
# - len(string_variable)
#
# #### Sample Output
#
# apple 5 <br>
# snowwoman 9 <br>
# penguin 7 <br>
# kitten 6 <br>
# jax 3 <br>
# apple 5 <br>

# In[ ]:

string_list = ["apple", "jax", "kitten", "penguin", "snowwoman", "apple"]

while #insert while condition here
    #insert your code here


# Next, let's use a dictionary to turn every string in our list in the "key" of a key-value pair. For the value, we will temporarily use the number "1". Please update your code to create a blank dictionary and, for each word, store the value "1" in your dictionary, associated with that key.
#
# You will want to use the following syntax:
# - dictionary_name[key] = value
#
# #### Sample Output
# {'snowwoman': 1, 'kitten': 1, 'apple': 1, 'penguin': 1, 'jax': 1}

# In[ ]:

string_list = ["apple", "jax", "kitten", "penguin", "snowwoman", "apple"]
count_dict = {}

# Insert your code here

print(count_dict)


# Now, we will update our code to add 1 to the dictionary each time a word is encountered. This will let us count the number of times we see each word in a very effective way!
#
# You will want to use the following function:
# - dict_var.get()
#
# #### Sample Output
#
# {'penguin': 1, 'jax': 1, 'kitten': 1, 'apple': 2, 'snowwoman': 1}

# In[ ]:

string_list = ["apple", "jax", "kitten", "penguin", "snowwoman", "apple"]

# Insert your code here


# Great! We're almost done. Now, use the "input" command to let the user enter any number of words for your program to count!
#
# You can translate their input string into a list using the following function:
# - list_variable = string_variable.split()
#
# you can make the function case insensitive with
# - str.lower()
#
# #### Sample Output
# Enter a bunch of words to count: The Quick Brown fox ran into the FOX house <br>
# {'ran': 1, 'house': 1, 'quick': 1, 'brown': 1, 'fox': 2, 'the': 2, 'into': 1}

# In[ ]:

string = input("Enter a bunch of words to count: ")

# Insert your code here


# In[ ]:

## mutability

Your client wants a scoreboard that reports the ranking of contestants over
a week long contest. They give you a list of dictionaries. The dictionaries
hold stats about each contestant. The scoreboard is initialized with the
predicted rankings.  Your job is to change teh scoreboard to reflect changes that
occured during the contest.

Changes that occured:

* Fred decided that his name will be "The Last Cyborg" for the duration of the competition.
* On Wednesday Buba took first place pushing "The Last Cyborg" down one ranking.
* After taking the lead Buba changed his team color to purple and his name to "Rocky"

To do:
- the scoreboard is represented as a set of dictionaries where order represents rank. Modfiy them to represent the 3 events above

Challenge question: ** hint, you can use a loop to extract the names **

- use **in** and **not in** to verifiy that Bubba was in the competition on Monday but not Friday


# In[ ]:

from copy import deepcopy

Contestants = [{"name":"fred", "teamColor":"Red"},
               {"name":"Layla", "teamColor":"Yellow"},
               {"name":"Tammy", "teamColor":"Green"},
               {"name":"Buba", "teamColor":"Blue"}]


RankMon=[Contestants[0],Contestants[1],Contestants[2],Contestants[3]]
RankTues=RankMon
RankWed=RankTues
RankThurs=RankWed
RankFri=RankThurs

################################# Student start
## modify the order/names here

################################# Student end

#Output

print ("Monday")
print ("-------")
for n in range(len(RankMon)):
    print ("Name:" + (RankMon[n]['name']), "   teamColor:" + RankMon[n]['teamColor'])

print ()
print ("Friday")
print ("-------")
for n in range(len(RankFri)):
    print ("Name:" + (RankFri[n]['name']), "   teamColor:" + RankFri[n]['teamColor'])



# In[2]:


from copy import deepcopy


# ## Congratulations! You finished.

# In[ ]:
