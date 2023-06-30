#!/usr/bin/env python
# coding: utf-8

# In[3]:


# python variable & data types
#One of the most fundamental concepts of Python is variables. 
#A Python variable is used to store some value or values. Each variable has a name and a data type. 
#We can assign a value to a variable and then reference this value with the variable name.#
x=7


# In[5]:


#Variables are important because they can allow our code to be more flexible, take input, 
#and can make it easier to read and interpret as well
y = 10
z= 50


# In[8]:


#Assigning Variables,"A variable is created when you assign a value to it and execute the code."

#We can assign multiple variables on different lines in one cell. For example, we assign variable y to be equal to 11. 
#Press enter to start a new line and create another variable z to be equal to 25. 
#After we execute both lines, both variables have been assigned."


# In[10]:


#Variable Starting with letter
a5=20 
#Variable starting with Underscore
_a8 = 45
#descriptive variable with letters and underscore
company01_Ebidta = 6003


# In[11]:


#printing variable. if we type x the vairiable will be printed

x=7
x


# In[12]:


#if we assign to variables and type both the assigned letters only the last variable output will be printed

a =32
b=100
a
b


# In[13]:


#Variables are also case sensitive
#lets say we asign x and try to print X we would get an error
x = 100
X


# In[14]:


#inorder to print mutiple variables at the same time we need to use the print()


# In[15]:


print(a)
print(b)


# In[16]:


#reassigning variables
x


# In[17]:


x=2
x


# In[18]:


#Datatype of a variable
#The data type of a variable is defined when a value is assigned to the variable. 
#The data type of a variable is a way to classify the type of value that it can represent. 
#This will help determine what type of actions and operations can be performed on it.
#There are four basic types of data in Python: integers (whole numbers), float (decimal numbers), boolean (True or False),
#and string (text). 
#To see what data type a variable is, you can apply the `type()` function to the variable."

#integer(int)- whole number


# In[19]:


int_a =7
type(int_a)


# In[21]:


a = 100
type(a)


# In[22]:


x = 10.5
type(x)


# In[23]:


print(x > 5)


# In[25]:


#booleans are case sensitive and need to be capitalized


boolean_a = True
type(boolean_a)


# In[26]:


#string data type
string_a = "Elizabeth"
type(string_a)


# In[27]:


print("Elizabeth")


# In[28]:


#common errors in strings data types
g = 'i can't fly'
g


# In[30]:


#correction using double quote ""
g = "i can't fly"


g


# In[31]:


#better still use the backslash\
H = 'i shouldn\'t be going home now'
H


# In[33]:


#concatenating strings
'Net' 'margin'


# In[34]:


'net ' 'profit'


# In[36]:


'Net'+' profit'


# In[39]:


#use a print stetment around the value or string into to get just text without quotes

print('net','profit')


# In[40]:


#converting data types
floata = 10.25
int(a)


# In[41]:


int_a = 5673
float(int_a
     )


# In[42]:


int_z = 1000
str(int_z)


# In[43]:


str_z = "100"
int(str_z)


# In[45]:


float_b = 100.567
str(float_b)


# In[46]:


str(3<1)


# In[49]:


#combining data types
number = 3000
print(number, "USD")


# In[51]:


#another way is to convert the strings
int_z = 5000
print(str(int_z),"USD")


# In[54]:


#Data Structures
#list are denoted with square brackets[]
List_a = ['Yuting','Mark','Joy','Amaka']
#you can call a list by index and the index for list starts from 0
List_a[0]


# In[57]:


#we can call a list using a negative index
List_a[-2]


# In[58]:


#Creating numeric list
list_3=[1,2,3,4]
list_3[1
      ]


# In[60]:


#creating mixed list
Listmix = [1,2,'emeka',10.25]
Listmix


# In[62]:


#list can also contain other list
listj = [Listmix,list_3,'henry']
listj


# In[65]:


#combining different list with individual data points
list_y = list_3 + Listmix
list_y


# In[66]:


#manipulating list
#we cant sort list that contains different data types
list_y.sort()


# In[69]:


#Sorting a string
List_a.sort()
print(List_a)


# In[70]:


#sorting from descending to ascending order using sortreverse
list_3.sort(reverse=True)
list_3


# In[71]:


# a list is mutable meaning that we can update and edit it using the append()
List_a.append("Junior")
List_a


# In[72]:


#replacing values in a list
List_a[2] = "Chinedu"
List_a


# In[73]:


#deleting values from a list using del()
del List_a[-2]
List_a


# # Tuple
# 

# In[75]:


Tuple_a = (1,2,3,4,5,6)
Tuple_a


# In[76]:


Prices = (2000,2300,3500,4000,3500)
Prices


# In[77]:


Tuple_b = ("Joy","Amara","lovelyn","Mark")
Tuple_b


# In[78]:


Mix=("True",1,3,5,"Boy")
Mix


# In[81]:


Joined_tuples = (Mix,Tuple_b,Prices, List_a)
Joined_tuples


# In[85]:


#list can contain tuples
List_H = [List_a ,Tuple_b]
List_H


# In[86]:


#Combining Tuples
Tuple_b + Prices


# In[87]:


#tuples are immutable that is they can not be altered or deleted
Tuple_b.append("b")


