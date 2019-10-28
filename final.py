import random

listofmovies=['avengers endgame','star wars the force awakens','avengers infinity war','jurassic world','the lion king','furious seven','black panther','harry potter',
'frozen','beauty and the beast','incredibles two','iron man three','minions','aquaman','aladdin','finding dory','zootopia','spectre','spider man homecoming','batman v superman','hunger games'
]
vowels=['a','e','i','o','u']
string=['h','o','l','l','y','w','o','o','d']


while True:
    choosen=random.choice(listofmovies)

    choosen='/'.join(choosen.split(' '))
    toshow=[]
    tempstring=string

    for x in choosen:
        if x in vowels:
            toshow.append(x)
        elif x=='/': 
            toshow.append('/')
        else:
            toshow.append('_')
    print('press any key to start playing!')
    _=input()
    while len(string)!=0:
        print(''.join(toshow))
        print('you have left:'+str(len(tempstring))+' tries')
        print('guess an alphabet of the movie!')

        guess=input()
        if guess in choosen:
            indexes=[i for i in range(len(choosen)) if choosen[i]==guess]
            for index in indexes:
                toshow[index]=guess
        else:
            tempstring.pop()

        if len(tempstring)==0:
            print('game over!')
        elif ''.join(toshow)==choosen:
            print('you won!!!')
            break
    print('press y if you want to play again')
    if input()=='y':
        pass
    else:
        break
    
    