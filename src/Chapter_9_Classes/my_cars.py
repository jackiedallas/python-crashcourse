from car import Car, ElectricCar as EV


my_car = Car('Subaru', 'Impreza', 2017)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 65_000
my_car.read_odometer()
my_car.update_odometer(100)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.increment_odometer(-50)
my_car.read_odometer()

my_ev = EV('ford', 'mustang mach-e', 2025)
print(my_ev.get_descriptive_name())
my_ev.battery.set_battery_size(20)
my_ev.battery.get_range()
my_ev.battery.upgrade_battery()
my_ev.battery.describe_battery()
my_ev.battery.get_range()
