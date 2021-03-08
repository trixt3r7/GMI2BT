import concurrent.futures
import multiprocessing
import psutil
import time
import numpy as np


def logo():
    print(r"___ _  _ ____    _  _ ____ _   _    ____ _ _  _ ___  ____ ____ ")
    print(r" |  |__| |___    |_/  |___  \_/     |___ | |\ | |  \ |___ |__/ ")
    print(r" |  |  | |___    | \_ |___   |      |    | | \| |__/ |___ |  \ ")
    print()


def menu():
    print(f'+——[  Choose Brute force difficulty  ]———————————————————————+')
    print('    1. Easy | 2. Normal | 3. Difficult')
    print('    4. Difficult with Static value (quick) | 5. QUIT')
    print(f'+————————————————————————————————————————————————————————————+')


# init global variables for processes
def init_globals(key_not_found, secret_key):
    global KEY_NOT_FOUND
    global SECRET_KEY
    KEY_NOT_FOUND = key_not_found
    SECRET_KEY = secret_key


def create_keyspaces(cpu, max_num):
    """
    Divide key range between each cpu core,
    creates two lists with start values and second with end values.\n
    :param cpu: number of cpu cores
    :param max_num: 0 to highest given value
    :return: A dictionary: {'start': [], 'end': []}
    """
    offset = int(max_num / cpu)
    offset_temp = offset
    start_keys_list = [0]
    end_keys_list = []
    for core in range(cpu):
        start_keys_list.append(offset)
        end_keys_list.append(offset)
        offset += offset_temp
    start_keys_list.pop()
    end_keys_list.pop()
    end_keys_list.append(max_num)
    return {'start': start_keys_list, 'end': end_keys_list}


def find_key(cpu, current_key, end_key):
    print(f'    CPU{cpu} key range: {current_key:,} - {end_key:,}')

    while KEY_NOT_FOUND.value and (current_key <= end_key):
        if current_key == SECRET_KEY:
            KEY_NOT_FOUND.value = False
            line1 = f'+——————————————————————————————————————————————+\n'
            line2 = f'    SECRET KEY FOUND by CPU{cpu}: {current_key:,}\n'
            line3 = f'+——————————————————————————————————————————————+'
            return f'{line1}{line2}{line3}'
        else:
            current_key += 1
        if current_key % 1000000 == 0:
            print(f'    CPU: {cpu} is at value: {current_key:,}')
    return f'    CPU: {cpu} reached key: {current_key:,}'


def average_kps(key, start, time_done, cpu_cores):
    '''Calculate keys checked per second based on the cpu core that finds the key'''
    i = 0
    start_key = 0
    while cpu_cores > i and key > start[i]:
        i += 1
        start_key = start[i - 1]
    return ((key - start_key) / time_done) * cpu_cores


def main():
    # Lookup number of cores on processor including Logical cores (Hyper Threading)
    cpu_cores = psutil.cpu_count(logical=True)
    # Make a list to name each cpu-core with a number
    cpus = []
    for i in range(cpu_cores):
        cpus.append(i)

    keyspace = create_keyspaces(cpu_cores, max_value)

    # Variables to be shared between processes
    key_not_found = multiprocessing.Value('i', True)
    secret_key = np.random.randint(low=0, high=max_value, dtype=np.uint32)
    if choice == '4':
        secret_key = 1000000  # Quick Brute Force, to show time it would take to go through all keys

    print(f'+——[  SETTINGS  ]————————————————————————————————————————————+')
    print(f'    CPU Count: {cpu_cores}')
    print(f'    Key Range: 0 - {max_value:,}')
    print(f'    (Random secret key: {secret_key:,})')
    print(f'\n+——[  KEY RANGES & PROCESS  ]————————————————————————————————+')

    # Start timer
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_cores, initializer=init_globals,
                                                initargs=(key_not_found, secret_key,)) as executor:
        for result in executor.map(find_key, cpus, keyspace["start"], keyspace["end"]):
            print(result)

    # Stop timer
    finish = time.perf_counter()
    time_taken = finish - start
    keys_per_sec = average_kps(secret_key, keyspace["start"], time_taken, cpu_cores)
    timestamp = time.strftime('%H:%M:%S', time.gmtime(int(max_value / keys_per_sec)))

    print(f'\n+——[  STATISTICS  ]——————————————————————————————————————————+')
    print(f'    Finished in {round(time_taken, 2)} seconds')
    print(f'    Average {round(keys_per_sec)} keys per second')
    print(f'    Time to check entire keyspace: {timestamp} ')
    print(f'+————————————————————————————————————————————————————————————+')


if __name__ == '__main__':
    # Menu Loop
    while True:
        logo()
        menu()
        choice = input('    CHOOSE MENU ITEM: ')
        if choice == '1':
            max_value = np.uint32(5000000)  # SMALL value, will be very fast to find
            main()
        elif choice == '2':
            max_value = np.uint32(50000000)  # MEDIUM value, will likely take a little time
            main()
        elif choice == '3' or choice == '4':
            max_value = (np.iinfo(np.uint32)).max  # HIGHEST POSSIBLE value, will likely take very long time
            main()
        elif choice == '5':
            # Exit Program
            break
        else:
            print(f'+————————————————————————————————————————————————————————————+')
            print("    INVALID MENU ITEM, please try again.")
            print(f'+————————————————————————————————————————————————————————————+')
