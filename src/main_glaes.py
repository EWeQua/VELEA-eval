import timeit

from glaes import ExclusionCalculator

import shared_paths

pixel_resolutions = [0.5, 0.1, 1, 10, 100]
number_of_repetitions = 10


def run():
    ec = ExclusionCalculator(
        shared_paths.region_path,
        srs=25832,
        pixelRes=pixel_resolution,
        initialValue=False,
    )
    for include in shared_paths.includes:
        ec.excludeVectorType(**include)
    for exclude in shared_paths.excludes:
        ec.excludeVectorType(**exclude)
    # ec.pruneIsolatedAreas(minSize=100)
    return ec


for pixel_resolution in pixel_resolutions:
    print(
        f"Running GLAES {number_of_repetitions} times with a pixel resolution of {pixel_resolution}"
    )
    timer = timeit.Timer(run).repeat(number=1, repeat=number_of_repetitions)
    print(f"Runtimes of GLAES with pixel resolution of {pixel_resolution}:")
    print(timer)
    print(
        f"Minimum runtime of GLAES with pixel resolution of {pixel_resolution}: {min(timer):.2f}"
    )

    exclusion_calculator = run()
    exclusion_calculator.save(
        f"{shared_paths.output_directory}/GLAES_{pixel_resolution}.tif"
    )

    # exclusion_calculator.draw()
