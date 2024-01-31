def linearis():
    also = 42
    felso = 67
    van = True
    i = also
    while (i <= felso and i % 10 == 0):
        van = True
        i+=1
    if van == True:
        print(f"van 0-ra vegzodo szam {i}")
    if van == False:
        print(f"nincs 0-ra vegzodo")