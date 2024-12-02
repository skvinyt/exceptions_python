import os

# Файл для хранения сообщений чата
CHAT_FILE = 'chat.txt'

def read_messages():
    try:
        with open(CHAT_FILE, 'r') as file:
            messages = file.read()
            return messages
    except FileNotFoundError:
        return "No messages yet."

def write_message(username, message):
    with open(CHAT_FILE, 'a') as file:
        file.write(f"{username}: {message}\n")

def main():
    username = input("Enter your name: ")

    while True:
        print("\nChoose an action:")
        print("1. View current chat")
        print("2. Send a message")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            messages = read_messages()
            print("\nCurrent chat:")
            print(messages)
        elif choice == '2':
            message = input("Enter your message: ")
            write_message(username, message)
            print("Message sent.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
