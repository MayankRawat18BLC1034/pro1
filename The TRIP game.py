print("Welcome to the game, player!!")
name=input("Enter your name:")
print(" So which game do u want to play?")
q={"A":"a simple one","B":"a really nice one",
    "C":"or are u a lazy ass and wants to quit"
    }
print(q)
answer=input()
print("the game hasn’t started yet so your choice just doesn’t matter, u can’t quit and u will be playing the game of my choice")
print("Well this is my game so listen to my rules CAREFULLY cuz they won’t be displayed again!")
print("1.u are not going to get any extra lives “GAME OVER means GAME OVER”")
print("2.u and only u are responsible for anything that happens to u in the game, creater of the game should not be blamed for any losses!")
print("3. It’s my choice to Over the game when I want no questions what so-ever")
print("                                             !!!!!!The Game Begins!!!!!!")
print("THIS IS A GAME OF PLANNING AND EXECUTING A TRIP WITH YOUR FRIENDS PLAY CAREFULLY AS IF U WANT TO WIN THIS GAME U HAVE TO TAKE EVERY STEP CAREFULLY SO AS THE TRIP GETS COMPLETED WITHOUT GETTING CANCELLED")

print("So here’s the situation u and ur friends are planning to go on a trip to Kashmir. All of u have agreed to the trip except on of ur friend as she fears of terrorism in Kashmir but all of u guys think that’s crap. So what do u guys think of next?")
q1={"A":"leave her alone and go for the trip alone to Kashmir?",
    "B":"plan a trip to some where else",
    "C":"cancel the trip"
    }
print(q1)
c1=input()
if c1=='A':
    print(q1["A"])
    print("u are willing to leave one of ur friend behind, that not a good thing to do when u tell this idea about ur other friends they just knocked u down and hence")
    print("!!!!GAME OVER!!!!")
    exit()
elif c1=='B':
    print(q1["B"])
    print("nice thought of shifting the trip to some other place but where though?")
elif c1=='C':
    print(q1["C"])
    print("well u just cancelled the trip so no point of asking more questions now so")
    print("!!!!GAME OVER!!!!")
    exit()
q2={"A":"Haridwar",
    "B":"New York",
    "C":"Kerela"
    }
print(q2)
c1=input()
if c1=='A':
    print(q2["A"])
    print("all the routes towards Haridwar have been closed by the government because of all the tourist that have went there for the trip have made a traffic congestion and hence u can’t go there so")
    print("!!!!GAME OVER!!!!")
    exit()
elif c1=='B':
    print(q2["B"])
    print("Very nicely u said New York but have u checked ur bank balance?\nU can’t go there so just sit back on ur couch and have a tour of New York on ur TV.\n!!!!GAME OVER!!!!")
    exit()
elif c1=='C':
    print(q2["C"])
    print("Nice choice, ur thought of going to “God‘s own country” is appreciated by everyone and all of u are planning to go there!!! But the question is how?")    
q3={"A":"By Air?",
    "B":"By Road?",
    "C":"Or are u planning to walk down there?"
    }
print(q3)
c1=input()
if c1=='A':
    print(q3["A"])
    print("don’t u remember due to the recent shutdown of the JET AIRWAYS the ticket prices of DELHI to KOCHI have surged by 200 percent so u guys can’t afford them now! So u cant go\n !!!!GAME OVER!!!!")
    exit()
elif c1=='B':
    print(q3["B"])
    print("well u sure have a thing for road trips so does ur friends and they are up for it! Great but there’s a catch none of u have a car so where will u get one from?")
elif c1=='C':
    print(q3["C"])
    print("u are really dumb u just proved that XD\n !!!!GAME OVER!!!!")
    exit()
q4={"A":"Rent one from Zoomcar",
    "B":"Ask your parents to give u their car for a week",
    "C":"Buy one today"
    }
print(q4)
c1=input()
if c1=='A':
    print(q4["A"])
    print(" that just seems the most practical way hence u guys book a car from zoomcar for the next day but while booking you just realised that they are not giving door step delivery of the car to your or any of ur friends home so u just have to take the car from the delivery point but which one will u choose?")
elif c1=='B':
    print(q4["B"])
    print("when u asked ur parents to give them ur car for a week they just kicked u ass and throwed u out of the house plan cancelled hence\n !!!!GAME OVER!!!!")
    exit()
