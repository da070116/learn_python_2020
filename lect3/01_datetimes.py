from datetime import datetime, timedelta

if __name__ == '__main__':
    dt_now = datetime.now()
    dt_generated = datetime(year=2022, month=2, day=2, hour=22, minute=22)
    delta = dt_generated - dt_now
    # shorter and more comfortable version
    delta = timedelta(days=1)
    dt_compared = datetime(year=2022, month=2, day=4, hour=22, minute=22)
    print(f'{dt_now = }\n{dt_generated = }\n{dt_compared = }\n{delta=}')
    # a few tests
    print('===========')
    test_values = (delta + delta, 2 * delta, 4 * delta // 2, delta, delta / 2)
    print(1, dt_generated == dt_now + delta)
    for index, value in enumerate(test_values):
        print(index + 2, f'{value=}', dt_generated + value == dt_compared)
    print(8, f'{dt_generated + delta / 2 = }')
    print(9, delta / 2)
    print('===========')
    # displaying data
    for dt_format in ('%d.%m.%Y %H:%M', '%Y-%m-%d', '%A %d %b %Y'):
        print(dt_now.strftime(dt_format))
