from velea import EligibilityAnalysis

from src.shared_paths import regionPath, includes, excludes, output_directory

base_area = {"source": regionPath}

eligible_areas, restricted_areas = EligibilityAnalysis(
    base_area,
    includes,
    excludes,
    sliver_threshold=100,
    crs="EPSG:25832",
).execute()
eligible_areas.to_file(f"{output_directory}/PV-BW.gpkg")
restricted_areas.to_file(f"{output_directory}/PV-BW-restricted.gpkg")