# In[88]:


#Dictionaries 
#Dictionaries do not allow duplicates
#A dictionary is a collection of unordered key value pairs and use `{}`. 
#Dictionaries are mutable, meaning that they can be edited, and can be called by both their key or index. 
#We can use the key as an index in the dictionary to return the values associated with that key.
Dict_a = {"Firstname":"Frank", "Lastname":"Park","Age": 20}
Dict_a


# In[89]:


#List Accepts duplicates unlike dictionaries
list_w =["Joy","Joy"]
list_w


# In[90]:


#However dictionaires do not accept duplicates as only one lastname:park printed
Dict_a = {"Firstname":"Frank", "Lastname":"Park","Lastname":"Park","Age": 20}
Dict_a


# In[96]:


#A common method of creating dictionaries is to use listsal

sales= [200,300,400,500]
stores = ["A","B","C","D"]
Dict_sales = {"sale" : sales , "store" : stores}
Dict_sales


# In[98]:


#item() used to return everything inside our list or dictionary or data frame
#To further inspect all of the items in a dictionary, we can use the `items()` function. We can use the `items()` function when using a `for loop` with a dictionary. 
#This allows us to access both the key and values in a dictionary. We'll see this a little bit later in this chapter.
Dict_sales.items()


# # operators are used to create the logic that our code will follow Mathematical operators
# 

# In[99]:


# + adds expression
3+67


# In[100]:


2-3


# In[101]:


38*9


# In[102]:


#% return the modulo that is the remainder

4%3


# In[103]:


# the ** exponent raises the left expression to the power of the right expression
4**2


# In[105]:


#python uses BEDMAS (Bracket, Exponents, Divide,multiple,add,subtract)
15 /(2+1) ** 4


# # Comparisim operators

# In[106]:


15 >20


# In[107]:


30<60


# In[109]:


#== is used as an equal sign
20 == 15


# In[110]:


"Hollywood" == "bollywood"


# In[112]:


# != is used to show that 2 values are not equal
20 != 3


# In[113]:


"Hollywood" != "bollywood"


# # Logical operators

# In[114]:


#Logical operators allow the capability to combine different comparison operators for a more complex result."
#"When using the `and` operator, both conditions need to be satisfied in order to be `True`. \n",
# "For example, a customer may be qualified only if they meet both the revenue requirement AND the order volume requirement."

x = 5
x<3 and x < 4


# In[115]:


#When using the `or` operator, at least one condition needs to be satisfied in order to be `True`.,
#An example of this can be when someone is approved for a credit card if they have an individual income of 60,000 OR a household income of 100,000."
x = 0
x<3 or x < 4


# In[116]:


x= 6
x>3 or x < 4


# In[118]:


#"We can also combine the different types of operators to create more complex conditions.
a = 3
b= 5
c= 7
a+b <b + c 


# # FUNCTION

# In[119]:


#A function is a block of reusable code that performs a specific task. 
#Now let's explore a few commonly used built-in Python fuctions. 
#These built-in functions provides a wide range of tasks that we can use in our code.
max(45,67,89,100)


# In[120]:


min(100,30,200,40)


# In[121]:


abs(-0.94)


# In[122]:


sum([1,2,3])


# In[123]:


round(47.9876,2)


# In[124]:


pow(2,3)


# In[125]:


len([1,3,4,5,6,7,9,0])


# In[127]:


#"A package (aka library) is a collection of functions. Using external packages allow us to utilize open source code that other people have created so we don't need to write all the code from scratch ourselves.\n",
#"There are various different packages in Python. When we installed Anaconda at the beginning of the course,
#we've already automatically installed most of the common Python packages so now we can import them directly. 
#There are also some packages that do not come with Anaconda and we need to install them separately. We'll talk about that later."

import math
math.sqrt(81)


# In[128]:


#using alliases to import packages
import math as mth
mth.sqrt(100)


# In[129]:


#"We can also directly import a function in a package. We use the key word from followed by the package name `math`,
#and import followed by the function name `sqrt`. This way, there is no need to call math in a separate line. 
#After importing the sqrt function, we can use it to calculate the square root."

from math import sqrt
sqrt(100)


# In[130]:


#If you just wanted to import all the functions within the package without calling the package every time,
#you can consider using `*` to import all functions. 
#This enables us to not have to write out the alias for the math package when using its functions."
from math import *
print(sqrt(100))
pow(2,3)


# In[131]:


#If you wanted to get help in what a function does, the `help` function pulls up some of the documentation without having to visit the site. 
#You can look up a specific function or the entire package with the full list of functions."
help(math.sqrt)


# In[ ]:


#Math` is just one example of packages that we can import in Python. Different packages serve different purposes.
#`Numpy`, `Pandas`, and `Matplotlib`, `Seaborn`."


# # Conditional Statements

# In[133]:


#A powerful feature of Python is the use of `conditional statements`. 
#The results of a conditional statement can evaluate to `True` or `False` and depending on the answer, 
#different computations or actions are executed."
#"One of the most common conditional statements are `If Statements`. If statements are used when there is a need to filter a dataset or to perform logical equations in a model.\n",
#If Statements` allows the user to use Python to initiate an output that follows a certain logic."
#"Consider the following example. If the initial condition is met, `a > b`, Python will run print statement below the condition. It is important to indent the action line after the condition. As a rule of thumb, anything after the \":\" should be indented if it corresponds with the condition."

