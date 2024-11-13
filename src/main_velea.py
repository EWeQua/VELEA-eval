import timeit

from velea import EligibilityAnalysis

import shared

number_of_repetitions = 10

base_area = {"source": shared.region_path}


def run():
    return EligibilityAnalysis(
        base_area,
        shared.includes,
        shared.excludes,
        shared.restricted,
        sliver_threshold=100,
        crs="EPSG:25832",
    ).execute()


print(f"Running VELEA {number_of_repetitions} times")
timer = timeit.Timer(run).repeat(number=1, repeat=number_of_repetitions)
print(f"Runtimes of VELEA:")
print(timer)
print(f"Minimum runtime of VELEA: {min(timer):.2f}")

eligible_areas, restricted_areas = run()
eligible_areas.to_file(f"{shared.output_directory}/VELEA-eligible.gpkg")
restricted_areas.to_file(f"{shared.output_directory}/VELEA-restricted.gpkg")
