import random

da=0
net=0

def diablo_sum():
    global da, net
    a=random.randint (13,13)
    b=random.randint (-13,13)
    suma=a*b
    print(f"{a}*{b}=", end="")
    c=input()
    c=int(c)
    if suma==c:
        print ("Правильно")
        da=da+1
    else:
        print (f"Неправильно. Будет {suma}")
        net=net+1
		
for d in range (1,16):
	diablo_sum()
print (f"Правильных {da} Неправильных {net}")
