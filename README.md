# Apk_Analysis
## Compatibility:
This code is primarily designed to run on Linux. MAVS-master is not compatible with Windows. For Windows users, consider using an alternative APK analyzer tool.
## Installation:
1. cd path/to/Desktop
2. git clone https://github.com/sho-luv/mavs.git
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
