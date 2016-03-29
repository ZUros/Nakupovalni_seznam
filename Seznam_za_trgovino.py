nakupovalni_seznam = []

print ("N A K U P O V A L N A I   S E Z N A M")
print ("(Ko boste koncali z dodajanjem vpisite 'KONCAJ') ")

while True:
    nov_izdelek = raw_input("Dodaj izdelek na seznam: ")
    if nov_izdelek == "KONCAJ":
        break

    nakupovalni_seznam.append(nov_izdelek)


print("Tu je tvoj nakupovalni seznam: ")

for izdelek in nakupovalni_seznam:
        print(izdelek)

