# 
#
employee_id = input ("Employee ID: ")


if not employee_id.isdigit() or len(employee_id) > 7:
    print("Invalid Employee ID. Must be a number with 7 or fewer digits")
    exit 

employee_name = input ("Name: ").strip()
forbidden_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\).'

for char in employee_name:
    if char in forbidden_chars:
        print("Invalid Employee Name.")
        exit
    if char.isalpha():
        letter_count = letter_count +  1

# Check if more than half of the characters are letters
if letter_count <= len(employee_name) / 2:
    print("Invalid Employee Name.")
    exit

# 3. Employee Email Address
employee_email = input("Email Address: ")
forbidden_email_chars = '!"\'#$%^&*()=+,<>/?;:[]{}\).'


