# Create an empty list to hold all employee dictionaries
employees = []

# Define forbidden character strings for validation 
forbidden_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\\'
forbidden_email_chars = '!"\'#$%^&*()=+,<>/?;:[]{}\\'
forbidden_address_chars = '!"\'$%^&*_=+<>@?;:[]{}\\'

# Loop up to 5 times to collect information for up to 5 employees
while len(employees) < 5:
    print("\n--- Enter Information for Employee #" + str(len(employees) + 1) + " ---")

# ==============================================================
# 1. Employee ID
# ==============================================================
    while True:
        employee_id = input ("Employee ID: ")

        # Check ID validity 
        if employee_id.isdigit() and len(employee_id) <= 7:
            break
        else:
            print("Invalid Employee ID. Must be a number with 7 or fewer digits")

    # ==============================================================
    # 2. Employee Name
    # ==============================================================
    while True:
        employee_name = input ("Name: ")

    # Ensure the user did not leave the required field blank
        if employee_name == "":
            print("Invalid Employee Name.")
            continue

        has_forbidden_char = False
        letter_count = 0

        # Loop through each character in the name 
        for char in employee_name:
            if char in forbidden_chars:
                has_forbidden_char = True
                break
            if char.isalpha():
                letter_count = letter_count +  1

    # Check if more than half of the characters are letters
        if not has_forbidden_char and letter_count > len(employee_name) / 2:
            break
        else:
            print("Invalid Name.")

    # ==============================================================
    # 3. Employee Email Address
    # ==============================================================
    while True:
        employee_email = input("Email Address: ")

        # Ensure the user did not leave the required field blank
        if employee_email == "":
            print("Invalid Email. Email cannot be blank")
            continue

        has_forbidden_char = False
        alnum_count = 0

        # Loop through each character in the email address
        for char in employee_email:
            if char in forbidden_email_chars:
                has_forbidden_char = True
                break
            if char.isalnum():
                alnum_count = alnum_count + 1

        # Check if more than half of the characters are letters or numbers
        if not has_forbidden_char and alnum_count > len(employee_email) / 2:
            break
        else:
            print("Invalid Email Address.")

    # ==============================================================
    # 4. Employee Address (Optional)
    # ==============================================================
    while True: 
        employee_address = input("Address(Optional): ")

        # Only run validation if the user actually typed an address
        if employee_address == "":
            break

        has_forbidden_char = False
        addr_count = 0

        # Loop through each character in the address
        for char in employee_address:
            if char in forbidden_address_chars:
                has_forbidden_char = True
                break
            if char.isalnum():
                addr_count = addr_count + 1

        # Check if more than half of the characters are letters
        if not has_forbidden_char and addr_count > len(employee_address) / 2:
            break
        else:
            print("Invalid Address.")

    # ==============================================================
    # 5. Store in Dictionary & Add to list 
    # ==============================================================
    # Create a dictionary
    employee_record = {"Employee ID": employee_id,
                        "Employee Name": employee_name,
                        "Employee Email": employee_email,
                        "Employee Address": employee_address,
                        }

        # Append the dictionary to the main employee list
    employees.append(employee_record)

        # Ask if the user wants to add another employee 
    if len(employees) < 5:
            add_more = input ("Would you like to enter another employee? (y/n): ").lower()
            if add_more != "y":
                break

# ==============================================================
# Print the Final List
 # ==============================================================
print("\n All Employee Records:")
print(employees)