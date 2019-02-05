def reverseNumber():
    num=int(raw_input("Enter the number:"))
    rev=0
    while(num>0):
        reminder=num%10
        rev=(rev*10) + reminder
        num=num//10
    
    print "Reversed Number: ",rev
    
if(__name__=="__main__"):
    reverseNumber()
    
    
