import rasterio
from geopandas import GeoDataFrame
from rasterio.features import shapes


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
    return GeoDataFrame.from_features(geoms, crs="EPSG:25832")


def intersection_over_union(df1: GeoDataFrame, df2: GeoDataFrame) -> float:
    intersection = df1.overlay(df2, how="intersection", keep_geom_type=True)
    union = df1.overlay(df2, how="union", keep_geom_type=True)
    return intersection.area.sum() / union.area.sum()


def ensure_no_overlap(gdf: GeoDataFrame) -> GeoDataFrame:
    return GeoDataFrame(geometry=list(gdf.union_all().geoms), crs=gdf.crs)
