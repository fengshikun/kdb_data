import os

count = 0
for f in os.listdir("."):
    if f.endswith(".pdb"):
        if "_" in f:
            # print(f)
            # count += 1
            pass
        else:
            print(f.split(".", 1)[0])
            count += 1


print(count)