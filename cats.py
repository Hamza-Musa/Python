print('How many cats do you have')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    if int(numCats)<=-1:
        print('You cant have minus cats, stupid.')


  
    else:
        print('That is not that many cats.')
except ValueError:
        print('You did not enter a number.')
        


