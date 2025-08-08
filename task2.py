# Task 2: Write and Append Data to a File

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data + "\n")

def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + "\n")

def read_file(filename):
    with open(filename, 'r') as file:
        print("Final content of the file:")
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    filename = "output.txt"
    
    user_input_1 = input("Enter initial data to write to the file: ")
    write_to_file(filename, user_input_1)

    user_input_2 = input("Enter additional data to append: ")
    append_to_file(filename, user_input_2)

    read_file(filename)
