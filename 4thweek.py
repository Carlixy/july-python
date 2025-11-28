#Ask the user for the input filename
filename = input("Enter the filename to read: ")

try:
    # Try to open the file for reading
    with open(filename, "r") as file:
        content = file.read()
    
    # Example modification: convert text to uppercase
    modified_content = content.upper()
    
    # Create a new file to write the modified content
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"Modified content written to {new_filename}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' cannot be read or written.")
