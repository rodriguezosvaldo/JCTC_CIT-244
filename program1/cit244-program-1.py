class Contact():
    def __init__(self):
        self.firstname = input("Enter the first name: ")
        self.lastname = input("Enter the last name: ")
        self.email = input("Enter the email: ")

    def data(self):
        contact_dict = {"Name":self.firstname, "Last Name":self.lastname, "email":self.email}
        return contact_dict
        
contacts = []    
def menu():
    print("*****Program Options*****\n")
    print("1.) Display all contacts")
    print("2.) Create new contact")
    print("3.) Exit")
    option = input("Enter 1, 2, or 3: ")
    print()
    options(option)

def options(option):
    if option == "1":
        if contacts == []:
            print("The list of contacts is empty")
            input("Press Enter to go back to the Program Options")
            menu()
        else:
            larger_word_list = []
            for dict in contacts:
                for values in dict.values():
                    larger_word_list.append(values) 
            len_larger_word = len(max(larger_word_list, key = len))
            header_list = list(contacts[0].keys())
            header = " | ".join(key.center(len_larger_word) for key in header_list)
            print()
            print(header)
            
            for dict in contacts:
                print(("-")*len(header))
                values_list = list(dict.values())
                row = " | ".join(value.center(len_larger_word) for value in values_list)
                print(row)

            input("\nPress Enter to go back to the Program Options")
            menu()

    elif option == "2":
        contact = Contact()
        contacts.append(contact.data())
        print("The new contact was created\n")
        input("Press Enter to go back to the Program Options")
        menu()

    elif option == "3":
        input("Press Enter to exit the program")

    else:
        input("\nWrong choice\nPress Enter to go back to the Program Options")
        menu()

menu()


  
        

       
       
    
    
    
    

    


