def main():
    file = open("komiwojazer.txt")

    n = int(file.readline())

    table = [[0] * n for i in range(n)]
    visited = []
    to_visit = [i for i in range(n)]

    for line in file:
        parts = line.split(" ")
        v1 = int(parts[0])
        v2 = int(parts[1])
        d = int(parts[2])
        table[v1][v2] = d
        table[v2][v1] = d

    distance = 0
    current_node = 0
    visited = [to_visit.pop(to_visit.index(current_node))]

    while len(to_visit) != 0:
        min_distance = 999999
        min_node = -1
        for node in to_visit:
            current_distance = distance + table[current_node][node]
            if current_distance < min_distance:
                min_distance = current_distance
                min_node = node
        print(f"Went from {current_node} to {min_node}\nCurrent distance: {min_distance}")
        current_node = min_node
        visited.append(to_visit.pop(to_visit.index(current_node)))
        distance = min_distance

    print(visited)

main()

