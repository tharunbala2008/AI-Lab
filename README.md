# AI Lab - Python & Data Science Laboratory Experiments

This repository contains the laboratory implementations and verified outputs for the **Artificial Intelligence & Data Science Lab Experiments** implemented in Python.

---

## Repository Structure

Each experiment is organized in its own dedicated directory containing the source code and its verified program output right beside it:

```text
AI-Lab/
├── exp1/
│   ├── exp1.py            # Student Marks, Percentage, Grade & Academic Performance
│   └── output1.txt
├── exp2/
│   ├── exp2.py            # Electricity Billing System Using Conditions & Loops
│   └── output2.txt
├── exp3/
│   ├── exp3.py            # Menu-Driven Student Information Management
│   └── output3.txt
├── exp4/
│   ├── exp4.py            # Student Record Management (Lists, Tuples, Dictionaries, CSV)
│   └── output4.txt
├── exp5/
│   ├── exp5.py            # IoT Sensor Data Analysis Using NumPy
│   └── output5.txt
├── exp6/
│   ├── exp6.py            # Analysis of Student Dataset Using Pandas Series & DataFrame
│   └── output6.txt
├── .gitignore             # Ignores byte-caches and local virtualenvs
└── README.md              # Documentation and execution guide
```

---

## Index of Experiments

| Exp No. | Experiment Title | Source Code | Output |
| :---: | :--- | :---: | :---: |
| **1** | Student Marks, Percentage, Grade and Academic Performance | [exp1.py](exp1/exp1.py) | [output1.txt](exp1/output1.txt) |
| **2** | Electricity Billing System Using Conditional Statements and Loops | [exp2.py](exp2/exp2.py) | [output2.txt](exp2/output2.txt) |
| **3** | Menu-Driven Student Information Management | [exp3.py](exp3/exp3.py) | [output3.txt](exp3/output3.txt) |
| **4** | Student Record Management Using Lists, Tuples, Dictionaries, Files and CSV | [exp4.py](exp4/exp4.py) | [output4.txt](exp4/output4.txt) |
| **5** | IoT Sensor Data Analysis Using NumPy | [exp5.py](exp5/exp5.py) | [output5.txt](exp5/output5.txt) |
| **6** | Analysis of Student Dataset Using Pandas Series and DataFrame | [exp6.py](exp6/exp6.py) | [output6.txt](exp6/output6.txt) |

---

## Experiment Summaries & Outputs

### Experiment 1: Student Marks, Percentage, Grade and Academic Performance
- **Aim**: Calculate total marks, percentage, grade, and display performance using basic I/O and conditional statements.
- **Sample Output**:
  ```text
  Enter student name: Priya
  Enter number of subjects: 5
  Enter mark for Subject 1: 85
  Enter mark for Subject 2: 78
  Enter mark for Subject 3: 92
  Enter mark for Subject 4: 88
  Enter mark for Subject 5: 81

  --- Academic Performance ---
  Student Name : Priya
  Total Marks : 424.0
  Percentage : 84.8 %
  Grade : A
  Performance : Excellent
  ```

### Experiment 2: Electricity Billing System
- **Aim**: Calculate electricity consumption charges using slab rates, conditionals, and loops.
- **Sample Output**:
  ```text
  Enter number of customers: 1

  Customer 1
  Enter customer name: Arun
  Enter units consumed: 350
  Customer Name : Arun
  Units : 350.0
  Bill Amount : Rs. 1000.0
  ```

### Experiment 3: Menu-Driven Student Information Management
- **Aim**: Manage student records (Add, View, Search, Delete) using functions, dictionaries, and a menu-driven loop.
- **Sample Output**:
  ```text
  1. Add Student
  2. View Students
  3. Search Student
  4. Delete Student
  5. Exit
  Enter your choice: 1
  Enter Roll No: 101
  Enter Name: Anitha
  Enter Department: CSE
  Student added successfully.

  1. Add Student
  2. View Students
  3. Search Student
  4. Delete Student
  5. Exit
  Enter your choice: 2

  --- Student Records ---
  Roll No: 101 | Name: Anitha | Department: CSE

  1. Add Student
  2. View Students
  3. Search Student
  4. Delete Student
  5. Exit
  Enter your choice: 5
  Exiting...
  ```

### Experiment 4: Student Record Management with Files & CSV
- **Aim**: Store and manipulate records using Python Lists, Tuples, Dictionaries, plain text files, and the `csv` module.
- **Sample Output**:
  ```text
  Course Tuple: ('Python', 4)

  --- Records from CSV ---
  101 Anitha CSE 86
  102 Bala CSE 91
  103 Chitra ECE 78
  ```

### Experiment 5: IoT Sensor Data Analysis Using NumPy
- **Aim**: Perform mathematical and statistical operations (mean, median, min, max, standard deviation, threshold filtering) on IoT sensor readings using NumPy.
- **Sample Output**:
  ```text
  Sensor Data: [24.5 25.1 26.3 27.  28.2 29.1 27.8 26.5 25.7 30.2]
  Mean : 27.04
  Median : 26.75
  Minimum : 24.5
  Maximum : 30.2
  Std. Dev. : 1.77
  Values above 28.0 : [28.2 29.1 30.2]
  ```

### Experiment 6: Analysis of Student Dataset Using Pandas
- **Aim**: Create and manipulate Pandas Series and DataFrames to compute column averages and filter high-performing students.
- **Sample Output**:
  ```text
  --- Pandas Series ---
  A    85
  B    91
  C    78
  D    88
  E    95
  dtype: int64

  --- DataFrame ---
     RollNo    Name Department  Mark
  0     101  Anitha        CSE    85
  1     102    Bala        CSE    91
  2     103  Chitra        ECE    78
  3     104  Dinesh        CSE    88
  4     105   Ezhil        ECE    95

  Average Mark: 87.4

  Students scoring above 85:
     RollNo    Name Department  Mark
  1     102    Bala        CSE    91
  3     104  Dinesh        CSE    88
  4     105   Ezhil        ECE    95
  ```

---

## Running the Experiments

To run the experiments, ensure you have Python 3 and the required libraries installed:

```bash
# Install dependencies for experiments 5 and 6
pip install numpy pandas

# Run any experiment
python exp1/exp1.py
python exp2/exp2.py
python exp3/exp3.py
python exp4/exp4.py
python exp5/exp5.py
python exp6/exp6.py
```
