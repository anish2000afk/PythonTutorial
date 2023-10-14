def main():
    # Student={'Name':"hussein alrubaye",'Age':27,'Salary':232.5};
    Student = dict(Name="hussein alrubaye", Age=27, Salary=232.5)
    print(Student)
    # Replacing the earlier student with another student.
    Student["Name"] = "Hussein Ahmed"
    Student["Dept"] = "software engineer"
    print(Student, type(Student))
    # Deleting the value Dept and it's value.
    del Student["Dept"]
    print(Student, type(Student))
    print(Student["Name"])
    print(Student["Age"])
    # Clearing the Student dictionary.
    Student.clear()
    print(Student, type(Student))


if __name__ == "__main__":
    main()
