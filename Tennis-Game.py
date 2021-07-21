import random
from time import sleep
SLEEP_TIME=0.5
SETS=3

players=[['Novak Djokovic','22/05/1987',30,510],
      ['Rafael Nadal','03/06/1986',17,480],
      ['Roger Federer','08/08/1981',27,490],
      ['Dominic Thiem','03/09/1996',14,300],
      ['Kei Nishikori','29/12/1989',23,500],
      ['Alexander Zverev','20/04/1997',18,320],
      ['Stefanos Tsitsipas','12/08/1998',17,450],
      ['Daniil Medvedev','11/02/1996',16,340],
      ['Karen Khachanov','21/05/1996',14,380],
      ['Fabio Fognini','24/05/1987',27,350],  ]
def doMatch(n,n1):
      print('<Match',players[n][0],'-',players[n1][0]+'>')     
      set1=0
      set2=0
      set_count=1
      game_count=1
      while set1<2 and set2<2:                                 
            game_p1=0
            game_p2=0
            print('<set',str(set_count)+'>')
            while game_p1<6 and game_p2<6:
                  p1=0
                  p2=0
                  print('game {0:2d}'.format(game_count),end=': ')
                  while p1<55 and p2<55:
                        print('{0:02d}-{1:02d}'.format(p1,p2),end=',')
                        num=randrange(0,1000)
                        if num%2==0:
                              if p1<30:
                                    p1+=15
                              elif p1==30:
                                    p1+=10
                              else:
                                    p1+=20
                                    game_p1+=1
                                    game_count+=1
                                
                        else:
                               if p2<30:
                                     p2+=15
                               elif p2==30:
                                     p2+=10
                               else:
                                     p2+=20
                                     game_p2+=1
                                     game_count+=1
                             
                  print('game Winner',end=':')
                  if p1 == 60:
                        print(players[n][0],end=',')
                        print('{0:d}:{1:d}'.format(game_p1,game_p2))
                  if p2 ==60:
                        print(players[n1][0],end=',')
                        print('{0:d}:{1:d}'.format(game_p1,game_p2))           
                  if game_p1 ==6:
                        set1+=1
                        set_count+=1
                  if game_p2 ==6 :
                        set2+=1
                        set_count+=1
            #print("the set 1:",set1)
            print("Set winner is :",end=',')
            if game_p1 == 6:
                  print(players[n][0],end=',')
                  print('{0:d}:{1:d}'.format(set1,set2))
            if game_p2 ==6:
                  print(players[n1][0],end=',')
                  print('{0:d}:{1:d}'.format(set1,set2))

            
    
   
from random import randrange  
def doTournament():
   for i in range(len(players)):
        i+=1
   print("the counter of the players are:",i)
   rlist=[]
   tlist=[]
   for _ in range(len(players[0])):
       rlist.append(players.pop(randrange(0,len(players))))
   for _ in rlist:
       tlist.append(rlist.pop(randrange(0,len(rlist))))
   
   print("the first couple players are:",rlist[0][0],',',rlist[1][0])    
   print("the second couple are:",tlist[0][0],',',tlist[1][0])


def PrintPlayers(num):
      if num >=0:
            print("from the first to the last players: ")
            for i in range(len(players)):
                  print(players[i]) 
      if num<0:
         new_order=[]
         count=len(players)-1
         while count >=0:
            new_order.append(players[count])
            count-=1
         print("from last to the first players: ")  
         for i in range(len(players)):
               print(new_order[i])

    
def removePlayer(players):
      temp=players[0][3]
      for i in range(len(players[3])):
            if players[i][3]<temp:
                  players.remove
      print("the player to remove is:",players[i])
      players.remove(players[i])
      for i in range(len(players)):
            print (players[i])
      #print(players)
   


def addPlayer(players):
    print("please enter your personal data to enter in the play")
    rlist=[]
    rlist.append(input("enter name: "))
    rlist.append(input("enter date of birth[day/month/year]: "))
    rlist.append(int(input("enter numbers of the wins: ")))
    rlist.append(int(input("enter number of the points: ")))
    players.append(rlist)
    print(players)
    print("congratulation!!!you are now  part of the tennis game")

def sortPlayers(players):
      temp=[0,0,0,0]
      for i in range(len(players)):
            for j in range(len(players)):
                  if(players[i][3]>players[j][3]):
                        temp=players[i]
                        players[i]=players[j]
                        players[j]=temp
      print("the order from the hight to less points is: ")
      for i in range(len(players)):
            print (players[i])
 
def menu():
    print("WELCOME TO THE MENU\n 1.PRINT THE LIST OF THE PLAYERS \n 2.REMOVE THE PLAYER WITH THE LESS POINTS \n 3.ADD PLAYER AT LIST OF THE PLAYERS \n 4.SORT LIST OF THE PLAYERS FROM HIGHEST TO LOWEST(POINTS)  \n 5.TOURNAMENT PLAYERS\n 6.LET S START THE GAME!(domatch) ")
    choise = 10
    while  choise!=0:
        if choise == 1:
            num=int(input("enter your positive number: "))
            PrintPlayers(num)
            print("---------------------------------------------------------")
        elif choise == 2:
            removePlayer(players)
            print("-----------------------------------------------------------")
        elif choise == 3:
            addPlayer(players)
            print("-----------------------------------------------------------")
        elif choise == 4:
            sortPlayers(players)
            print("-----------------------------------------------------------")
        elif choise == 5:
            doTournament()
            print("----------------------------------------------------------")
            print("tournament choiser players")
        elif choise == 6:
            n=int(input("enter player number: "))
            n1=int(input("enter second player number: "))
            doMatch(n,n1)
        elif choise ==0:
            print("exit")
        choise=int(input("chose from the menu number: "))