a = 50
b = 35

if a > b :
    print("greater")


# In[135]:


#If the condition is NOT met, then Python will not run the code below the if statement."
a = 20
b = 35

if a > b :
    print("greater")


# In[136]:


# Else & Elif Statements\n",
#Statements that are frequently used in conjunction with `if statements` are `Else` and `Elif`. 
#These statements provide the ability to add additional conditions and actions after the `if statement`."

Nestle = 23000

if Nestle > 20000 :
    print("high")
else:
    print("low")
    


# In[137]:


sona = 21000
if sona < 22000 :
    print("low")
else :
    print("high")


# In[139]:


#Elif
sona = 21000
if sona < 22000 :
    print("low")
elif  sona > 22000 :
    print("high")
else :
    print("med")


# In[141]:


sona = 21000
if sona < 22000 :
    print("low")
elif  sona > 22000 :
    print("high")
else :
    print("med")
#nestle

if Nestle > 20000 :
    print("high")
elif Nestle < 19000 :
    print("low")
else:
    print("med")


# # LOOPs

# In[143]:


customer_list = [21000, 23000,22000,19000]
for i_customer in customer_list :
    if i_customer < 22000 :
        print("low")
    elif  i_customer > 22000 :
        print("high")
    else :
        print("med")


# In[144]:


import numpy as np


# In[145]:


np.array([1,2,3])


# In[148]:


array_1 = np.array([[1,2,3,4,5],[7,8,9,11,13]])
print(array_1)


# In[151]:


#"We can assign an array with other types of data as well. For example, let's create an Array_2 with 4 numbers in one group, 
#and a mix of string and numbers in another group.\n",
#The result shows that one string value in the array turns all values into strings 
#even if you did not put quotation marks around the numbers. 
#This is different from Python lists where you can have different types of data in one list."


array_2 = np.array([[1,2,3,4],['hello world',6,7,8]])
array_2


# In[152]:


#To call a particular cell within an array, we use the row and column index to identify the location of the value. 
#Let's try to call the item in row 2 and column 1 and we get the value 4.
array_1


# In[153]:


array_1.shape


# In[154]:


#calling a cell within array[row,column]
array_1[1,2]


# In[155]:


# Retrieve the first item (index 0) from the second row (index 1)
array_1[1,0]


# In[156]:


print(array_1.min())
print(array_1.max())


# # PANDAS

# In[161]:


import pandas as pd


# In[158]:


markers = ['a','b','c']
list_1 = [12,34,36]
array_1 = np.array([36,78,92])
dict_1 = {'d': 20, 'e': 40, 'f': 50}


# In[159]:


#apply list into a series
pd.Series(data = list_1)


# In[160]:


#changing the index of a series
#We see that pandas automatically assigned indexs (0, 1, 2) to the list when the series was created. 
#We can change the index of a series by using the `markers` list we mentioned above by inserting it into the series code.
pd.Series(data = list_1, index = markers)


# In[162]:


pd.Series(data = array_1, index = markers)


# In[163]:


pd.Series(dict_1)


# In[164]:


a = "Mike"
b= sum
c = True
pd.Series([a,b,c])


# In[165]:


Gift_shop_sales = pd.Series(data = [300,400,500,600], index = ["magnets","coasters","handbags","snacks"])
Gift_shop_sales


# In[170]:


#gather a value by the index
Gift_shop_sales ['magnets']


# In[171]:


Gift_shop_sales2 = pd.Series(data = [360,400,800,600], index = ["magnets","coasters","handbags","snacks"])
Gift_shop_sales


# In[172]:


Gift_shop_sales + Gift_shop_sales2


# In[174]:


Gift_shop_sales3 = pd.Series(data = [360,400,800,600], index = ["magnets","coasters","handbags","Postcards"])
Gift_shop_sales3


# In[175]:


Gift_shop_sales + Gift_shop_sales2 + Gift_shop_sales3


# # PANDAS DATAFRAME

# In[177]:


Frame = np.array([[1,2,3,4],[5,6,7,8]])
Frame


# In[182]:


Rows = ['M','X']
Columns = ['U','Y', 'S','H']

Numbers = pd.DataFrame(Frame,Rows,Columns)
Numbers


# In[190]:


Dict_4 = {'Marks': [1,2,3,4],
         'Class':["A","B","C","E"]}
Dict_4


# In[191]:


Dictfram = pd.DataFrame(Dict_4  )
Dictfram


# # Generating Data using NumPy

# In[192]:


import numpy as np


# In[193]:


array_7 = np.arange(30)
array_7


# In[194]:


#providing a starting interval
np.arange(3,7)


# In[195]:


np.arange(10,30,3)


# In[196]:


np.linspace(0,10,30)


# In[198]:


#to call the index 4
array_7[3
       ]


# In[199]:


#gathering random floats
np.random.rand(10)


# In[200]:


#gathering a random integers with a range
np.random.randint(10,20)


# In[201]:


#gathering an array of random integers
np.random.randint(10,20,5)


# In[203]:


