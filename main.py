def get_shelfs_book(count):
    for number in range(count):
        shelf_num=input("На какую полку хотите добавить книгу: ")
        book_name=input("Название книги: ")
        book_creator=input("Автор: ")
        book_format={"name" : book_name, "authors" : book_creator}
        with open("library.txt", "a") as f:
            f.write(f"Shelf_{shelf_num}:{book_format}\n")
    return "Книги добавлены"


def read_file_library():
    with open("library.txt", "r") as f:
        for line in f:
            print(line)


def main():
    get_shelfs_book(3)
    read_file_library()

    
if __name__=="__main__":
    main()