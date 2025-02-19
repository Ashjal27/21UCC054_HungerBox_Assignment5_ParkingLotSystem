from ParkingLot import ParkingLot

parking_lot = ParkingLot(num_floors=3, spots_per_floor=3)

print(parking_lot.park_vehicle("KA-01-9999", "Truck"))
print(parking_lot.park_vehicle("KA-01-5678", "Bike"))

print(parking_lot.remove_vehicle("KA-01-9999"))

print(parking_lot.park_vehicle("KA-01-1234", "Car"))
print(parking_lot.park_vehicle("KA-01-9999", "Truck"))

print(parking_lot.park_vehicle("KA-01-1234", "Car"))

print(parking_lot.park_vehicle("KA-01-9722", "Truck"))
print(parking_lot.park_vehicle("KA-01-1221", "Car"))
print(parking_lot.park_vehicle("KA-01-9927", "Truck"))

print(parking_lot.get_available_spots())

print(parking_lot.is_full())

print(parking_lot.get_vehicle_location("KA-01-5678"))
