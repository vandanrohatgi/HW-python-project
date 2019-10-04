# HW-python-project
A basic movie guesing game for introduction to concepts like loops,if-else,indexing,lists,input-output etc. with more intermediate topics like list comprehensions.

Ever played hollywood-bollywood? well this project will help you make one that is a close second using python.
when you are all done with the project you will walk away with a pretty good game and a good idea of about how python works.

# Task1-Setting it all up

first of all to get python follow the instructions on https://realpython.com/installing-python/
second you will need an IDE or a text editor to write your programs in such as vs code,pycharm or maybe even the default in-built text editor. 
So for my projects I use visual studio code. get it from here https://code.visualstudio.com/download 
and don't forget to download the python extension after you install vs code.
if you are facing difficulties on linux on installing vs code then use the pre installed linux software store to install it.

So now you you are all set up. Go ahead and create a new file and name it anything you want to.
Make sure you save it with ".py" extension at the end to indicate to computer that we are working on a python file.

# Its coding Time!
for first task we will make a list of all the movies that we will want. You can you the list I have provided or make your own.
A list is just used to store stuff.
next will create two more lists that will contain the vowels and the word 'hollywood'.
listofmovies=['avengers endgame','star wars the force awakens','avengers infinity war','jurassic world','the lion king','furious seven','black panther','harry potter',
'frozen','beauty and the beast','incredibles two','iron man three','minions','aquaman','aladdin','finding dory','zootopia','spectre','spider man homecoming','batman v superman','hunger games'
]
vowels=['a','e','i','o','u']
string=['h','o','l','l','y','w','o','o','d']

next we will use our first library/module known as random. It handles all the tasks that require generating/choosing random values.
Use it to choose a random movie from the list of movies.Particularly use the random.choice() method.
refer https://docs.python.org/2/library/random.html to know more about random and how to use it.

next task is to convert the randomly chosen movie to the form that we know:-

harry potter ->  '_a___/_o__e_'
we remove all consonants and only leave the vowels.
first create an empty list like this :-
toshow=[] or toshow=list()
next we will use a for loop.
to know how a for loop in python works refer to https://www.w3schools.com/python/python_for_loops.asp
after starting the loop we will use the append feature of lists that attaches new elements to end of a list.

for example if the name of our movie is stored in the variable 'chosen'
we loop over individual alphabets of the movie and use an if-else statement to check if it is a vowel or not.

a small example of how you can achieve this is:
for x in chosen:
  if x=='type condition for vowel here':
    toshow.append(x)
  else:
    toshow.append('_')
 when finally the loop is done we will have something like this '_a___/_o__e_' stored in our list. 
 
 pro tip: use use print() funtion to see what different elements look like.

at the end of week 1 I wil post the code to task 1.
