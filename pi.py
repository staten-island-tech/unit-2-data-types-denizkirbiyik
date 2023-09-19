import math
import decimal

iterate = input("How many iterations of the algorithm do you want to compute? : ")
decimal.getcontext().prec = 1 + (
    int(
        input(
            "How much precision of digits would you like to compute for each calculation? : "
        )
    )
)
pi = 0

for i in range(int(iterate)):
    s1 = decimal.Decimal(
        decimal.Decimal(math.factorial(6 * i) * ((545140134 * i) + 13591409))
        / decimal.Decimal(
            (
                math.factorial(3 * i)
                * (math.factorial(i) ** 3)
                * ((-262537412640768000) ** i)
            )
        )
    )
    pi = pi + (s1)
pi = 1 / decimal.Decimal(pi)
pi = pi * (426880 * (decimal.Decimal(10005).sqrt()))
print(pi)