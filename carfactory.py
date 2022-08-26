from car import Car
from datetime import datetime
from engine import *
from battery import *


class CarFactory():
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpinderBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpinderBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_is_on: bool) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpinderBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
