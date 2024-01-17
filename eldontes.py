def feladat2():
    n = int(input("\nszám:"))
    prim = False
    if n < 2:
        prim = False
    else:
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i += 1
        prim = i > math.sqrt(n)
    if prim  == False:
        print("Nem prim")
    else:
        print("Prim")
