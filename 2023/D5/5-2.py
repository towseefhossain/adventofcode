def create_dictionary(lines: list) -> dict:
    res = {}
    sorted_lines = sorted(lines, key=lambda x: x[0])
    for line in sorted_lines:
        key_start = line[1]
        value_start = line[0]
        number_of_iters = line[2]
        res[(key_start, key_start+number_of_iters-1)] = (value_start, value_start+number_of_iters-1)
    return res

def get_from_dict(key: int, dictionary: dict) -> int:
    for item in dictionary:
        # print(f'{item} -> {dictionary[item]}')
        if key < item[0] or key > item[1]:
            continue
        else:
            difference = key - item[0]
            return dictionary[item][0] + difference
    return key

def solve():
    seeds_with_ranges = []
    seed_to_soil_lines = []
    soil_to_fertilizer_lines = []
    fertilizer_to_water_lines = []
    water_to_light_lines = []
    light_to_temp_lines = []
    temp_to_hum_lines = []
    hum_to_location_lines = []
    curlist = None
    with open('day5.txt') as my_file:
        for line in my_file:
            if (len(line.strip()) == 0):
                continue
            elif line.startswith('seeds'):
                seeds_line = [int(x) for x in line.strip().split()[1:]]
                seeds = seeds_line[::2]
                ranges = seeds_line[1::2]
                seeds_with_ranges = zip(seeds, ranges)
                continue
            elif line.startswith('seed-to-soil'):
                curlist = seed_to_soil_lines
                continue
            elif line.startswith('soil-to-fertilizer'):
                curlist = soil_to_fertilizer_lines
                continue
            elif line.startswith('fertilizer-to-water'):
                curlist = fertilizer_to_water_lines
                continue
            elif line.startswith('water-to-light'):
                curlist = water_to_light_lines
                continue
            elif line.startswith('light-to-temperature'):
                curlist = light_to_temp_lines
                continue
            elif line.startswith('temperature-to-humidity'):
                curlist = temp_to_hum_lines
                continue
            elif line.startswith('humidity-to-location'):
                curlist = hum_to_location_lines
                continue
            else:
                curlist.append([int(x) for x in line.strip().split()])
    
    seed_to_soil_map = create_dictionary(seed_to_soil_lines)
    soil_to_fertilizer_map = create_dictionary(soil_to_fertilizer_lines)
    fertilizer_to_water_map = create_dictionary(fertilizer_to_water_lines)
    water_to_light_map = create_dictionary(water_to_light_lines)
    light_to_temp_map = create_dictionary(light_to_temp_lines)
    temp_to_hum_map = create_dictionary(temp_to_hum_lines)
    hum_to_location_map = create_dictionary(hum_to_location_lines)

    results = None
    for seed_range in seeds_with_ranges:
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            # print(f'seed -> {seed}')
            soil = get_from_dict(seed, seed_to_soil_map)
            # print(f'soil -> {soil}')
            fertilizer = get_from_dict(soil, soil_to_fertilizer_map)
            # print(f'fertilizer -> {fertilizer}')
            water = get_from_dict(fertilizer, fertilizer_to_water_map)
            # print(f'water -> {water}')
            light = get_from_dict(water, water_to_light_map)
            # print(f'light -> {light}')
            temperature = get_from_dict(light, light_to_temp_map)
            # print(f'temperature -> {temperature}')
            humidity = get_from_dict(temperature, temp_to_hum_map)
            # print(f'humidity -> {humidity}')
            location = get_from_dict(humidity, hum_to_location_map)
            # print(f'location -> {location}')
            if results is None or location < results:
                results = location
    
    print(results)


if __name__ == "__main__":
    solve()