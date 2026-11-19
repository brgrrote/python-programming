<<<<<<< HEAD
# 1: Create a single list containing the given employe data
data = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

# 2: Separate the data into three lists without duplicates
employee_id = []
employee_name = []
hourly_wage = []

for item in data:
    if isinstance(item, bool):
        continue
    elif isinstance(item, int) and item not in employee_id:
        employee_id.append(item)
    elif isinstance(item, str) and item not in employee_name:
        employee_name.append(item)
    elif isinstance(item, float) and item not in hourly_wage:
        hourly_wage.append(item)

print("Employee ID: ", employee_id)
print("Employee Name: ", employee_name)
print("Hourly Wages: ", hourly_wage)

# 3: Calculate total hourly rates with benefits
total_hourly_rate = []

for salary in hourly_wage:
    total_rate = salary * 1.3
    total_hourly_rate.append(total_rate)

print("\nTotal Hourly Rates: ", total_hourly_rate)

# 4: Find the maximum total hourly rate and check the budget
maximum_rate = max(total_hourly_rate)
print("Maximum Total Hourly rate: ", maximum_rate)

if maximum_rate > 37.30:
    print("WARNING: Someone's salary may be a budget concern.")

# 5: Find total hourly rates between 28.15 and 30.65
underpaid_salaries = []

for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("\nUnderpaid Salaries: ", underpaid_salaries)
company_raises = []

# 6: Calculate employee raises based on their original hourly wages
for salary in hourly_wage:
    if salary >=22 and salary <= 24:
        new_salary = salary * 1.05

    elif salary >= 24 and salary <= 26:
        new_salary = salary * 1.04

    elif salary >= 26 and salary <= 28:
            new_salary = salary * 1.03

    else:
        new_salary = salary * 1.02

    company_raises.append(new_salary)

print("\nCompany Raises: ", company_raises)

# 7: Create a complex condition with at least four truth tests
# The company celebrates if: 
# 1. The maximum total hourly rate is below 40
# 2. At least 5 unique employee numbers
# 3. At 5 different hourly wages, 
# 4. At least one is listed as underpaid

if maximum_rate < 40 and len(employee_id) >= 5 and len(hourly_wage) >=5 and len(underpaid_salaries) > 0:
    print("\nYay! The company will be celebrating with pizza!")
else:
=======
# 1: Create a single list containing the given employe data
data = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

# 2: Separate the data into three lists without duplicates
employee_id = []
employee_name = []
hourly_wage = []

for item in data:
    if isinstance(item, bool):
        continue
    elif isinstance(item, int) and item not in employee_id:
        employee_id.append(item)
    elif isinstance(item, str) and item not in employee_name:
        employee_name.append(item)
    elif isinstance(item, float) and item not in hourly_wage:
        hourly_wage.append(item)

print("Employee ID: ", employee_id)
print("Employee Name: ", employee_name)
print("Hourly Wages: ", hourly_wage)

# 3: Calculate total hourly rates with benefits
total_hourly_rate = []

for salary in hourly_wage:
    total_rate = salary * 1.3
    total_hourly_rate.append(total_rate)

print("\nTotal Hourly Rates: ", total_hourly_rate)

# 4: Find the maximum total hourly rate and check the budget
maximum_rate = max(total_hourly_rate)
print("Maximum Total Hourly rate: ", maximum_rate)

if maximum_rate > 37.30:
    print("WARNING: Someone's salary may be a budget concern.")

# 5: Find total hourly rates between 28.15 and 30.65
underpaid_salaries = []

for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("\nUnderpaid Salaries: ", underpaid_salaries)
company_raises = []

# 6: Calculate employee raises based on their original hourly wages
for salary in hourly_wage:
    if salary >=22 and salary <= 24:
        new_salary = salary * 1.05

    elif salary >= 24 and salary <= 26:
        new_salary = salary * 1.04

    elif salary >= 26 and salary <= 28:
            new_salary = salary * 1.03

    else:
        new_salary = salary * 1.02

    company_raises.append(new_salary)

print("\nCompany Raises: ", company_raises)

# 7: Create a complex condition with at least four truth tests
# The company celebrates if: 
# 1. The maximum total hourly rate is below 40
# 2. At least 5 unique employee numbers
# 3. At 5 different hourly wages, 
# 4. At least one is listed as underpaid

if maximum_rate < 40 and len(employee_id) >= 5 and len(hourly_wage) >=5 and len(underpaid_salaries) > 0:
    print("\nYay! The company will be celebrating with pizza!")
else:
>>>>>>> b17c380284ed46537583abf047d91d12fea256af
    print("\nAww, the company will stay on serious mode and no pizza for you.")