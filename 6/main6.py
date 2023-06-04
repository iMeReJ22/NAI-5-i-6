import random


def get_distance(path, table):
    distance = 0
    for i in range(len(path) - 1):
        distance += table[path[i]][path[i + 1]]
    distance += table[path[len(path)-1]][path[0]]
    return distance


def swap(to_visit, i1, i2):
    tmp = to_visit[i1]
    to_visit[i1] = to_visit[i2]
    to_visit[i2] = tmp


def get_neighbours(path):
    neighbours = list()
    for i in range(1, len(path)):
        for j in range(1, i):
            neighbour = path.copy()
            swap(neighbour, i, j)
            neighbours.append(neighbour)
    return neighbours


def get_smallest_path(path, table):
    smallest = -1
    smallest_distance = get_distance(path, table)
    neighbours = get_neighbours(path)
    for i in range(len(neighbours)):
        current_distance = get_distance(neighbours[i], table)
        if current_distance < smallest_distance:
            smallest_distance = current_distance
            smallest = i
            path = neighbours[i]
    if smallest == -1:
        return path, smallest_distance
    else:
        print(f"Moving to \t\t{path}, with distance: \t{smallest_distance}")
        return get_smallest_path(path, table)


def main():
    file = open("komiwojazer.txt")

    n = int(file.readline())

    table = [[0] * n for i in range(n)]
    path = [i for i in range(n)]
    random.shuffle(path)

    for line in file:
        parts = line.split(" ")
        v1 = int(parts[0])
        v2 = int(parts[1])
        d = int(parts[2])
        table[v1][v2] = d
        table[v2][v1] = d

    print(f"Starting at \t{path}, with distance: \t{get_distance(path, table)}")
    path, distance = get_smallest_path(path, table)
    print(f"Ended with \t\t{path}, with distance: \t{distance}")


if __name__ == '__main__':
    main()

