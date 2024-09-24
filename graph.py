import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
csv_path = "./scanning_results.csv"
df = pd.read_csv(csv_path)

# Extract vulnerability columns
vulnerability_columns = df.columns[1:]

# 1. Bar chart: Number of APK files with each vulnerability
plt.figure(figsize=(10, 6))
for vulnerability in vulnerability_columns:
    plt.bar(vulnerability, df[vulnerability].sum(), label=vulnerability)

plt.xlabel("Vulnerabilities")
plt.ylabel("Number of APK files")
plt.title("Number of APK files with Each Vulnerability")
plt.legend()
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.show()

# 2. Stacked bar chart: Number of APK files with each vulnerability
plt.figure(figsize=(10, 6))
bottom = None
for vulnerability in vulnerability_columns:
    vulnerability_values = df[vulnerability].astype(float)  # Ensure data is of the same type (float)
    plt.bar(df["file name"], vulnerability_values, label=vulnerability, bottom=bottom)
    
    if bottom is None:
        bottom = vulnerability_values.values
    else:
        bottom += vulnerability_values.values

plt.xlabel("APK files")
plt.ylabel("Number of APK files")
plt.title("Number of APK files with Each Vulnerability (Stacked)")
plt.legend()
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.show()

# 3. Pie chart: Percentage of each vulnerability
plt.figure(figsize=(8, 8))
plt.pie(df[vulnerability_columns].sum(), labels=vulnerability_columns, autopct="%1.1f%%", startangle=140)
plt.title("Percentage of Each Vulnerability")
plt.legend()
plt.show()

# 4. line chart showing no. of vulnerabilities in each APK file.
plt.figure(figsize=(10, 6))
plt.plot(df["file name"], df[vulnerability_columns].sum(axis=1), marker='o')
plt.xlabel("APK files")
plt.ylabel("Total Number of Vulnerabilities")
plt.title("Total Number of Vulnerabilities in Each APK file")
plt.legend()
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.show()
