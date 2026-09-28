#Program 1-Loop Through the Times
times = ["1:27.95", "1:21.07", "1:30.96", "1:23.22", "1:27.95", "1:28.30"]

for time in times:
    print(time)


#program 2-Find the Best Time
best_time = times[0]

for time in times:
    if time < best_time:
        best_time = time

print("Best time:", best_time)


#Program 3-Age Group with if/elif/else
age = 12

if age < 13:
    print("under 13")
elif age < 15:
    print("under 15")
elif age < 17:
    print("under 17")
else:
    print("senior")


#Program 4-Number the times
for i in range(len(times)):
    print(f"Time {i + 1}: {times[i]}")


#Program 5-Count Repeats
count = 0

for time in times:
    if time == "1:27.95":
        count += 1

print("1:27.95 appears", count, "times")
