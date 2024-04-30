# def printNum(n):
#     if(n<0):
#         return
#     print(n,end=" ")
#     printNum(n-3)
# num=9
# printNum(num)

 

def fun(n):
    if(n == 4):
        return n
    else:
        return 2*fun(n+1)
print(fun(2))


 