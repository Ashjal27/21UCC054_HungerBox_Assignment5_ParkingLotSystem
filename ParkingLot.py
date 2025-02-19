from ParkingFloor import ParkingFloor
from VehicleType import Bike, Car, Truck

class ParkingLot:
    def __init__(self, num_floors, spots_per_floor):
        self.floors = [ParkingFloor(i, spots_per_floor) for i in range(num_floors)]
        self.vehicle_location = {}
        self.license_plate_registry = set()

    def park_vehicle(self, license_plate, vehicle_type):
        if license_plate in self.license_plate_registry:
            return f"Vehicle with license plate {license_plate} is already parked."

        vehicle = None
        if vehicle_type == "Bike":
            vehicle = Bike(license_plate)
        elif vehicle_type == "Car":
            vehicle = Car(license_plate)
        elif vehicle_type == "Truck":
            vehicle = Truck(license_plate)
        else:
            return "Invalid vehicle type"

        for floor in self.floors:
            location = floor.park_vehicle(vehicle)
            if location:
                self.license_plate_registry.add(license_plate)
                self.vehicle_location[license_plate] = location
                return f"Vehicle {license_plate} parked at floor {location[0]}, spot {location[1]}"

        return "Parking lot is full"

    def remove_vehicle(self, license_plate):
        if license_plate in self.vehicle_location:
            location = self.vehicle_location[license_plate]
            floor = self.floors[location[0]]
            vehicle = None
            for spot in floor.spots:
                if spot.is_occupied and spot.vehicle.license_plate == license_plate:
                    vehicle = spot.vehicle
                    break
            if vehicle:
                floor.remove_vehicle(vehicle)
                self.license_plate_registry.remove(license_plate)
                del self.vehicle_location[license_plate]
                return f"Vehicle {license_plate} removed from floor {location[0]}, spot {location[1]}"
        return "Vehicle not found"

    def get_available_spots(self):
        available_spots = {}
        for floor in self.floors:
            available_spots[floor.floor_number] = floor.get_available_spots()
        return available_spots

    def is_full(self):
        return all(floor.is_full() for floor in self.floors)

    def get_vehicle_location(self, license_plate):
        if license_plate in self.vehicle_location:
            location = self.vehicle_location[license_plate]
            return f"Vehicle {license_plate} is parked at floor {location[0]}, spot {location[1]}"
        return "Vehicle not found"