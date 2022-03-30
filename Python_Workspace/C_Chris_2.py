
#Chris wang
#31/10/2021
#The program must collect input from the user, asking them to input a temperature.  The program will then output one of the following statements:
#•	If the temperature is below zero, it will output “Below Freezing”
#•	If the temperature is above zero, it will output “Above Freezing”
#•	If the temperature is zero, it will output “Freezing

def temp():
    temp=input("Enter the temp:")
    temp=int(temp)
    if(temp>0):#If the temperature is above zero, it will output “Above Freezing”
        print(str(temp)+": Above Freaze")
    elif(temp<0):#If the temperature is below zero, it will output “Below Freezing”
        print(str(temp)+": Below  Freaze")
    else:#If the temperature is zero, it will output “Freezing
        print(str(temp)+": Below Freaze")


temp()
temp()
temp()