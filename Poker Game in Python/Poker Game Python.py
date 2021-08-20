import random
import time

suits=["H","C","D","S"]
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

#Dimiourgoume tin trapoula 
deck=[]

for s in suits:
    for v in values:
        card=v+s
        deck.append(card)
        
random.shuffle(deck) 
print("The full deck is:\n\n{}".format(deck))


#dimiourgoume ta duo xeria pou tha exoun oi paixtes
hand1=[]
hand2=[]
for num in range(5):
    c1=random.choice(deck)
    hand1.append(c1)
    deck.remove(c1)
    c2=random.choice(deck)
    hand2.append(c2)
    deck.remove(c2)
    
print("\nPlayer 1 got {}".format(hand1))
print("\nPlayer 2 got {}".format(hand2))
    

#Elegxos gia ena zebgari difilias
def pair(hand):
    values1=[]
    for i in hand:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    value_counts={}
    for c in values1:
        if c not in value_counts:
            value_counts[c]=1
        else:
            value_counts[c]=value_counts[c]+1      
    if 2 in value_counts.values():
        return True
    else:
        return False
    
#Elegxos gia duo zebgaria diflias
def two_pair(hand):
    values1=[]
    for i in hand:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    value_counts={}
    for c in values1:
        if c not in value_counts:
            value_counts[c]=1
        else:
            value_counts[c]=value_counts[c]+1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

#Elegxos gia trifilia
def three_of_a_kind(hand):
    values1=[]
    for i in hand:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    value_counts={}
    for c in values1:
        if c not in value_counts:
            value_counts[c]=1
        else:
            value_counts[c]=value_counts[c]+1
            
    if sorted(value_counts.values())==[1,1,3]:
        return True
    else:
        return False
    

#Elegxos gia straight
def straight(hand):
    values1=[]
    for i in hand:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    value_counts={}
    for c in values1:
        if c not in value_counts:
            value_counts[c]=1
        else:
            value_counts[c]=value_counts[c]+1           
    v = [values[i] for i in values1]
    v_range = max(v) - min(v)
    if len(set(value_counts.values())) == 1 and (v_range==4):
        return True
    else: 
        #Elegxos gia straight me xamilo A
        if set(values1) == set(["A", "2", "3", "4", "5"]):
            return True
        return False
    
#Elegxos gia Flush
def flush(hand):
    suits1=[]
    for i in hand:
        if len(i)==3:
            suits1.append(i[2])
        else:
            suits1.append(i[1])
    if len(set(suits1))==1:
        return True
    else:
        return False
    
    
#Elegxos gia Full House
def full_house(hand):
    values1=[]
    for i in hand:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    value_counts={}
    for c in values1:
        if c not in value_counts:
            value_counts[c]=1
        else:
            value_counts[c]=value_counts[c]+1
            
    if sorted(value_counts.values())==[2,3]:
        return True
    else:
        return False
    
    
#Elegxos gia 4 fila idias aksias
def four_of_a_kind(hand):
    values1=[]
    for i in hand:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    value_counts={}
    for c in values1:
        if c not in value_counts:
            value_counts[c]=1
        else:
            value_counts[c]=value_counts[c]+1
            
    if sorted(value_counts.values())==[1,4]:
        return True
    else:
        return False
    
#Elegxos gia straight flush
def straight_flush(hand):
    if straight(hand) and flush(hand):
        return True
    else:
        return False
    
#Elegxos gia monofilia
def high_card(hand):
    if not pair(hand) and not two_pair(hand) and not three_of_a_kind(hand) and not straight(hand) and not flush(hand) and not full_house(hand) and not four_of_a_kind(hand) and not straight_flush(hand):
        return True
    else:
        return False

def check_compination(hand):
    if straight_flush(hand):
        return 9
    elif four_of_a_kind(hand):
        return 8
    elif full_house(hand):
        return 7
    elif flush(hand):
        return 6
    elif straight(hand):
        return 5
    elif three_of_a_kind(hand):
        return 4
    elif two_pair(hand):
        return 3
    elif pair(hand):
        return 2
    else:
        return 1
    
