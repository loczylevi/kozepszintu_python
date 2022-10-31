import random

N = int(input("Hány alkalommal legyen feldobás? "))
anni = 0
panni = 0
for szam in range(N):
    generalt_szam1 = random.randint(1,6)
    generalt_szam2 = random.randint(1,6)
    generalt_szam3 = random.randint(1,6) 
    
    ossz = generalt_szam1 + generalt_szam2 + generalt_szam3
    if ossz > 10:
        panni += 1
        print(f"Dobás: {generalt_szam1} + {generalt_szam2} + {generalt_szam3} = {ossz} \tNyert: Panni")
    elif ossz < 10:
        anni += 1
        print(f"Dobás: {generalt_szam1} + {generalt_szam2} + {generalt_szam3} = {ossz} \tNyert: Anni")
        
print(f"A játék során {anni} alkalommal Anni, {panni} alkalommal Panni nyert.")
