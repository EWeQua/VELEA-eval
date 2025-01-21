import timeit

from velea import EligibilityAnalysis

import shared

# If you are not interested in the runtime evaluation, set number_of_repetitions to 0
number_of_repetitions = 10


def run():
    return EligibilityAnalysis(
        shared.base_area,
        shared.includes,
        shared.excludes,
        shared.restricted,
        sliver_threshold=None,
        crs="EPSG:25832",
    ).execute()


if number_of_repetitions > 0:
    print(f"Running VELEA {number_of_repetitions} times")
    timer = timeit.Timer(run).repeat(number=1, repeat=number_of_repetitions)
    print(f"Runtimes of VELEA:")
    print(timer)
    print(f"Minimum runtime of VELEA: {min(timer):.2f}")

eligible_areas, restricted_areas = run()
eligible_areas.to_file(f"{shared.output_directory}/VELEA-eligible.gpkg")
restricted_areas.to_file(f"{shared.output_directory}/VELEA-restricted.gpkg")
