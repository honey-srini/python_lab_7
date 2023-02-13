bdays = {"srini": "20/11/2000","honey": "20/11/2000", "balaji": "23/10/1999"}

name = input("Enter name: ").lower()

if name not in bdays:
    bday = input("Name is not available. Please enter bday to add: ")
    bdays[name] = bday
else:
    print(bdays[name])

print(bdays)
