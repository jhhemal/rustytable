import rustytable

def main():
    # Create a new table
    headers = ["Name", "Age", "City"]
    table = rustytable.Table(headers, None, True)

    # Add some rows
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

    # Set title and subtitle
    table.set_title("User Information")
    table.set_subtitle("A table displaying user data")

    # Add a column
    table.add_column("Country", "USA")

    # Add a row with the new column
    table.add_row([
        rustytable.Cell("Charlie", None, False, None, None),
        rustytable.Cell("40", None, False, None, None),
        rustytable.Cell("Los Angeles", None, False, None, None),
        rustytable.Cell("USA", None, False, None, None)
    ])

    # Remove a column
    table.remove_column(3)

    # Sort by Age
    table.sort_by("Age", True)

    # Print table in different formats
    print("Table as string:")
    print(table.to_string())

    print("\nTable as CSV:")
    print(table.to_csv())

    print("\nTable as HTML:")
    print(table.to_html())

    print("\nTable as Markdown:")
    print(table.to_markdown())

    # Calculate summary statistics
    print(f"\nSum of Age: {table.sum('Age')}")
    print(f"Average Age: {table.average('Age')}")
    print(f"Min Age: {table.min('Age')}")
    print(f"Max Age: {table.max('Age')}")

    # Apply conditional formatting
    table.conditional_format("City", "New York", "NYC")
    print("\nTable after conditional formatting (City = New York to NYC):")
    print(table.to_string())

    # Filter the table
    filtered_table = table.filter("City", "NYC")
    print("\nFiltered table (City = NYC):")
    print(filtered_table.to_string())

    # Paginate the table
    pages = table.paginate(2)
    for i, page in enumerate(pages, start=1):
        print(f"\nPage {i}:")
        print(page.to_string())

    # Set a theme
    theme = rustytable.Theme(header_color="32", row_colors=["31", "34"])
    table.set_theme(theme)
    print("\nTable with theme applied:")
    print(table.to_string())

    # Load data dynamically
    data = [
        {"Name": "Alice", "Age": "30", "City": "New York"},
        {"Name": "Bob", "Age": "25", "City": "San Francisco"},
        {"Name": "Charlie", "Age": "40", "City": "Los Angeles"}
    ]
    table.load_data(data)
    print("\nTable after loading data dynamically:")
    print(table.to_string())

if __name__ == "__main__":
    main()
