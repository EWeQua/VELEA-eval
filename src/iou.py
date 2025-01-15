import geopandas as gpd
import pandas as pd
import rasterio
from geopandas import GeoDataFrame
from rasterio.features import shapes

import shared

output_directory = shared.output_directory
conversion_factor = 10**6  # m^2 --> km^2


def vectorize(path: str) -> GeoDataFrame:
    # Inspired by https://gis.stackexchange.com/questions/187877/how-to-polygonize-raster-to-shapely-polygons
    with rasterio.Env():
        with rasterio.open(path) as src:
            image = src.read(1)  # first band
            geoms = [
                {"properties": {"raster_val": v}, "geometry": s}
                for _, (s, v) in enumerate(shapes(image, transform=src.transform))
                # We're only interested in the eligible areas (v == 100) --> drop other values
                if v == 100
            ]
    return gpd.GeoDataFrame.from_features(geoms, crs="EPSG:25832")


def intersection_over_union(df1: GeoDataFrame, df2: GeoDataFrame) -> float:
    intersection = df1.overlay(df2, how="intersection", keep_geom_type=True)
    union = df1.overlay(df2, how="union", keep_geom_type=True)
    return intersection.area.sum() / union.area.sum()


velea_eligible_gdf = gpd.read_file(f"{output_directory}/VELEA-eligible.gpkg")
velea_restricted_gdf = gpd.read_file(f"{output_directory}/VELEA-restricted.gpkg")
velea_gdf = gpd.GeoDataFrame(
    pd.concat([velea_eligible_gdf, velea_restricted_gdf], ignore_index=True)
)
velea_gdf = GeoDataFrame(
    geometry=list(velea_gdf.union_all().geoms),
    crs=velea_gdf.crs,
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
