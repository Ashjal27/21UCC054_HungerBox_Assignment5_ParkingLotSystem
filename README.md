# 21UCC054_HungerBox_Assignment5_ParkingLotSystem

## Overview

This project implements a Parking Lot System that efficiently manages parking spaces across multiple floors. The system assigns the nearest available parking spot to vehicles and allows for easy tracking of parked vehicles.

## Features

- Supports multiple floors with a fixed number of parking spots per floor.

- Handles different vehicle types:

  - Bike → 1 spot

  - Car → 1 spot

  - Truck → 2 consecutive spots

- Assigns the nearest available spot upon vehicle entry.

- Allows vehicles to exit, freeing up their spots.

- Provides queries for:

  - Available spots per floor.

  - Whether the parking lot is full.

  - Current location of a parked vehicle.

- Implements concurrency handling for parallel parking operations.

- Optimized for quick vehicle lookups.
