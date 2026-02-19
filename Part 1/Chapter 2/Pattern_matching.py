def match_command(pattern):
    match pattern:
        case [sound, freq]:
            return "Detected sound"
        case ["Throttle", angle, acceleration]:
            return "Throttling"
        case ["Light", r, g, b]:
            return "Red: ", r, " Blue: ", b, " Green: ", g
        case _:
            return "Default case - Matched no other command"

print(match_command([1, 5]))
print(match_command(["Throttle", 4.5, 98])) # throttle str must be first in pattern to be matched
print(match_command(["Light", 0.6, 332, 78.1]))
print(match_command(1))


metro_areas = [
    ('Delhi', 'IN', '10', (35.35836, 32.28787)),
    ('New York', 'US', '9', (64.8869, -72.78877)),
    ('Tokyo', 'Japan', '5.5', (-110.84848, 100.7474))
]

for record in metro_areas:
    match record:
        case [str(name), *_, (float(lat), float(lon))] if lon >= 100: # name must be a str
            # lat, lon must be floats
            # *_ means match any number of items
            print(f"Name: {name}")
