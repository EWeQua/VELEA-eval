import geopandas as gpd
import rasterio
from geopandas import GeoDataFrame
from rasterio.features import shapes

output_directory = "../output/"

filename = "GLAES"
resolutions = [1, 10, 100]


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


velea_gdf = gpd.read_file(f"{output_directory}/VELEA-eligible.gpkg")
for resolution in resolutions:
    path_to_file = f"{output_directory}/{filename}_{resolution}"
    print(f"Vectorizing raster for resolution {resolution}")
    glaes_vector_gdf = vectorize(f"{path_to_file}.tif")
    # glaes_vector_gdf.to_file(f"{path_to_file}.gpkg")
    print(f"Calculating IoU for resolution {resolution}")
    iou = intersection_over_union(glaes_vector_gdf, velea_gdf)
    print(f"IoU for resolution {resolution}: {iou:.2f}")
