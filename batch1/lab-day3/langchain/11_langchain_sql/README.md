# SQL Database Setup for LangChain Project

This guide provides instructions on how to set up either an SQLite or a MySQL database for use with this project. The project uses the Chinook sample database.

## Option 1: SQLite Setup

SQLite is a lightweight, file-based database. It's the quickest way to get started.

### 1. Download SQLite

-   **Windows/macOS/Ubuntu**: Download the appropriate command-line tools for your operating system from the official website:
    [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)

### 2. Create and Load the Database

Open your terminal or command prompt, navigate to your project directory, and run the following commands.

```bash
# Create a new database file named 'Chinook.db' and open the SQLite shell
sqlite3 Chinook.db

# Inside the SQLite shell, load the data from the SQL script
# (Assuming you have a 'Chinook_Sqlite.sql' file)
.read Chinook_Sqlite.sql

# Exit the SQLite shell
.exit
```

### 3. Test the Database

You can quickly test if the data was loaded correctly:

```bash
# Open the database again
sqlite3 Chinook.db

# Run a query to select from the 'albums' table
SELECT * FROM albums LIMIT 5;

# Exit
.exit
```

---

## Option 2: MySQL Setup (for macOS)

For a more robust, server-based database, you can use MySQL. These instructions are for macOS using Homebrew.

### 1. Install MySQL

```bash
# Install MySQL using Homebrew
brew install mysql
```

### 2. Start and Secure MySQL

```bash
# Start the MySQL service
brew services start mysql

# Check the status of the service (optional)
brew services list

# Run the secure installation script to set a root password and apply security settings
mysql_secure_installation
```
Follow the on-screen prompts to set your root password and configure security options.

### 3. Create and Load the Database

Log in to MySQL and create the `chinook` database.

```bash
# Log in to MySQL as the root user
mysql -u root -p
```

Once you are logged into the MySQL shell, run the following SQL commands:

```sql
-- Create the database
CREATE DATABASE chinook;

-- Switch to the new database
USE chinook;

-- Load the data from the SQL script
-- (Assuming you have a 'Chinook_MySql.sql' file in the directory where you started mysql)
SOURCE Chinook_MySql.sql;
```

### 4. Test the Database

While still in the MySQL shell, you can test if the data was loaded correctly:

```sql
-- Select a few records from the albums table
SELECT * FROM albums LIMIT 10;

-- Exit the MySQL shell
exit;
```

## Project Dependencies

To run the Python notebook (`langchain_sql.ipynb`), you will need to install the following packages:

```bash
pip install langchain-community langchain-openai mysql-connector-python
```