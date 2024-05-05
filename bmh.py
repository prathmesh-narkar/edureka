import pandas as pd

# Read the input Excel file
input_file = "test.xlsx"
df = pd.read_excel(input_file)
#These are b1 code changes
# Create a list to store the rows of the output
output_data = []

import pandas as pd
#this is test 1 code base dx. This is testing again
# Read the input Excel file
input_file = "test.xlsx"
df = pd.read_excel(input_file)

# Create a list to store the rows of the output
output_data = []

# Iterate through each row in the input DataFrame
for index, row in df.iterrows():
    username = row["Name"]
    email = row["Email Id"]
    departments = row[2:41].dropna().tolist()  # Get non-empty department values as a list
    months = row[41:].dropna().tolist()  # Get non-empty month values as a list

    # If departments are blank, add a None value
    if not departments:
        departments.append(None)

    # If months are blank, add a None value
    if not months:
        months.append(None)

    # Iterate through departments and months
    for department in departments:
        for month in months:
            output_data.append([username, email, department, month])

# Create a new DataFrame from the output list
result_df = pd.DataFrame(output_data, columns=["Username", "Email", "Department", "Month"])

# Write the result to a new Excel file
output_file = "output.xlsx"
result_df.to_excel(output_file, index=False)




