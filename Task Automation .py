import re
import os

def extract_emails(input_file, output_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"The file {input_file} does not exist.")
        return

    # Read the contents of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Regular expression for extracting email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    # Write the extracted emails to the output file
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"Extracted {len(emails)} email(s) to {output_file}.")

# Example usage
input_file = 'input.txt'  # Replace with your input file path
output_file = 'output_emails.txt'  # Replace with your desired output file path
extract_emails(input_file, output_file)
