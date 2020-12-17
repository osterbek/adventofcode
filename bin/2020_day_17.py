from pathlib import Path


def neighbours_3_dim(cubeset, x, y, z):
    active_neighbours = {}
    inactive_neighbours = {}
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i, j, k) != (x, y, z) and cubeset.get((i, j, k)):
                    active_neighbours[(i, j, k)] = 1
                else:
                    inactive_neighbours[(i, j, k)] = 1
    return inactive_neighbours, active_neighbours


def neighbours_4_dim(cubeset, x, y, z, w):
    active_neighbours = {}
    inactive_neighbours = {}
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if (i, j, k, l) != (x, y, z, w) and cubeset.get((i, j, k, l)):
                        active_neighbours[(i, j, k, l)] = 1
                    else:
                        inactive_neighbours[(i, j, k, l)] = 1
    return inactive_neighbours, active_neighbours


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_17.txt').read_text().split('\n')]
    cubes_3 = {}
    cubes_4 = {}
    for y in range(0, len(dataset)):
        for x in range(0, len(dataset[y])):
            if dataset[y][x] == '#':
                cubes_3[(x, y, 0)] = 1
                cubes_4[(x, y, 0, 0)] = 1
    for cycle in range(0, 6):
        print(cycle, end=' ')
        temp_cubes_3 = {}
        temp_cubes_4 = {}
        for cube in cubes_3:
            neighbours = neighbours_3_dim(cubes_3, cube[0], cube[1], cube[2])
            if len(neighbours[1]) in [2, 3]:
                temp_cubes_3[cube] = 1
            for inac_neigh in neighbours[0]:
                if len(neighbours_3_dim(cubes_3, inac_neigh[0], inac_neigh[1], inac_neigh[2])[1]) == 3:
                    temp_cubes_3[inac_neigh] = 1
        cubes_3 = temp_cubes_3
        for cube in cubes_4:
            neighbours = neighbours_4_dim(cubes_4, cube[0], cube[1], cube[2], cube[3])
            if len(neighbours[1]) in [2, 3]:
                temp_cubes_4[cube] = 1
            for inac_neigh in neighbours[0]:
                if len(neighbours_4_dim(cubes_4, inac_neigh[0], inac_neigh[1], inac_neigh[2], inac_neigh[3])[1]) == 3:
                    temp_cubes_4[inac_neigh] = 1
        cubes_4 = temp_cubes_4
    print('Answer part 1 = {:d} '.format(len(cubes_3)), len(cubes_3) == 448)
    print('Answer part 2 = {:d} '.format(len(cubes_4)), len(cubes_4) == 2400)
