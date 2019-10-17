# task 2

So I have posted the solution to task1 here. If you feel you have any problem just reach out to any hello world member.

so next we will use some very fundamental and very useful functions known as input(), print(), and while loop.
first print 'press any key to start playing!' using the print function.

then use input() to take the key that the user presses.

refer https://www.hackerearth.com/practice/python/getting-started/input-and-output/tutorial/

next we start a while loop with the condition that repeat until all the alphabets of string 'hollywood' are not cut.
or to say it simply we loop till there are no alphabets left in 'hollywood'.

hint:use len() function to know if there are alphabets left in veriable containg the string 'hollywood'.
reference for while loops https://www.w3schools.com/python/python_while_loops.asp

next print the number of tries the user has left using the len function again.
to get the guess that the user has made use the input() function and store it to a variable guess.

always use variable names that will help you know what is stored inside them. using variable names such as 'a' or 'b' and so on make things confusing.

next we take the guess that user has made and check if it is present in the movie name and based on that make ur next decision.
1.If the guess is present in the movie name we find all the places the alphabet is present in the name and replace the '_' with the guess user made.
2.If guess is not in the movie name we remove one alphabet from string hollywood.

for first step try to use a new concept knwon as list comprehension.
we iterate over each alphabet of movie name and check if it matches with guess made by user and store the index of the place where the alphabet matches the guess made by user.
next we we start a for loop and go to those indexes from previous step and replace "_" with alphabet.
reference:https://www.programiz.com/python-programming/list-comprehension

for step 2 where the user guess does not match with any alphabet in movie name we remove one alphabet from hollywood. For simplicity use the pop() function to remove one element.

thats all for this task. I will post the solution to this task2 next week.
or if you are a curious cat just hit me up!
