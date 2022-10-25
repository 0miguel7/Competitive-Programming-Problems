# Vanya and lanterns
# Vanya walks late at night along a straight street of length l, lit by n lanterns.
# The lantern lights all points of the street that are at the distance of at most d from it,
# where d is some positive number, common for all lanterns.
# Vanya wonders: what is the minimum light radius d should the lanterns have to light the whole street?
# Input
# The first line contains two integers n, l the number of lanterns and the length of the street respectively.
# The next line contains n integers,the position of each lantern
# Output
# Print the minimum light radius d, needed to light the whole street. 


n, l = input().split()
n = int(n)
l = int(l)

posiciones = []

for i in range(n):
    posiciones.append(int(input()))
posiciones.sort()

d1 = posiciones[0]

for i in range(1,len(posiciones)):
    distancia = (posiciones[i] - posiciones[i-1])/2
    if (distancia > d1):
        d1 = distancia 

if (d1 < l- posiciones[n-1]):
    d1 = l - posiciones[n-1]

print(d1)