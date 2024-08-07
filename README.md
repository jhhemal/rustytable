
# RustyTable

**RustyTable** is a high-performance, feature-rich table formatting library for Python, built using Rust for maximum efficiency. It offers a variety of functionalities to create, format, and manipulate tables for different output formats, including plain text, CSV, HTML, and Markdown.

## Features

- Add and remove rows and columns
- Sort and filter data
- Apply themes for better readability
- Export tables to CSV, HTML, and Markdown formats
- Compute summary statistics (sum, average, min, max)
- Conditional formatting
- Paginate large tables

## Installation

You can install RustyTable from PyPI using pip:

```sh
pip install rustytable
```

## Usage

Here are detailed usage examples for all the features provided by RustyTable.

### 1. Creating a Table

```python
from rustytable import Table, Cell, Theme

headers = ["Name", "Age", "City"]
table = Table(headers, None, True)

# Add some rows
table.add_row([
    Cell("Alice", None, False, None, None),
    Cell("30", None, False, None, None),
    Cell("New York", None, False, None, None)
])
table.add_row([
    Cell("Bob", None, False, None, None),
    Cell("25", None, False, None, None),
    Cell("San Francisco", None, False, None, None)
])

# Set title and subtitle
table.set_title("User Information")
table.set_subtitle("A table displaying user data")
```

Output:
```
User Information
A table displaying user data
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Alice         | 30            | New York      |
| Bob           | 25            | San Francisco |
+---------------+---------------+---------------+
```

### 2. Adding and Removing Columns

```python
# Add a column
table.add_column("Country", "USA")

# Add a row with the new column
table.add_row([
    Cell("Charlie", None, False, None, None),
    Cell("35", None, False, None, None),
    Cell("Los Angeles", None, False, None, None),
    Cell("USA", None, False, None, None)
])

# Remove a column
table.remove_column(3)  # Remove the "Country" column
```

Output:
```
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Alice         | 30            | New York      |
| Bob           | 25            | San Francisco |
| Charlie       | 35            | Los Angeles   |
+---------------+---------------+---------------+
```

### 3. Exporting Tables

```python
# Export to CSV
csv_data = table.to_csv()

# Export to HTML
html_data = table.to_html()

# Export to Markdown
markdown_data = table.to_markdown()

# Print table as a string
print(table.to_string())
```

Output:
CSV:
```
Name,Age,City
Alice,30,New York
Bob,25,San Francisco
Charlie,35,Los Angeles
```

HTML:
```html
<table>
<caption>User Information</caption>
<thead>
<tr><th>Name</th><th>Age</th><th>City</th></tr>
</thead>
<tbody>
<tr><td>Alice</td><td>30</td><td>New York</td></tr>
<tr><td>Bob</td><td>25</td><td>San Francisco</td></tr>
<tr><td>Charlie</td><td>35</td><td>Los Angeles</td></tr>
</tbody>
</table>
```

Markdown:
```
| Name | Age | City |
| --- | --- | --- |
| Alice | 30 | New York |
| Bob | 25 | San Francisco |
| Charlie | 35 | Los Angeles |
```

### 4. Setting Title and Subtitle

```python
table.set_title("Employee Details")
table.set_subtitle("Detailed Information")
```

Output:
```
Employee Details
Detailed Information
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Alice         | 30            | New York      |
| Bob           | 25            | San Francisco |
| Charlie       | 35            | Los Angeles   |
+---------------+---------------+---------------+
```

### 5. Statistical Functions

```python
sum_age = table.sum("Age")
avg_age = table.average("Age")
min_age = table.min("Age")
max_age = table.max("Age")
```

Output:
```
Sum of ages: 90
Average age: 30.0
Minimum age: 25
Maximum age: 35
```

### 6. Conditional Formatting

```python
table.conditional_format("City", "San Francisco", "SF")
```

Output:
```
Employee Details
Detailed Information
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Alice         | 30            | New York      |
| Bob           | 25            | SF            |
| Charlie       | 35            | Los Angeles   |
+---------------+---------------+---------------+
```

### 7. Sorting and Filtering

```python
# Sorting
table.sort_by("Age", ascending=True)

# Filtering
filtered_table = table.filter("City", "SF")
```

Output (Sorting):
```
Employee Details
Detailed Information
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Bob           | 25            | SF            |
| Alice         | 30            | New York      |
| Charlie       | 35            | Los Angeles   |
+---------------+---------------+---------------+
```

Output (Filtering):
```
Employee Details
Detailed Information
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Bob           | 25            | SF            |
+---------------+---------------+---------------+
```

### 8. Pagination

```python
paginated_tables = table.paginate(2)
```

Output:
```
Page 1:
Employee Details
Detailed Information
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Bob           | 25            | SF            |
| Alice         | 30            | New York      |
+---------------+---------------+---------------+

Page 2:
Employee Details
Detailed Information
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Charlie       | 35            | Los Angeles   |
+---------------+---------------+---------------+
```

### 9. Theming

```python
theme = Theme(header_color="32", row_colors=["31", "34"])
table.set_theme(theme)
print("
Table with theme applied:")
print(table.to_string())
```

Output:
```
Table with theme applied:
Employee Details
Detailed Information
+---------------+---------------+---------------+
| [32mName          | [32mAge           | [32mCity          |
+---------------+---------------+---------------+
| [31mBob           | [31m25            | [31mSF            |
| [34mAlice         | [34m30            | [34mNew York      |
| [31mCharlie       | [31m35            | [31mLos Angeles   |
+---------------+---------------+---------------+
```

### 10. Dynamic Data Loading

```python
data = [
    {"Name": "Alice", "Age": "30", "City": "New York"},
    {"Name": "Bob", "Age": "25", "City": "San Francisco"},
    {"Name": "Charlie", "Age": "40", "City": "Los Angeles"}
]
table.load_data(data)
print("
Table after loading data dynamically:")
print(table.to_string())
```

Output:
```
Table after loading data dynamically:
Employee Details
Detailed Information
+---------------+---------------+---------------+
| Name          | Age           | City          |
+---------------+---------------+---------------+
| Alice         | 30            | New York      |
| Bob           | 25            | San Francisco |
| Charlie       | 40            | Los Angeles   |
+---------------+---------------+---------------+
```

## Contributing

We welcome contributions to RustyTable! If you'd like to contribute, please fork the repository and submit a pull request.

## License

RustyTable is licensed under the MIT License. See the LICENSE file for more information.

## Contact

For any questions or feedback, feel free to reach out to the maintainer at [jhhemalusa@gmail.com](mailto:jhhemalusa@gmail.com).

---

Enjoy using RustyTable for all your table formatting needs!
