class NameError(Exception):
    def __init__(self, message="Name must consist of at least two words, each starting with a capital letter."):
        super().__init__(message)

class EmailError(Exception):
    def __init__(self, message="Email must contain @ and a dot after @."):
        super().__init__(message)

class AgeError(Exception):
    def __init__(self, message="Age must be an integer between 0 and 120."):
        super().__init__(message)

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        words = value.split()
        if len(words) < 2 or not all(word[0].isupper() for word in words):
            raise NameError()
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        parts = value.split('@')
        if len(parts) != 2 or '.' not in parts[1]:
            raise EmailError()
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or not (0 <= value <= 120):
            raise AgeError()
        self._age = value

def main():
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        user = User(name, email, age)
        print("User created successfully!")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Age: {user.age}")
    except NameError as e:
        print(f"NameError: {e}")
    except EmailError as e:
        print(f"EmailError: {e}")
    except AgeError as e:
        print(f"AgeError: {e}")
    except ValueError:
        print("Age must be an integer.")

if __name__ == "__main__":
    main()
