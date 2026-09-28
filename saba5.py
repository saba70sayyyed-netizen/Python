#Program 1-Work with a list
times = ["1:27.95", "1:21.07", "1:30.96", "1:23.22", "1:27.95", "1:28.30"]

print(times[0])
print(times[-1])
print(times[:3])
print(len(times))


#Program 2-Sorted & Unique
print(sorted(times))
print(len(set(times)))


#Program 3-Tuples
swimmer = ("Darius", 13)

print(swimmer[0])
print(swimmer[1])

swimmers = [("Darius", 13), ("Carl", 13), ("Aurora", 15)]
print(len(swimmers))


#Program 4-DicTionary
ages = {"Darius": 13, "Carl": 13, "Aurora": 15}

print(ages["Darius"])
print(ages.keys())
print(ages.values())


#Program 5-Unique Names with a set
names = ["Darius", "Carl", "Aurora", "Darius", "Carl"]

unique_names = set(names)

print(sorted(unique_names))
print(len(unique_names))