#gathering random integers with rows and columns
np.random.randint (1,100,(5,4))


# In[204]:


# to elimante randomness in values use the seed()
np.random.seed(10)
np.random.rand(6)


# # Importing data from external sources

# In[3]:


import pandas as pd
import pandas_datareader.data as pdr


# In[203]:


#pdr.DataReader("S&P/TSX", "Yahoo", '2023-06-01','2023-06-14')
import yfinance as yf

data = yf.download('^GSPTSE', start='2023-06-01', end='2023-06-14')
data


# In[212]:


pdr.DataReader("005930", "naver", '2023-06-01','2023-06-14')


# In[213]:


data = yf.download('^DJI', start='2023-06-01', end='2023-06-14')
data


# # Importing CSV File

# In[232]:


import os as os
Stores_dataframe = os.listdir(r"C:\Users\osuag\Downloads\Stores")

Stores_dataframe


# In[337]:


df = pd.read_csv(r"C:\Users\osuag\Downloads\Stores\train.csv")
df


# In[237]:


df.info()


# In[238]:


pd.to_datetime(df['date'])


# In[241]:


df['date'] = pd.to_datetime(df['date'])
df.info()


# # how to handle missing values

# In[243]:


df.isna()


# In[245]:


df.isna().sum()


# In[246]:


#removing null vales
df.dropna()


# In[249]:


#to check for no missing values
df.notna().sum()


# In[8]:


# replacing missing values with o
data_source = pd.read_csv(r"C:\Users\osuag\Downloads\Data Source.csv")
data_source


# In[9]:


data_source.isna().sum()


# In[10]:


data_source.info()


# In[256]:


pd.to_datetime(data_source['Date'])


# In[11]:


data_source['Date'] = pd.to_datetime(data_source['Date'])


# In[12]:


data_source.info()


# In[13]:


#converting objects to int
#pd.to_numeric(data_source['Q1'])
data_source['Q1'] = pd.to_numeric(data_source['Q1'], errors='coerce')
data_source.info()


# In[14]:


pd.to_numeric(data_source['Q1'],errors = 'coerce')
data_source['Q2'] = pd.to_numeric(data_source['Q1'],errors = 'coerce')
data_source.info()


# In[349]:


#filling empty cells with 0

data_source.fillna(0)


# In[265]:


#filling empty cells with ffillna that is filling forward
data_source.fillna(method = 'ffill')


# In[360]:


#filling empty cells with bfill that is filling backward
data_source.fillna(method = 'bfill')


# In[55]:


#filling with mean, median, mode
data_source = data_source.fillna({'Q1':data_source['Q1'].mode()[0],
           'Q2':data_source['Q2'].mean(),
           'Q3':data_source['Q3'].median(),
           'Q4':data_source['Q4'].mean()})
data_source


# In[281]:


data_source.dropna(axis = 1)


# In[285]:


#identifying unique values
pd.unique(data_source['Store'])


# In[287]:


# to see uniques values by column
data_source.nunique()


# In[289]:


data_source.drop_duplicates()


# In[291]:


data_source.drop_duplicates(subset = ['Store'])


# In[305]:


#spliting text strings

data_source['ProductID'].str.split('-',expand=True)
data_source


# In[57]:


#to instantiate a change
data_source = data_source[['ProductID','SpecialID']] = data_source['ProductID'].str.split('-',expand=True)


# # Eporting data with pandas

# In[308]:


data_source.to_csv('export.csv')


# In[127]:


exercise = pd.read_csv(r"C:\Users\osuag\Downloads\Chapter Exercise Data.csv")
exercise


# In[311]:


exercise.info()


# In[313]:


exercise.isna().sum()


# In[315]:


exercise.fillna(0 )


# In[321]:


Sales = exercise['PricePerItem']* exercise['Quantity']
Sales


# In[322]:


exercise.dropna()


# In[323]:


exercise.fillna(0)


# In[351]:


data_source


# In[352]:


#selecting a particular column
data_source['Store']


# In[354]:


#selecting multiple columns
data_source[['Store','CategoryID', 'ProductID']]


# In[355]:


# getting the first 5 rows
data_source.head()


# In[356]:


data_source.tail()


# In[17]:


#loc is  label based
#iloc is integer based
data_source.loc[:,['Store','Date']]


# In[18]:


#selecting columns using iloc with column index
data_source.iloc[:,[0,1]]


# In[20]:


#selecting all rows with all columns in order from store to product
data_source.loc[:,'Store':'ProductID']


# In[21]:


data_source.iloc[:,0:5]


# In[22]:


#selecting rows and columns
data_source.loc[[0,7],:]


# In[24]:


data_source.iloc[[0,7],:]


# In[29]:


#selecting a range of rows
data_source.iloc[0:7,:]


# # Conditional statement

# In[34]:


Quarter40k = data_source['Q1'] >= 40000
Quarter40k


# In[35]:


data_source[Quarter40k]


# In[36]:


data_source[data_source['ProductID'] == '12XXRP-Q']


# In[38]:


00


# In[73]:


df_grades = pd.read_csv(r"C:\Users\osuag\Downloads\Student Grades.csv")


# In[74]:


#Adding a new column, the rows has to be the same number with the index

