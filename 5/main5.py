file = open("plecak.txt")
line1 = file.readline()
parts1 = line1.split(" ")
k = int(parts1[0])
n = int(parts1[1])

line2 = file.readline()
line3 = file.readline()
values = line2.split(",")
weights = line3.split(",")

biggest_value = -1
biggest_vector = "-1"
for i in range(pow(2, n)):
    bit_vector = format(i, f"0{n}b")
    current_value = 0
    current_weight = 0
    for j in range(n):
        if bit_vector[j] == "1":
            current_value += int(values[j])
            current_weight += int(weights[j])
        if current_weight > k:
            break

    if current_weight <= k:
        if current_value > biggest_value:
            biggest_value = current_value
            biggest_vector = bit_vector
            print(f"{i+1}. Found new best fit: {bit_vector} \nwith a value of: {biggest_value}"
                  f"\nand weight {current_weight}/{k}")
