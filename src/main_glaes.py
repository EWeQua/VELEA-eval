# Import GLAES
from glaes import ExclusionCalculator

from src.shared_paths import regionPath, includes, excludes, input_directory

ec = ExclusionCalculator(regionPath, srs=3035, pixelRes=1, initialValue=False)
for include in includes:
    print(include['source'])
    ec.excludeVectorType(**include)
for exclude in excludes:
    print(exclude['source'])
    ec.excludeVectorType(**exclude)
ec.save(f'{input_directory}/output.tif')
ec.draw()
import matplotlib.pyplot as plt

plt.show()
