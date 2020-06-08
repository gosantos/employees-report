def get_adults(employees_list):
    return list(filter(lambda employee: employee['age'] >= 18, employees_list))


def get_all_employees_sorted_by_name(given_employees):
    return sorted(given_employees, key=lambda k: k['name'], reverse=True)


def capitalize_employee_names(given_employees):
    return list(map(lambda employee: {'name': employee['name'].upper(), 'age': employee['age']}, given_employees))


employees = [
    {'name': 'Max', 'age': 17},
    {'name': 'Sepp', 'age': 18},
    {'name': 'Nina', 'age': 15},
    {'name': 'Mike', 'age': 51},
]

adults = get_adults(employees)
adults_sorted_by_name = get_all_employees_sorted_by_name(adults)
employee_names = capitalize_employee_names(adults_sorted_by_name)

print(employee_names)
