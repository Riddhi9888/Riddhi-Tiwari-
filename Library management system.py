
import colorama
from colorama import Fore,Back,Style,init



books = {}      # {id: {"name": "Python", "available": True}}
students = {}   # {id: "name"}

def menu():
    print(Fore.CYAN + "\n╔══════════════════════════════════════╗")
    print(Fore.CYAN + "║     Library Management System        ║")
    print(Fore.CYAN + "╚══════════════════════════════════════╝")
    print(Fore.GREEN + """ 
    1. Add Book
    2. View Books
    3. Search Book
    4. Register Student
    5. Issue Book
    6. Exit
    """)

while True:
    menu()
    choice = input("Enter your choice b/w 1 to 6: ").strip()

    if choice == "1": # Add Book
        book_id = input("Enter Book Id: ").strip()
        if not book_id.isdigit():
            print(Fore.RED + "Invalid Book Id! It Should be number only")
            continue
        if book_id in books:
            print(Fore.RED + "This Book Id already exists!")
            continue
        book_name = input("Enter the Book Name: ").strip()
        if not book_name:
            print(Fore.RED + "Book name cannot be empty!")
            continue
        books[book_id] = {"name": book_name, "available": True, "issued_to": None}
        print(Fore.YELLOW + f"Book '{book_name}' Added Successfully!")

    elif choice == "2": # View Books
        if not books:
            print(Fore.RED + "No Books in Library!")
        else:
            print(Fore.YELLOW + "\n--- All Books ---")
            for b_id, info in books.items():
                status = "Available" if info["available"] else f"Issued to {info['issued_to']}"
                print(f"ID: {b_id} | Name: {info['name']} | {status}")

    elif choice == "3": # Search Book
        search = input("Enter Book Id or Name to search: ").strip().lower()
        found = False
        for b_id, info in books.items():
            if search == b_id.lower() or search in info["name"].lower():
                status = "Available" if info["available"] else f"Issued to {info['issued_to']}"
                print(Fore.YELLOW + f"Found -> ID: {b_id} | Name: {info['name']} | {status}")
                found = True
        if not found:
            print(Fore.RED + "Book Not Found!")

    elif choice == "4": # Register Student
        s_id = input("Enter Student Id: ").strip()
        if not s_id.isdigit():
            print(Fore.RED + "Student Id should be number only!")
            continue
        s_name = input("Enter Student Name: ").strip()
        students[s_id] = s_name
        print(Fore.GREEN + f"Student '{s_name}' Registered Successfully!")

    elif choice == "5": # Issue Book
        b_id = input("Enter Book Id to Issue: ").strip()
        if b_id not in books:
            print(Fore.RED + "Book Id not found!")
            continue
        if not books[b_id]["available"]:
            print(Fore.RED + f"Book already issued to {books[b_id]['issued_to']}")
            continue
        s_id = input("Enter Student Id: ").strip()
        if s_id not in students:
            print(Fore.RED + "Student not registered! First register in option 4")
            continue
        books[b_id]["available"] = False
        books[b_id]["issued_to"] = students[s_id]
        print(Fore.GREEN + f"Book '{books[b_id]['name']}' Issued to {students[s_id]}")

    elif choice == "6":
        print(Fore.MAGENTA + "Exiting... Bye!")
        break
    else:
        print(Fore.RED + "Invalid choice! Please enter 1 to 6")
        
