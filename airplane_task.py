import random


class Airplane:
    def __init__(self, name, side_number, weight, speed):
        self.name = name
        self.side_number = side_number
        self.weight = weight
        self.speed = speed
        self.in_order = True if random.randint(0, 1) else False
        self.allow = False

    def take_off(self):
        if self.allow:
            print(f'Airplane {self.name} with side number "{self.side_number}" took off')
        else:
            print(f'No permission to take off for airplane {self.name} with side number "{self.side_number}"')


class CargoAirplane(Airplane):
    def __init__(self, name, side_number, weight, speed, carrying_capacity):
        super().__init__(name, side_number, weight, speed)
        self.carrying_capacity = carrying_capacity


class Liner(Airplane):
    def __init__(self, name, side_number, weight, speed, number_of_passengers):
        super().__init__(name, side_number, weight, speed)
        self.number_of_passengers = number_of_passengers


class WarPlane(Airplane):
    def __init__(self, name, side_number, weight, speed, arming):
        super().__init__(name, side_number, weight, speed)
        self.arming = arming


class Building:
    def __init__(self, name, space):
        self.name = name
        self.space = space
        self.airplanes_in_building = list()

    def add_airplane(self, airplane):
        if airplane is None:
            print('Nothing to add')
        else:
            if len(self.airplanes_in_building) < self.space:
                self.airplanes_in_building.append(airplane)
                print(f'{airplane.name} with side number "{airplane.side_number}" go to {self.name}')
            else:
                print(f'{self.name} is full')

    def remove_airplane(self, side_number):
        for _ in self.airplanes_in_building:
            if _.side_number == side_number:
                print(f'{_.name} with side number "{_.side_number}" go from {self.name}')
                self.airplanes_in_building.remove(_)
                return _
        print(f'Airplane not found in {self.name}')


class Runway(Building):
    def __init__(self, name='Runway', space=10):
        super().__init__(name, space)

    def allow_take_off(self):
        for _ in self.airplanes_in_building:
            if _.in_order:
                _.allow = True
                print(f'Take off done for airplane {_.name} with side number "{_.side_number}"')
            else:
                print(f'Take off canceled for airplane {_.name} with side number "{_.side_number}"')


class Hangar(Building):
    def __init__(self, name='Hangar', space=25):
        super().__init__(name, space)

    def airplanes_repair(self, side_number=None):
        if side_number is None:
            for _ in self.airplanes_in_building:
                if not _.in_order:
                    _.in_order = True
            print('All airplanes are repaired')
        else:
            for _ in self.airplanes_in_building:
                if _.side_number == side_number:
                    _.in_order = True
                    print(f'Airplane with side number "{_.side_number}" are repaired')


if __name__ == "__main__":
    a = Liner('Boeing 733', 'N231OP', 150, 450, 500)
    r = Runway()
    h = Hangar()
    a.take_off()
    if a.in_order:
        r.add_airplane(a)
        r.allow_take_off()
        a.take_off()
    else:
        h.add_airplane(a)
        h.airplanes_repair()
        r.add_airplane(h.remove_airplane('N231OP'))
        r.allow_take_off()
        a.take_off()
