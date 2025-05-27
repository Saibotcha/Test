# demo: read and print contents of a file

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_file("sample.txt")
