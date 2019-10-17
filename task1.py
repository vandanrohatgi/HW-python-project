import random

#create a list of all movies for the game
listofmovies=['avengers endgame','star wars the force awakens','avengers infinity war','jurassic world','the lion king','furious seven','black panther','harry potter',
'frozen','beauty and the beast','incredibles two','iron man three','minions','aquaman','aladdin','finding dory','zootopia','spectre','spider man homecoming','batman v superman','hunger games'
]
#list of all vowels to remove everything except them from the name of the movie 
vowels=['a','e','i','o','u']
#list of alphabets of 'hollywood' to cut them one by one everytime the user makes a wrong guess
string=['h','o','l','l','y','w','o','o','d']

#choosing random movie from list of movies
choosen=random.choice(listofmovies)
'''okay so quite a bit to explain here...
first we remove the spaces from the name of movie using the split function which splits the string from there is a space
'''
remove_spaces=choosen.split(' ')

'''secondly we take the previous variable and put a '/' where there was a space in the name using the join function
if you feel it is too many functions, don't fret just head over to python docs to read about every function that I have used here'''

choosen='/'.join(remove_spaces)

#create empty list to get the final string that is formatted to our desire
toshow=[]

tempstring=string
for x in choosen:
    if x in vowels:
        toshow.append(x)
    elif x=='/': 
        toshow.append('/')
    else:
        toshow.append('_')
