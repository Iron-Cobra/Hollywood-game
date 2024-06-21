import csv
import random
#Adds the movies in the csv file to a list
def importmovies():
    with open("movies.csv","r") as movcsv:
        movies=csv.reader(movcsv)
        movielist=[]
        for i in movies:
            if i !=[]:
                movielist.append(i)
        return movielist    
print(r'  _    _  ____  _      _  __     ____          ______   ____  _____  ')
print(r' | |  | |/ __ \| |    | | \ \   / /\ \        / / __ \ / __ \|  __ \ ')
print(r' | |__| | |  | | |    | |  \ \_/ /  \ \  /\  / / |  | | |  | | |  | |')
print(r' |  __  | |  | | |    | |   \   /    \ \/  \/ /| |  | | |  | | |  | |')
print(r' | |  | | |__| | |____| |____| |      \  /\  / | |__| | |__| | |__| |')
print(r' |_|  |_|\____/|______|______|_|       \/  \/   \____/ \____/|_____/ ')
print(r'                                                                     ')
    
while True:
    print(r'                                                                     ')
    print(r'[1] Play Game')
    print(r'[2] Add Movie')
    print(r'[3] Display Movies')
    print(r'[4] Clear Movies')
    print(r'[5] Exit')
    choice=input("Enter your choice:")
    if choice=="1":
        movielist=importmovies()
        if movielist!=[]:
            movie=(random.choice(movielist))
            holly="HOLLYWOOD"
            movie=movie[0]
            guslist=[]
            print(len(movie)*" _")
            while holly !="":
                movieout=""
                gusall=""
                print(holly)
                gus=input("Enter Your Guess:")
                gus=gus.lower()
                for i in gus:
                    if i not in gusall:
                        gusall+=i
                gus=gusall
                if gus not in movie:
                    holly=holly[len(gus):]
                guslist+=gus
                for i in movie:
                    if i in guslist:
                        movieout+=i
                    else:
                        movieout+=" _"
                print(movieout)
                if "_" not in movieout:
                    print(r"_____________________________________")
                    print(r"                            _       ")
                    print(r"                           (_)      ")
                    print(r" _   _  ___  _   _    _ _ _ _ ____  ")
                    print(r"| | | |/ _ \| | | |  | | | | |  _ \ ")
                    print(r"| |_| | |_| | |_| |  | | | | | | | |")
                    print(r" \__  |\___/|____/    \___/|_|_| |_|")
                    print(r"(____/                              ")
                    print(r"_____________________________________")
                    break
                    
            if "_" in movieout:
                print(r"__________________________________________")
                print(r"                      _                  ")
                print(r"                     | |                 ")
                print(r" _   _  ___  _   _   | | ___   ___ _____ ")
                print(r"| | | |/ _ \| | | |  | |/ _ \ /___) ___ |")
                print(r"| |_| | |_| | |_| |  | | |_| |___ | ____|")
                print(r" \__  |\___/|____/    \_)___/(___/|_____)")
                print(r"(____/                                   ")
                print(r"__________________________________________")
                print("The Movie Was",movie)
        else:
            print("There Are No Movies In The List Add Movies To Play The Game")
    elif choice=="2":
        while True:
            movielist=importmovies()
            newmovie=input("Enter New Movie To Be Added:")
            if [newmovie] in movielist:
                print("The Movie Is Aready In The List")
            else:
                with open("movies.csv","a") as addmovie:
                    newadd=csv.writer(addmovie)
                    newadd.writerow([newmovie.lower()])
                print(newmovie,'Was Added To The List')
            yorn=input("Do You Want To Keep Adding Movies?(Y/N)")
            if yorn.lower()=='y':
                continue
            else:
                break
    elif choice=="3":
        movielist=importmovies()
        x=0
        #x is the maximum number of carachters in a movie
        for i in movielist:
            if len(i[0])>x:
                x=len(i[0])
        #making x even
        if x%2==0:
            x+=2
        else:
            x+=3
        numbercount=1
        #space between "MOVIES" and border
        trailspacecount=((x-6)//2)
        if movielist!=[]:
            print("+---",end='')
            print('+'+'-'*x+'+')
            print("| "+"N ",end='')
            print('|'+' '*trailspacecount+"MOVIES"+" "*trailspacecount+'|')
            print("+---",end='')
            print('+'+'-'*x+'+')
            for i in movielist:
                print("| "+str(numbercount)+" ",end='')
                moviespacecount=x-len(i[0])
                print("|"+i[0]+" "*moviespacecount+"|")
                print("+---",end='')
                print('+'+'-'*x+'+')
                numbercount+=1
        
        else:
            print("There Are No Movies In The List")
    elif choice=="4":
        movielist=importmovies()
        if movielist==[]:
            print("The List Is Already Empty")
        else:
            yorn=input("Are You Sure?(y/n):")
            if yorn.lower()=="y":
                with open("movies.csv","w") as movcsv:
                        continue
    elif choice=="5":
        print("Thanks For Playing...")
        break
    else:
        print("Choose a valid input")
