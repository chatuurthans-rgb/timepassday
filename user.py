from srvice import UserSecurity
from database import (
    user_collection,
    jobs_collection,
    applications_collection
)


class User:

    def __init__(self):

        while True:

            print("\n===== User Menu =====")
            print("1. Login")
            print("2. Register")
            print("3. Back")

            choice = input("Enter your choice: ")

            match choice:

                case "1":
                    self.login()

                case "2":
                    self.register()

                case "3":
                    break

                case _:
                    print("Invalid Choice!")

    def login(self):

        while True:

            username = input("Enter Username: ")
            password = input("Enter Password: ")

            user = user_collection.find_one({
                "username": username
            })

            if user is None:
                print("User not found!")
                continue

            security = UserSecurity(
                user["username"],
                user["password"]
            )

            if security.authenticate(password):
                print(f"\nWelcome {user['username']}")
                self.user_panel(user["username"])
                return

            print("Incorrect Password!")

    def register(self):

        username = input("Enter Username: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if user_collection.find_one({"username": username}):
            print("Username already exists!")
            return

        if user_collection.find_one({"email": email}):
            print("Email already exists!")
            return

        security = UserSecurity(username, password)

        if not security.validate_password():

            print("Password must contain:")
            print("- At least 6 characters")
            print("- One uppercase letter")
            print("- One number")
            return

        user_collection.insert_one({
            "username": username,
            "email": email,
            "password": password,
            "role": "user"
        })

        print("Registration Successful!")

    def user_panel(self, username):

        while True:

            print("\n===== User Dashboard =====")
            print("1. View All Jobs")
            print("2. Search Job by Location")
            print("3. Search Job by Skill")
            print("4. Apply Job")
            print("5. View Applied Jobs")
            print("6. Logout")

            choice = input("Enter your choice: ")

            match choice:

                case "1":
                    self.view_jobs()

                case "2":
                    self.search_location()

                case "3":
                    self.search_skill()

                case "4":
                    self.apply_job(username)

                case "5":
                    self.view_applied_jobs(username)

                case "6":
                    print("Logout Successful!")
                    break

                case _:
                    print("Invalid Choice!")

    def view_jobs(self):

        jobs = jobs_collection.find()

        print("\n===== Available Jobs =====")

        found = False

        for job in jobs:

            found = True

            print("---------------------------")
            print("Job :", job["job_name"])
            print("Company :", job["company"])
            print("Location :", job["location"])
            print("Salary :", job["salary"])
            print("Skill :", job["skill"])

        if not found:
            print("No Jobs Available!")

    def search_location(self):

        location = input("Enter Location: ")

        jobs = jobs_collection.find({
            "location": location
        })

        found = False

        for job in jobs:

            found = True

            print("---------------------------")
            print("Job :", job["job_name"])
            print("Company :", job["company"])
            print("Salary :", job["salary"])
            print("Skill :", job["skill"])

        if not found:
            print("No Jobs Found!")

    def search_skill(self):

        skill = input("Enter Skill: ")

        jobs = jobs_collection.find({
            "skill": skill
        })

        found = False

        for job in jobs:

            found = True

            print("---------------------------")
            print("Job :", job["job_name"])
            print("Company :", job["company"])
            print("Location :", job["location"])
            print("Salary :", job["salary"])

        if not found:
            print("No Jobs Found!")

    def apply_job(self, username):

        job_name = input("Enter Job Name: ")

        job = jobs_collection.find_one({
            "job_name": job_name
        })

        if job is None:
            print("Job Not Found!")
            return

        applications_collection.insert_one({
            "username": username,
            "job_name": job_name,
            "company": job["company"]
        })

        print("Applied Successfully!")

    def view_applied_jobs(self, username):

        jobs = applications_collection.find({
            "username": username
        })

        print("\n===== Applied Jobs =====")

        found = False

        for job in jobs:

            found = True

            print("---------------------")
            print("Job :", job["job_name"])
            print("Company :", job["company"])

        if not found:
            print("No Applied Jobs!")