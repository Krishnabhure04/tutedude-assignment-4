# Task 1: Read a File and Handle Errors

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

if __name__ == "__main__":
    read_file("sample.txt")
