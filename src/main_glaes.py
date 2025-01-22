import timeit

from glaes import ExclusionCalculator

import shared

# If you are not interested in the runtime evaluation, set number_of_repetitions to 0
number_of_repetitions = 10


def run():
    ec = ExclusionCalculator(
        shared.region_path,
        srs=25832,
        pixelRes=pixel_resolution,
        initialValue=False,
    )
    for include in shared.includes:
        ec.excludeVectorType(**include)
    for exclude in shared.excludes:
        ec.excludeVectorType(**exclude)
    return ec


for pixel_resolution in shared.glaes_pixel_resolutions:
    if number_of_repetitions > 0:
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
        f"{shared.output_directory}/{shared.glaes_filename}_{pixel_resolution}.tif"
    )

    # exclusion_calculator.draw()
