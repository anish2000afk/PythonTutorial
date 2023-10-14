import sqlite3


def main():
    # Connection to a database called information.db
    db = sqlite3.connect("information.db")
    # row_factory returns everything as a ditionary rather that a tuple.
    db.row_factory = sqlite3.Row
    # creates a table with 4 columns.
    # Name would be text and age would be int.
    db.execute("create table if not exists Admin(Name text,age int)")
    db.execute("insert into Admin (Name,age) values (? , ?)", ("Hussein", 26))
    db.execute("insert into Admin (Name,age) values (? , ?)", ("Jena", 1))
    db.commit()
    # You could delete the entire row with Jena a the Name.
    # db.execute("delete from Admin where name='Jena'")

    # db.execute("Update Admin set age=2 where name='Jena'")

    # Selecting all from admin
    cusror = db.execute("select * from Admin")
    for row in cusror:
        print("Name:{}, Age:{}".format(row["Name"], row["age"]))


if __name__ == "__main__":
    main()
