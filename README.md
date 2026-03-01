# 🏨 Hotel Management System — Python GUI & MySQL Database

A simple and elegant **Hotel Management System** built with **Python (Tkinter)** and **MySQL** that allows hotel staff to manage guest records through an intuitive desktop GUI application. Perform full **CRUD operations** — Create, Read, Update, and Delete guest data — with real-time database connectivity.

---

##  Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Database Schema](#-database-schema)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Demo Video](#-demo-video)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Insert Data** | Add new guest records (GuestID, Name, Number, City, Room) to the database |
| **Update Data** | Modify existing guest information by GuestID |
| **Delete Data** | Remove a guest record from the database using GuestID |
| **Select / View Data** | View all guest records in a clean tabular format using Treeview |
| **Clear Fields** | Reset all input fields with a single click |
| **Error Handling** | User-friendly error messages and input validations |
| **Real-time DB Sync** | All changes are instantly committed to the MySQL database |

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **Tkinter** | GUI framework for the desktop interface |
| **ttk (Treeview)** | Tabular data display widget |
| **MySQL** | Relational database for persistent data storage |
| **mysql-connector-python** | Python-MySQL database driver |

---

## 🗄 Database Schema

The application uses a MySQL database named `db` with a single `users` table:

```sql
CREATE DATABASE db;
USE db;

CREATE TABLE users (
    GuestID  VARCHAR(20)  PRIMARY KEY,
    Name     VARCHAR(100),
    Number   VARCHAR(15),
    City     VARCHAR(50),
    Room     VARCHAR(10)
);
```

| Column | Data Type | Constraint | Description |
|--------|-----------|------------|-------------|
| `GuestID` | `VARCHAR(20)` | `PRIMARY KEY` | Unique identifier for each guest |
| `Name` | `VARCHAR(100)` | — | Full name of the guest |
| `Number` | `VARCHAR(15)` | — | Contact phone number |
| `City` | `VARCHAR(50)` | — | City of residence |
| `Room` | `VARCHAR(10)` | — | Assigned room number |

---

## 📁 Project Structure

```
Hotel-Management-System-Using-python-GUI/
│
├── Hotel Management System Using python GUI.py   # Main application source code
├── Hotel Management System Using python GUI.sql  # MySQL database setup script
├── Photo of Hotel Management System.png          # Application screenshot
├── Demo Video of Hotel Management System.gif     # Animated demo of the application
├── Demo Video of Hotel Management System.mp4     # Video demo of the application
└── README.md                                     # Project documentation
```

---

## 📋 Prerequisites

Before running the project, make sure you have the following installed:

1. **Python 3.x** — [Download Python](https://www.python.org/downloads/)
2. **MySQL Server** — [Download MySQL](https://dev.mysql.com/downloads/mysql/)
3. **mysql-connector-python** — Python library to connect with MySQL

Install the MySQL connector via pip:

```bash
pip install mysql-connector-python
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Hotel-Management-System-Using-python-GUI.git
cd Hotel-Management-System-Using-python-GUI
```

### 2. Set Up the MySQL Database

Open **MySQL Workbench** or the **MySQL command-line client** and run the SQL script:

```bash
mysql -u root -p < "Hotel Management System Using python GUI.sql"
```

Or manually execute the following SQL commands:

```sql
CREATE DATABASE db;
USE db;

CREATE TABLE users (
    GuestID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Number VARCHAR(15),
    City VARCHAR(50),
    Room VARCHAR(10)
);
```

### 3. Configure Database Credentials

Open `Hotel Management System Using python GUI.py` and update the connection details on **line 7**:

```python
con = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",     # Replace with your MySQL username
    password="your_mysql_password", # Replace with your MySQL password
    database="db"                   # Database name (must match the SQL script)
)
```

### 4. Run the Application

```bash
python "Hotel Management System Using python GUI.py"
```

The GUI window will launch, and you'll see **"Database is Connected"** printed in the console if the connection is successful.

---

## 💡 Usage

1. **Insert a Guest Record**
   - Fill in all the fields: GuestID, Name, Number, City, and Room.
   - Click **"Insert Data"** to save the record to the database.

2. **Update a Guest Record**
   - Enter the **GuestID** of the record you want to modify.
   - Update the other fields as needed.
   - Click **"Update Data"** to apply the changes.

3. **View All Guest Records**
   - Click **"Select Data"** to open a new window displaying all records in a table format.

4. **Delete a Guest Record**
   - Enter the **GuestID** of the record to be removed.
   - Click **"Delete Data"** to permanently remove the record.

5. **Clear Input Fields**
   - Click **"Clear Fields"** to reset all entry boxes.

---

## ⚙ How It Works

### Architecture Overview

```
┌──────────────────────────────┐
│       Tkinter GUI Layer      │
│  (Labels, Entry, Buttons)    │
├──────────────────────────────┤
│    Application Logic Layer   │
│  (insert, update, delete,    │
│   select, clear functions)   │
├──────────────────────────────┤
│   mysql.connector Driver     │
│  (Database Communication)    │
├──────────────────────────────┤
│      MySQL Database          │
│   (db → users table)         │
└──────────────────────────────┘
```

### Code Breakdown

| Function | Description |
|----------|-------------|
| `insert_data()` | Collects input from entry fields and inserts a new row into the `users` table |
| `update_data()` | Updates an existing record identified by `GuestID` with new field values |
| `delete_data()` | Deletes the record matching the provided `GuestID` |
| `select_data()` | Fetches all records from the `users` table and displays them in a `Treeview` popup |
| `clear_fields()` | Clears all five entry fields in the GUI |

### GUI Components

- **5 Label–Entry pairs** for `GuestID`, `Name`, `Number`, `City`, and `Room`
- **5 Buttons**: Insert Data, Update Data, Select Data, Delete Data, Clear Fields
- **Treeview popup** (via `Toplevel`) for displaying tabular guest data
- **MessageBox dialogs** for success, error, and warning notifications

---

## 📸 Screenshots

![Hotel Management System Screenshot](https://github.com/ArokiyaNithish/Hotel-Management-System-using-PythonGUI/blob/main/images/image1.png)

---

## 🎬 Demo Video



https://github.com/user-attachments/assets/f2280221-159b-4deb-bcfa-b50cd880d4c6



---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/new-feature`)
3. **Commit** your changes (`git commit -m "Add new feature"`)
4. **Push** to the branch (`git push origin feature/new-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

```
MIT License

Copyright (c) 2026 Arokiya Nithish J

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

---

# 👨‍💻 Author & Contact

**Arokiya Nithish J**

- GitHub: [ @ArokiyaNithish](https://github.com/ArokiyaNithish)
- LinkedIn: [ @Arokiya Nithish J](https://www.linkedin.com/in/arokiya-nithishj/)
- Email ID :  @arokiyanithishj@gmail.com
- My Portfoilio :[ @Arokiya Nithish](arokiyanithish.github.io/portfolio/)

## 📞 Support

For support, email @arokiyanithishj@gmail.com or create an issue in the GitHub repository.

---

**⭐ If you find this project useful, please consider giving it a star!**
