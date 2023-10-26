notes = {}

def create_note():
    title = input("Enter the note title: ")
    content = input("Enter the note content: ")
    notes[title] = content
    print("Note created!")

def view_note():
    title = input("Enter the note title: ")
    if title in notes:
        print(f"Title: {title}\nContent: {notes[title]}")
    else:
        print("Note not found.")

def list_notes():
    if notes:
        print("List of Notes:")
        for title in notes:
            print(f"- {title}")
    else:
        print("No notes available.")

def delete_note():
    title = input("Enter the note title to delete: ")
    if title in notes:
        del notes[title]
        print("Note deleted!")
    else:
        print("Note not found.")

def main():
    while True:
        print("\nSimple Note-Taking App")
        print("1. Create a Note")
        print("2. View a Note")
        print("3. List Notes")
        print("4. Delete a Note")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            view_note()
        elif choice == '3':
            list_notes()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Exiting the Note-Taking App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
