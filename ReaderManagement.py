from datetime import datetime, timedelta

class Reader:
    def __init__(self, name, email, phone_number, book_title, borrow_date, status='False', fine=0):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.book_title = book_title
        self.borrow_date = datetime.strptime(borrow_date, '%Y-%m-%d')
        self.expired_date = self.borrow_date + timedelta(days=30)
        self.status = status
        self.fine = fine

    def display_info(self):
        print(f"|{self.name.center(25)}|{self.email.center(25)}|{self.phone_number.center(13)}|{self.book_title.center(21)}"
              f"| {self.borrow_date.strftime('%Y-%m-%d')}  | {self.expired_date.strftime('%Y-%m-%d')}  "
              f"|{self.status.center(8)}|{str(self.fine).center(6)}|")
        print("+-------------------------+-------------------------+-------------+---------------------+-------------+-------------+--------+------+")

reader_list = list()

class ReaderManagement:
    def __init__(self):
        self.readers = reader_list

    def add_reader(self, new_reader):
        self.readers.append(new_reader)
        print(f"Added new reader successfully!")

    def change_reader_info(self):
        name = input("Enter the name of the reader needed to change info: ")
        book = input(f"Enter title of book {name.title()} borrowed: ")
        change = input("Enter the category you want to change: Name  |  Email  | Phone number \n")
        new = input("Enter new info: ")
        for reader in self.readers:
            if reader.name == name.title() and reader.book_title == book.title():
                if change.lower() == 'name':
                    reader.name = new.title()
                    print("Reader information updated successfully.")
                elif change.lower() == 'email':
                    reader.email = new.lower()
                    print("Reader information updated successfully.")
                elif change.lower() == 'phone number':
                    if new.isnumeric():
                        reader.phone_number = new
                        print("Reader information updated successfully.")
                    else:
                        print("Invalid phone number.")
                else:
                    print("Invalid category.")
                return True
        return False

    def remove_reader(self):
        name = input("Enter name of the reader to remove: ")
        book = input(f"Enter title of book {name.title()} borrowed: ")
        for reader in self.readers:
            if reader.name == name.title() and reader.book_title == book.title():
                self.readers.remove(reader)
                print("Reader removed successfully.")
                return True
        return False
            
    def find_reader_by_name(self):
        if not self.readers:
            print("There is no reader to find.")
        else:
            found = False
            name = input("Enter the name of the reader to find: ")
            print_table()
            for reader in self.readers:
                if reader.name == name.title():
                    reader.display_info()
                    found = True
            return found

    def display_list_of_readers(self):
        if not self.readers:
            print("There is no reader to display.")
        else:
            print_table()
            for reader in sorted(self.readers, key=lambda x: x.name):
                reader.display_info()

    def print_list_by_borrow_date_or_fine(self):
        if not self.readers:
            print("There is no reader to print.")
        else:
            sort_key = input('Sort by "borrow_date" or "fine"? ')
            if sort_key.lower() in ["borrow_date", "fine"]:
                print_table()
                for reader in sorted(self.readers, key=lambda x: getattr(x, sort_key.lower()), reverse=True):
                    reader.display_info()
            else:
                print('Sort key must be "borrow_date" or "fine".')

    def show_list_of_readers_with_filter(self):
        if not self.readers:
            print("There is no reader to show.")
        else:
            category = input("Enter category you want to filter: name | book_title | status | fine \n")
            if category.lower() in ['name', 'book_title', 'status', 'fine']:
                value = input("Enter value want to filter out: ")
                print_table()
                for reader in self.readers:
                    if getattr(reader, category.lower()) == value.title() or getattr(reader, category.lower()) == int(value):
                        reader.display_info()
            else:
                print("Invalid category. Please try again!")

    def add_returned_book(self, name, book):
        for reader in self.readers:
            if reader.name == name.title() and reader.book_title == book.title():
                reader.status = 'True'
                return True
        return False

    def check_expired_date(self):
        count = 0
        for reader in self.readers:
            if reader.expired_date < datetime.now().strftime('%Y-%m-%d'):
                count += 1
                self.add_fine_to_reader(reader.name)
                print(f"Fine issued to {reader.name} for late return of book: {reader.book_title}")
        if count == 0:
            print("No reader is given fine issued.")
        else:
            print(f"Issued fine to {count} reader(s).")

    def add_fine_to_reader(self, name):
        for reader in self.readers:
            if reader.name == name:
                reader.fine += 100
        print("Fine added successfully.")

    def save_to_file(self):
        if not self.readers:
            print("There is no data to save.")
        else:
            file = open('reader.txt', 'w')
            file.write("+-------------------------+-------------------------+-------------+---------------------+-------------+-------------+--------+------+\n")
            file.write("|          Name           |          Email          |    Phone    |    Book Borrowed    | Borrow date | Return date | Status | Fine |\n")
            file.write("+-------------------------+-------------------------+-------------+---------------------+-------------+-------------+--------+------+\n")
            for reader in self.readers:
                file.write(f"|{reader.name.center(25)}|{reader.email.center(25)}|{reader.phone_number.center(13)}|"
                           f"{reader.book_title.center(21)}| {reader.borrow_date.strftime('%Y-%m-%d')}  | "
                           f"{reader.expired_date.strftime('%Y-%m-%d')}  |{reader.status.center(8)}|{str(reader.fine).center(6)}|\n")
                file.write("+-------------------------+-------------------------+-------------+---------------------+-------------+-------------+--------+------+\n")
            file.close()
            print("Data saved to file successfully.")

    def check_reader(self, name):
        for reader in self.readers:
            if reader.name == name.title():
                return True
        return False

def print_table():
    print("+-------------------------+-------------------------+-------------+---------------------+-------------+-------------+--------+------+")
    print("|          Name           |          Email          |    Phone    |    Book Borrowed    | Borrow date | Return date | Status | Fine |")
    print("+-------------------------+-------------------------+-------------+---------------------+-------------+-------------+--------+------+")
