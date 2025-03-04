def print_to_note_file(output_data, filename="output.txt"):
    """
    Prints the given output data to a specified text file.

    Args:
        output_data: The data to be printed (can be a string, list, dictionary, etc.).
        filename (str): The name of the file to write to. Defaults to "output.txt".
    """
    try:
        with open(filename, "w") as file:  # "w" mode overwrites existing content
            if isinstance(output_data, (list, tuple, set)):
                for item in output_data:
                    file.write(str(item) + "\n")  # Write each item on a new line
            elif isinstance(output_data, dict):
                for key, value in output_data.items():
                    file.write(f"{key}: {value}\n") #Write each key value pair on a new line.
            else:
                file.write(str(output_data)) #If it is not a list, dict, or tuple, write it directly.

        print(f"Output written to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_note_file(output_data, filename="output.txt"):
    """
    Appends the given output data to a specified text file.

    Args:
        output_data: The data to be printed (can be a string, list, dictionary, etc.).
        filename (str): The name of the file to write to. Defaults to "output.txt".
    """
    try:
        with open(filename, "a") as file:  # "a" mode appends to existing content
            if isinstance(output_data, (list, tuple, set)):
                for item in output_data:
                    file.write(str(item) + "\n")
            elif isinstance(output_data, dict):
                for key, value in output_data.items():
                    file.write(f"{key}: {value}\n")
            else:
                file.write(str(output_data))

        print(f"Output appended to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

# # Example Usage:
# data_to_write = "This is some output data."
# print_to_note_file(data_to_write)

# list_data = ["item1", "item2", "item3"]
# print_to_note_file(list_data, "my_list_output.txt")

# dict_data = {"name": "John Doe", "age": 30, "city": "New York"}
# print_to_note_file(dict_data, "my_dict_output.txt")

# append_data = "This is more data to append."
# append_to_note_file(append_data)

# append_list = ["append_item1", "append_item2"]
# append_to_note_file(append_list)