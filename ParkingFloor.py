import threading
from ParkingSpot import ParkingSpot
from VehicleType import Truck

class ParkingFloor:
    def __init__(self, floor_number, spots_per_floor):
        self.floor_number = floor_number
        self.spots = [ParkingSpot(i) for i in range(spots_per_floor)]
        self.lock = threading.Lock()

    def park_vehicle(self, vehicle):
        with self.lock:
            if isinstance(vehicle, Truck):
                for i in range(len(self.spots) - 1):
                    if not self.spots[i].is_occupied and not self.spots[i+1].is_occupied:
                        self.spots[i].park_vehicle(vehicle)
                        self.spots[i+1].park_vehicle(vehicle)
                        return self.floor_number, i
            else:
                for spot in self.spots:
                    if not spot.is_occupied:
                        spot.park_vehicle(vehicle)
                        return self.floor_number, spot.spot_number
        return None

    def remove_vehicle(self, vehicle):
        with self.lock:
            for spot in self.spots:
                if spot.is_occupied and spot.vehicle == vehicle:
                    spot.remove_vehicle()
                    return True
        return False

    def get_available_spots(self):
        return len([spot for spot in self.spots if not spot.is_occupied])

    def is_full(self):
        return all(spot.is_occupied for spot in self.spots)