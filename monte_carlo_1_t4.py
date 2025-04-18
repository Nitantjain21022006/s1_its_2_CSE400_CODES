# -*- coding: utf-8 -*-
"""Monte_Carlo_1_T4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vJdRpps7GfUL8V1ziicrqrfFSUSm_jDC
"""

import random

num_junctions = 4
iterations = 10
min_time, max_time = 10, 60

traffic_data = [100, 200, 150, 250]

def generate_random_schedule():
    return [random.randint(min_time, max_time) for _ in range(num_junctions)]

def fitness(schedule):
    return sum(abs(traffic_data[i] / schedule[i]) for i in range(num_junctions))

def monte_carlo():
    best_schedule = None
    best_fitness = float('inf')

    print("\nInitial Monte Carlo Random Trials:")

    for i in range(iterations):
        schedule = generate_random_schedule()
        score = fitness(schedule)

        print(f"Trial {i+1}: {schedule} | Fitness: {round(score, 2)}")

        if score < best_fitness:
            best_fitness = score
            best_schedule = schedule
            print(f" New Best Found: {schedule} | Fitness: {round(best_fitness, 2)}")

    print("\n Final Optimized Traffic Signal Plan:", best_schedule)

monte_carlo()