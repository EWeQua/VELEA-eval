import geopandas as gpd

import shared

extent = gpd.read_file(f"{shared.input_directory}/base.shp")

files_to_clip = [
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221330_ln_versorgungundentsorgung",
        f"{shared.excludes_path}/Versorgung.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "222100_ln_strassenundwegeverkehr",
        f"{shared.excludes_path}/Straßen und Wege.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221500_ln_bestattung",
        f"{shared.excludes_path}/Bestattung.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221430_ln_sportanlage",
        f"{shared.excludes_path}/Sportanlage.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221420_ln_freizeitanlage",
        f"{shared.excludes_path}/Freizeitanlage.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221220_ln_kulturundunterhaltung",
        f"{shared.excludes_path}/Kultur.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221210_ln_oeffentlicheeinrichtungen",
        f"{shared.excludes_path}/Öffentlich.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221410_ln_freiluftundnaherholung",
        f"{shared.excludes_path}/Freiluft.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221310_ln_gewerblichedienstleistungen",
        f"{shared.excludes_path}/Gewerbe.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "221320_ln_industrieundverarbeitendesgewerbe",
        f"{shared.excludes_path}/Industrie.shp",
    ),
    (
        f"{shared.input_directory}/bw_32_ln_2024_01.gpkg",
        "222200_ln_bahnverkehr",
        f"{shared.excludes_path}/Bahnverkehr.shp",
    ),
]

for filename, layer, filename_clipped in files_to_clip:
    gdf = gpd.read_file(filename, layer=layer)
    clipped_gdf = gdf.clip(extent)
    clipped_gdf.to_file(filename_clipped)
    print(f'{{"source": "{{excludes_path}}/{filename_clipped}"}},')
