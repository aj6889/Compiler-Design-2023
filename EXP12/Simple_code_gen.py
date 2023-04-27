def generate_machine_instructions(three_address_code):
    machine_instructions = []
    for instruction in three_address_code:
        op = instruction[0]
        arg1 = instruction[1]
        arg2 = instruction[2]
        result = instruction[3]

        if op == '+':
            machine_instructions.append(f"ADD {arg1}, {arg2}, {result}")
        elif op == '-':
            machine_instructions.append(f"SUB {arg1}, {arg2}, {result}")
        elif op == '*':
            machine_instructions.append(f"MUL {arg1}, {arg2}, {result}")
        elif op == '/':
            machine_instructions.append(f"DIV {arg1}, {arg2}, {result}")
        elif op == '=':
            machine_instructions.append(f"MOV {arg1}, {result}")
        else:
            raise ValueError(f"Unsupported operation: {op}")

    return machine_instructions

def read_three_address_code():
    three_address_code = []
    while True:
        instruction = input("Enter a three-address instruction (or 'done' to finish): ")
        if instruction == 'done':
            break
        parts = instruction.split()
        op = parts[1]
        arg1 = parts[0]
        arg2 = parts[2]
        result = parts[4]
        three_address_code.append((op, arg1, arg2, result))
    return three_address_code

three_address_code = read_three_address_code()

machine_instructions = generate_machine_instructions(three_address_code)

# print the generated machine instructions
print("Generated machine instructions:")
for instruction in machine_instructions:
    print(instruction)
