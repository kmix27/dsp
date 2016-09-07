# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples are immutable, meaning you cannot change a tuple once it's been defined.  Lists are mutable and can be added to, removed from, sorted, inserted into, and further changed once they have been defined.  Generally you will use one or the other based on this mutability or lack thereof.  Because they are immutable tuples are much faster to iterate through, because python doesn't need to concern itself with the potential for values to change.  Syntactically you define a tuple as simply an assortment of comma separated values alone or enclosed within round brackets, lists are defined as an assortment of comma separated values within square brackets.  Both are an assortment of comma separated values that you can do something with.  Only tuples can be used as keys in dictionaries.  This is done to dramatically reduce the complexity of lookup functions. efficient lookup funtions operate by hashing the values and comparing hashed lookup value with the hashed key values, and lists do not provide a valid hash method.  If lists could be used as keys, every lookup would require searching sequentially through every value in the list, which would quickly become unweildy given large datasets.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are both containers which store assortments of data, with both you are able to retrive individual elements.  Both are iterable, and will support functions that call for an iterable object. With both you are able to use comprehension syntax to apply transformations or filtrations accross the elements contained within in a concise manner. Though they use diffrent methods, you can add or remove elements providing the set is not a frozenset type. 

Sets are unordered, and each element must be unique. When creating a set, all duplicate values are dropped in the process. They allow operations of set theory, such as union or intersection, which allows one to perform membership testing.  Because sets are searched via a hash lookup, only hashable items can be stored in sets.  This also makes them far more efficient at finding elements. Sets can be mutable or immutable depending on the constructor used.  Immutable sets because they are immutable, can be used as dictionary keys.  You would use a set if speed was important and or you couldn't have repeated values,  say you wanted an assortment of customer ID's that had placed 1 or more orders from a dataset where customer ID's were paired with order numbers. a set would be appropriate, because it would exclude any repeat values upon creation.  Using the same example, you could also create a set of customer ID's that had contacted customer service and use set operations to easily compare the differences between the two sets.  sets are faster because they are implemented using hash tables, so instead of looking through the entire list to determin if a match is present, hash location is compared and if the locations are equal, then a match is present. this is important because it makes search performance more or less independent of size, thus dramaticly improving performance on large sets.

Lists are a mutable sequence type, they support a variety of operations to modify them in place, such as slicing, sorting, reversing, among others.  Lists are ordered, and should be used where order counts.  If you were doing text analysis for example, and you wanted to split a paragraph up into individual words for analysis, a list could do that while inherently maintaining the original order, or not depnding on the end goal, and the transformations you preform on the resulting list. Lists can contain unhashable values, which sets cannot.  When searching a python list, every value within the list must be checked against the search value, fine for small datasets, but expensive for large ones. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

A lambda function is an anonymous function that is not associated with an identifier.  They are used to pass value to higher order functions, or in cases where there won't be repeat use to justify defining a named function.  Lambda functions can make your code cleaner and easier to read,  and can limit instances of simple one line functions.  They are best used when the function needed is simple, anything too complex it's better to define a seprate function.   An example of lambda's use in the sort function would be:

n = [1,0,-15,-2,10,-5,3,4,11,1,-4,6]
n.sort(key = lambda x: abs(x) )
print(n)
>>>[0, 1, 1, -2, 3, 4, -4, -5, 6, 10, 11, -15]

In this example we are sorting using absolute value, a lambda function is used within sort to determin the absolute value of each element of the list and sort returns the list in ascending order.  

Lambda is also useful for filtering and mapping functions to lists:

from math import sqrt
def findPrimes(x,y):
	nums = range(x,y)
	for i in range(2,int(sqrt(y))+1):
		nums = list(filter(lambda x: x == i or x % i, nums))
	return nums

The above function uses lambda within the filter function to apply the seive of eratosthenes algorithim to a given range of numbers. This returns a list of the prime numbers included within that range. Of note,  this is written for printing out the list within python 3, filter() returns a filter object in python 3, so in order to print the list we enclose it in list().  In python 2 you could omit the list() portion.  


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

list comprehensions are a way of performing operations on a list. Because they are all on one line they are generally easier to read and understand than mapping to a function, and generally makes for cleaner code.  There are up to 3 parts in both.  A loop, where we ID the control variable and the list, the transformation, where we modify the control variable and return the modified value, and the filtering, where we select the elements to process into the new list.   Map is when you define a function to append to a new list the result calling a given function or performing an operation and or filtering on the elements of your original list. 

#ex 1 double the elements in a list:
numList = [4,6,2,3,4,5,6,4,8,6,5,9,1]

#list comprehension:

dubList = [i*2 for i in numList]
print(dubList)
>>>[8, 12, 4, 6, 8, 10, 12, 8, 16, 12, 10, 18, 2]

#The same accomplished with map would look like this:

def dubIt(myList):
	dub_List=[]
	for n in myList:
		dub_List.append(n*2)
	return dub_List

print(dubIt(numList))
>>>[8, 12, 4, 6, 8, 10, 12, 8, 16, 12, 10, 18, 2]

#ex 2, return only positive numbers:
numList = [-1, 3,6,-6,2,9,12,0,-14,9,3,5,1,7,-2]
#list comprehension:
posList = [ i for i in numList if i>=0 ]
print(posList)
>>>[3, 6, 2, 9, 12, 0, 9, 3, 5, 1, 7]

# the same accomplished with mapping:


def findPositives(myList):
	pos_List=[]
	for n in myList:
		if n >= 0:
			pos_List.append(n)
	return pos_List
print(findPositives(numList))
>>>[3, 6, 2, 9, 12, 0, 9, 3, 5, 1, 7]

# ex 3 set comprehension:
# using the same function as example 1, we change to curly braces so the output is a set.  The result is a set of 2X each unique value in the original list
numList = [4,6,2,3,4,5,6,4,8,6,5,9,1]
dubSet = {i*2 for i in numList}
print(dubSet)
>>>{2, 4, 6, 8, 10, 12, 16, 18}



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
513 days 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





