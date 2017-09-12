
# coding: utf-8

# # Homework 2 - Summer Session
# 
# ### Assignment due date: 24 hours before the Week 3 Live Session.
# 
# 
# 

# ## Section 1 text and arithmetic
# 
# In the first section you will create simple text and arithmetic scripts. These tasks are designed to give you an introduction to input/output and text formating. Each of these should be saved as a separate .py script and each should labeled so that it is clear which problem each script is for. Make sure you run your .py scripts from the command line to ensure they run successfully before submitting them.
# 
# When you sync your repository to GitHub, we expect that you will have one script for each of the problems in section 1. Section 2 (further below) can be completed in this Jupter Notebook.
# 
# ### 1-1. Tip Calculator
# 
# Below, you can see the script we wrote to compute the tip for a meal.  Fix it so that it works correctly.  Save your result as the file tip.py.

# In[1]:

price = float(input("Enter the price of a meal:"))

tip = price * 0.16
total = price + tip

print("A 16% tip would be ", tip)
print("The total including tip would be ", total)


# ### 1-2. Pig Latin Translator
# 
# Write a script that translates names into a (simplified) Pig Latin. Have your script ask the user for his or her name. Move the first letter to the end of the name and add the letters "ay".  Make sure that only the first letter of your output is capitalized. Your script should re-create the following behavior exactly:
# 
# ```
# Enter your name: Paul Laskowski
# Aulpay Askowskilay
# ```
# 
# Save your script as **piglatin.py**

# In[9]:

print("Please do not put a space in front of the first name or after the last name")
name = input("Enter your name: ")
i = 0
ad = "ay"
while i <= (len(name)-1):
    if name [0] == " ":
        print("Please do not put a space in front of the first name")
        break
    else:
        f_l = name[0]
        if name[i] != " ":
            i = i+1
        else:
            f_n = name[0].lower()
            new_name_f_U = name[1].upper()
            new_name_f_L = name[2:i] 
            new_name_f = new_name_f_U + new_name_f_L + f_n + ad
            
            l_n = name[i+1].lower()
            new_name_l_U = name[i+2].upper()
            new_name_l_L = name[i+3:len(name)]
            new_name_l = new_name_l_U + new_name_l_L +l_n + ad
            print(new_name_f, new_name_l)
            break


# ## 1-3. Matrix Inverter
# 
# One place tuples are convenient is in the representation of matrices.  Label the values in a 2x2 matrix as follows:
# $$
# \begin{bmatrix}
#     a       & b  \\
#     c       & d
# \end{bmatrix}
# $$
# Write a script, matrix_fun.py, that asks the user for a text string including the four values, a, b, c, and d, separated by spaces.  You can use the `split()` method on the string to create a list of the four values in order.
# 
# Create a tuple that represents each row, then create a tuple that contains those two tuples.  It should have the form `((a, b), (c, d))`.  Print this representation.
# 
# The inverse of the matrix above is given by the formula,
# 
# $$
# \frac{1}{ad-bc} \begin{bmatrix}
#     d       & -b  \\
#     -c       & a
# \end{bmatrix}
# $$
# 
# Compute the inverse of the given matrix, again represented as nested tuples, and print this representation. For example:
# 
# 
# input: 1 2 3 4
# 
# output:
# ```
# matrix: ((1.0, 2.0), (3.0, 4.0))
# inverse: ((-2.0, 1.0), (1.5, -0.5))
# ```

# In[10]:

values = input("input: ")
s_v = values.split()
f_n = []; i_n = []; i_m = [];
i = 0; j = 0
while i <= 3:
    f_n.append(float(s_v[i]))
    i = i+1
row_1 = tuple(f_n[0:2])
row_2 = tuple(f_n[2:4])
matrix = (row_1, row_2)
print("output: ")
print("\tmatrix: ",matrix)
D = f_n[0] * f_n[3] - f_n[1] *f_n[2] 
if  D == 0:
    print("this matrix does not have an inverse because ad-bc = 0")
else:
    while j <= 3:
        i_n.append(1/D * f_n[j])
        j = j+1
i_m.append(i_n[3]); i_m.append(-i_n[1]); i_m.append(-i_n[2]); i_m.append(i_n[0])
row_1 = tuple(i_m[0:2])
row_2 = tuple(i_m[2:4])
matrix = (row_1, row_2)
print("\tinverse: ",matrix)


# ## Section 2 - Flow control 
# 
# For these tasks you answer the questions inside this ipython notebook file and submit it. Questions can be labelled accordingly.
# 
# 

# ## 2-1. If statements
# 
# The mythical island nation of Laskoatu has a rather simple tax code.  The first \$1000 of income is taxed at 5%.  The next \$1000 is taxed at 10%.  Any income beyond the first \$2000 is taxed at 15%.  Complete the following script so that it asks the user for his or her income and outputs the amount of tax owed.

# In[24]:

income = int(input("Please enter your income:"))
if income >= 0 and income <= 1000:
    tax = income * 0.05
elif income >= 1000 and income <=2000:
    tax = 1000 * 0.05 + (income -1000)*0.1
else:
    tax = 1000*0.05 + 1000*0.1 + (income-2000)*0.15
print("tax: ",tax)


