import rustytable

# Define headers
headers = ["Name", "Age", "City"]

# Create a table with a theme
theme = rustytable.Theme(header_color="32", row_colors=["31", "34"])
table = rustytable.Table(headers, theme, True)

# Add some data
table.add_row([
    rustytable.Cell("Alice", None, False, None, None),
    rustytable.Cell("30", None, False, None, None),
    rustytable.Cell("New York", None, False, None, None)
])
table.add_row([
    rustytable.Cell("Bob", None, False, None, None),
    rustytable.Cell("25", None, False, None, None),
    rustytable.Cell("San Francisco", None, False, None, None)
])
table.add_row([
    rustytable.Cell("Charlie", "31", True, "left", None),
    rustytable.Cell("40", None, False, "right", None),
    rustytable.Cell("Los Angeles", "34", False, "center", None)
])

# Set title and subtitle
table.set_title("Employee List")
table.set_subtitle("List of employees with their details")

# Print the table to the terminal
print(table.to_string())

# Export to CSV
csv_data = table.to_csv()
print(csv_data)

# Export to HTML
html_data = table.to_html()
print(html_data)

# Export to Markdown
md_data = table.to_markdown()
print(md_data)

# Summary statistics
print(f"Sum of Age: {table.sum('Age')}")
print(f"Average Age: {table.average('Age')}")
print(f"Min Age: {table.min('Age')}")
print(f"Max Age: {table.max('Age')}")

# Conditional formatting
table.conditional_format("City", "New York", "NYC")
print(table.to_string())

# Validate the table
try:
    table.validate()
    print("Table validation successful")
except Exception as e:
    print(f"Table validation failed: {e}")

# Load data dynamically
def fetch_data_from_api(url):
    # Simulate API data fetching
    return [
        {"Name": "Alice", "Age": "30", "City": "New York"},
        {"Name": "Bob", "Age": "25", "City": "San Francisco"},
        {"Name": "Charlie", "Age": "40", "City": "Los Angeles"}
    ]

data = fetch_data_from_api('https://api.example.com/data')
table.load_data(data)
print(table.to_string())

# Run interactive CLI
def interactive_cli():
    while True:
        print(table.to_string())
        command = input("Enter command (add, remove, sort, filter, exit): ")
        if command == "add":
            row = input("Enter row data (comma-separated): ").split(',')
            table.add_row([rustytable.Cell(cell.strip(), None, False, None, None) for cell in row])
        elif command == "remove":
            index = int(input("Enter row index to remove: "))
            table.remove_row(index)
        elif command == "sort":
            column = input("Enter column to sort by: ")
            ascending = input("Ascending? (yes/no): ").lower() == "yes"
            table.sort_by(column, ascending)
        elif command == "filter":
            column = input("Enter column to filter by: ")
            value = input("Enter value to filter: ")
            filtered_table = table.filter(column, value)
            print(filtered_table.to_string())
        elif command == "exit":
            break
        else:
            print("Invalid command")

interactive_cli()
