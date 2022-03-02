#3 10 14 | 21 
#10 3 21 | 14
#2 12 14 | 0
#12 2 0 | 14
#0 0 0 | 0

#time_zone_A = (int,input("Enter A time zone: ") + (print(".00")))

x, y, z = list(map (int, input("Enter three values: ").split()))
print("A time zone:", x)
print("B time zone:", y)
print("A time:", z)

B_time = (z-x+y)%24 
print ("B time:", B_time)