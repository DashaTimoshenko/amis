def sum_(ilist):
    if len(ilist)==0:
        return 0
    else:
        return (ilist[0]) + (sum_(ilist[1:]))
n=input() 
slist=n.split(" ")
k=list(map(int,slist))
print(sum_(k))
