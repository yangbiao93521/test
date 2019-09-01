# a=1
# b=0
# c=0
# while   a<6:
#     d=a*1
#     b+=d
#     c+=b
#     a+=1
# print(c)

a=0
for   i  in range(1,101):
    for   j  in   range(2,101):
        if    i%j==0:
            break
    if  i==j:
        a+=i
print(a)

# for   i   in range(1,1001):
#     a=0
#     for  j   in  range(1,i):
#         if   i%j==0:
#             a+=j
#     if   i==a:
#             print(a)