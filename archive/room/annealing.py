from room.algos import Annealer
from room.functions import generate_initial_state, objective, room_change


class FurniturePlacementAnnealer(Annealer):
    def __init__(self, room_width, room_height, doors, furniture_dict):
        self.room_width = room_width
        self.room_height = room_height
        self.doors = doors
        self.furniture_dict = furniture_dict
        self.state = generate_initial_state(furniture_dict, room_width, room_height)

    def move(self):
        """
        Randomly select a piece of furniture and move it to a new position.
        """
        self.state = room_change(self.state, self.furniture_dict, self.room_width, self.room_height, self.doors)

    def energy(self):
        """
        Calculate the energy of the current furniture placement.
        The energy is based on the distance of each furniture from the door and balcony,
        as well as overlaps between furniture, whether furniture is attached to a wall,
        and the distance between furniture and its nearby furniture.
        """
        return objective(self.state, self.furniture_dict, self.room_width, self.room_height, self.doors)
