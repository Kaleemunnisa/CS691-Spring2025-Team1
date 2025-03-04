import pandas as pd

def delete_rows_with_missing_data(csv_file, output_csv):
    """
    Reads a CSV file, deletes rows with any missing data (NaN), and saves the result to a new CSV.

    Args:
        csv_file (str): Path to the input CSV file.
        output_csv (str): Path to the output CSV file.
    """
    try:
        df = pd.read_csv(csv_file)
        df_cleaned = df.dropna()  # Drop rows with any NaN values
        df_cleaned.to_csv(output_csv, index=False)
        print(f"Rows with missing data deleted. Results saved to {output_csv}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
#input_csv_file = "input_missing.csv"  # Replace with your input CSV file path
#output_csv_file = "output_cleaned.csv" #Replace with your desired output file name

# Create a sample input_missing.csv for testing:
'''data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, None, 30, 35, 28],
        'City': ['New York', 'London', None, 'Paris', 'Tokyo']}
df_test = pd.DataFrame(data)
df_test.to_csv(input_csv_file, index=False)
'''

# input_csv_file= r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\against_filtered.csv"
# delete_rows_with_missing_data(input_csv_file, input_csv_file)

# Example with specific columns being considered.
def delete_rows_with_missing_data_specific_columns(csv_file, output_csv, columns_to_check):
    """
    Reads a CSV file, deletes rows with missing data (NaN) in specified columns, and saves the result to a new CSV.

    Args:
        csv_file (str): Path to the input CSV file.
        output_csv (str): Path to the output CSV file.
        columns_to_check (list): List of column names to check for missing data.
    """
    try:
        df = pd.read_csv(csv_file)
        df_cleaned = df.dropna(subset=columns_to_check)  # Drop rows with NaN in specific columns
        df_cleaned.to_csv(output_csv, index=False)
        print(f"Rows with missing data in specified columns deleted. Results saved to {output_csv}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except KeyError as e:
        print(f"Error: Column '{e.args[0]}' not found in the CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
'''
#Example usage with specific columns.
output_specific_columns = "output_specific_columns.csv"
columns_to_check = ['Age', 'City']
delete_rows_with_missing_data_specific_columns(input_csv_file, output_specific_columns, columns_to_check)'''