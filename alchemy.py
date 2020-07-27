"""
Edgar and his younger brother Alfred are alchemists in search of the legendary Philosopher's Stone. The Philosopher's Stone (also known as the Red Stone, the Fifth Element, and the Elixir of Life in liquid form) is a powerful alchemical substance rumoured to support the transmutation of silver, gold, and even human lives. Edgar is hoping to use the stone to restore his brother's body to its original form following a terrifying human transmutation accident.
It is known that Philosopher's Stones break apart into an odd number of shards when they're used up. After searching far and wide, Edgar has collected NN shards of what he believes to be a previously-used Philosopher's Stone, where NN is an odd integer. He believes that fusing these shards back together will yield a real stone in its entirety.

Leveraging his encyclopedic knowledge of alchemy, Edgar recalls an ancient book with the following ritual for fusing shards:
1.  Arrange the NN shards in a row, numbered from 1 to NN.
2.  Note the colour Ci of each shard i, which is either auburn or black (denoted by the characters "A" and "B" respectively).
3.  Choose a consecutive sequence of three shards, remove them from the row, and fuse them together into one new shard. The three shards must not all be the same colour, or such an intense concentration of similar energies will cause a dangerous rebound explosion. Instead, there must be two differently-coloured shards that will neutralize each other, get converted into energy (via the Law of Equivalent Exchange), and become infused with the third shard. In other words, assuming no explosion, the resulting shard's colour will be equal to the most common colour present amongst the three chosen shards.
4.  Place the resulting shard back into the original gap in the row, with the remaining shards in the same relative order before and after it.
5.  Repeat steps 3 and 4 until only one shard remains.
Note that each time steps 3 and 4 are performed, the number of remaining shards decreases by 2. Therefore, given that the initial number of shards is odd, enough successful repetitions will result in exactly one final shard: the Philosopher's Stone. Help Edgar determine whether or not it's possible to get to that point and hopefully save Alfred, without causing any rebound explosions along the way.

Input
Input begins with an integer T, the number of Philosopher's Stones that Edgar tries to reconstitute. For each stone there are two lines. The first contains the integer N. The second contains the length-NN string C_{1..N}
	 .
Output
For the ith stone, output a line containing "Case #i: " followed by a single character, either "Y" if it's possible For Edgar to end up with the Philosopher's Stone, or "N" if not.

Sample input:
6
3
BAB
3
BBB
5
AABBA
7
BAAABAA
11
BBBAABAAAAB
11
BABBBABBABB

Sample Output:
Case #1: Y
Case #2: N
Case #3: Y
Case #4: N
Case #5: Y
Case #6: N

Explanation of Sample
In the first case, Edgar is able to fuse the three shards together, as they include two differently-coloured shards, yielding a single black-coloured shard: the Philosopher's Stone.
In the second case, the three black shards will inevitably cause a rebound explosion if fused.
In the third case, Edgar can begin by fusing the first three shards into a single auburn-coloured shard. The row of shards will then feature colours "ABA", and those shards can be fused into the Philosopher's Stone.
"""


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
