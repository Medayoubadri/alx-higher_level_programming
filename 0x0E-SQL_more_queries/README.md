
# 0x0E. SQL - More Queries

This project focuses on mastering advanced SQL queries and database management, including user privileges, constraints, multi-table data retrieval, and aggregations.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Tasks](#tasks)
5. [Installation and Usage](#installation-and-usage)

---

## Project Description
This project covers advanced SQL concepts using MySQL. You will learn how to:
- Create and manage MySQL users and their privileges.
- Work with primary and foreign keys.
- Use constraints like NOT NULL and UNIQUE.
- Query data from multiple tables using JOINs and subqueries.
- Implement database normalization and design principles.

---

## Learning Objectives
At the end of this project, you should be able to explain:
- How to create a new MySQL user.
- How to manage user privileges for a database or table.
- What primary and foreign keys are.
- How to use NOT NULL and UNIQUE constraints.
- How to retrieve data from multiple tables in one query.
- The use of subqueries, JOINs, and UNIONs.

---

## Requirements
- **Environment**: Ubuntu 20.04 LTS, MySQL 8.0 (version 8.0.25).
- **Editors**: vi, vim, emacs.
- **Coding Standards**: All SQL keywords must be in uppercase (e.g., `SELECT`, `WHERE`).
- **File Format**: Each SQL file must start with a comment describing the task and end with a newline.

---

## Installation and Usage
1. Install MySQL 8.0 on your system:
   ```bash
   sudo apt update
   sudo apt install mysql-server
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/medayoubadri/alx-higher_level_programming.git
   ```
3. Navigate to the project directory:
   ```bash
   cd alx-higher_level_programming/0x0E-SQL_more_queries
   ```
4. Execute SQL scripts using the MySQL CLI:
   ```bash
   mysql -uroot -p <database_name> < script.sql
   ```

---

## Tasks
1. **My Privileges!**: List all privileges for specific MySQL users.
2. **Root User**: Create a MySQL user with all privileges.
3. **Read User**: Create a user with SELECT privileges.
4. **Always a Name**: Create a table with a NOT NULL constraint.
5. **ID Can't Be Null**: Create a table with a default value for the ID column.
6. **Unique ID**: Create a table with a unique ID.
7. **States Table**: Create a table for states with an auto-incremented primary key.
8. **Cities Table**: Create a table for cities with a foreign key referencing states.
9. **Cities of California**: List all cities in California.
10. **Cities by States**: List all cities and their corresponding states.
11. **Genre ID by Show**: List [shows](/assets/hbtn_0d_tvshows.sql) with at least one genre.
12. **No Genre**: List [shows](/assets/hbtn_0d_tvshows.sql) without any genre.
13. **Number of Shows by Genre**: Count [shows](/assets/hbtn_0d_tvshows.sql) for each genre.
14. **My Genres**: List all genres for the show 'Dexter'.
15. **Only Comedy**: List all comedy [shows](/assets/hbtn_0d_tvshows.sql).
16. **List Shows and Genres**: List all [shows](/assets/hbtn_0d_tvshows.sql) and their genres.
17. **Not My Genre**: List all genres not linked to the show 'Dexter'.
18. **No Comedy Tonight!**: List [shows](/assets/hbtn_0d_tvshows.sql) without the comedy genre.
19. **Rotten Tomatoes**: Rank shows by their [ratings](/assets/hbtn_0d_tvshows_rate.sql).
20. **Best Genre**: Rank genres by their total [ratings](/assets/hbtn_0d_tvshows_rate.sql).

---

## Fun Fact
Did you know that SQL was initially called **SEQUEL (Structured English Query Language)** but had to be renamed due to a trademark issue? So yeah, it was "sequentially" named SQL!

---

`SELECT * FROM world WHERE happiness='true';`
- If only SQL could fix everything.

---