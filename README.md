# Apk_Analysis
## Compatibility:
This code is primarily designed to run on Linux. MAVS-master is not compatible with Windows. For Windows users, consider using an alternative APK analyzer tool.
## Installation:
1. cd path/to/Desktop
2. git clone https://github.com/harshitSingh1/Apk_Analysis.git
3. [extract All the files from zip]
4. Scanning APKs:
   a) chmod 777 scan_apks.py
   b) python scan_apks.py
5. Analyzing Results:
   a) chmod 777 graph.py
   b) python graph.py
## Folder Structure:
1. Apk_files: Contains APK files to be scanned.
2. mavs_master: MAVS tool for scanning APK files.
3. scanning_results.csv: CSV file containing the scanning results.(you may delete this before you start scanning)
4. scan_apks.py: Python script for scanning APK files.
5. graph.py: Python script for analyzing and visualizing the scanning results.
## Result:
### 1. Output while scanning the files:
   ![Screenshot (560)](https://github.com/harshitSingh1/Apk_Analysis/assets/95095505/bd4db7ed-c91c-4b93-a062-90578cae9537)

### 2. CSV file data after scanning:
   ![Screenshot (561)](https://github.com/harshitSingh1/Apk_Analysis/assets/95095505/96d71809-c940-454d-95c4-99361bc1211b)

### 3. Bar chart: Number of APK files vs each vulnerability
   ![Screenshot (562)](https://github.com/harshitSingh1/Apk_Analysis/assets/95095505/0f6a2fc1-24cb-41e6-9936-152f9d7dae00)

### 4. Stacked bar chart: Number of APK files with each vulnerability
   ![Screenshot (563)](https://github.com/harshitSingh1/Apk_Analysis/assets/95095505/4f716bff-fa54-4006-bc90-80f624e34c30)

### 5. Pie chart: Percentage of each vulnerability
   ![Screenshot (564)](https://github.com/harshitSingh1/Apk_Analysis/assets/95095505/3533a2c9-d5d6-442a-9850-6a55ef0dc67c)

### 6. line chart: Apk files vs No. of vulnerabilities
   ![Screenshot (565)](https://github.com/harshitSingh1/Apk_Analysis/assets/95095505/b2bad716-391a-4cf1-8dd1-341b4db8e4d3)



