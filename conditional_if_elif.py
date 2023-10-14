def main():
    Age = input("enter your Age:")
    # If statement that checks age within 8 and 10
    # Including 8 and 10
    # Prints children 4 times.
    if int(Age) >= 8 and int(Age) <= 10:
        print("children")
        print("children")
        print("children")
        print("children")
    elif int(Age) >= 11 and int(Age) <= 15:
        print("Kids")
    elif int(Age) >= 16 and int(Age) <= 18:
        print("Teenagers")
    elif int(Age) >= 19 and int(Age) <= 30:
        print("Youngsters")
    else:
        print("Boomers")
    print("End")


if __name__ == "__main__":
    main()
