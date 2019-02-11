
#To reverse the number:
def reverse(num):
    l=len(str(num))
    new=''
    for each in range(0,l):
        new=new+str(num%10)
        num=num//10
    return int(new)