# A function called main
def main():
    # Age takes input as age.
    Age = input("enter your Age:")
    # checks if the age is above 18
    # it would not work if Age entered is a string.
    if int(Age) > 18:
        print("welcome")


# Again if the function is within the program it would
# call the main() function
if __name__ == "__main__":
    main()
