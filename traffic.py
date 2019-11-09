class Vehicle:
    def __init__(self, vehicle_type, speed, carter_crossing_time, permitted_wheather):
        self.type = vehicle_type
        self.speed = speed
        self.carter_crossing_time = carter_crossing_time
        self.permitted_wheather = permitted_wheather

    def pemitted_vehicle(self, wheather):
        if wheather in self.permitted_wheather:
            return True
        else:
            return False

class Wheather:
    def __init__(self, wheather_type, carter_effect):
        self.type = wheather_type
        self.carter_effect = carter_effect

    def carter_count(self, total_carter_count):
        carter_count_in_wheather = (total_carter_count * self.carter_effect) * 100
        return total_carter_count + carter_count_in_wheather

class Orbit:
    def __init__(self, name, source, destination, distance, carter_count):
        self.name = name
        self.source = source
        self.destination = destination
        self.distance = distance
        self.carter_count = carter_count

class Traffic:
    def __init__(self):
        self.wheathers = self.__intialize_wheather()
        self.vehicles = self.__intialize_vehicle()
        self.orbits = self.__intialize_orbit()

    def __intialize_vehicle(self):
        self.__bike = Vehicle('bike', 10, 2, [self.__sunny, self.__windy] )
        self.__tuktuk = Vehicle('tuktuk', 12, 1, [self.__sunny, self.__rainy])
        self.__car = Vehicle('car', 20, 3, [self.__sunny, self.__rainy, self.__windy])
        return [self.__bike, self.__tuktuk, self.__car]

    def __intialize_wheather(self):
        self.__sunny = Wheather('sunny', -10)
        self.__rainy = Wheather('rainy', 20)
        self.__windy = Wheather('windy', 0)
        return [self.__sunny, self.__rainy, self.__windy]

    def __intialize_orbit(self):
        self.orbit1 = Orbit('orbit1', 'Silk Dorb', 'Hallitharam', 18, 20)
        self.orbit2 = Orbit('orbit2', 'Silk Dorb', 'Hallitharam', 20, 10)
        return [self.orbit1, self.orbit2]

    def find_route(self, wheather):
        current_wheather = self.wheathers[0]
        allowed_vehicle_in_given_wheather = self.__find_vehicle(current_wheather)
        possible_orbits = self.__find_posible_orbit()
        orbit, vehicle = self.__find_fastest_route(allowed_vehicle_in_given_wheather, possible_orbits, current_wheather)
        return [orbit, vehicle]

    def __find_vehicle(self, current_wheather):
        allowed_vehicle_in_given_wheather = []
        for vehicle in self.vehicles:
            allowed = vehicle.pemitted_vehicle(current_wheather)
            if allowed:
                allowed_vehicle_in_given_wheather.append(vehicle)
        return allowed_vehicle_in_given_wheather

    def __find_posible_orbit(self):
        possible_orbits = []
        for orbit in self.orbits:
            if orbit.source == 'Silk Dorb' and orbit.destination == 'Hallitharam':
                possible_orbits.append(orbit)
        return possible_orbits


    def __find_fastest_route(self, allowed_vehicle, possible_orbits, current_wheather):
        fastest_orbit, fastest_vehicle, time_taken = None, None, float('inf')
        for vehicle in allowed_vehicle:
            for orbit in possible_orbits:
                total_carter_count = orbit.carter_count
                carter_count_in_wheather = current_wheather.carter_count(total_carter_count)
                time = (orbit.distance / vehicle.speed)*60 + (carter_count_in_wheather* vehicle.carter_crossing_time)
                if time < time_taken:
                    time_taken = time
                    fastest_orbit = orbit
                    fastest_vehicle = vehicle

        return [fastest_orbit, fastest_vehicle]

traffic = Traffic()
t = traffic.find_route(0)
print('vehicle ' + t[1].type + ' on ' + t[0].name)








