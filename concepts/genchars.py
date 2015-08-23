# Takes an integer "n" and a character, and returns a string of the character
# that is "n" times long.

def generate_n_chars(n, char):
    count = 0
    word = ""
    templist = []
    while count < n:
        count += 1
        templist.append(char)
    word = "".join(templist)
    return word

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    char = input("Enter a character: ")
    print(generate_n_chars(n, char))