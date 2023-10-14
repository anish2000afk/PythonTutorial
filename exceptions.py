def main():
    try:
        # We try to open a file and store it in readFile.
        # We do so with r parameter which is read.
        readFile = open("test.txt", "r")
        # Print each line.
        for line in readFile:
            print(line)
        # We close the file.
        readFile.close()

    except IOError:
        print("File not found")
    else:
        print("File is read")


if __name__ == "__main__":
    main()
