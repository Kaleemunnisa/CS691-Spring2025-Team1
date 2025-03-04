import pandas as pd

def filter_rows_by_names(csv_file, output_csv, names_to_keep, name_column="Name"):
    """
    Reads a CSV file, keeps rows where the 'Name' column matches names in the provided list, and saves the result.

    Args:
        csv_file (str): Path to the input CSV file.
        output_csv (str): Path to the output CSV file.
        names_to_keep (list): List of names to keep.
        name_column (str): Name of the column containing names.
    """
    try:
        df = pd.read_csv(csv_file)
        df_filtered = df[df[name_column].isin(names_to_keep)]
        df_filtered.to_csv(output_csv, index=False)
        print(f"Rows filtered. Results saved to {output_csv}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except KeyError:
        print(f"Error: Column '{name_column}' not found in the CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

'''
# Example usage:
input_csv_file = "input_names.csv"  # Replace with your input CSV file path
output_csv_file = "output_filtered.csv" #Replace with your desired output file name
names = ["Novak", "Nadal"]

# Create a sample input_names.csv for testing:
data = {'Name': ['Novak', 'Federer', 'Nadal', 'Murray', 'Novak', 'Djokovic'],
        'Score': [10, 8, 9, 7, 12, 11]}
df_test = pd.DataFrame(data)
df_test.to_csv(input_csv_file, index=False)

filter_rows_by_names(input_csv_file, output_csv_file, names)
'''

'''
#Example with a different column name
output_csv_different_column = "output_different_column.csv"
data_different_column = {'Players': ['Novak', 'Federer', 'Nadal', 'Murray', 'Novak', 'Djokovic'],
        'Score': [10, 8, 9, 7, 12, 11]}
df_test_different_column = pd.DataFrame(data_different_column)
df_test_different_column.to_csv("input_players.csv", index=False)

filter_rows_by_names("input_players.csv", output_csv_different_column, names, "Players")
'''