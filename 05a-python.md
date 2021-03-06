# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Similarities:  
* Both are a sequence of values  
* Both use integer indexing  
* Both support slicing, adding, multiplying, and checking for membership
* Both can have values of any type  
 
>> Differences:  
* Tuples are immutable while lists are mutable (elements of a tuple cannot be modified)  
* Tuples are enclosed in parentheses while lists are enclosed in square brackets  

>> Dictionary keys must be immutable so only tuples will work as dictionary keys.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Similarities:  
* Both are a sequence of values  
* Both objects are mutable   
 
>> Differences:  
* A set is unordered while a list uses integer indexing  
* The elements of a set are unique while lists can have duplicates  
* Sets are enclosed in curly brackets while lists are enclosed in square brackets  

>>Finding an element in a set is faster than a list because lists use a linear search algorithm while sets use a hashtable algorithm. Unlike sets, the longer the list, the longer the search time.
>>Example:  
```python
my_string = 'sets and lists'
my_set = set(my_string)
my_list = list(my_string)
print my_set
print my_list
```  
```python
set(['a', ' ', 'e', 'd', 'i', 'l', 'n', 's', 't'])
['s', 'e', 't', 's', ' ', 'a', 'n', 'd', ' ', 'l', 'i', 's', 't', 's']
``` 
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A `lambda` function, also called an anonymous function, is a function which is defined for one time use without a name. This is useful when you would like to create a quick and simple function without having to seperately define it for use.  

>> When using the `sorted()` function, the `key` parameter is used to specify a function to be called on each list element before sorting.  
```python
sorted([11, -2, 7, -43, -15, 4], key=lambda x: abs(x))
```  
```python
[-2, 4, 7, 11, -15, -43]
```  
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a tool to construct a list from an iterator such as another list. You could use map and filter to contruct a list in the same way, however using list comprehensions can be more concise and easier to read. For example to create a list which doubles the even numbers of a list of integers called `numbers`, you can use either of the following ways:
```python
numbers = [6, 10, 4, 7, 4]
double_evens_mf = map(lambda n: n * 2, filter(lambda n: n % 2 == 0, numbers))
double_evens_lc = [n * 2 for n in numbers if n % 2 == 0]
print double_numbers_mf
print double_numbers_lc
```  
```python
[12, 20, 8, 8]
[12, 20, 8, 8]
```  
Set comprehensions work the same way as lists comprehensions. You just replace the square bracket syntax for lists with the curly bracket used for sets:
```python
double_evens_set = {n * 2 for n in numbers if n % 2 == 0}
print double_evens_set
```  
```python
set([8, 20, 12])
```  
To create a dictionary, use the same syntax as a set, but specify the key:
```python
double_evens_dict = {n: n * 2 for n in numbers if n % 2 == 0}
print double_evens_dict
```  
```python
 {10: 20, 4: 8, 6: 12}
 ```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> There are 937 days between 01-02-2013 and 07-28-2015

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> There are 513 days between 12312013 and 05282015

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> There are 7850 days between 15-Jan-1994 and 14-Jul-2015

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





