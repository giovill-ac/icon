import random

from room.algos import StochasticBeamSearch
from room.functions import generate_initial_state, objective, room_change


class FurniturePlacementBeamSearch(StochasticBeamSearch):
    def __init__(
        self,
        room_width,
        room_height,
        doors,
        furniture_dict,
        population_size,
        temperature,
        max_generations=1000,
        acceptable_fitness=0,
    ):
        self.room_width = room_width
        self.room_height = room_height
        self.doors = doors
        self.furniture_dict = furniture_dict
        super().__init__(population_size, temperature, max_generations, acceptable_fitness=acceptable_fitness)

    def mutate(self, assignment):
        """
        Randomly change the position of a piece of furniture in the room.
        """
        return room_change(
            assignment,
            self.furniture_dict,
            self.room_width,
            self.room_height,
            self.doors,
        )

    def crossover(self, assignment1: list, assignment2: list):
        """
        Combine the furniture placements of two states.
        """

        # Create copies of the input dictionaries to hold the crossover results
        assignment1_cross = assignment1.copy()
        assignment2_cross = assignment2.copy()

        for i, coord in enumerate(assignment1):
            if random.random() < 0.5:
                assignment1_cross[i] = assignment2[i]
                assignment2_cross[i] = coord

        return assignment1_cross, assignment2_cross

    def fitness(self, assignment):
        """
        Calculate the fitness of the current furniture placement.
        The fitness is based on the distance of each furniture from the door and balcony,
        as well as overlaps between furniture, whether furniture is attached to a wall,
        and the distance between furniture and its nearby furniture.
        """
        return objective(
            assignment,
            self.furniture_dict,
            self.room_width,
            self.room_height,
            self.doors,
        )

    def random_assignment(self):
        return generate_initial_state(
            self.furniture_dict, self.room_width, self.room_height
        )
