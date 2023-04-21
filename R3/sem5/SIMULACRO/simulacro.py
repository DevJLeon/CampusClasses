import json
import time

with open("R3/sem5/SIMULACRO/Biblioteca.json") as biblioteca:
    access_b = json.load(biblioteca)
    bookstore = access_b["bookstore"]
    books = bookstore["book"]

def save():
    with open("R3/sem5/SIMULACRO/Biblioteca.json", "w") as save:
        json.dump(access_b,save, indent=4)

def addBook():
    lang = input("language of the book: \t")
    textT = input("Title: \t")

    authorsAmmount = int(input("How many authors does this book have?: \t"))
    authorList = []
    for i in range(authorsAmmount):
        if authorsAmmount == 1:
            authors = input("Name of author: \t")
        else:
            print("Name of ("+ str(i+1)+ ") author: \t")
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
                    print("*",autor)
            else:
                print("*",libro["author"])
            print("Publish year:", libro["year"]+"\nPrice:", libro["price"],"$","USD","\nCategory:", libro["_category"])

def deleteBook():
    print("Choose wich book you want to delete:")
    for i in range(len(books)):
        print(str(i)+": ",books[i]["title"]["__text"])
    deleteID = int(input("Write the ID to delete: "))
    books.pop(deleteID)
    save()
    

deleteBook()
#addBook()        
#readBooks()