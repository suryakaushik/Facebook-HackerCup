"""
You just landed yourself a gig as a delivery driver for a nationwide supply chain. You've been assigned a series of long-haul jobs, so it's time to get to work.
For each job, you will be provided with a map of the relevant region, which includes N cities (numbered from 1 to N) and N-1 two-way roads running amongst them. The cities are connected by roads in a single line, such that there's a road between each pair of consecutive cities. In other words, cities i and j are directly connected by a road if and only if |i - j| = 1
You will begin in city 1 with a shipment of supplies to be delivered to city N, and with a full gas tank having a capacity of M gallons. You will then have two options at each point in time:
1.  Drive along a road from your current city to an adjacent one, using up 1 gallon of gas. You may not do this if your tank is empty, but it's fine if your tank becomes empty as a result.
2.  Fill your tank all the way back up to M gallons of gas at a cost of Ci dollars, where i is your current city. Note that the cost is independent of how much gas your tank had before refueling. You may not do this if city i has no gas station (indicated with Ci= 0 )

Determine the minimum cost required to arrive at city NN, if it's possible at all.

Input
Input begins with an integer T, the number of long-haul jobs you've been assigned. For each job there is first a line containing the space-separated integers N and M. Then, N lines follow, the ith of which contains the single integer Ci

Output
For the ith job, output a line containing "Case #i: " followed by a single integer, the minimum cost in dollars to get from city 1 to city N, or -1 if it's impossible.

Sample Input:
7
5 3
0
20
30
0
10
5 2
0
20
30
0
10
5 1
0
20
30
0
10
4 1
99
88
77
66
4 4
99
88
77
66
6 2
0
0
20
30
0
10
12 3
0
1
4
7
0
5
9
8
0
3
0
6


Sample Output:
Case #1: 20
Case #2: 30
Case #3: -1
Case #4: 165
Case #5: 0
Case #6: 50
Case #7: 19


Sample Explanation
In the first job, you will begin in city 1 with 3 gallons of gas. You cannot drive all the way to your destination (city 5) without refueling along the way, as that would require a total of 4 gallons of gas. The cheapest option is to drive to city 2, top up your tank for a cost of $20, and then drive through cities 3 and 4 before reaching city 5 with no more gas to spare.
In the second job, your gas tank only has a capacity of 2 gallons. In this case, the cheapest strategy involves depleting all of your gas to drive to city 3, refueling there for $30, and then depleting all of your gas to reach city 5.
In the third job, your gas tank only has a capacity of 1 gallon. No matter what you do, you will deplete all of your gas in the drive from city 3 to city 4, where there will be no way to refuel to reach city 5.

"""

def fun(n,m,l,cost,fuelleft,i):
    if(i==n-1):
        return(cost)
    if(fuelleft==0):
        if(l[i]==0):
            return(-1)
        else:
            t=fun(n,m,l,cost+l[i],m-1,i+1)
    else:
        if(l[i]==0):
            t=fun(n,m,l,cost,fuelleft-1,i+1)
        else:
            t1=fun(n,m,l,cost,fuelleft-1,i+1)
            t2=fun(n,m,l,cost+l[i],m-1,i+1)
            if(t1==-1 and t2==-1):
                t=-1
            if(t1==-1):
                t=t2
            elif(t2==-1):
                t=t1
            else:
                t=min(t1,t2)
            return(t)
    return(t)
    
    
for i in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for j in range(n):
        l.append(int(input()))
    a=fun(n,m,l,0,m,0)
    print("Case #"+str(i+1)+":",a)
