import timeit

from velea import EligibilityAnalysis

from src.shared_paths import regionPath, includes, excludes, output_directory

number_of_repetitions = 10

base_area = {"source": regionPath}


def run():
    return EligibilityAnalysis(
        base_area,
        includes,
        excludes,
        sliver_threshold=0,
        crs="EPSG:25832",
    ).execute()


print(f'Running VELEA {number_of_repetitions} times')
timer = timeit.Timer(run).repeat(number=1, repeat=number_of_repetitions)
print(f'Runtimes of VELEA:')
print(timer)
print(f'Minimum runtime of VELEA: {min(timer):.2f}')

eligible_areas, restricted_areas = EligibilityAnalysis(
    base_area,
    includes,
    excludes,
    sliver_threshold=0,
    crs="EPSG:25832",
).execute()
eligible_areas.to_file(f"{output_directory}/VELEA-eligible.gpkg")
restricted_areas.to_file(f"{output_directory}/VELEA-restricted.gpkg")
