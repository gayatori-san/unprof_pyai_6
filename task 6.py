import pandas as pd
import numpy as np

# ============================================================
# STEP 1: READ DATA (simulating read_csv())
# ============================================================
data = {
    'Student_ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010'],
    'Name': ['Aisha', 'Ben', 'Chloe', 'David', 'Emma', 'Farhan', 'Grace', 'Henry', 'Isha', 'Jack'],
    'Math': [85, 92, np.nan, 78, 88, 95, 67, np.nan, 91, 74],
    'Science': [90, 85, 88, np.nan, 92, 78, 85, 88, np.nan, 91],
    'English': [78, 88, 92, 85, np.nan, 90, 82, 75, 88, np.nan],
    'History': [82, 75, 88, 90, 85, np.nan, 78, 92, 85, 88]
}

df = pd.DataFrame(data)
subjects = ['Math', 'Science', 'English', 'History']

print("=" * 60)
print("📊 RAW DATA")
print("=" * 60)
print(df.to_string())
print(f"\n⚠️ Missing values:\n{df.isnull().sum()}")

# ============================================================
# STEP 2: CLEAN DATA (fillna())
# ============================================================
print("\n" + "=" * 60)
print("🧹 CLEANING DATA")
print("=" * 60)

for subject in subjects:
    subject_mean = df[subject].mean()
    df[subject] = df[subject].fillna(round(subject_mean, 1))
    print(f"  • {subject}: filled with avg {subject_mean:.1f}")

print(f"\n✅ Cleaned:\n{df.to_string()}")

# ============================================================
# STEP 3: SUBJECT-WISE AVERAGES (groupby concept)
# ============================================================
print("\n" + "=" * 60)
print("📈 SUBJECT AVERAGES")
print("=" * 60)

subject_averages = df[subjects].mean().round(2)
print(subject_averages.to_string())
print(f"\n🏆 Best: {subject_averages.idxmax()} ({subject_averages.max():.2f})")
print(f"💀 Worst: {subject_averages.idxmin()} ({subject_averages.min():.2f})")

# ============================================================
# STEP 4: STUDENT PERFORMANCE
# ============================================================
print("\n" + "=" * 60)
print("👤 STUDENT REPORT")
print("=" * 60)

df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1).round(2)
df['Grade'] = df['Average'].apply(
    lambda x: 'A+' if x >= 90 else 'A' if x >= 80 else 'B' if x >= 70 else 'C' if x >= 60 else 'F'
)

df_sorted = df.sort_values('Average', ascending=False)
print(df_sorted[['Student_ID', 'Name', 'Total', 'Average', 'Grade']].to_string(index=False))

# ============================================================
# STEP 5: MERGE WITH TEACHER DATA
# ============================================================
print("\n" + "=" * 60)
print("🔗 MERGE DEMO")
print("=" * 60)

teachers_df = pd.DataFrame({
    'Subject': subjects,
    'Teacher': ['Mr. Sharma', 'Ms. Patel', 'Mrs. Khan', 'Mr. Dubey'],
    'Department': ['STEM', 'STEM', 'Humanities', 'Humanities']
})

subject_stats = pd.DataFrame({
    'Subject': subjects,
    'Avg': [round(df[s].mean(), 2) for s in subjects],
    'Max': [df[s].max() for s in subjects],
    'Min': [df[s].min() for s in subjects]
})

merged = pd.merge(subject_stats, teachers_df, on='Subject', how='left')
print(merged.to_string(index=False))

# ============================================================
# STEP 6: FINAL SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("📋 SUMMARY REPORT")
print("=" * 60)

print(f"👥 Students: {len(df)}")
print(f"📚 Subjects: {', '.join(subjects)}")
print(f"\n📊 Grades:\n{df['Grade'].value_counts().to_string()}")
print(f"\n📈 Class Avg: {df['Average'].mean():.2f}%")
print(f"🥇 Top: {df_sorted.iloc[0]['Name']} ({df_sorted.iloc[0]['Average']:.2f}%)")
print(f"📉 Bottom: {df_sorted.iloc[-1]['Name']} ({df_sorted.iloc[-1]['Average']:.2f}%)")

print("\n📚 Subject Stats:")
for subj in subjects:
    above = (df[subj] > df[subj].mean()).sum()
    print(f"   • {subj}: {above}/{len(df)} above avg")

# Save to CSV
df.to_csv('student_marks_cleaned.csv', index=False)
print("\n💾 Saved: student_marks_cleaned.csv")