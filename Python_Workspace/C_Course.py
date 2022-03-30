def asseccScore(scorceList):
    for i in range(0,len(scorceList)):
        if(scorceList[i]>=100):
            print("computer",i+1,"has no known security issues.")
        elif(scorceList[i]>=80):
            print("coomputer",i+1,"has minor security issue.")
        elif(scorceList[i]<60):
            print("computer",1+i,"has ***severe*** security issues")
    print("Process complete:",len(scorceList),"computer scanned.")
    return

scores=[1,50,60,70,80,90]
asseccScore(scores)