import json
import time

##NOTA PARA EL PROFESOR: 
#### Mi ruta acá es local, así que cuando ejecute el programa, debe colocar el archivo en una ruta similar, o modificar las que están escritas acá (no alcancé a arreglar este pqueño detalle por tiempo)

with open("R3/sem5/SIMULACRO/Biblioteca.json") as biblioteca:
    access_b = json.load(biblioteca)
    bookstore = access_b["bookstore"]
    books = bookstore["book"]


def save():
    with open("R3/sem5/SIMULACRO/Biblioteca.json", "w") as save:
        json.dump(access_b, save, indent=4)


def addBook():
    lang = input("language of the book: \t")
    textT = input("Title: \t")

    authorsAmmount = int(input("How many authors does this book have?: \t"))
    authorList = []
    for i in range(authorsAmmount):
        if authorsAmmount == 1:
            authors = input("Name of author: \t")
        else:
            print("Name of (" + str(i+1) + ") author: \t")
            author = input()
            authorList.append(author)
            authors = authorList

    year = int(input("Year of publish: \t"))
    price = float(input("Price of the book: \t"))
    category = input("Category: \t")

    newbook = {
        "title": {
            "_lang": lang,
            "__text": textT
        },
        "author": authors,
        "year": str(year),
        "price": str(price),
        "_category": category
    }
    books.append(newbook)

    save()


def readBooks():
    option = int(
        input("Select an option: \n1.See all the books. \t2.Search an specific one."))

    if option == 1:
        for libro in books:
            time.sleep(1)
            print("\n------------------------------------------------------------\nTitle:",
                  libro["title"]["__text"]+"\nAuthor/s:"
                  )
            if type(libro["author"]) == list:
                for autor in libro["author"]:
                    print("*", autor)
            else:
                print("*", libro["author"])
            print("Publish year:", libro["year"]+"\nPrice:",
                  libro["price"], "$", "USD", "\nCategory:", libro["_category"])


def updateBook():
    print("Choose wich book you want to update:")
    for i in range(len(books)):
        print(str(i)+": ", books[i]["title"]["__text"])
    nombre = input("Name of the book to update: \t")
    updateID = books.index(nombre)

    libro = books[updateID]
    print("\n------------------------------------------------------------\nTitle:",
          libro["title"]["__text"]+"\nAuthor/s:")
    if type(libro["author"]) == list:
        for autor in libro["author"]:
            print("*", autor)
    else:
        print("*", libro["author"])
    print("Publish year:", libro["year"]+"\nPrice:",
          libro["price"], "$", "USD", "\nCategory:", libro["_category"])

    change = int(input(
        "What do you want to update?: \n1.Title 2.Authors\n3.Publish year 4.Price\n5.Category 0.EXIT\n"))

    while change > 0:
        if change == 1:
            libro["title"]["__text"] = input("Write the new name: \t")
        elif change == 2:
            authorsAmmount = int(
                input("How many authors does this book have?: \t"))
            authorList = []
            for i in range(authorsAmmount):
                if authorsAmmount == 1:
                    authors = input("Name of author: \t")
                else:
                    print("Name of (" + str(i+1) + ") author: \t")
                    author = input()
                    authorList.append(author)
                    authors = authorList
            libro["author"] = authors
        elif change == 3:
            libro["year"] = input("Write the new publish year: \t")
        elif change == 4:
            libro["price"] = input("Write the new price: \t")
        elif change == 5:
            libro["_category"] = input("Write the new category: \t")
        change = int(input(
            "What do you want to update?: \n1.Title 2.Authors\n3.Publish year 4.Price\n5.Category 0.EXIT\n"))
        
        save()

def deleteBook():
    print("Choose wich book you want to delete:")
    for i in range(len(books)):
        print(str(i)+": ", books[i]["title"]["__text"])
    deleteID = int(input("Write the ID to delete: "))
    books.pop(deleteID)
    save()


menuopt = int(input("Select an option: \n1.Add a new book 2.Search Books \n3.Update an existing book 4.Delete a book\n 0.EXIT: \t"))

while menuopt >0:
    if menuopt == 1:
        addBook()
    elif menuopt == 2:
        readBooks()
    elif menuopt == 3:
        updateBook()
    elif menuopt == 4:
        deleteBook()
    menuopt = int(input("Select an option: \n1.Add a new book 2.Search Books \n3.Update an existing book 4.Delete a book\n 0.EXIT: \t"))


