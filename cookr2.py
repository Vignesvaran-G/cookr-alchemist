a=int(input('enter the first person distance:'))
b=1
y=int(input('enter the first shop distance:'))
z=1
time=2 #min
def rule1(a,b,y,z):
    c=a+y
    print('distance travelled:',c)
    print('time taken:',c*time+10)

def rule2(a,b,y,z):
    c=a+b+y+z
    print('distance travelled:', c)
    print('time taken:', c * time+10)

def rule3(a,b,y,z):
    c=a+b+y
    print('distance travelled:', c)
    print('time taken:', c * time+10)

def rule4(a,b,y,z):
    c = a + b + y
    print('distance travelled:', c)
    print('time taken:', c * time+10)

def rule5(a,b,y,z):
    c=a+y+z
    print('distance travelled:', c)
    print('time taken:',c*time+10)

def rule6(a,b,y,z):
    c=a+y
    print('distance travelled:', c)
    print('time taken:', c * time+10)

def rule7(a,b,y,z):
    c=a+y
    print('distance travelled:', c)
    print('time taken:', c * time+10)

def rule8(a,b,y,z):
    c=a+y
    print('distance travelled:', c)
    print('time taken:',c*time+10)

k=int(input('enter the rule:'))
if k==1:
    rule1(a,b,y,z)
elif k==2:
    rule2(a,b,y,z)
elif k==3:
    rule3(a,b,y,z)
elif k==4:
    rule4(a,b,y,z)
elif k==5:
    rule5(a,b,y,z)
elif k==6:
    rule6(a,b,y,z)
elif k==7:
    rule7(a,b,y,z)
else:
    rule8(a,b,y,z)
