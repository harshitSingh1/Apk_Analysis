import os
import csv
import subprocess

# Path to MAVS script
mavs_script = "/home/harshit/Desktop/mavs-master/mavs.sh"

# Path to APK files folder
apk_folder = "/home/harshit/Desktop/Apk_files"

# Output CSV file path
output_csv = "/home/harshit/Desktop/scanning_results.csv"

# Header for the CSV file
csv_header = ["file name", "Hostname Verified", "auth in protected space",
              "Logging Enabled (Log.e calls)", "Logging Enabled (Logger calls)",
              "Snapshots Allowed", "Outdated Software Versions", "Backups Allowed",
              "Cleartext Allowed", "Debugging Enabled", "hardcoded *.pem files"]

# List to store results for each APK
results_list = []

# Iterate through APK files in the folder
for idx, apk_file in enumerate(os.listdir(apk_folder)):
    if apk_file.endswith(".apk"):
        apk_path = os.path.join(apk_folder, apk_file)

        # Print scanning progress
        print(f"{idx + 1}. Scanning {apk_file}....")

        # Run MAVS script for scanning
        command = [mavs_script, "-f", apk_path]
        result = subprocess.run(command, capture_output=True, text=True)
        result_lines = result.stdout.split("\n")

        # Extract relevant information from MAVS output
        apk_results = [apk_file]
        for line in result_lines:
            for header in csv_header[1:]:
                if header in line:
                    # Assign 1 for Vulnerable, 0 for Not Vulnerable
                    apk_results.append("1" if "Vulnerable" in line else "0")

        results_list.append(apk_results)

# Write results to CSV file
with open(output_csv, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(csv_header)
    csv_writer.writerows(results_list)

# Print a message indicating the CSV file generation completion
print(f"\nCSV file generated: {output_csv}")
