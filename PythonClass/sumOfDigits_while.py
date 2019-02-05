def sumOfdigits():
    num=input("Enter the number: ")
    str_num=str(num)
    i=len(str_num)
    sum=0
    while(i>0):
        i-=1
        sum+=int(str_num[i])
    print "Sum is:",sum

def another_version():
    num=input("Enter the number:")
    sum=0
    while (num>0):
        sum+=num%10
        num=num//10
    print "Sum is:",sum
if(__name__=="__main__"):
    #sumOfdigits()
    another_version()
