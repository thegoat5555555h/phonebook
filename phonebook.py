phonebook = []

def find_phone_info(phone_number):
    # Simulating phone info retrieval
    name = "John Doe"
    phone_provider = "Example Telecom"
    return name, phone_provider

def save_to_phonebook(name, phone_number, phone_provider):
    entry = {"Name": name, "Phone Number": phone_number, "Phone Provider": phone_provider}
    phonebook.append(entry)

def open_link(link):
    response = input("Do you want to open the link? (Y/N): ")
    if response.upper() == "Y":
        print("Opening the link...")
        # Code to open the link in a web browser
        print("Link opened:", link)
    else:
        print("Exiting...")

phone_number = input("Enter the phone number: ")
name, phone_provider = find_phone_info(phone_number)
save_to_phonebook(name, phone_number, phone_provider)

paypal_link = "https://www.paypal.com/donate/?hosted_button_id=68FYWBYFTUFRJ"
open_link_permission = input("Do you want to open the PayPal link? (Y/N): ")
if open_link_permission.upper() == "Y":
    open_link(paypal_link)
else:
    print("Exiting...")
