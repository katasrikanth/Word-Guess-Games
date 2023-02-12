print("------Game(2)-------")
print("------word Guess-----")
print("Information:")
print("Firstly You have to choose a word of any number of letter this code will guess your word by following the Execuition Flow:")
print("")
d={1:list("A E I M Q U Y".split()),2:list("B F J N R V Z".split()),3:list("C G K O S W @".split()),4:list("D H L P T X @".split())}
for i,j in d.items():
    print(i,"=",j)
l=int(input("enter length of string:"))
s=[]
for i in range(l):
    s.append(d[int(input(f"enter row number of your {i+1} letter of your word from above given table"))])
h=list(zip(*s)) 
rd={}
k=1
for i in h:
    print(k,"=",list(i))
    rd[k]=list(i)
    k+=1
ans=[]
c=0
for i in range(l):
    ans.append(rd[int(input(f"enter row number of your {c+1} letter of Your word from given above table:"))][c])
    c+=1
print("Your word is:","".join(ans))  
