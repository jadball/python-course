import h5py

f = h5py.File("data/i22-4996.nxs", "r")

for group in f:
    print(f[f"/{group}"])
    for subgroup in f[group]:
        print(f[f"/{group}/{subgroup}"])
