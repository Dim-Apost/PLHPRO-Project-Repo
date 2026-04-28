from classes.user import User
from classes.activity import Hobbie,Task

#τεστ ότι δουλεύουν οι κλάσεις και οι συναρτήσεις
def app():
    user1 = User("Amalia", "std170663@ac.eap.gr", "pass123$", 8, 8)
    print(user1)
    print("hello")

    hobbie1 = Hobbie(2, 5, "tennis")
    print(hobbie1)

    hobbie1.edit_time(5)
    print(hobbie1)

    task1 = Task(5, 9, "job")
    print(task1)

    task1.edit_priority(7)
    print(task1)


# --- Κύριο Μενού ---
def main():
    # Η τοπική λίστα που θα κρατάει τα δεδομένα μας κατά την εκτέλεση
    read_log_file = 'user_names_log.csv'

    while True:
        print("\n=== MENOY ΔΙΑΧΕΙΡΙΣΗΣ ΧΡΟΝΟΥ ===")
        print("1. Εισαγωγή Δεδομένων")
        print("2. Exit")

        choice = input("Επιλογή: ")

        if choice == '1':
            sign_in_choice = input("a. Για εισαγωγή νέων χρηστών: \nb. Σύνδεση χρήστη:\n")
            if sign_in_choice == 'a':
                name = input("Όνομα: ")
                email = input("email: ")
                password = input("password: ")
                our_spend_activities = input("Εκτιμώμενος χρόνος υποχρεώσεων: ")
                our_spend_hobbies = input("Εκτιμώμενος χρόνος δραστηριοτήτων: ")
                read_log_file.add_new_user(new_user)
                print("Συγχαρητήρια!\nΝέος χρήστης προστέθηκε με επιτυχία")
            elif choice == 'b':
                email = input("email: ")
                password = input("password: ")
                #read_log_file.add_new_user(new_user) να γίνει αλλαγή σε διάβασμα δεδομένων
                print("Συνδεθήκατε")
            else:
                print ("Ops!\nΠληκτρολόγησες δεδομένα :( \nΞαναπροσπάθησε")

        elif choice == '9':
            print("Έξοδος...")
            break
        else:
            print("Λάθος επιλογή, προσπαθήστε ξανά.")

        choice = input("Επιλογή: ")

if __name__ == "__main__":
    app() #τεστ ότι δουλεύουν οι κλάσεις και οι συναρτήσεις
    main() # --- Κύριο Μενού ---