# ## 2-2 While loops
# Write a script that prompts the user for his or her name. Using a while loop that counts downwards, print the name with the letters reversed. You may use `s.lower()` and `s.upper()` to change a string `s` to lowercase and uppercase letters.
# ```
# Enter your name: Paul 
# Luap
# ```
# If the name is the same forward and backwards, print "Palindrome!" on the next line.
# ```
# Enter your name: Ana 
# Ana 
# Palindrome!
# ```

# In[13]:

name = input("Enter your name: ")
i = len(name)
r_n = name[i-1].upper()
while i > 1:
    if name [0] == " ":
        print("Please do not put a space in front of the first name")
        break
    else:
        if i != 2:
            i = i-1
            r_n_0 = name[i-1]
            r_n = r_n + r_n_0
        else:
            i = i-1
            r_n_0 = name[i-1].lower()
            r_n = r_n + r_n_0
            print(r_n)
if r_n == name:
    print("Palindrome!")


# ## 2-3 Create a to-do list using a dictionary of lists
# 
# 
# Your program should have the following elements:
# 
# 1. Empty dictionary to store information
# 
# 2. Key for each day of the week
# 
# 3. Each key has a list value that stores items
# 
# 4. User is prompted to add to or view to-do list
# 
# 5. User can type "add" program will ask what day and add it correctly
# 
# 6. User can type "get" and the program will ask for the day and print the values
# 
# Example:
# ```
# What would you like to do?
# add
# What day?
# Friday
# What would you like to add to Friday's to-do list?
# practice clarinet
# What would you like to do?
# get
# What day?
# Friday
# You have to practice clarinet.
# What would you like to do?
# ```

# In[56]:

calendar = dict([('Monday',''),('Tuesday',''),('Wednesday',''),
            ('Thursday',''),('Friday',''),('Saturday',''),
           ('Sunday','')])
calendar["Monday"] = ["You have to practice clarinet","go to school",
                      "play the piano"]
calendar["Tuesday"] = ["drink some wine","fix my computer"]
calendar["Wednesday"] = ["relax","clean the house"]
calendar["Thursday"] = ["You have to practice clarinet","read Python books"]
calendar["Friday"] = ["play with your dog","Do some coding"]
calendar["Saturday"] = ["write a paper","watch a movie"]
calendar["Sunday"] = ["clean the house","but some milk"]                                            
Do = input("What would you like to do?\n")
if Do == "add":
    Day = input("What day?\n")
    if Day in calendar.keys():
        print("What would you like to add to",Day, "\'s to-do list?")
        calendar[Day].append(input())
        print("This is now your", Day, "\'s to-do list\n")
        print(calendar[Day])
    else:
        print("There is no such day")
elif Do == "get":
    Day = input("What day?\n")
    if Day in calendar.keys():
        if calendar[Day] == '':
            print("There is nothing to do yet")
        else:
            print(calendar[Day])
    else:
        print("There is no such day")
else:
    print("please only enter add or get")


# ## 2-4 Fibonacci
# 
# The Fibonacci numbers begin with 1, 1.  After the first two numbers, each number is the sum of the previous two. 1 + 1 = 2, so 2 is the third number. Then 1 + 2 = 3, so 3 is the next one, and so on. Write a script that prompts the user for a number, then prints all the Fibonacci numbers that are less than or equal to the input, in order.
# 
# ```
# Enter a number: 15
# 1 1 2 3 5 8 13
# ```

# In[16]:

n = int(input("Enter a number: "))
a = 1
b = 1
c = 2
Fi = [1,1]
if n <1:
    print("Please enter a number >= 1")
elif n == 1:
    print("1 1")
elif n > 1:
    while c <= n:
        c = a + b
        a = b
        b = c
        Fi.append(c)
Fi.pop()
print(Fi)
        


# ## 2-5 Pascal's Triangle
# 
# Pascal's triangle is a triangle of numbers that is computed as follows.  The first row contains a 1.  Each row after that begins and ends with a 1, and every other number is the sum of the two numbers above it.  The first six rows of Pascal's triangle are shown below.
# ```
#       1
#      1 1
#     1 2 1
#   1  3 3  1
#  1 4  6  4 1
# 1 5 10 10 5 1
# ```
# Write a script to compute the *n*th row of Pascal's triangle.

# In[80]:

n = int(input("Enter a number: "))
lt_1 = (1)
lt_2 = (1,1)
j = 2
col = 0
if n < 1:
    print("Please enter a number that is >= 1")
elif n == 1:
    print(lt_1)
elif n == 2:
    print(lt_2)
elif n >=3:
    print(" "*(n-col-1),"[1]")
    print(" "*(n-col-2),"[1,1]")
    for row in range (3,n+1):
        #print("row is", row)
        lt_1 = lt_2
        #print("\t lt_1=lt_2 gives", lt_1)
        lt_2 = list(lt_2)
        lt_2[0:len(lt_2)]=[1,1]
        tuple(x)
        #print("\t lt_2 is now", lt_2)
        for col in range (1,row-1):
            #print("col is", col)
            #print("lt_1[col-1]+lt_1[col] is",lt_1[col-1], "+", lt_1[col])
            #print(lt_1)
            lt_2.insert(col,lt_1[col-1]+lt_1[col]) 
            #print("\t lt_2 is ", lt_2)
            #print("\n")
        #print("\t lt_2 is ", lt_2)
        print(" "*(n-col-2),lt_2)


# ## Please submit feedback for any and all homeworks!
# 
# http://goo.gl/forms/74yCiQTf6k
