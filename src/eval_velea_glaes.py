import geopandas as gpd
import pandas as pd
from geopandas import GeoDataFrame

import shared
from helpers import ensure_no_overlap, vectorize, intersection_over_union

output_directory = shared.output_directory
conversion_factor = 10**6  # m^2 --> km^2

# Ensure no overlap in the geometries of VELEA-eligible
velea_eligible_gdf = ensure_no_overlap(
    gpd.read_file(f"{output_directory}/VELEA-eligible.gpkg")
)
# Ensure no overlap in the geometries of VELEA-restricted
velea_restricted_gdf = ensure_no_overlap(
    gpd.read_file(f"{output_directory}/VELEA-restricted.gpkg")
)
# Ensure no overlap in the combined geometries of VELEA-eligible and VELEA-restricted
velea_gdf = ensure_no_overlap(
    GeoDataFrame(
        pd.concat([velea_eligible_gdf, velea_restricted_gdf], ignore_index=True)
    )
)

print(f"VELEA overall size : {sum(velea_gdf.area) / conversion_factor:.4f}")
for resolution in shared.glaes_pixel_resolutions:
    path_to_file = f"{output_directory}/{shared.glaes_filename}_{resolution}"
    print(f"Vectorizing raster for resolution {resolution}")
    glaes_vector_gdf = vectorize(f"{path_to_file}.tif")
    print(f"Calculating IoU for resolution {resolution}")
    iou = intersection_over_union(glaes_vector_gdf, velea_gdf)
    print(f"IoU for resolution {resolution}: {iou:.4f}")
    print(
        f"GLAES overall size for resolution {resolution}: {sum(glaes_vector_gdf.area) / conversion_factor:.4f}"
    )
