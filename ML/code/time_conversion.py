import pandas as pd

def convert_time_to_minutes(time_str):
    """Converts time string in 'H:MM' format to minutes."""
    try:
        parts = time_str.split(':')
        if len(parts) == 2:
            hours = int(parts[0])
            minutes = int(parts[1])
            return hours * 60 + minutes
        elif len(parts) == 1: #handle cases like just "50"
            return int(parts[0])

        else:
            return None  # Handle invalid formats
    except (ValueError, AttributeError):
        return None  # Handle cases where the input is not a string or cannot be converted

def convert_excel_time_column_to_minutes(csv_file, column_name, output_csv):
    """
    Reads a CSV file, converts a specified time column to minutes, and saves the result to a new CSV.

    Args:
        csv_file (str): Path to the input CSV file.
        column_name (str): Name of the column containing time in 'H:MM' format.
        output_csv (str): Path to the output CSV file.
    """
    try:
        df = pd.read_csv(csv_file)
        df[column_name + "_minutes"] = df[column_name].apply(convert_time_to_minutes)
        df.to_csv(output_csv, index=False)
        print(f"Conversion successful. Results saved to {output_csv}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except KeyError:
        print(f"Error: Column '{column_name}' not found in the CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#input_csv_file = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\raw_kaggle.csv"  # Replace with your input CSV file path
#time_column = "Time"  # Replace with the name of your time column
#output_csv_file = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\output.csv" #Replace with your desired output file name

# Create a sample input.csv for testing:
#data = {'Time': ['1:50', '2:30', '0:45', '10:00', '50', 'invalid']}
#df_test = pd.DataFrame(data)
#df_test.to_csv(input_csv_file, index=False)

#convert_excel_time_column_to_minutes(input_csv_file, time_column, output_csv_file)

#Example with seconds instead of minutes.
def convert_time_to_seconds(time_str):
    """Converts time string in 'H:MM' format to seconds."""
    try:
        parts = time_str.split(':')
        if len(parts) == 2:
            hours = int(parts[0])
            minutes = int(parts[1])
            return (hours * 60 + minutes) * 60
        elif len(parts) == 1: #handle cases like just "50"
            return int(parts[0]) * 60

        else:
            return None  # Handle invalid formats
    except (ValueError, AttributeError):
        return None  # Handle cases where the input is not a string or cannot be converted

def convert_excel_time_column_to_seconds(csv_file, column_name, output_csv):
    """
    Reads a CSV file, converts a specified time column to seconds, and saves the result to a new CSV.

    Args:
        csv_file (str): Path to the input CSV file.
        column_name (str): Name of the column containing time in 'H:MM' format.
        output_csv (str): Path to the output CSV file.
    """
    try:
        df = pd.read_csv(csv_file)
        df[column_name + "_seconds"] = df[column_name].apply(convert_time_to_seconds)
        df.to_csv(output_csv, index=False)
        print(f"Conversion successful. Results saved to {output_csv}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except KeyError:
        print(f"Error: Column '{column_name}' not found in the CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#output_csv_seconds = r"C:\Users\Dalyn\OneDrive - Pace University\Desktop\Capstone\ML\datasets\op.csv"
#convert_excel_time_column_to_seconds(input_csv_file, time_column, output_csv_seconds)