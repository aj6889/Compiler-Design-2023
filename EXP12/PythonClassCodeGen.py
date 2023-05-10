# Python Class Code Generator

# 1. Take user inputs for the name of the class and the number of fields.
class_name = input("Enter the name of your class: ")
num_fields = int(input("Enter the number of fields for your class: "))

# 2. Initialize an empty list called `fields`.
fields = []

# 3. Loop through the range of the number of fields:
for i in range(num_fields):
    # 3.1. Take user inputs for the name and type of each field.
    field_name = input(f"Enter name for field {i+1}: ")
    field_type = input(f"Enter type for field {i+1}: ")
    # 3.2. Append a tuple containing the field name and type to the `fields` list.
    fields.append((field_name, field_type))

# 4. Use string formatting to generate the code for the class, including the `__init__`, `__str__`, and `__repr__` methods. Store the generated code in a variable called `code`.
code = f'''class {class_name}:
    def __init__(self, {", ".join([f"{field[0]}: {field[1]}" for field in fields])}):
        {"        ".join([f"self.{field[0]} = {field[0]}\n" for field in fields])}

    def __str__(self):
        return " | ".join([f"{field[0]}: {{self.{field[0]}}}" for field in fields])

    def __repr__(self):
        return str(self)

'''

# 5. Print the generated code to the console.
print("Generated code:")
print(code)
