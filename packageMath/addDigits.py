#To add the digits of a number
def addDigits(num):
    num=str(num)
    sum=0
    for each in range(0,len(num)):
        sum=sum+int(num[each])
    return sum