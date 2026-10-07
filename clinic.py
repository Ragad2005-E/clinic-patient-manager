import re


def read_required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def valid_email(value):
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value))


class Patient():
    def __init__(self, id, fname, lname, email, phoneNumber, password, treatments):
        self.id = id
        self.fname = fname.strip()
        self.lname = lname.strip()
        self.email = email
        self.phoneNumber = f"05{phoneNumber}"
        self.password = password
        self.treatments = treatments

    def __str__(self):
        return f"Name: {self.fname} {self.lname}.\nID: {self.id}. \nGmail: {self.email}.\nPhone Number: {self.phoneNumber}.\nTreatments: {self.treatments}"


class Admin():
    def __init__(self):
        self.patients = {}
        self.treatments = []

    def treatmentsPage(self):
        while True:
            print("""********** Treatments Page **********
Menu:
1) Add Treatment.
2) Show All Treatments.
3) Delete Treatment.
4) Back.
""")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("Your Treatments:")
                if self.treatments:
                    for i, tr in enumerate(self.treatments):
                        print(f"{i+1}. {tr}.")
                else:
                    print("You don't have any treatment yet.")

                while True:
                    tr = input("Enter a Treatment: ").capitalize().strip()
                    if not tr:
                        print("Treatment cannot be empty.")
                    elif tr in self.treatments:
                        print("This treatment already exists !!!\n")
                    else:
                        self.treatments.append(tr)
                        print("Treatment added Successfully...")
                        break

            elif choice == '2':
                print("Your Treatments:")
                if self.treatments:
                    for i, tr in enumerate(self.treatments):
                        print(f"{i+1}. {tr}.")
                else:
                    print("You don't have any treatment yet.")

            elif choice == '3':
                print("Your Treatments:")
                if self.treatments:
                    for i, tr in enumerate(self.treatments):
                        print(f"{i+1}. {tr}.")
                else:
                    print("You don't have any treatment yet.")
                    continue

                while True:
                    tr = input("Enter a Treatment: ").capitalize().strip()
                    if tr not in self.treatments:
                        print("Not found !!!")
                    else:
                        self.treatments.remove(tr)
                        print("Treatment deleted Successfully...")
                        break

            elif choice == '4':
                break

            else:
                print("Invalid Input.\n")

    def showAll(self):
        print("\n********PATIENTS********\n")
        if self.patients:
            for x in self.patients.values():
                print(x)
                print("*" * 20, "\n")
        else:
            print("There are no patients yet.\n")

    def search(self):
        print("********** Searching Page. **********\n")
        enter = input("Enter ID: ").strip()

        if enter in self.patients:
            print("*" * 25, "\n")
            print(self.patients[enter], "\n")
        else:
            print("The patient was not found !!!")

    def add(self):
        print("********** Adding Page. **********\n")
        treatments = []

        while True:
            id = read_required("Enter ID: ")
            if id in self.patients:
                print("This ID already exists !!!")
            else:
                break

        fname = read_required("Enter first name: ").capitalize()
        lname = read_required("Enter last name: ").capitalize()

        while True:
            email = input("Enter Email: ").strip()
            if not valid_email(email):
                print("Invalid email address.")
            else:
                break

        while True:
            pn = input("Enter Phone Number without 05: ").strip()
            if pn.isdigit() and len(pn) == 8:
                break
            else:
                print("Invalid phone number !!! It must be 8 digits only.")

        pw = read_required("Enter Password: ")

        while True:
            print("Your Treatments:")
            if self.treatments:
                for i, tr in enumerate(self.treatments):
                    print(f"{i+1}. {tr}.")
            else:
                print("You don't have any treatment yet.")
                break

            treatment = input("Enter Treatment: ").capitalize().strip()

            if treatment in self.treatments:
                
                if treatment not in treatments:
                    treatments.append(treatment)
            else:
                print("This treatment was not found !!!")

            if input("Do you want to add another treatment? (yes/no): ").lower() != "yes":
                break

        self.patients[id] = Patient(id, fname, lname, email, pn, pw, treatments)
        print("Patient was added Successfully...")

    def edit(self):
        print("********** Editing Page. **********\n")

        while True:
            id = read_required("Enter ID: ")
            if id in self.patients:
                break
            else:
                print("ID not found !!!")

        print("""1) First Name
2) Last Name
3) Email
4) Phone Number
5) Password
6) Treatments
7) Exit""")

        choice = input("Enter what you want to edit: ")

        if choice == '1':
            self.patients[id].fname = read_required("Enter new First Name: ").capitalize()

        elif choice == '2':
            self.patients[id].lname = read_required("Enter new Last Name: ").capitalize()

        elif choice == '3':
            while True:
                new = input("Enter Email: ").strip()
                if valid_email(new):
                    self.patients[id].email = new
                    break
                print("Invalid email!")

        elif choice == '4':
            while True:
                new = input("Enter Phone Number without 05: ").strip()
                if new.isdigit() and len(new) == 8:
                    self.patients[id].phoneNumber = "05" + new
                    break
                print("Invalid phone number!")

        elif choice == '5':
            self.patients[id].password = read_required("Enter new Password: ")

        elif choice == '6':
            treatments = []

            print("Your Treatments:")
            if self.treatments:
                for i, tr in enumerate(self.treatments):
                    print(f"{i+1}. {tr}.")
            else:
                print("You don't have any treatment yet.")
                return

            while True:
                treatment = input("Enter new Treatment: ").capitalize().strip()

                if treatment in self.treatments:
                    treatments.append(treatment)
                else:
                    print("This treatment was not found !!!")

                if input("Add another? (yes/no): ").lower() != "yes":
                    break

            self.patients[id].treatments = list(dict.fromkeys(treatments))

        elif choice == '7':
            return

        else:
            print("Invalid choice!")

    def delete(self):
        print("********** Deleting Page. **********\n")

        while True:
            id = input("Enter ID to delete: ")
            if id in self.patients:
                break
            else:
                print("ID not found !!!")

        confirm = input("Are you sure you want to delete this patient? (yes/no): ").lower()

        if confirm == "yes":
            del self.patients[id]
            print("Patient deleted successfully.")
        else:
            print("Delete canceled.")


