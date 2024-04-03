def displayTitle():
    print("Virginia 'Addition / Substraction Only' Calculator")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def main():
    
    displayTitle()

    c = int(input("Enter 1st number: "))
    d = int(input("Enter 2nd number: "))

    print("Option:")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Enter choice: ")

    if choice == '1':
        print("Result:", addition(c, d))
    elif choice == '2':
        print("Result:", subtraction(c, d))
    else:
        print("Invalid")

if __name__ == "__main__":
    main()