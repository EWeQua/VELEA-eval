import timeit

from glaes import ExclusionCalculator

from src.shared_paths import region_path, includes, excludes, output_directory

pixel_resolutions = [1, 10, 100]
number_of_repetitions = 10


def run():
    ec = ExclusionCalculator(region_path, srs=3035, pixelRes=pixel_resolution, initialValue=False)
    for include in includes:
        ec.excludeVectorType(**include)
    for exclude in excludes:
        ec.excludeVectorType(**exclude)
    return ec


for pixel_resolution in pixel_resolutions:
    print(f'Running GLAES {number_of_repetitions} times with a pixel resolution of {pixel_resolution}')
    timer = timeit.Timer(run).repeat(number=1, repeat=number_of_repetitions)
    print(f'Runtimes of GLAES with pixel resolution of {pixel_resolution}:')
    print(timer)
    print(f'Minimum runtime of GLAES with pixel resolution of {pixel_resolution}: {min(timer):.2f}')

    exclusion_calculator = run()
    exclusion_calculator.save(f'{output_directory}/GLAES_{pixel_resolution}.tif')

    # exclusion_calculator.draw()
