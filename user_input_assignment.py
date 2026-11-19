# Start the program
program_running = True

# Ask for Employee ID
employee_id = input("Employee ID: ")

# Validate Employee ID
if employee_id.isdigit() and len(employee_id) <= 7:
    pass 
else:
    print("Invalid Employee ID.")
    exit()

# Ask for Employee Name
employee_name = input("Name: ")

invalid_chars = '!"@#$%^&*()_=+,<>/?;:[]{}\).'

# Validate Employee Name (required)