admin = Admin()


def adminPage():
    if input("Enter User name: ") == 'admin' and input("Enter Password: ") == 'admin':
        print("Complete verification...\n")
    else:
        print("You have a mistake, try again !!! \n")
        return

    while True:
        print("""Admin Menu:
1) Add patient.
2) Display all patients.
3) Search.
4) Edit.
5) Delete.
6) Treatments Page.
7) Back.""")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            admin.add()
        elif choice == '2':
            admin.showAll()
        elif choice == '3':
            admin.search()
        elif choice == '4':
            admin.edit()
        elif choice == '5':
            admin.delete()
        elif choice == '6':
            admin.treatmentsPage()
        elif choice == '7':
            break
        else:
            print("Invalid Input !!!")


def patientPage():
    print("********** Patient Page **********\n")

    id = read_required("Enter ID: ").strip()

    if id not in admin.patients:
        print("Patient not found !!!")
        return

    pw = read_required("Enter Password: ")
    patient = admin.patients[id]

    if pw != patient.password:
        print("Wrong password !!!")
        return

    while True:
        print("""Patient Menu:
1) View my information
2) Edit my information
3) Exit""")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n", patient)

        elif choice == '2':
            print("""Edit:
1) First Name
2) Last Name
3) Email
4) Phone Number
5) Password
6) Treatments""")

            c = input("Choose: ")

            if c == '1':
                patient.fname = read_required("New First Name: ").capitalize()

            elif c == '2':
                patient.lname = read_required("New Last Name: ").capitalize()

            elif c == '3':
                while True:
                    new = input("New Email: ").strip()
                    if valid_email(new):
                        patient.email = new
                        break
                    print("Invalid email!")

            elif c == '4':
                while True:
                    new = input("New Phone without 05: ").strip()
                    if new.isdigit() and len(new) == 8:
                        patient.phoneNumber = "05" + new
                        break
                    print("Invalid phone number!")

            elif c == '5':
                patient.password = read_required("New Password: ")

            elif c == '6':
                treatments = []

                print("Your Treatments:")
                if admin.treatments:
                    for i, tr in enumerate(admin.treatments):
                        print(f"{i+1}. {tr}.")
                else:
                    print("You don't have any treatment yet.")
                    continue

                while True:
                    treatment = input("Enter new Treatment: ").capitalize().strip()

                    if treatment in admin.treatments:
                        treatments.append(treatment)
                    else:
                        print("This treatment was not found !!!")

                    if input("Add another? (yes/no): ").lower() != "yes":
                        break

                patient.treatments = list(dict.fromkeys(treatments))

            else:
                print("Invalid choice!")

        elif choice == '3':
            break

        else:
            print("Invalid input!")


def ClinicPatientManagementSystem():
    print("*" * 45)
    print("***** CLINIC PATIENT MANAGEMENT SYSTEM *****")
    print("*" * 45)

    while True:
        print("""Menu:
1) Admin.
2) Patient.
3) Exit.""")

        choice = input("Enter your choice: ")

        if choice == '1':
            adminPage()
        elif choice == '2':
            patientPage()
        elif choice == '3':
            print("Good bye...")
            break
        else:
            print("Invalid input !!!\n")


if __name__ == "__main__":
    ClinicPatientManagementSystem()
