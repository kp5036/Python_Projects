# Acadmix – University Enrollment & Billing System (Python)

Acadmix is a Python-based academic management system that models how a university might handle
courses, catalogs, semesters, students, staff, tuition billing, and loans.

The project is built with object-oriented design and focuses on the **backend logic** of a student
information system: adding/removing courses, registering semesters, enrolling/dropping classes,
charging tuition, and applying loans to a student account.

---
## Demo Video

[![Watch the demo] --> https://youtu.be/9YM_wZx23n8?si=EjUyxVSufFdqLHBI )
## Features

- **Course & Catalog Management**
  - `Course` class for course ID, name, and credits
  - `Catalog` class to store course offerings and load them from a CSV file
  - Add or remove courses from the catalog

- **Semester Planning**
  - `Semester` class that holds a student’s courses for a single term
  - Tracks total credits and whether the student is full-time

- **Student Records**
  - `Person` and `Student` classes with generated student IDs based on name + SSN
  - Students can:
    - Register for new semesters
    - Enroll in courses from the catalog
    - Drop courses (with partial tuition refund logic)
  - Automatic update of class standing (Freshman, Sophomore, Junior, Senior) based on number of semesters

- **Staff & Administration**
  - `Staff` class for staff members with IDs derived from name + SSN
  - Staff can:
    - Place or remove holds on students
    - Unenroll students (set them inactive)
    - Create new `Student` records from a `Person`

- **Student Accounts & Loans**
  - `StudentAccount` class tracks a student’s balance and loans
  - Tuition is charged per credit (`CREDIT_PRICE = 1000`)
  - `Loan` class creates loans with a randomly generated loan ID
  - Loans can be applied to reduce the student’s balance
  - Basic payment and refund logic when dropping courses

---

## Tech Stack

- **Language:** Python 3
- **Paradigm:** Object-Oriented Programming (OOP)
- **Standard Library:** `random`, file I/O
- **Data File:** CSV (e.g., `cmpsc_catalog_small.csv` for course data)

No external dependencies are required; everything runs with standard Python.

---

## Project Structure

A simplified version of the repo layout:

```text
Python_Projects/
├── Acadmix.py                 # All core classes (Course, Catalog, Semester, Student, Staff, Loan, StudentAccount, etc.)
├── cmpsc_catalog_small.csv    # Sample catalog data: course ID, name, credits
└── README.md                  # Project documentation (this file)
