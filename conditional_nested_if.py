def main():
    Degree = input("Enter your Degree:")
    # There are 2 conditions if you get above 90.
    if int(Degree) >= 90:
        print("Hiya!!!")
        x = 5
        if int(Degree) > 94:
            print("Your Score is A+")
        else:
            print("Your Score is A-")
    # Conditions if you get below 90.
    elif int(Degree) >= 80 and int(Degree) <= 89:
        print("Your Score is B")
    elif int(Degree) >= 70 and int(Degree) <= 79:
        print("Your Score is C")
    elif int(Degree) >= 60 and int(Degree) <= 69:
        print("Your Score is D")
    elif int(Degree) >= 50 and int(Degree) <= 59:
        print("Your Score is E")
    else:
        print("You Fail")


if __name__ == "__main__":
    main()
