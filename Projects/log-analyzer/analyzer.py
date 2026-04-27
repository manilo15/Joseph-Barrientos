log_file = "sample_logs/sample.log"

error_count = 0
warning_count = 0
failed_login_count = 0

with open(log_file, "r") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip().upper()

    if "ERROR" in line:
        error_count += 1

    if "WARNING" in line:
        warning_count += 1

    if "FAILED LOGIN" in line:
        failed_login_count += 1

print("Log Analysis Summary:\n")
print(f"Errors: {error_count}")
print(f"Warnings: {warning_count}")
print(f"Failed Logins: {failed_login_count}")

output_file = "output/results.txt"

with open(output_file, "w") as f:
    f.write("Log Analysis Summary:\n\n")
    f.write(f"Errors: {error_count}\n")
    f.write(f"Warnings: {warning_count}\n")
    f.write(f"Failed Logins: {failed_login_count}\n")