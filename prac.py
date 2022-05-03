#Exception handling(Zero,Name,value)
try:
    x = input("Enter a number : ")
    y = input("Enter a number : ")

    x = int(x)
    y = int(y)

    z = t/y
    print(f"Quoient of {x} and {y} is {z} " )

except ZeroDivisionError:
    print("Zero in denominator invalid")

except ValueError:
    print("Improper argument")

except NameError:
    print("Variable not defined")
else:
    print("No exception")

finally:
    print("Exceptional handling done here")


#File Handling(Sum,Mean,Sqsum)
with open('num.txt','r') as file1:
    numlist = []
    for i in file1:
        numlist.append(int(i))
        sumlist = sum(numlist)
        meanlist = sumlist/len(numlist)
        sumsq = 0
        for item in numlist:
            sumsq+=item**2
        print(sumlist,meanlist,sumsq)
        with open("result.txt","w") as file2:
            file2.write("sum : "+ str(sumlist) + "\n")
            file2.write("mean : "+ str(meanlist) + "\n")
            file2.write("square sum : "+ str(sumsq) + "\n")


# employee 
empid = []
empname = []
basic = []
netsalary = []

with open('emp.txt') as file1:
    for line in file:
        eid,ename,b,=line.split()
        empid.append(eid)
        empname.append(ename)
        basic.append(int(b))
print("Employee Id")
for i in empid:
    print(i)
print("employee Names")
for i in empname:
    print(i)
print("basic salary")
for i in basic:
    print(i)
    da = 0.85*i
    hra = 0.5*i
    ta = 0.12*i
    ns = i+da+hra+ta
    netsalary.append(ns)
    with open("payslip.txt",'w') as file1:
        for i in range(0,len(empid)):
            x = str(empid[i])+ " "+str(netsalary)[i] +"\n"
            file1.write(x)

# file 1 file 2 (read and store)
fact = 1 
with open('file1.txt','r') as file1, open('file2.txt','w') as file2:
    for i in file1:
        fact = fact*int(i)
        file2.write(str(fact)+'\n')

# Regurlar expression (username,mobile,emial)
import re
x = input("Enter username : ")
y = input("Enter mobile number : ")
z = input("Enter email : ")

if re.match(r'^[A-Za-z]\\w{5, 29}$',x):
    print("Valid username")
else:
    print("Invalid username")

if re.match(r"\d{10}$",y):
    print("valid number")
else:
    print("Invalid number")

if re.match(r"[a-z][a-z0-9._]*@[a-z0-9]+[.]",z):
    print("valid number")
else:
    print("invalid number")


# regurlar expression (text_match)
import re 
def text_match(str):
    if re.match(r"a.*b$",str):
        res = f"the string{str} contain the patter"
    else:
        res = f"the string{str}  does not contain the patter"
    return res

str = input("enter the string : ")
x = text_match(str)
print(x)

# Regural expression (address)

import re
str = input("enter the address: ")
str = re.sub(r"[Rr]oad","Rd.",str)
print(str)
str = re.sub(r"[Ss]treet","St.",str)
print(str)
str = re.sub(r"[Dd]istrict","Dst.",str)
print(str)
