def osszegzes():
    n = int(input("N:"))
    ossz = 0
    while n < 0:
        n = int(input("N:"))
    for i in range(1,n + 1):
        ossz+=i
    print("Az első",n,"db termesztészetes szám összege",ossz)
