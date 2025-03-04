import pandas as pd
import re

def extract_second_name(name_list):
    """
    Extracts the second name from a list of strings in the format ['(1)Sinner', '(4)NovakDjokovic[SRB]'].

    Args:
        name_list (list): A list of strings.

    Returns:
        str: The extracted second name, or None if not found or an error occurs.
    """
    if not isinstance(name_list, list) or len(name_list) < 2:
        return None

    second_name_str = name_list[1]
    match = re.search(r'\)\s*([A-Za-z\s]+)(?:\[[A-Z]{3}\])?', second_name_str) #Regex to find the name
    if match:
        return match.group(1).strip()
    else:
        return None

def extract_second_name_from_column(csv_file, column_name, output_csv, output_column_name="Against_name"):
    """
    Reads a CSV file, extracts the second name from a specified column, and saves the result to a new CSV.

    Args:
        csv_file (str): Path to the input CSV file.
        column_name (str): Name of the column containing the lists of names.
        output_csv (str): Path to the output CSV file.
        output_column_name (str): Name of the new column for extracted names.
    """
    try:
        df = pd.read_csv(csv_file)
        df[output_column_name] = df[column_name].apply(eval).apply(extract_second_name) #eval to convert string list to list.
        df.to_csv(output_csv, index=False)
        print(f"Second names extracted. Results saved to {output_csv}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except KeyError:
        print(f"Error: Column '{column_name}' not found in the CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# input_csv_file = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\raw_kaggle.csv"
# output_csv_file = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\against_filtered.csv"

# # Create a sample input_names_list.csv for testing:
# data = {'against': ["['(1)Sinner', '(4)NovakDjokovic[SRB]']", "['(2)Alcaraz', '(3)Medvedev']", "['(5)Rublev', '(10)Tiafoe']"]}
# df_test = pd.DataFrame(data)
# df_test.to_csv(input_csv_file, index=False)

# extract_second_name_from_column(input_csv_file, "against", output_csv_file)