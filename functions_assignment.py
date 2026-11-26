# Define forbidden character strings for validation 
FORBIDDEN_NAME_CHARS = '!"@#$%^&*()_=+,<>/?;:[]{}\\'
FORBIDDEN_EMAIL_CHARS = '!"\'#$%^&*()=+,<>/?;:[]{}\\'
FORBIDDEN_ADDRESS_CHARS = '!"\'$%^&*_=+<>@?;:[]{}\\'

# Helper Function to Check Text Rules
def get_validated_text(prompt, forbidden_chars, error_msg, is_optional=False, letters_only=False):
    # Keep asking the user until they type a valid user
    while True:
        user_input = input(prompt)

        # Handle blank input based on whether the field is optional
        if user_input == "":
            if is_optional:
                return user_input
            print(error_msg)
            continue

        has_forbidden_char = False
        valid_char_count= 0 

        # Check every character the user typed one by one
        for char in user_input:
            if char in forbidden_chars:
                has_forbidden_char = True
                break

            # Check how many valid characters were typed
            if letters_only and char.isalpha():
                valid_char_count += 1
            elif not letters_only and char.isalnum():
                valid_char_count += 1

        # Accept the input if there are no banned symbols and more than half is valid text
        if not has_forbidden_char and valid_char_count > len(user_input) / 2:
            return user_input

        # Show an error message and ask again if the rules were broken
        print(error_msg)

# ==============================================================
# 1. Employee ID
# ==============================================================
def get_employee_id():
    while True:
        employee_id = input ("Employee ID: ")

        # Check ID validity 
        if employee_id.isdigit() and len(employee_id) <= 7:
            return employee_id
        print("Invalid Employee ID. Must be a number with 7 or fewer digits")

# ==============================================================
# 2. Employee Name
# ==============================================================
def get_employee_name():
    return get_validated_text(
        prompt="Name: ",
        forbidden_chars=FORBIDDEN_NAME_CHARS,
        error_msg="Invalid Employee Name.",
        is_optional=False,
        letters_only=True
    )

# ==============================================================
# 3. Employee Email Address
# ==============================================================
def get_employee_email():
    return get_validated_text( 
        prompt="Email Address: ",
        forbidden_chars=FORBIDDEN_EMAIL_CHARS,
        error_msg="Invalid Email Address.",
        is_optional=False,
        letters_only=False
    )

# ==============================================================
# 4. Employee Address (Optional)
# ==============================================================
def get_employee_address():
    return get_validated_text(
        prompt="Address: ",
        forbidden_chars=FORBIDDEN_ADDRESS_CHARS,
        error_msg="Invalid Address.",
        is_optional=True,
        letters_only=False
    )

# ==============================================================
# 5. Main loop to collect records for up to max_employees.
# ==============================================================
def collect_all_employees(max_employees=5):
    # An empty list to store all completed employee records
    employees = []

    while len(employees) < max_employees:
        print(f"\nEnter Information for Employee #{len(employees) + 1}")

        # Gather each piece of data using its dedicated function
        employee_record = {
            "Employee ID": get_employee_id(),
            "Employee Name": get_employee_name(),
            "Employee Email": get_employee_email(),
            "Employee Address": get_employee_address(),
        }

        # Save the finished employee record into the main list
        employees.append(employee_record)

        # Ask if the user wants to add another employee
        if len(employees) < max_employees:
            add_more = input("Would you like to enter enother employee? (y/n)").lower()
            if add_more != "y":
                break

    return employees

# ==============================================================
# Print the Final List
# ==============================================================
employee_list = collect_all_employees()

print("\n All Employee Records:")
print(employee_list)