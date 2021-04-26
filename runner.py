import os
import glob
import time


# def parse_line(ln):
#     ln = ln[1:]
#     fields = {}
#     for fs in ln.split("|"):
#         k, v = fs.split("=")
#         fields[k.strip()] = int(v)
#     return fields


# def append_record(filename, key, new_record):
#     try:
#         open(filename)
#     except FileNotFoundError:
#         with open(filename, "w") as f:
#             f.write("{}")

#     import json
#     with open(filename) as f:
#         rec = json.load(f)

#     rec[key] = new_record

#     with open(filename, "w") as f:
#         json.dump(rec, f)


record_filename = "records.json"

circuit_path = "benchmarks/alu2"
n_generation = 100_000
n_population = 100
n_elite = 10
n_select = 40
n_crossover = (n_population-n_select) // 2
p_mutation = 0.3

for circuit_path in glob.glob("benchmarks/*.blif"):
    args_str = "{} {} {} {} {} {} {}".format(
        circuit_path, n_generation, n_population, n_elite, n_select, n_crossover, p_mutation)

    filename = '"{}.txt"'.format(args_str.replace(" ", "_"))

    st = time.time()
    os.system(f"cargo r --release -- {args_str} > {filename} 2>/dev/null")
    # os.system(f"cargo r --release -- {args_str} > {filename}")
    ed = time.time()
    os.system(f'echo "# time={ed-st:.0f}" >> {filename}')
    print(f"time={ed-st:.0f}s")


# append_record(record_filename, args_str, bests)
