A1 = input("Steph Curry is: (adjective)")
A2 = input("In the NBA, he: (adjective)")
A3 = input("He is also a (adjective) person:")
A4 = input("He: (adjective)")
A5 = input("His kid is: (adjective")

print(" Steph Curry is " + A1)
print(" In the NBA, he " + A2)
print(" He is also a " + A3 + " person")
print(" He " + A4)
print(" His kid is " + A5)

def main():
    words = str(input("Input Sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()


main()