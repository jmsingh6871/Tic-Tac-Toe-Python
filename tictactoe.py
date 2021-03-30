import os
###flags
p=1
win=1
draw=-1
run=0
game=run
b= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def playboard():    
    print(" %c | %c | %c " % (b[1],b[2],b[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (b[4],b[5],b[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (b[7],b[8],b[9]))    
    print("   |   |   ")    

#for postion is empty  or not
def checkpos(x):
    if(b[x]==' '):
        return True
    else:
        return False
#functiokn check wheather won or loose
def checkwin():
    global game
#########horizontal winning
    if(b[1]==b[2] and b[2]==b[3] and b[3]!=' '):
        game=win
    elif(b[4]==b[5] and b[5]==b[6] and b[4]!=' '):
        game =win
    elif(b[7]==b[8] and b[8]==b[9] and b[7]!=' '):
        game = win
#########vaertical winning
    elif(b[1]==b[4] and b[4]==b[7] and b[1]!=' '):
         game = win
    elif(b[2]==b[5] and b[5]==b[8] and b[2]!=' '):
        game = win
    elif(b[3]==b[6] and b[6]==b[9] and b[3]!=' '):
        game = win
#########diagonal winning
    elif(b[1]==b[5] and b[5]==b[9] and b[1]!=' '):
        game = win
    elif(b[3]==b[5] and b[5]==b[7] and b[3]!=' '):
        game = win
#########draw game
    elif(b[1]!=' ' and  b[2]!=' ' and  b[3]!=' 'and  b[4]!=' 'and b[5]!=' ' and  b[6]!=' ' and  b[7]!=' ' and  b[8]!=' ' and  b[9]!=' '):
        game = draw
    else:
        game=run
print('\t\t\twelcome to the tic tac toe ')
print('only player 1 can choose the design')
print('1. O\n2. X')
p1=input('enter your choice')
if(p1=='O'):
    p2='X'
elif(p1=='X'):
    p2='O'

while game==run:
    os.system('cls')
    playboard()
    if(p%2!=0):
        print('player 1 chance')
        mark=p1
    else:
        print('palyer 2 chance')
        mark=p2
    ch=int(input('enter the position from(1-9),where you want to place your mark'))
    if(checkpos(ch)==True):
        b[ch]=mark
        p+=1
        checkwin()
os.system('cls')
playboard()
if (game==draw):
    print('game draw')
elif (game==win):
    p-=1
    if(p%2!=0):
        print('player 1 won')
    else:
        print('player 2 won')
        
