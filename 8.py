words  = [ "srini","honey","balaji","mani","murali"]

letter = input("Enter a character: ")
if (len(letter) > 1):
    print("Enter a single character")
elif(letter.isdigit()):
     print("Enter an alphabet")

for i in words:
    if(i.startswith(letter)):
        print(i)
