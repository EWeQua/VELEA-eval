import geopandas as gpd
import osmnx

import shared

base_area = gpd.read_file(f"{shared.input_directory}/base.shp").to_crs(epsg=4326)

shared_parameters = {
    "polygon": base_area.iloc[0]["geometry"],
    "retain_all": True,
    "truncate_by_edge": True,
}

filename_params_tuples = [
    (
        f"{shared.input_directory}/Autobahnen.shp",
        {"custom_filter": "['highway'~'motorway|trunk']"} | shared_parameters,
    ),
    (
        f"{shared.input_directory}/Straßen.shp",
        {"network_type": "drive"} | shared_parameters,
    ),
    (
        f"{shared.input_directory}/Alle Straßen.shp",
        {"network_type": "all_public"} | shared_parameters,
    ),
    (
        f"{shared.input_directory}/Schienennetz.shp",
        {"custom_filter": "['railway'~'rail|disused|tram']"} | shared_parameters,
    ),
]

for filename, params in filename_params_tuples:
    print(f"Downloading to {filename}")
    graph = osmnx.graph.graph_from_polygon(**params)
    gdf = osmnx.convert.graph_to_gdfs(graph, nodes=False, edges=True)
    gdf = gdf.to_crs(epsg=25832)
    gdf[["geometry"]].to_file(filename)
