from admin import Admin
from user import User

print("===================================")
print("      Welcome to Job's Hub")
print("===================================")

class Choice:

    def __init__(self):

        while True:

            print("\n===== Main Menu =====")
            print("1. Admin")
            print("2. User")
            print("3. Exit")

            choice = input("Enter your choice: ")

            match choice:

                case "1":
                    Admin()

                case "2":
                    User()

                case "3":
                    print("\nThank You for using Job's Hub!")
                    break

                case _:
                    print("Invalid Choice! Please try again.")


# Start Program
Choice()