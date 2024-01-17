import os


def read_earthquakes(file_name):
    script_path = os.path.abspath(__file__)
    file_path = os.path.join(os.path.dirname(script_path), file_name)
    earthquakes = {}
    with open(file_path, "r") as file:
        for line in file:
            (
                magnitude,
                date,
                _,
                _,
                _,
                _,
                *region_parts,
            ) = line.split()
            region = region_parts[-1].strip()
            region_earthquakes = earthquakes.get(region, [])
            region_earthquakes.append({"date": date, "magnitude": magnitude})
            earthquakes[region] = region_earthquakes
    return earthquakes


def write_earthquakes(earthquakes, file_name):
    script_path = os.path.abspath(__file__)
    file_path = os.path.join(os.path.dirname(script_path), file_name)
    # Open a file in 'w' (write) mode
    with open(file_path, "w") as file:
        # Write lines to the file
        for region, region_earthquakes in earthquakes.items():
            file.write(f"[{region}")
            for earthquake in region_earthquakes:
                file.write(f", [{earthquake['date']}, {earthquake['magnitude']}]")
            file.write(']\n')

def main():
    earthquakes = read_earthquakes("earthquake.txt")
    write_earthquakes(earthquakes, "earthquakefmt.txt")


if __name__ == "__main__":
    main()