elif c1=='C':
    print(q4["C"])
    print("u are really dumb u just proved that XD\n !!!!GAME OVER!!!!")
    exit()
q5={"A":"Rajouri Garden",
    "B":"Raj Nagar",
    "C":"Gurgaon"
    }
print(q5)
c1=input()
if c1=='A':
    print(q5["A"])
    print("u are an idiot!, Said one of ur friend if a nearby pickup is available why are u going that far after saying that he left and the trip got cancelled hence\n !!!!GAME OVER!!!!")
    exit()
elif c1=='B':
    print(q5["B"])
    print("well that’s what everyone would have picked(the most practical choice) but next day when u guys went to pickup the car u just found out that due to some technical problems at Zoomcar’s HQ the car wasn’t available here then u were left with these options then-")
elif c1=='C':
    print(q5["C"])
    print("u are an idiot!, Said one of ur friend if a nearby pickup is available why are u going that far after saying that he left and the trip got cancelled hence \n!!!!GAME OVER!!!!")
    exit()
q6={"A": "Cancel the trip",
    "B":"The zoomcar executive asked u to get a smaller Santro instead of the car of ur choice and apologised for the mistake",
    "C":"The executive suggested the the car u wanted is available at the pickup point near IGI Airport and I u want that car then u can go their and get the car."
    }
print(q6)
c1=input()
if c1=='A':
    print(q6["A"])
    print("before thinking about buying the car now why don’t u check ur bank balance then u would realise it is not possible and u are left with no car so trip cancelled hence you know\n!!!!GAME OVER!!!!XD XD XD")
    exit()
elif c1=='B':
    print(q6["B"])
    print("ur friends didn’t agreed with your idea to get santro as its too small and they won’t be comfortable hence trip cancelled \n!!!!GAME OVER!!!!")
    exit()
elif c1=='C':
    print(q6["C"])
    print("u went to the IGIA pickup point to get the car with all ur friends and saw the car to took it! Now we can start the trip, said one of ur friend but because of all that drama that happened today all of ur friends are very tired and asked u if they can start the trip after a break what would u say?")
q7={"A":"NO we should leave as early as we can ",
    "B":"Yea we can take a lil’ break"
    }
print(q7)
c1=input()
if c1=='A':
    print(q7["A"])
    print("ur friends got annoyed and left u alone and u had no choice but to cancel the trip hence\n!!!!GAME OVER!!!!")
    exit()
else:
    print(q7["B"])
    print("u start the journey after an hour with all u friends after having some snacks but then u asked ur friends about which way to go as u had no idea about the way to KOCHI and then they were blank as well so what would u do now?")
q8={"A":"use google maps",
    "B":"give up",
    "C":"take the road that u like without even looking for the signs"
    }
print(q8)
c1=input()
if c1=='A':
    print(q8["A"])
    print("u Used google maps to get directions to kochi and started following it and started ur road trip to kochi!\nOn the way when u were passing a jungle in Madhya Pradesh your two of ur cars tyres punctured and u guys stopped as u had only one spare tyre and couldn’t do anything as their were no signal so what would u do now?")
elif c1=='B':
    print(q8["B"])
    print("u gave up \n!!!!GAME OVER!!!!")
    exit()
elif c1=='C':
    print(q8["C"])
    print("u took any road without looking and got lost and ur trip ruined so as ur friendship\n!!!!GAME OVER!!!!")
    exit()
q9={"A": "keep trying to call for some road side assistance", 
    "B": "wait for some to come on the road and ask for some help",
    "C": "start walking in order to get out of the jungle and get help"
    }
print(q9)
c1=input()
if c1=='A':
    print(q9["A"])
    print("u kept trying to call and nothing happened u are stuck here\n!!!!GAME OVER!!!!")
    exit()
elif c1=='B':
    print(q9["B"])
    print("u waited and after some time a bus came and u asked for some help and with the help of the bus u came out of the jungle called the zoomcar helper and got the car fixed and started the journey again!Now even after all the drama that have happened in the past u have managed to reach kochi!! Yayyyy….. Congo.\n*******LEVEL-1 COMPLETED*******")
elif c1=='C':
    print(q9["C"])
    print("u started walking in the jungle and u met a bear who just happened to be very happy to find u and ate u all XD \n!!!!!GAME OVER!!!!")
    exit()
    





