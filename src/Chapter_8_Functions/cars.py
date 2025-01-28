def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

new_car = make_car('chevrolet', 'impala', color='black', transmission='manual', year=1987, isClassic=True)

print(new_car)