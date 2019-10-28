'''print() function for printing stuff on screen'''
print('press any key to start playing!')

'''input() function to get user input()'''
_=input()


string='hollywood'
tempstring=list(string)
choosen='hunger/games'
toshow=['_', 'u', '_', '_', 'e', '_', '/', '_', 'a', '_', 'e', '_']#hunger games

'''while loop with condtion to loop till there are alphabets left in string "hoolywood". '''

while len(string)!=0:
    print(''.join(toshow))
    print('you have left:'+str(len(tempstring))+' tries')#string concatination used 
    print('guess an alphabet of the movie!')
    guess=input()
    if guess in choosen:
        '''the below used technique used is known as a list comprehansion which is used to generate lists according to our needs'''
        indexes=[i'''output''' for i in range(len(choosen))'''loop''' if choosen[i]==guess'''condition''']
        '''now the list indexes contains all the places where the input of user can be filled'''
        '''next we fill the user input at the places where its applicable. for example if the user input is h so we fill the 'h' at the 
        first position of the movie i.e hunger/games'''
        for index in indexes:
            toshow[index]=guess
    else:
        #if the user input is not there in the name of the movie we just remove an alphabet from string 'hollywood'
        tempstring.pop()
    '''finally we check if the user has run out of chances or not. if length of the string is 0 we display game over'''
    if len(tempstring)==0:
        print('game over!')
    '''else if the user has filled all the blancks of the movie correctly we display you won'''
    elif ''.join(toshow)==choosen:
        print('you won!!!')
        break
