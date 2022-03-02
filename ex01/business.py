# 100 30 30 | 21
# 2340 15 10 | 198.9
# 30 15 23 | 5.865

x, y, z = list(map (int, input("Enter three values: ").split()))
print("Original price:", x)
print("Discount:", y)
print("Markup:", z)
t = (x*(y/100)-x)*(-1)
profit_sum = t*(1+z/100)-t
print("Profit sum:", int(profit_sum//1))