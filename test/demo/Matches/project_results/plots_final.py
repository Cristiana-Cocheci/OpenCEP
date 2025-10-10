import matplotlib.pyplot as plt
import numpy as np
import ast
import glob

files = [...]

label_names = ['10%', '30%', '50%', '70%', '90%', 'Baseline']

p95s = []
recalls = []
throughputs = []
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
        elif "throughput" in line:
            throughput = float(line.split(":")[1].strip())
    
    if latencies is None or p95 is None:
        print(f"Skipping {filename}: missing data")
        continue

    p95s.append(p95)
    recalls.append(recall)
    throughputs.append(throughput)




# Normalize all three arrays to [0, 1]
def normalize(arr):
    arr = np.array(arr)
    return (arr - arr.min()) / (arr.max() - arr.min())

print("p95s",p95s)
print("recalls",recalls)
print("throughputs",throughputs)

p95s_norm = normalize(p95s)
recalls_norm = normalize(recalls)
throughputs_norm = normalize(throughputs)

x = np.arange(len(label_names))

plt.figure(figsize=(10, 6))
plt.plot(x, p95s_norm, marker='o', label='p95 Latency (normalized)', color='#ED3F27')
plt.plot(x, recalls_norm, marker='s', label='Recall (normalized)', color='#134686')
plt.plot(x, throughputs_norm, marker='^', label='Throughput (normalized)', color='#FEB21A')

plt.xticks(x, label_names, rotation=45, ha='right')
plt.title("Normalized Metrics Across Variants")
plt.xlabel("Variant")
plt.ylabel("Normalized Value (0–1)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

'''
import matplotlib.pyplot as plt
import numpy as np
import ast

# -------------------------
# Input files and labels
# -------------------------
# 
# label_names = [
#     'l = 0.08; dr = 0.3; O', 'l = 0.1; dr = 0.3; O', 'l = 0.08; dr = 0.3; R',
#     'l = 0.08; dr = 0.15; O', 'l = 0.1; dr = 0.15; O', 'l = 0.08; dr = 0.1; O',
#     'l = 0.1; dr = 0.1; O', 'l = 0.08; dr = 0.1; R'
# ]
label_names = ['10%', '30%', '50%', '70%', '90%', 'Baseline']

# -------------------------
# Extract metrics
# -------------------------
p95s, recalls, throughputs = [], [], []

for filename in files:
    with open(filename, 'r') as f:
        lines = f.readlines()

    p95 = None
    throughput = None
    recall = len(lines) / 4441  # total possible matches

    for line in lines:
        if "p95 latency" in line:
            p95 = float(line.split(":")[1].strip())
        elif "throughput" in line:
            throughput = float(line.split(":")[1].strip())

    if p95 is None or throughput is None:
        print(f"⚠️ Skipping {filename}: missing data")
        continue

    p95s.append(p95)
    recalls.append(recall)
    throughputs.append(throughput)

# -------------------------
# Plotting
# -------------------------
x = np.arange(len(label_names))
colors = ['#ED3F27', '#134686', '#FEB21A']

fig, axs = plt.subplots(1, 3, figsize=(16, 6), sharex=True)

# p95 latency
axs[0].bar(x, p95s, color=colors[0])
axs[0].set_title("p95 Latency (s)")
axs[0].set_ylabel("Seconds")
axs[0].grid(axis='y', linestyle='--', alpha=0.6)

# recall
axs[1].bar(x, recalls, color=colors[1])
axs[1].set_title("Recall")
axs[1].set_ylabel("Recall")
axs[1].grid(axis='y', linestyle='--', alpha=0.6)

# throughput
axs[2].bar(x, throughputs, color=colors[2])
axs[2].set_title("Throughput (events/s)")
axs[2].set_ylabel("Events / Second")
axs[2].grid(axis='y', linestyle='--', alpha=0.6)

# Common x-axis setup
for ax in axs:
    ax.set_xticks(x)
    ax.set_xticklabels(label_names, rotation=45, ha='right')

plt.suptitle("Performance Metrics Across Variants", fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
'''