![image](https://img.thedailybeast.com/image/upload/d_placeholder_euli9k/dpr_2.0/c_limit,w_585/fl_lossy,q_auto/v1/galleries/2011/05/05/cute-seals/cute-seals-4_pdysfd)

# Practice with for loops

## Exercises:

### 1. Given the numbers 1 through 10, write code that adds 5 to each number and prints out the result. 
Do not use for loops for this exercise: You should write a new line of code for each operation. 

  Discussion (with a partner): 
 - What value is changing every time you write a line of code? 
 - What operation is repeated? 
 - How long did it take you to write the code for this exercise? How long do you think it would take if you wanted to perform this exercise for the numbers 1 through 1000?
 
### 2. Now, see if you can find a more efficient way to write #1.
You may want to use the [range function](https://www.w3schools.com/python/ref_func_range.asp), which we used previously, to represent large ranges of numbers. 

### 3. Given a list `a = [1, 'ocean', -101, 2.2, 'hello world', 'eddies', '110']`, print out every element in the list using loops.

### 4. (Challenging): For the list `a` above, write a loop that prints out the value of the element plus 10, if the element is an integer. If it is a string, print out "string". 
Hint: Using the [type function](https://www.pythoncentral.io/check-object-type-python/) will tell you whether an object is a string, integer or something else. For example, `type(10)` should return `int`.

### 5. `days = [[1901,1,2], [1992, 12, 11], [1685, 9, 4], [2018, 6,29]]` is a list of dates with the format `[year, month, day]`.
i.e., [1901, 1, 2]  corresponds to Jan. 2, 1901.<br/>
Recall what we have learned about [datetime.date function](https://www.w3schools.com/python/python_datetime.asp). Your goal is to create a new list called `new_dates` that contains each of these dates in `days` as a datetime object. 
<br/>
First, write this code without using any loops. i.e., you should have a new line of code (or more!) for each date conversion.
<br/>
Once you have written the code *without* using any loops, rewrite it with a for loop! If you get stuck, try to answer these two questions:
- What operation/action is repeated every single time?
- What value changes each time the operation takes place?

**Challenge (practice with timedelta)**: Create a new list called new_dates_plus_30. Using the [timedelta function](https://www.guru99.com/date-time-and-datetime-classes-in-python.html) function, alter the code you have already written to fill this new list with each of the values in new_dates plus 31 days. For example, Jan. 2, 1901 will become Feb. 2, 1901, Dec. 11, 1992 will become Jan. 11, 1993, etc. 

### 6. You've just opened up a netCDF file to find out that your time variable doesn't make any sense! 
It has values between 1 and 16, with no obvious units! After some exploration, you realize that the units are actually days since Jan. 1, 2019. 

a. Using the [datetime.date function](https://www.w3schools.com/python/python_datetime.asp) and [timedelta function](https://www.guru99.com/date-time-and-datetime-classes-in-python.html), write a function called `date_adder` that takes in a value from your time variable and converts it into mm/dd/yy. 
Hint: If your first time value is "1 day since Jan. 1, 2019", what is its value in mm/dd/yy? What mathematical operation are you performing?

b. Now, create a new list called `mmddyy`. *Without using any loops*, use your function `date_adder` to fill this list with the mm/dd/yy equivalent of the dates in your time variable. 

c. Lastly, see if you can find a more efficient way to perform **b** using a for loop. Again, it may help to ask yourself:
 - What operation/action is repeated every single time?
 - What value changes each time that operation takes place?
 
 
If you finish and want more practice with loops, try [these exercises](https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php). 




 


