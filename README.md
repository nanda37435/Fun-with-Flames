# Fun-with-Flames

sai="Y"
while(sai=="y" or sai=="Y"):
    a=input('Enter name of first person : ').strip()
    b=input("Enter name of second person: ").strip()
    a=[i.lower() for i in a if i!=" "]
    b=[j.lower() for j in b if j!=" "]
    x=a[:]
    y=b[:]
    for i in x:
        for j in y:
            if i==j and i in a and j in b:
                a.remove(i)
                b.remove(j)
                break
    #print(a,b)
    count=len(a)+len(b)
    flames=["Friendship","Love","Affection","Marriage","Enemies","Siblings"]
    while(len(flames)!=1):
        i=count%len(flames)
        if i==0:
            i=len(flames)
        flames=flames[i:]+flames[:(i-1)]    
    
    #print(flames)
    print("Relation is:",str(flames[0]))
    print(end='\n')
    print("Press 'Y' and hit enter to play again else just hit enter")
    sai=input().strip()
    
