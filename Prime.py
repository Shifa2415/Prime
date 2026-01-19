import sys

def Prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        number = int(sys.argv[1])
    except IndexError:
        number = int(input("Enter number: "))
    except ValueError:
        print("Invalid input")
        sys.exit(1)

    print("Prime" if Prime(number) else "Not Prime")