city = ['Vancouver','Toronto','Calgary','Edmonton','Regina', 'Burnaby', 'Coquitlam', 'London', 'Ottawa', 'Texas',
       'Coquitlam', 'London', 'Ottawa', 'Texas','Edmonton','Regina', 'Burnaby', 'Coquitlam', 'London', 'Ottawa',
         'Texas', 'Toronto','Calgary','Edmonton','Regina', 'Burnaby', 'Coquitlam', 'London',  'Texas','Edmonton']
    
df_grades['City'] = city
df_grades


# In[75]:


#Another method of adding new columns is to use the `insert()` function. 
#This function allows us to add the column in any position we like and not only the end. 
#Consider a scenario where now we want to add the age of students in our data, and want to see it before their name

df_grades.insert(1,"Age",[21, 23, 24, 21, 25, 18, 22, 25, 28, 34,
                      22, 23, 25, 21, 25, 26, 24, 23, 29, 31,
                         28, 24, 24, 23, 22, 20, 23, 25, 28, 33])
df_grades


# In[76]:


new_student = {'StudentID': 20123420, 'Age': 21, 'FirstName': 'Scottie', 'LastName': 'Barnes', 'GradeAverage' : 'A', 
               'Faculty':'Science', 'Tuition': 50000, 'OfficeHoursParticipated': 0, 'ClassesSkipped' : 0, 'City': 'Toronto'}
df2 = pd.DataFrame(data=new_student, index=[30])
df_grades = df_grades.append(df2)
df_grades.tail()


# In[77]:


df_grades = df_grades.drop([30])
df_grades


# In[59]:


# another way
business_students = df_grades['Faculty'] == 'Business'
business_students


# In[78]:


df_grades[business_students]


# In[79]:


df_grades[business_students].index


# In[80]:


#droping the indexes
df_grades = df_grades.drop(df_grades[business_students].index)
df_grades


# In[81]:


#dropping columns
df_grades = df_grades.drop(['City'], axis = 1)
df_grades


# In[89]:


#setting new index so its more related to your need
if 'StudentID' in df_grades.columns:
    df_grades = df_grades.set_index('StudentID')
df_grades


# In[90]:


# to revert to the old index
df_grades = df_grades.reset_index()
df_grades


# In[91]:


#selecting the count of students IDs, grouped by faculty
df_grades.groupby(by = 'Faculty')['StudentID'].count()


# In[92]:


#selecting the avareage age by faculty
df_grades.groupby(by = 'Faculty')['Age'].mean()


# In[93]:


#selecting the average tuition by each faculty and Grade
df_grades.groupby(by=['Faculty', 'GradeAverage'])['Tuition'].sum()


# In[94]:


data2 = {'StudentID': [20123420,20123421], 'Age':[33,31], 'FirstName': ['Stephen','Klay'],
 'LastName': ['Curry','Thompson'], 'GradeAverage': ['A','A'], 'Faculty': ['Science','Math'], 
         'Tuition': [31000,41000], 'OfficeHoursParticipated': [3,1], 'ClassesSkipped': [4,6], 'State': ['California','California']}
df_grades2 = pd.DataFrame(data2)
df_grades2


# In[100]:


#merging tables together
df_gradez = pd.concat([df_grades,df_grades2])
df_gradez


# In[97]:


#joining horizontally
pd.concat([df_grades,df_grades2], axis =1)


# # statistics in python

# In[98]:


import pandas as pd
import numpy as np


# In[101]:


df_gradez['Tuition'].mean()


# In[102]:


df_gradez['OfficeHoursParticipated'].median()


# In[103]:


df_gradez['ClassesSkipped'].mode()


# In[105]:


df_gradez[['ClassesSkipped', 'Tuition']].mean()


# In[107]:


df_gradez.var(numeric_only = True)


# In[108]:


df_gradez.std(numeric_only = True)


# In[109]:


df_grades['Tuition'].std()


# In[110]:


df_grades['Tuition'].var()


# In[111]:


#exploratory analysis using describe
df_grades.describe()


# In[115]:


#z-score` is a measurement that describes the distance a value is from the mean of a normal data distribution. 
#`Z-score` is measured in terms of `standard deviations`.
#A `z-score` typically tells us how far a value is in standard deviations, so that we can understand it in a scaled value.
#A `z-score` can be calculated using the following formula: z = (X – μ) / σ
mean = df_grades['OfficeHoursParticipated'].mean()
std = df_grades['OfficeHoursParticipated'].std()


# In[116]:


df_grades['z-score'] = df_grades['OfficeHoursParticipated'] - mean/std
df_grades


# In[117]:


#Outliers` are defined as data points that are abnormally far from what is considered \"normal\". 
#Sometimes, outliers causes hinderance to our data, as they might be there due to errors and it is up to us to decide if these abnormal data are to be included.
#Before we start identifying outliers, we are going to add a new column to our DataFrame `GPA`, based on the `GradeAverage` of the students. We will create this using the `np.select` function.
#np.select ([list of categories], [list of categories to be replaced, in the same order]),

df_grades['GPA'] = np.select([df_grades['GradeAverage'] == 'A', 
                                  df_grades['GradeAverage'] == 'B',
                                  df_grades['GradeAverage'] == 'C',
                                  df_grades['GradeAverage'] == 'D',
                                  df_grades['GradeAverage'] == 'F'],
                                  [4,3,2,1,0])

