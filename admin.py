from srvice import UserSecurity
from database import user_collection, jobs_collection


class Admin:

    def __init__(self):

        while True:

            print("\n===== Admin Menu =====")
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

            admin = user_collection.find_one({
                "username": username,
                "role": "admin"
            })

            if admin is None:
                print("Admin not found!")
                continue

            security = UserSecurity(admin["username"], admin["password"])

            if security.authenticate(password):
                print("\nLogin Successful!")
                self.admin_panel(admin["username"])
                return

            print("Incorrect Password!")

    def register(self):

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if user_collection.find_one({"username": username}):
            print("Username already exists!")
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
            "password": password,
            "role": "admin"
        })

        print("Admin Registration Successful!")
        self.admin_panel(username)

    def admin_panel(self, username):

        while True:

            print(f"\n===== Welcome {username} =====")
            print("1. Add Job")
            print("2. View All Jobs")
            print("3. Update Job Salary")
            print("4. Delete Job")
            print("5. Logout")

            choice = input("Enter your choice: ")

            match choice:

                case "1":
                    self.add_job()

                case "2":
                    self.view_jobs()

                case "3":
                    self.update_job()

                case "4":
                    self.delete_job()

                case "5":
                    print("Logged Out Successfully!")
                    break

                case _:
                    print("Invalid Choice!")

    def add_job(self):

        job_name = input("Enter Job Name: ")
        company = input("Enter Company Name: ")
        location = input("Enter Location: ")
        salary = input("Enter Salary: ")
        skill = input("Enter Required Skill: ")

        jobs_collection.insert_one({
            "job_name": job_name,
            "company": company,
            "location": location,
            "salary": salary,
            "skill": skill
        })

        print("Job Added Successfully!")

    def view_jobs(self):

        jobs = jobs_collection.find()

        print("\n===== All Jobs =====")

        found = False

        for job in jobs:
            found = True
            print("-----------------------------")
            print("Job Name :", job["job_name"])
            print("Company  :", job["company"])
            print("Location :", job["location"])
            print("Salary   :", job["salary"])
            print("Skill    :", job["skill"])

        if not found:
            print("No Jobs Available!")

    def update_job(self):

        job_name = input("Enter Job Name: ")
        new_salary = input("Enter New Salary: ")

        result = jobs_collection.update_one(
            {"job_name": job_name},
            {"$set": {"salary": new_salary}}
        )

        if result.modified_count > 0:
            print("Job Updated Successfully!")
        else:
            print("Job Not Found!")

    def delete_job(self):

        job_name = input("Enter Job Name: ")

        result = jobs_collection.delete_one({
            "job_name": job_name
        })

        if result.deleted_count > 0:
            print("Job Deleted Successfully!")
        else:
            print("Job Not Found!")