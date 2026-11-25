Database Search and Date Processing:

A Python application that uses SQLite to search and retrieve personal records from a database.

Features:

- Automatically creates and initializes an SQLite database.
- Populates the database with predefined records.
- Searches for records using SQL `SELECT` and `LIKE` queries.
- Uses parameterized SQL queries to prevent SQL injection.
- Prevents duplicate records using `UNIQUE` constraints and `INSERT OR IGNORE`.
- Calculates ages based on birth dates.
- Validates and formats dates using Python's `datetime` module.
- Handles database errors and unexpected exceptions.

Technologies:

- Python
- SQLite
- SQL

Project Structure:

- `main.py`: Handles user interaction, database searches, age calculations, and result presentation.
- `database.py`: Creates the database, initializes the table, and inserts predefined records.

How to Run:

1. Make sure Python is installed.
2. Clone this repository.
3. Open the project directory.
4. Run the following command:

```bash
python main.py
```

The database and its initial records will be created automatically when the application runs for the first time.