df_grades


# In[ ]:


#Data that is far outside the `interquartile range (IQR)` is identified as an outlier, also known as the`IQR rule`. 
#The `IQR` is a measure of how 50% of the \"middle\" of the data is spread out.
    #"The `IQR` is calculated by subtracting the 75th percentile data point (third quartile) with the 25th percentile data point (first quartile). \n",
    #"The `IQR rule` is calculated by multipying the `IQR` by 1.5 and adding it to the third quartile and subtracting it from the first quartile. If a number is greater than the third quartile or less than the first quartile after the addition/subtraction, then it can be seen as an outlier.\n",
  #Example
    # IQR = 20 
    #  Q3 = 70
   # Q1 = 50
# IQR x 1.5 = 30
  # Q3 + 30 = 100 --> Anything above 100 is considered an outlier for this dataset
   #Q1 - 30 = 20 --> Anything below 20 is considered an outlier for this dataset
    #"With this logic, we can identify if any students have a GPA that is an outlier and add this to our data
    


# In[118]:


#np.percentilefinds the specified percentile of an array
q3 = np.percentile(df_grades['GPA'], 75)
q1 = np.percentile(df_grades['GPA'],25)
IQR = q3 - q1

IQR


# In[119]:


#define the IQR rule for the GPA column
IQR_rule = (1.5 * IQR + q3 < df_grades['GPA']) | (q1- 1.5* IQR > df_grades['GPA'])
# use np.where to cretate outlier column is a student 's GPA an outlier or not 
df_grades ['Outlier'] = np.where(IQR_rule, 'yes','no')
df_grades


# In[120]:


#Correlation` is the method to evaluate the strength of a relationship between two continous variables. 
#This not only shows the direction between two variables, but also the magnitude of the relationship. 
#`Correlation` values are between -1 and 1, with -1 being the highest value indirectly proportional, and 1 being the highest value directly proportional
df_grades.corr()


# In[125]:


# using heat map to see relationships
import seaborn as sns

sns.heatmap(df_grades.corr(), cmap = 'coolwarm')


# In[198]:


import pandas as pd
cakes = pd.read_csv(r"C:\Users\osuag\Downloads\Chapter Exercise Data.csv")
cakes


# In[199]:


df_cakes = pd.concat([cakes,exercise])
df_cakes


# In[149]:


df_cakes.info()


# In[150]:


df_cakes.fillna(0)


# In[130]:


df_cakes.nunique()


# In[146]:


Quantitymax = df_cakes['Quantity'].max()
Quantitymax


# In[147]:


df_cakes['Quantitymax'] = df_cakes['Quantity'] >= 10
df_cakes


# In[142]:


df_cakes['Quantitymax']
df_cakes


# In[143]:


Order = df_cakes['OrderID'] 
Order


# In[144]:


#if 'StudentID' in df_cakes.columns:
df_cakes = df_cakes.set_index('OrderID')
df_cakes


# In[145]:


df_cakes['Quantity'].mean()


# In[176]:


#John realized that he wanted to add the amount he would make per order onto his DataFrame. 
#Create a new column that displays the amount he would make per order.
df_cakes['sales'] = df_cakes['Quantity'] * df_cakes['PricePerItem']
df_cakes


# In[175]:


#John wants to send out thank you cards to the customers that spent at least $50 on their order. 
#Filter the DataFrame for the list of customer IDs that fit this criteria.
df_cakes['cake_50'] = df_cakes['sales'] >= 50
df_cakes


# In[171]:


df_cakes[cake_50]


# In[187]:


#John wants to send out a gift card for every 300th customer. Find the list of CustomerIDs that qualify for a gift card.
df_cakes.iloc[[299,599,899],:]


# In[180]:


df_cakes['ShippingDistance'].mean()


# In[196]:


df_cakes.drop(['ShippingDistance'], axis = 1)
df_cakes.reset_index()


# In[182]:


df_cakes['Quantity'].count()


# In[185]:


df_cakes['Quantity'].mode()[0]


# In[200]:


count_of_quantity = df_cakes.groupby('Quantity')['OrderID'].count()
count_of_quantity


# # Visualizing data for exploratory analysis

# In[278]:


#importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[279]:


# setting start date
startdate = '2022-01-01'
enddate = '2022-12-31'
stocks = yf.download('SPY',startdate,enddate )[['Adj Close']]
bonds = yf.download('TLT',startdate,enddate )[['Adj Close']]
oil = yf.download('USO',startdate,enddate )[['Adj Close']]
print(stocks.head())
print(bonds.head())
print(oil.head())


# In[230]:


stocks = stocks.pct_change()
bonds = bonds.pct_change()
oil = oil.pct_change()

print(stocks.head())
print(bonds.head())
print(oil.head())


# In[220]:


#concatenating columns
stocksAndBonds = pd.concat([stocks,bonds,oil], axis = 1, join = 'inner')
#renaming columns
stocksAndBonds.columns = ['SPY', 'TLT', 'USO']
stocksAndBonds.head()


# # CREATING HISTOGRAMS

# In[231]:


