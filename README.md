# 📊 Student Marks Analysis using Pandas

A simple Python project demonstrating **data wrangling and data analysis** using the **Pandas** library. This application reads student marks from CSV files, cleans missing or invalid data, calculates subject-wise and class-wise averages, and generates summary reports.

---

## ✨ Features

* 📂 Read student details and marks from CSV files
* 🧹 Clean missing and invalid values
* 📊 Calculate subject-wise average marks
* 👥 Generate class-wise average using `groupby()`
* 🔗 Merge multiple datasets using `merge()`
* 💾 Export cleaned data and summary reports as CSV files

---

## 🛠️ Concepts Covered

* `DataFrame`
* `read_csv()`
* `fillna()`
* `groupby()`
* `merge()`
* `to_csv()`

---

## 📁 Project Structure

```text
Student-Marks-Analysis/
│
├── data/
│   ├── students.csv
│   └── marks.csv
│
├── output/
│   ├── cleaned_marks.csv
│   └── summary_report.csv
│
├── analysis.py
├── requirements.txt
└── README.md
```

---

## 📄 Sample Dataset

### students.csv

```csv
Student_ID,Name,Class
101,Alice,A
102,Bob,A
103,Charlie,B
104,David,B
105,Eva,A
```

### marks.csv

```csv
Student_ID,Math,Science,English
101,85,78,90
102,92,,88
103,110,70,76
104,65,-5,
105,88,91,95
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/gayatori-san/unprof_pyai_6
```

Navigate to the project directory:

```bash
cd Student-Marks-Analysis
```

Install the required library:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python analysis.py
```

---

## 📈 Example Output

### Subject-wise Average

```text
Math       82.50
Science    79.80
English    87.25
```

### Class-wise Average

```text
Class A

Math       88.30
Science    84.50
English    91.00

Class B

Math       73.70
Science    74.00
English    83.00
```

---

## 📂 Output Files

After execution, the project generates:

```text
output/
├── cleaned_marks.csv
└── summary_report.csv
```

---

## 📚 Learning Outcomes

Through this project, you will learn how to:

* Read CSV files using Pandas
* Clean missing and invalid data
* Merge multiple DataFrames
* Group and summarize data
* Calculate averages and totals
* Export processed data into CSV files


