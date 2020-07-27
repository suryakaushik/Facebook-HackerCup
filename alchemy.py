l1=['AAB','ABA','BAA']
l2=['BBA','BAB','ABB']
def fun(n,s):
    f=-1
    for i in range(0,n):
        t=s[i:i+3]
        if(t in l1):
            s=s[:i]+"A"+s[i+3:]
            f=1
        if(t in l2):
            s=s[:i]+"B"+s[i+3:]
            f=2
    if(len(s)==1):
        return("Y")
    if(f==-1):
        return("N")
    return(fun(len(s),s))



for i in range(int(input())):
    n=int(input())
    c=input()
    a=fun(n,c)
    print("Case #"+str(i+1)+":",a)