#create a hostogram or distribution plots for stocks
sns.histplot(stocksAndBonds['SPY'])


# In[232]:


# one way to control the display of our histogram is bins.
sns.histplot(stocksAndBonds['SPY'], bins = 50)


# In[233]:


#create histogram with multiple column
sns.histplot(stocksAndBonds, bins = 25, multiple = 'dodge')


# In[234]:


sns.histplot(stocksAndBonds[['SPY','TLT']], bins = 25, multiple = 'layer')


# In[235]:


#creating boxplot
sns.boxplot(stocksAndBonds)


# In[236]:


# comparing spy and tlt
sns.boxplot(stocksAndBonds[['SPY','TLT']])


# In[237]:


#creating pairplot
sns.pairplot(stocksAndBonds)


# In[238]:


#correlation matrix for the 3 stocks
stocksAndBonds.corr()


# In[239]:


sns.heatmap(stocksAndBonds.corr())


# In[ ]:


#Three common arguments to control the display of a heatmap are:

#vmin & vmax
#annot
#cmap
#vmin` and `vmax` control the scale of the heatmap.As correlation is measured between -1 and 1, we can update the minimum value to -1.\n",
#The `annot` argument allows us to display the values of a section in the heatmap. We can set this to `True` to see the correlation coefficient for each section.\n",
#The `cmap` argument lets us set the color of the scale in the heatmap. There are several built-in options to choose from. We can update our heatmap to use the `coolwarm` option."


# In[241]:


sns.heatmap(stocksAndBonds.corr(), vmin = -1, annot = True, cmap = 'coolwarm')


# # Creating insightful visulas
# 

# In[290]:


startdate = '2022-01-01'
enddate = '2023-05-31'
stocks = yf.download('SPY',startdate,enddate )[['Adj Close']]
bonds = yf.download('TLT',startdate,enddate )[['Adj Close']]
oil = yf.download('USO',startdate,enddate )[['Adj Close']]
print(stocks.head())
print(bonds.head())
print(oil.tail())


# In[291]:


#concatenating columns
stocksAndBonds = pd.concat([stocks,bonds,oil], axis = 1, join = 'inner')
#renaming columns
stocksAndBonds.columns = ['SPY', 'TLT', 'USO']
stocksAndBonds.head()


# In[287]:


#creating line charts using years and stock_value

years = stocksAndBonds.index
stock_value = stocksAndBonds['SPY']

plt.plot(years,stock_value)


# In[292]:


#creating line charts using years and stock_value

years = stocksAndBonds.index
stock_value = stocksAndBonds['SPY']

plt.plot(years,stock_value);


# In[253]:


#formating line chart
plt.plot(years,stock_value)
plt.title('Trends in SPY')
plt.xlabel('Years')
plt.ylabel('Adj Close')
plt.xticks(rotation = 45);


# In[259]:


#formating line chart
plt.figure(figsize = (12,8))
plt.plot(years,stock_value, color = 'red')
       
plt.title('Trends in SPY')
plt.xlabel('Years')
plt.ylabel('Adj Close')
plt.xticks(rotation = 45);


# In[263]:


#setting size plot
plt.figure(figsize = (12,8))
plt.plot(years,stock_value, color = 'red', marker = 'o', markersize = 3 , linestyle = '--')
#adding titles and labels    
plt.title('Trends in SPY')
plt.xlabel('Years')
plt.ylabel('Adj Close')
plt.xticks(rotation = 45)
#add limits to the axes
plt.ylim(340,500);


# In[264]:


stock_mean = stocksAndBonds.mean()
stock_mean


# In[266]:


bar_plot = pd.DataFrame(data = stock_mean, columns = ['mean_value'])
bar_plot


# In[267]:


#set plot size
plt.figure(figsize = (12,8))
#create bar plot to compare the means of our stocks
sns.barplot(x = bar_plot.index, y = 'mean_value', data = bar_plot);


# In[272]:


#Formatting Bar Plots
#We've created a standard bar plot using the seaborn `barplot()` function. 
#To start to change the appearance of bar plot, we can change some parameters from their default setting and add some other functions as well.\n",
#The first parameter that we can update is `palette`. This changes the color of the bars in the bar plot. 
#There are lots of built-in options to choose from. A list of palettes from the Seaborn documentation can be found here: https://seaborn.pydata.org/tutorial/color_palettes.html. In our example, we can look at the `coolwarm` palette that we used for our correlation matrix heatmap. We can also use the `colorblind` palette, which ensures that our visuals are accessible to all users."
#set plot size
plt.figure(figsize= (12,8))

#create bar plot with 'coolwarm' palette
sns.barplot(x = bar_plot.index, y = 'mean_value', data= bar_plot, palette = 'coolwarm')
#add titles and labels
plt.title('Mean Adj Close for stocks')
plt.xlabel('stocks')
plt.ylabel ('Mean Adj Close');


# In[274]:


#set plot size
plt.figure(figsize= (12,8))

#create bar plot with 'coolwarm' palette
sns.barplot(x = bar_plot.index, y = 'mean_value', data= bar_plot, palette = 'colorblind')
#add titles and labels
plt.title('Mean Adj Close for stocks')
plt.xlabel('stocks')
plt.ylabel ('Mean Adj Close');


