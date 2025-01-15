import geopandas as gpd
import pandas as pd
from geopandas import GeoDataFrame

import shared

output_directory = shared.output_directory
conversion_factor = 10**6  # m^2 --> km^2


def intersection_over_union(df1: GeoDataFrame, df2: GeoDataFrame) -> float:
    intersection = df1.overlay(df2, how="intersection", keep_geom_type=True)
    union = df1.overlay(df2, how="union", keep_geom_type=True)
    return intersection.area.sum() / union.area.sum()


velea_eligible_gdf = gpd.read_file(f"{output_directory}/VELEA-eligible.gpkg")
velea_restricted_gdf = gpd.read_file(f"{output_directory}/VELEA-restricted.gpkg")


lubw_disadvantaged_gdf = gpd.read_file(
    f"{shared.input_directory}/LUBW/disadvantaged.shp"
)
lubw_conversion_gdf = gpd.read_file(f"{shared.input_directory}/LUBW/conversion.shp")
lubw_combined_gdf = GeoDataFrame(
    pd.concat([lubw_disadvantaged_gdf, lubw_conversion_gdf], ignore_index=True)
)

restricted_mask = (
    lubw_combined_gdf["HINWEIS"] == "Liegt innerhalb einer weichen Restriktionsfläche"
)

lubw_restricted_gdf = GeoDataFrame(
    geometry=list(lubw_combined_gdf[restricted_mask].union_all().geoms),
    crs=lubw_combined_gdf.crs,
)
lubw_eligible_gdf = GeoDataFrame(
    geometry=list(lubw_combined_gdf[~restricted_mask].union_all().geoms),
    crs=lubw_combined_gdf.crs,
)

velea_combined_gdf = GeoDataFrame(
    geometry=list(velea_eligible_gdf.union_all().geoms)
    + list(velea_restricted_gdf.union_all().geoms),
    crs=velea_eligible_gdf.crs,
)
print(f"VELEA overall size: {sum(velea_combined_gdf.area)/ conversion_factor:.4f}")

print(f"Calculating IoU overall")
iou_overall = intersection_over_union(
    velea_combined_gdf,
    lubw_combined_gdf,
)
print(f"IoU overall: {iou_overall:.4f}")
print(f"LUBW overall size: {sum(lubw_combined_gdf.area)/ conversion_factor:.4f}")

print(f"Calculating IoU for restricted areas")
iou_restricted = intersection_over_union(velea_restricted_gdf, lubw_restricted_gdf)
print(f"IoU for restricted areas: {iou_restricted:.4f}")
print(f"VELEA restricted size: {sum(velea_restricted_gdf.area)/ conversion_factor:.4f}")
print(f"LUBW restricted size: {sum(lubw_restricted_gdf.area)/ conversion_factor:.4f}")

print(f"Calculating IoU for eligible areas")
iou_eligible = intersection_over_union(velea_eligible_gdf, lubw_eligible_gdf)
print(f"IoU for eligible areas: {iou_eligible:.4f}")
print(f"VELEA eligible size: {sum(velea_eligible_gdf.area)/ conversion_factor:.4f}")
print(f"LUBW eligible size: {sum(lubw_eligible_gdf.area)/ conversion_factor:.4f}")
