# AI Lab - Python & Data Science Laboratory Experiments

This repository contains the laboratory implementations and verified outputs for the **Exploration in Artificial Intelligence (AD/AM/IT/CB/CZ/CS6102)** laboratory experiments implemented in Python.

---

## Repository Structure

Each experiment is organized in its own dedicated directory containing the source code, any required input datasets/generated assets, and its verified program output right beside it:

```text
AI-Lab/
├── exp1/
│   ├── exp1.py                                  # Student Marks, Percentage, Grade & Academic Performance
│   └── output1.txt
├── exp2/
│   ├── exp2.py                                  # Electricity Billing System Using Conditions & Loops
│   └── output2.txt
├── exp3/
│   ├── exp3.py                                  # Menu-Driven Student Information Management
│   └── output3.txt
├── exp4/
│   ├── exp4.py                                  # Student Record Management (Lists, Tuples, Dictionaries, CSV)
│   └── output4.txt
├── exp5/
│   ├── exp5.py                                  # IoT Sensor Data Analysis Using NumPy
│   └── output5.txt
├── exp6/
│   ├── exp6.py                                  # Analysis of Student Dataset Using Pandas Series & DataFrame
│   └── output6.txt
├── exp7/
│   ├── exp7.py                                  # Data Cleaning and EDA Using Pandas
│   ├── exp7_colab.py                            # CSV-based Colab variant
│   ├── students1.csv
│   ├── output7.txt
│   └── output7_colab.txt
├── exp8/
│   ├── exp8.py                                  # Data Cleaning, EDA & Visualization Using Pandas & Matplotlib
│   ├── experiment_8_student_performance.csv
│   ├── department_wise_average_exam_score.png
│   ├── student_performance_distribution.png
│   └── output8.txt
├── exp9/
│   ├── exp9.py                                  # Data Visualization Using Matplotlib
│   ├── experiment_9_retail_sales.csv
│   ├── monthly_revenue_line_chart.png
│   ├── category_wise_revenue_bar_chart.png
│   ├── region_wise_revenue_pie_chart.png
│   ├── units_sold_vs_revenue_scatter.png
│   └── output9.txt
├── exp10/
│   ├── exp10.py                                 # Prompt Design and Evaluation Using Generative AI
│   ├── experiment_10_prompt_evaluation.csv
│   └── output10.txt
├── exp11/
│   ├── exp11.py                                 # Role-Based, Zero-Shot, One-Shot & Few-Shot Prompting
│   ├── experiment_11_prompting_techniques.csv
│   └── output11.txt
├── exp12/
│   ├── exp12.py                                 # AI-Assisted Generation of Technical Content & Python Programs
│   ├── experiment_12_technical_generation.csv
│   ├── generated_technical_content/
│   └── output12.txt
├── exp13/
│   ├── exp13.py                                 # AI-Powered Study Assistant Using Python & Generative AI
│   ├── experiment_13_study_materials.csv
│   └── output13.txt
├── .gitignore                                   # Ignores byte-caches, generated exp4 data, and local virtualenvs
└── README.md                                    # Documentation and execution guide
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
| **7** | Data Cleaning and Exploratory Data Analysis Using Pandas | [exp7.py](exp7/exp7.py) | [output7.txt](exp7/output7.txt) |
| **8** | Data Cleaning, Exploratory Data Analysis and Visualization Using Pandas and Matplotlib | [exp8.py](exp8/exp8.py) | [output8.txt](exp8/output8.txt) |
| **9** | Data Visualization Using Matplotlib | [exp9.py](exp9/exp9.py) | [output9.txt](exp9/output9.txt) |
| **10** | Prompt Design and Evaluation Using Generative AI | [exp10.py](exp10/exp10.py) | [output10.txt](exp10/output10.txt) |
| **11** | Role-Based, Zero-Shot, One-Shot and Few-Shot Prompting | [exp11.py](exp11/exp11.py) | [output11.txt](exp11/output11.txt) |
| **12** | AI-Assisted Generation of Technical Content and Python Programs | [exp12.py](exp12/exp12.py) | [output12.txt](exp12/output12.txt) |
| **13** | AI-Powered Study Assistant Using Python and Generative AI | [exp13.py](exp13/exp13.py) | [output13.txt](exp13/output13.txt) |

---

## Experiment Summaries & Outputs

### Experiment 1: Student Marks, Percentage, Grade and Academic Performance
- **Aim**: Calculate total marks, percentage, grade, and display performance using basic I/O and conditional statements.
- **Output**: [output1.txt](exp1/output1.txt)

### Experiment 2: Electricity Billing System
- **Aim**: Calculate electricity consumption charges using slab rates, conditionals, and loops.
- **Output**: [output2.txt](exp2/output2.txt)

### Experiment 3: Menu-Driven Student Information Management
- **Aim**: Manage student records (Add, View, Search, Delete) using functions, dictionaries, and a menu-driven loop.
- **Output**: [output3.txt](exp3/output3.txt)

### Experiment 4: Student Record Management with Files & CSV
- **Aim**: Store and manipulate records using Python Lists, Tuples, Dictionaries, plain text files, and the `csv` module.
- **Output**: [output4.txt](exp4/output4.txt)

### Experiment 5: IoT Sensor Data Analysis Using NumPy
- **Aim**: Perform mathematical and statistical operations (mean, median, min, max, standard deviation, threshold filtering) on IoT sensor readings using NumPy.
- **Output**: [output5.txt](exp5/output5.txt)

### Experiment 6: Analysis of Student Dataset Using Pandas
- **Aim**: Create and manipulate Pandas Series and DataFrames to compute column averages and filter high-performing students.
- **Output**: [output6.txt](exp6/output6.txt)

### Experiment 7: Data Cleaning and Exploratory Data Analysis Using Pandas
- **Aim**: Perform missing value treatment, duplicate removal, department-wise aggregation, and descriptive analysis on student datasets (`exp7.py` and CSV-based `exp7_colab.py`).
- **Outputs**: [output7.txt](exp7/output7.txt), [output7_colab.txt](exp7/output7_colab.txt)

### Experiment 8: Data Cleaning, EDA and Visualization Using Pandas and Matplotlib
- **Aim**: Load `experiment_8_student_performance.csv`, impute missing numerical/categorical values, remove duplicates, classify performance, and plot department-wise scores and performance distribution.
- **Output**: [output8.txt](exp8/output8.txt)

### Experiment 9: Data Visualization Using Matplotlib
- **Aim**: Analyze retail sales data from `experiment_9_retail_sales.csv` and generate monthly line charts, category bar charts, region pie charts, and units-vs-revenue scatter plots.
- **Output**: [output9.txt](exp9/output9.txt)

### Experiment 10: Prompt Design and Evaluation Using Generative AI
- **Aim**: Evaluate weak vs. improved prompts from `experiment_10_prompt_evaluation.csv` against structured prompt engineering criteria (role, context, task clarity, constraints, output format).
- **Output**: [output10.txt](exp10/output10.txt)

### Experiment 11: Role-Based, Zero-Shot, One-Shot and Few-Shot Prompting
- **Aim**: Construct prompts from `experiment_11_prompting_techniques.csv` across Zero-Shot, One-Shot, Few-Shot, and Role-Based techniques with rule-based Python demonstration responses.
- **Output**: [output11.txt](exp11/output11.txt)

### Experiment 12: AI-Assisted Generation of Technical Content and Python Programs
- **Aim**: Generate reusable Python program templates and explanatory study notes from `experiment_12_technical_generation.csv` into `exp12/generated_technical_content/`.
- **Output**: [output12.txt](exp12/output12.txt)

### Experiment 13: AI-Powered Study Assistant Using Python and Generative AI
- **Aim**: Retrieve relevant study notes and quiz questions from `experiment_13_study_materials.csv` using keyword-overlap scoring.
- **Output**: [output13.txt](exp13/output13.txt)

---

## Running the Experiments

To run the experiments, ensure you have Python 3 and the required libraries installed:

```bash
# Install dependencies for experiments 5 to 13
pip install numpy pandas matplotlib

# Run any experiment
python exp1/exp1.py
python exp2/exp2.py
python exp3/exp3.py
python exp4/exp4.py
python exp5/exp5.py
python exp6/exp6.py
python exp7/exp7.py
python exp7/exp7_colab.py
python exp8/exp8.py
python exp9/exp9.py
python exp10/exp10.py
python exp11/exp11.py
python exp12/exp12.py
python exp13/exp13.py
```
