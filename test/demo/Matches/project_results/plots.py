import matplotlib.pyplot as plt
import ast
import glob

# Adjust this to match your file names or path
files = ['/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_1.txt',
         '/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_2.txt',
         '/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_3.txt',
         '/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_4.txt',
         '/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_5.txt',
         '/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_6.txt',
         '/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_1_RANDOM.txt',
         '/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP recover/OpenCEP/test/demo/Matches/testing/output_citibike_VARIANT_3_RANDOM.txt']

label_names = ['VARIANT_1', 'VARIANT_2', 'VARIANT_3', 'VARIANT_4', 'VARIANT_5', 'VARIANT_6', 'VARIANT_1_RANDOM', 'VARIANT_3_RANDOM']
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']
plt.figure(figsize=(10, 6))

for i, filename in enumerate(files):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Extract p95 latency
    p95 = None
    latencies = None
    file_length = len(lines)
    recall = file_length / 4441 # 4441 is the max no of possible matches
    for line in lines:
        if "p95 latency" in line:
            p95 = float(line.split(":")[1].strip())
        elif "latencies:" in line:
            # Safely evaluate the list using ast.literal_eval
            lat_str = line.split(":", 1)[1].strip()
            latencies = ast.literal_eval(lat_str)
    
    if latencies is None or p95 is None:
        print(f"⚠️ Skipping {filename}: missing data")
        continue

    # Plot latencies
    plt.ylim(0, max(p95, max(latencies)))  # Adjust y-axis limit for better visibility
    plt.plot(latencies, label=f"{label_names[i]} latencies", alpha=0.7, color=colors[i])

    # Plot p95 line
    plt.axhline(y=p95, linestyle='--', label=f"{label_names[i]} p95 ({p95})", alpha=0.7, color=colors[i])

plt.title("Latency Comparison Across Files")
plt.xlabel("Event Index")
plt.ylabel("Latency (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
