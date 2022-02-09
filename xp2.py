# Mahdi Hassanzadeh

import random

POPULATION_SIZE = 50
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.01
TARGET = 255
ALL_POPULATION = []

for i in range(256):
    b = bin(i)[2:]
    b = "0" * (8 - len(b)) + b
    ALL_POPULATION.append([b, i])

# SELECTING POPULATION
population = random.choices(ALL_POPULATION, k=POPULATION_SIZE)

# STARTING THE LOOP
gen_number = 0
for i in range(100):
    new_population = []

    # ELITISM
    new_population.append(sorted(population, reverse=True)[0])

    for i in range(int(len(population) / 2)):
        # CROSSOVER
        parent_chromosome1 = sorted(
            random.choices(population, k=TOURNAMENT_SELECTION_SIZE), reverse=True
        )[0]
        parent_chromosome2 = sorted(
            random.choices(population, k=TOURNAMENT_SELECTION_SIZE), reverse=True
        )[0]

        point = random.randint(0, 7)

        child_chromosome1 = (
            parent_chromosome1[0][0:point] + parent_chromosome2[0][point:]
        )
        child_chromosome2 = (
            parent_chromosome2[0][0:point] + parent_chromosome1[0][point:]
        )

        # MUTATION
        if random.random() < MUTATION_RATE:
            point1 = random.randint(0, 7)
            point2 = random.randint(0, 7)

            if child_chromosome1[point1] == "0":
                child_chromosome1 = (
                    child_chromosome1[0:point1] + "1" + child_chromosome1[point1 + 1 :]
                )
            else:
                child_chromosome1 = (
                    child_chromosome1[0:point1] + "0" + child_chromosome1[point1 + 1 :]
                )

            if child_chromosome1[point2] == "0":
                child_chromosome1 = (
                    child_chromosome1[0:point2] + "1" + child_chromosome1[point2 + 1 :]
                )
            else:
                child_chromosome1 = (
                    child_chromosome1[0:point2] + "0" + child_chromosome1[point2 + 1 :]
                )

        new_population.append([child_chromosome1, int(child_chromosome1, 2)])
        new_population.append([child_chromosome2, int(child_chromosome2, 2)])

    population = new_population

    gen_number += 1
    if sorted(population, reverse=True)[0][1] == TARGET:
        break


answer = sorted(population, reverse=True)[0]

print("\n----------------------------------------------------------------")
print("Generation: " + str(gen_number))
print(
    "Fittest chromosome fitness: "
    + str(answer[0])
    + " => "
    + str(answer[1])
    + " => f(x)="
    + str(answer[1] ** 2)
)
print(
    "Target chromosome: 11111111"
    + " => "
    + str(TARGET)
    + " => f(x)="
    + str(TARGET ** 2)
)
print("----------------------------------------------------------------\n")
