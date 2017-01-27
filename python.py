#Dæmi1
tala = int(input("Sláðu inn tölu "))
tala2 = int(input("Sláðu inn aðra tölu "))
tala3 = str(tala + tala2)
tala4 = str(tala * tala2)
print("Samanlagt er það:",tala3,"og margfaldað er það:",tala4)
#Dæmi2
nafn = input("Sláðu inn fornafnið þitt ")
nafn1 = input("Sláðu inn eftirnafnið þitt ")
print("Halló",nafn,nafn1)
#dæmi3
upperCounter = 0
lowerCounter = 0
lowerAfterUpperCounter = 0
texti = input("Sláðu inn texta: ")
for i in texti:
    if i == " ":
        fyrriStafur = "o"
    elif i.isupper():
        upperCounter = upperCounter + 1
        fyrriStafur = i
    elif i.islower():
        lowerCounter = lowerCounter + 1
        if fyrriStafur.isupper():
            lowerAfterUpperCounter = lowerAfterUpperCounter + 1
        fyrriStafur = i
print(upperCounter,"hástafir, og",lowerCounter,"lágstafir. ",lowerAfterUpperCounter,"lágstafir komu strax eftir hástaf")
