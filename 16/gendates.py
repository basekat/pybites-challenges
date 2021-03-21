from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    counter = 100
    while True:
        yield PYBITES_BORN + timedelta(days=counter)
        counter += 100