# In[275]:


#set plot size
plt.figure(figsize= (12,8))

#create bar plot with 'coolwarm' palette
sns.barplot(y = bar_plot.index, x = 'mean_value', data= bar_plot, palette = 'colorblind')
#add titles and labels
plt.title('Mean Adj Close for stocks')
plt.ylabel('stocks')
plt.xlabel ('Mean Adj Close');


# In[277]:


#set plot size
plt.figure(figsize= (12,8))

#create bar plot with 'coolwarm' palette
sns.barplot(y = bar_plot.index, x = 'mean_value', data= bar_plot, palette = 'colorblind')
#add titles and labels
plt.title('Mean Adj Close for stocks')
plt.ylabel('stocks')
plt.xlabel ('Mean Adj Close')
plt.annotate('SPY has the highest mean value', xy= ( 300,0.5));


# # Scatter Plots

# In[294]:


stocks = stocks.pct_change()
bonds = bonds.pct_change()
oil = oil.pct_change()

stocksAndBonds_pct = pd.concat([stocks, bonds, oil], axis = 1, join = 'inner')
stocksAndBonds_pct.columns = ['SPY','TLT','USO']
stocksAndBonds_pct.tail()


# In[295]:


#set plot size
plt.figure(figsize=(12,8))
#scatter plot witj seaborn.scatterplot()
sns.scatterplot(x = stocksAndBonds_pct ['SPY'], y = stocksAndBonds_pct ['TLT']);


# In[297]:


stocksAndBonds_pct['Year'] = stocksAndBonds_pct.index.year
stocksAndBonds_pct.head()


# In[298]:


#set plot size
plt.figure(figsize=(12,8))
#scatter plot witj seaborn.scatterplot() and style parameter
sns.scatterplot(x = 'SPY' , y = 'TLT', data = stocksAndBonds_pct,style  = 'Year')
plt.title('percentage change in stocks vs bonds');


# In[299]:


#set plot size
plt.figure(figsize=(12,8))
#scatter plot witj seaborn.scatterplot() and style parameter
sns.scatterplot(x = 'SPY' , y = 'TLT', data = stocksAndBonds_pct,hue  = 'Year')
plt.title('percentage change in stocks vs bonds');


# In[300]:


#set plot size
plt.figure(figsize=(12,8))
#scatter plot witj seaborn.scatterplot() and style parameter
sns.scatterplot(x = 'SPY' , y = 'TLT', data = stocksAndBonds_pct,size  = 'Year')
plt.title('percentage change in stocks vs bonds');


# In[310]:


import seaborn as sns
import matplotlib.pyplot as plt

stocksAndBonds_pct.fillna(0)
# Set plot size
plt.figure(figsize=(12, 8))


# Scatter plot with seaborn.scatterplot() and style parameter
sns.scatterplot(x='SPY', y='TLT', data=stocksAndBonds_pct, style='Year', hue='USO', size='USO')

# Set title
plt.title('Percentage Change in Stocks vs Bonds')

# Display the plot
plt.show()


# In[311]:


#importing file
exercise_2 = pd.read_csv(r"C:\Users\osuag\Downloads\Chapter Exercise Data.csv")
exercise_2


# In[312]:


exercise_2.fillna(0)


# In[313]:


exercise_2.info()


# In[315]:


exercise_2['Amount'] = exercise_2['Quantity'] * exercise_2['PricePerItem']
exercise_2


# In[316]:


exercise_2.set_index(['OrderID'])


# In[342]:


#order gretaer than 50dollar
exercise_2['order_50'] = exercise_2['Amount'] >= 50
exercise_2


# In[350]:


exercise_2['order_50']  = exercise_2['Amount'] >= 50
exercise_2[order_50]


# In[351]:


#removing the shipping distance
exercise_2.drop('ShippingDistance', axis = 1)


# In[353]:


count_of_quantity = exercise_2.groupby('Quantity')['OrderID'].count()
count_of_quantity


# In[365]:


#John wants to see the number of products contained in each order - the distribution of quantity. 
#Create a histogram on the Quantity column from the df DataFrame.
plt.figure(figsize = (12,8))
sns.histplot(exercise_2['Quantity'])


# In[367]:


#John would like to know how many orders each customers has placed. Create a bar plot to show this – 
#each bar should be the number of orders, aggregated by the count of customers who placed that many orders."
count_of_order = pd.DataFrame(exercise_2.groupby('CustomerID')['OrderID'].count())
count_of_order


# In[370]:


#count number of customers for each order quantity
orders_by_cust = pd.DataFrame(count_of_order.groupby('OrderID')['OrderID'].count())
orders_by_cust


# In[371]:


#creating the barplot
sns.barplot(x = orders_by_cust.index, y = 'OrderID', data = orders_by_cust);


# In[364]:


#John wants to know the relationship between the quantity of products in an order and the amount paid for that order. 
#Create a scatter plot of Quantity vs Amount.
#set plot size
plt.figure(figsize=(12,8))
#scatter plot witj seaborn.scatterplot() and style parameter
sns.scatterplot(x = 'Amount' , y = 'Quantity', data = exercise_2)
plt.title('Quantity Vs Amount paid');


# In[ ]:




