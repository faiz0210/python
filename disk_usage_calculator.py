server_name = "webserver-03"
cpu_cores = 4
memory_gb = 8.0
disk_total_gb = 500
disk_used_gb = 350


disk_used_percentage = disk_used_gb / disk_total_gb
print(disk_used_percentage)

summary = f"'{server_name.upper()}' ({cpu_cores} cores, {memory_gb} GB RAM,  Disk Usage = {disk_used_percentage} )"
print(summary)

summary_formatted = f"'{server_name.upper()}' ({cpu_cores} cores, {memory_gb} GB RAM,  Disk Usage = {disk_used_percentage:.2%} )"
print(summary_formatted)


hostname = "server-a"
hostname[7] = "b"
print(hostname)