res1=check_compination(hand1)
print(res1)
res2=check_compination(hand2)
print(res2)

if res1>res2:
    print("Player 1 WINS!!")
elif res1<res2:
    print("Player 2 WINS!!")
#Se periptwsh pou exoume thn idia aksia sundiasmwn elegxoume poios exei kalutero xeri
elif ((res1==1) and (res2==1)) or ((res1==5) and (res2==5)) or ((res1==6) and (res2==6)) or ((res1==9) and (res2==9)) :
    values1=[]
    for i in hand1:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    v1 = [values[i] for i in values1]
    values2=[]
    for i in hand2:
        if len(i)==3:
            values2.append(i[0]+i[1])
        else:
            values2.append(i[0])
    v2 = [values[i] for i in values2]
    if max(v1)>max(v2):
        print("Player 1 WINS!!")
    elif max(v2)>max(v1):
        print("Player 2 WINS!!")
    else:
        print("Really Unlucky ... Try again")
elif (res1==2) and (res2==2):
    from itertools import combinations
    values1=[]
    for i in hand1:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    v1 = [values[i] for i in values1]
    values2=[]
    for i in hand2:
        if len(i)==3:
            values2.append(i[0]+i[1])
        else:
            values2.append(i[0])
    v2 = [values[i] for i in values2]
    for (a,b) in list(combinations(v1,2)):
        if a==b:
            x=a
    for (c,d) in list(combinations(v2,2)):
        if c==d:
            y=c
    if x>y:
        print("Player 1 WINS!!")
    elif x<y:
        print("Player 2 WINS!!")
    else:
        print("Really Unlucky ... Try again")
elif(res1==3) and (res2==3):
    from itertools import combinations
    values1=[]
    for i in hand1:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    v1 = [values[i] for i in values1]
    values2=[]
    for i in hand2:
        if len(i)==3:
            values2.append(i[0]+i[1])
        else:
            values2.append(i[0])
    v2 = [values[i] for i in values2]
    for (a,b) in list(combinations(v1,2)):
        if a==b:
             for (c,d) in list(combinations(v1,2)):
                    if c==d:
                        x=a
                        y=c
    for (e,f) in list(combinations(v2,2)):
        if e==f:
            for (g,h) in list(combinations(v2,2)):
                if g==h:
                    x2=e
                    y2=g
            
    if max(x,y)>max(x2,y2):
        print("Player 1 WINS!!")
    elif max(x,y)<max(x2,y2):
        print("Player 2 WINS!!")
    else:
        print("Really Unlucky ... Try again")
elif((res1==4) and (res2==4)) or ((res1==7) and (res2==7)):
    from itertools import combinations
    values1=[]
    for i in hand1:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    v1 = [values[i] for i in values1]
    values2=[]
    for i in hand2:
        if len(i)==3:
            values2.append(i[0]+i[1])
        else:
            values2.append(i[0])
    v2 = [values[i] for i in values2]
    for (a,b,c) in list(combinations(v1,3)):
        if a==b==c:
            x=a
    for (d,e,f) in list(combinations(v2,3)):
        if d==e==f:
            y=d
    if x>y:
        print("Player 1 WINS!!")
    elif x<y:
        print("Player 2 WINS!!")
    else:
        print("Really Unlucky ... Try again")
elif (res1==8) and (res2==8):
    from itertools import combinations
    values1=[]
    for i in hand1:
        if len(i)==3:
            values1.append(i[0]+i[1])
        else:
            values1.append(i[0])
    v1 = [values[i] for i in values1]
    values2=[]
    for i in hand2:
        if len(i)==3:
            values2.append(i[0]+i[1])
        else:
            values2.append(i[0])
    v2 = [values[i] for i in values2]
    for (a,b,c,d) in list(combinations(v1,4)):
        if a==b==c==d:
            x=a
    for (e,f,g,h) in list(combinations(v2,4)):
        if e==f==g==h:
            y=e
    if x>y:
        print("Player 1 WINS!!")
    elif x<y:
        print("Player 2 WINS!!")
    else:
        print("Really Unlucky ... Try again")