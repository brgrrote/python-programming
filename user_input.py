# 1. Employee ID
employee_id = input ("Employee ID: ")

# Check ID validity 
if not employee_id.isdigit() or len(employee_id) > 7:
    print("Invalid Employee ID. Must be a number with 7 or fewer digits")
    exit() 

# 2. Employee Name
employee_name = input ("Name: ")

# Define characters that are not allowed in the name
forbidden_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\\'

# Ensure the user did not leave the required field blank
if employee_name == "":
    print("Invalid Employee Name.")
    exit()

# Track how many characters are actual letters
letter_count = 0

# Loop through each character in the name 
for char in employee_name:
    if char in forbidden_chars:
        print("Invalid Employee Name.")
        exit()
    if char.isalpha():
        letter_count = letter_count +  1

# Check if more than half of the characters are letters
if letter_count <= len(employee_name) / 2:
    print("Invalid Employee Name.")
    exit()

# 3. Employee Email Address
employee_email = input("Email Address: ")

# Define characters that are not allowed in the name
forbidden_email_chars = '!"\'#$%^&*()=+,<>/?;:[]{}\\'

# Ensure the user did not leave the required field blank
if employee_email == "":
    print("Invalid Email.")
    exit()

# Track letters and numbers
alnum_count = 0

# Loop throuch each character in the email address
for char in employee_email:
    if char in forbidden_email_chars:
        print("Invalid Email Address.")
        exit()
    if char.isalnum():
        alnum_count = alnum_count + 1

# Check if more than half of the characters are letters or numbers
if alnum_count <= len(employee_email) / 2:
    print("Invalid Email Address.")
    exit()

# 4. Employee Address (Optional)
employee_address = input("Address(Optional): ")
forbidden_address_chars = '!"\'@$%^&*_=+<>?;:[]{})'

# Only run validation if the user actually typed an address
if employee_address !="":
    addr_count = 0

    # Loop through each character in the address
    for char in employee_address:
        if char in forbidden_address_chars:
            print("Invalid Address.")
            exit()
        if char.isalnum():
            addr_count = addr_count + 1

    # Check if more than half of the characters are letters
    if addr_count <= len(employee_address) / 2:
        print("Invalid Address.")
        exit()

    # Prepare the final sentence when an address is provided
    last_sentence = "Your address is " + employee_address + "."
else:
    last_sentence = "You did not provide an address."

# 5. Final Output 
print("Hello, " + employee_name + ". " + "Your Employee ID is " + employee_id + ", " + "and your email address is " + employee_email + ". "
      + last_sentence)