#fizzbuzz 

max_stevilo = int(input("Vnesi željeno število (med 1 in 100)"))

for i in range (1, max_stevilo + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(str(i))
    i = i + 1
    
#male crke

besede = str(input("Vnesi besedilo: "))
besede_v_male_crke = besede.lower()
print(besede_male_crke)