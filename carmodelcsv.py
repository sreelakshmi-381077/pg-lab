import csv
field_name = ['no','company','car model']
car = [
    {'no': 1,'company': 'ferrari', "car model": 'GH'},
    {'no': 2, 'company': 'BMW', "car model": 'X5'},
    {'no': 3,'company': 'Maruti suzuki', "car model": 'swift'},
    {'no': 4,'company': 'audi', "car model": 'RS7'},
    {'no': 5, 'company': 'Toyota', "car model": 'Fortuner'},
]
with open ('car.csv','w', newline ='') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open ('car.csv', newline ='') as csvfile:
    d = csv.reader(csvfile)
    for r in d:
        print (','.join(r))
        print (r)


output
        no, company, car
        model
        ['no', 'company', 'car model']
        1, ferrari, GH
        ['1', 'ferrari', 'GH']
        2, BMW, X5
        ['2', 'BMW', 'X5']
        3, Maruti
        suzuki, swift
        ['3', 'Maruti suzuki', 'swift']
        4, audi, RS7
        ['4', 'audi', 'RS7']
        5, Toyota, Fortuner
        ['5', 'Toyota', 'Fortuner']