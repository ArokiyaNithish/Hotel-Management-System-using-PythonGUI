<div align="center">

# 🏨 Hotel Management System Using python GUI

### *Python Desktop GUI & MySQL Database Application*

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-brightgreen?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> 🚀 **A simple and elegant desktop application** to manage hotel guest records. Perform full **CRUD operations** — Create, Read, Update, and Delete guest data — with real-time MySQL database connectivity.

</div>

---

## 📋 Table of Contents

- [📌 Problem Statement](#-problem-statement)
- [💡 Solution & Approach](#-solution--approach)
- [🎯 Objectives](#-objectives)
- [🗄️ Database Schema](#️-database-schema)
- [🛠️ Technology Stack](#️-technology-stack)
- [📦 Libraries & Dependencies](#-libraries--dependencies)
- [📁 Project Structure](#-project-structure)
- [🔬 How It Works — Architecture](#-how-it-works--architecture)
- [🚀 Installation & Setup](#-installation--setup)
- [💻 Usage Guide](#-usage-guide)
- [🖥️ Desktop Interface](#️-desktop-interface)
- [🔍 Code Breakdown](#-code-breakdown)
- [🌍 Impact & Real-World Significance](#-impact--real-world-significance)
- [🖼️ Screenshots](#️-screenshots)
- [🎬 Working Prototype Video](#-working-prototype-video)
- [🚀 Future Enhancements](#-future-enhancements)
- [🤝 Open Source Contribution](#-open-source-contribution)
- [📄 License](#-license)
- [👨‍💻 Author & Acknowledgments](#-author--acknowledgments)

---

## 📌 Problem Statement

> **"Manual record-keeping in hotels is inefficient, prone to human error, and poses significant risks to data security and retrieval."**

### Background

Traditional hospitality management often relies on fragmented ledger books and manual data entry. As hotels grow, keeping track of guest information, contact details, and assigned rooms becomes increasingly complex and error-prone.

### The Core Problem

| Challenge | Description |
|-----------|-------------|
| 🔴 **Data Loss Risk** | Physical ledgers can be lost, damaged, or misplaced. |
| 🔴 **Slow Retrieval** | Searching through manual records for a specific guest ID takes too long. |
| 🔴 **Data Redundancy** | Higher chance of duplicate entries and inconsistent data formatting. |
| 🔴 **Inefficient Updates** | Modifying details for an existing guest is messy and unstructured. |

---

## 💡 Solution & Approach

### Our Strategy

We built a **desktop-based GUI application** that systematically digitizes guest data management:

1. **Intuitive Interface → Python Tkinter** for a simple, accessible staff dashboard
2. **Persistent Storage → MySQL Database** to securely store guest details
3. **Data Display → ttk Treeview** for clean tabular representation of records
4. **Seamless Integration → mysql-connector-python** to link the front-end with the back-end

---

## 🎯 Objectives

- ✅ **Build an interactive user interface** for hotel staff
- ✅ **Implement robust CRUD functionalities** to manage guest registers
- ✅ **Connect to a relational database** for persistent data storage
- ✅ **Provide real-time data visualization** via Treeview components
- ✅ **Incorporate error handling** and clear field toggles for usability

---

## 🗄️ Database Schema

### Database Details

The application uses a MySQL database named `db` with a single structured table `users`:

| Column | Data Type | Constraint | Description |
|--------|-----------|------------|-------------|
| `GuestID` | `VARCHAR(20)` | `PRIMARY KEY` | Unique identifier for each guest |
| `Name` | `VARCHAR(100)` | — | Full name of the guest |
| `Number` | `VARCHAR(15)` | — | Contact phone number |
| `City` | `VARCHAR(50)` | — | City of residence |
| `Room` | `VARCHAR(10)` | — | Assigned room number |

---

## 🛠️ Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Language** | Python | 3.x | Core programming language |
| **GUI Framework** | Tkinter | Built-in | Desktop interface layout |
| **Grid Data Display** | ttk (Treeview) | Built-in | Tabular viewing of database records |
| **Database** | MySQL | 8.0+ | Relational data persistence |
| **Database Driver** | mysql-connector | Latest | Python-to-MySQL communication |

---

## 📦 Libraries & Dependencies

```bash
pip install mysql-connector-python
```

---

## 📁 Project Structure

```
Hotel-Management-System-Using-python-GUI/
│
├── Hotel Management System Using python GUI.py   # Main Tkinter application code
├── Hotel Management System Using python GUI.sql  # MySQL database initialization script
├── Photo of Hotel Management System.png          # UI Screenshot
├── Demo Video of Hotel Management System.gif     # Animated demo
├── Demo Video of Hotel Management System.mp4     # Video demo
└── README.md                                     # Project documentation
```

---

## 🔬 How It Works — Architecture

### Architecture Overview

```text
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

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.x — [Download Python](https://www.python.org/downloads/)
- MySQL Server — [Download MySQL](https://dev.mysql.com/downloads/mysql/)
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/ArokiyaNithish/Hotel-Management-System-Using-python-GUI.git
cd Hotel-Management-System-Using-python-GUI
```

### 2. Set Up the MySQL Database

Open your MySQL client or MySQL Workbench and execute the setup script:

```bash
mysql -u root -p < "Hotel Management System Using python GUI.sql"
```

Or execute manually:
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

### 3. Install Dependencies

```bash
pip install mysql-connector-python
```

### 4. Configure Credentials

Open `Hotel Management System Using python GUI.py` and modify the connection details on **line 7** to match your local MySQL configuration.

```python
con = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",     
    password="your_mysql_password", 
    database="db"                   
)
```

---

## 💻 Usage Guide

### Starting the Application

Run the python script from your terminal:

```bash
python "Hotel Management System Using python GUI.py"
```

The GUI window will launch, and you'll see **"Database is Connected"** printed in the console if the connection is successful.

### Common Workflows

1. **Insert Data**: Fill all fields (GuestID, Name, Number, City, Room) and click **Insert Data**.
2. **Update Data**: Enter an existing GuestID, edit the respective fields, and click **Update Data**.
3. **Delete Data**: Enter the GuestID of the record to remove and click **Delete Data**.
4. **Select / View Data**: Click **Select Data** to pop out a window showing all registered guests in a tabular format.
5. **Clear Fields**: Click **Clear Fields** to reset all entry boxes.

---

## 🖥️ Desktop Interface

| Feature | Display/Component |
|--------|---------|
| **Input Fields** | Clearly labeled text boxes for data entry |
| **Action Buttons** | Color-coded buttons mapped to specific actions |
| **Data Viewer** | A popup Treeview grid replacing clunky console logs |
| **Feedback Dialogs** | MessageBox alerts indicating success, errors, or warnings |

---

## 🔍 Code Breakdown

### Function Breakdown

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
- **MessageBox dialogs** for smooth real-time user notification

---

## 🌍 Impact & Real-World Significance

### Practical Benefits

- ⏱ **Time Efficiency**: Eliminates the hassle of scanning through paper ledgers.
- 💾 **Data Safety**: Digital and persistent tracking prevents data losses natively.
- 🤝 **Ease of Use**: Designed to have a zero-learning-curve for non-technical hotel staff to adapt cleanly.

---

## 🖼️ Screenshots

<img width="800" alt="Hotel Management System Screenshot" src="https://github.com/ArokiyaNithish/Hotel-Management-System-using-PythonGUI/blob/main/images/image1.png" />

---

# 🎬 Working Prototype Video

https://github.com/user-attachments/assets/f2280221-159b-4deb-bcfa-b50cd880d4c6

---

## 🚀 Future Enhancements

- [ ] **Data Export**: Allow exporting the Treeview data to CSV/Excel formats.
- [ ] **Authentication**: Add a login screen to verify administrative privileges before modifications.
- [ ] **Search Filters**: Introduce searching by Name or Room without having to view the entire user table.
- [ ] **Billing Integration**: Calculate charges based on room type and stay duration.

---

## 🤝 Open Source Contribution

We warmly welcome contributions from the open source community! Whether it's **bug fixes**, **new features**, or **documentation** — every contribution helps!

### How to Contribute

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/ArokiyaNithish/Hotel-Management-System-Using-python-GUI.git

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make changes and commit
git commit -m "feat: add PDF exporter"

# 5. Push to your fork
git push origin feature/your-feature-name

# 6. Open a Pull Request on GitHub
```
---
### Reporting Issues

Please use [GitHub Issues](https://github.com/ArokiyaNithish/Hotel-Management-System-using-PythonGUI/issues) to:
- 🐛 Report bugs
- 💡 Request features
- ❓ Ask questions

---
---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

```text
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

See [LICENSE](LICENSE) for full details.

---

## 👨‍💻 Author & Acknowledgments

### Author

**Arokiya Nithish J**
- Role : Python Develeoper
- - 📅 Year: 2024
- GitHub: [@ArokiyaNithish](https://github.com/ArokiyaNithish)
- LinkedIn: [@Arokiya Nithish J](https://www.linkedin.com/in/arokiya-nithishj/)
- Email ID: @arokiyanithishj@gmail.com
- My Portfoilio: [@Arokiya Nithish](arokiyanithish.github.io/portfolio/)

### Acknowledgments

- 🐍 **Python Community** — For providing comprehensive standard libraries
- 🐬 **MySQL Documentation** — For solid foundations in relational databases
- ✨ **All contributors and testers** who helped refine this system

---

<div align="center">

For support, email @arokiyanithishj@gmail.com or create an issue in the GitHub repository.

### 🌟 If you find this project useful, please consider giving it a ⭐ Star on GitHub!

**#Python #Tkinter #MySQL #HotelManagement #GUI**

*Made with ❤️ by Arokiya Nithish*

*© 2026 — Arokiya Nithish J*

</div>
