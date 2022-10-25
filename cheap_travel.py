# Cheap Travel
# Ann has recently started commuting by subway. We know that a one ride subway 
# ticket costs a rubles. Besides, Ann found out that she can buy a special ticket 
# for m rides (she can buy it several times). It costs b rubles. Ann did the math;
#  she will need to use subway n times. Help Ann, tell her what is the minimum sum of 
# money she will have to spend to make n rides?

# Input
# The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000)
#  — the number of rides Ann has planned, the number of rides covered by the m ride ticket,
#  the price of a one ride ticket and the price of an m ride ticket.

# Output
# Print a single integer — the minimum sum in rubles that Ann will need to spend.

n,m,a,b = input().split()

n = int(n)
m = int(m)
a = int(a)
b = int(b)

normal_cost = n * a

if (n % m == 0):
    special_cost = n/m * b
else:
    special_cost = int(n/m) * b
    aditional = (n % m) * a
    special_cost += aditional

if special_cost <= normal_cost:
    print(special_cost)
else:
    print(normal_cost)   