input_directory = "../input/RMK"
output_directory = "../output/"

region_path = f"{input_directory}/base.shp"
excludes_path = f"{input_directory}/exclude"
includes_path = f"{input_directory}/include"
restricted_path = f"{input_directory}/restricted"

base_area = {"source": region_path}

glaes_filename = "GLAES"
glaes_pixel_resolutions = [1, 10, 100]

includes = [
    {"source": f"{includes_path}/Benachteiligte Gebiete.shp", "mode": "include"},
    {
        "source": f"{includes_path}/Deponie.shp",
        "mode": "include",
        "where": "zustand = '2100' and funktion = '8100'",
    },
    {
        "source": f"{includes_path}/Schienennetz.shp",
        "buffer": 110,
        "mode": "include",
    },
    {
        "source": f"{includes_path}/Tagebau.shp",
        "mode": "include",
        "where": "zustand = '2100' and art = '3110'",
    },
]

excludes = [
    {"source": f"{excludes_path}/Alle Straßen.shp", "buffer": 2.5},
    {"source": f"{excludes_path}/Schienennetz.shp", "buffer": 22.5},
    {
        "source": f"{excludes_path}/Biosphaerengebiet Kernzone.shp",
        "where": "ZONE = 'Kernzone'",
    },
    {"source": f"{excludes_path}/Flächenhafte Naturdenkmal.shp"},
    {
        "source": f"{excludes_path}/Gebäude.shp",
        "buffer": 10,
        "where": "GFK not in ('31001_1313')",
    },
    {"source": f"{excludes_path}/Nationalparke.shp"},
    {"source": f"{excludes_path}/Naturschutzgebiete.shp"},
    {"source": f"{excludes_path}/Offenlandkartierung Biotope.shp"},
    {"source": f"{excludes_path}/Stehende Gewaesser.shp"},
    {"source": f"{excludes_path}/Straßen.shp", "buffer": 22.5},
    {"source": f"{excludes_path}/Waldkartierung Biotope.shp"},
    {
        "source": f"{excludes_path}/Wasserschutzgebiete.shp",
        "where": "ZONE = 'Zone I und II bzw. IIA'",
    },
    {"source": f"{excludes_path}/Überschwemmungsgebiete HQ100.shp"},
    {"source": f"{excludes_path}/Forstwirtschaft.shp"},
    {"source": f"{excludes_path}/Wohnnutzung.shp"},
    {"source": f"{excludes_path}/Straßen und Wege.shp"},
    {"source": f"{excludes_path}/Bestattung.shp"},
    {"source": f"{excludes_path}/Sportanlage.shp"},
    {"source": f"{excludes_path}/Freizeitanlage.shp"},
    {"source": f"{excludes_path}/Kultur.shp"},
    {"source": f"{excludes_path}/Öffentlich.shp"},
    {"source": f"{excludes_path}/Freiluft.shp"},
    {"source": f"{excludes_path}/Gewerbe.shp"},
    {"source": f"{excludes_path}/Industrie.shp"},
    {"source": f"{excludes_path}/Bahnverkehr.shp"},
    {"source": f"{excludes_path}/Versorgung.shp"},
]

restricted = [
    {"source": f"{restricted_path}/Biosphaerengebiet Kernzone.shp"},
    {"source": f"{restricted_path}/Biotopverbund Kernflaeche feucht.shp"},
    {"source": f"{restricted_path}/Biotopverbund Kernflaeche Mittel.shp"},
    {"source": f"{restricted_path}/Biotopverbund Kernflaeche trocken.shp"},
    {"source": f"{restricted_path}/Biotopverbund Kernraum feucht.shp"},
    {"source": f"{restricted_path}/Biotopverbund Kernraum Mittel.shp"},
    {"source": f"{restricted_path}/Biotopverbund Kernraum trocken.shp"},
    {"source": f"{restricted_path}/Biotopverbund Suchraum feucht.shp"},
    {"source": f"{restricted_path}/Biotopverbund Suchraum Mittel.shp"},
    {"source": f"{restricted_path}/Biotopverbund Suchraum trocken.shp"},
    {"source": f"{restricted_path}/Generalwildwegeplan.shp", "buffer": 1000},
    {"source": f"{restricted_path}/Landschaftsschutzgebiete.shp"},
    {"source": f"{restricted_path}/Natura 2000 FFH.shp"},
    {"source": f"{restricted_path}/Natura 2000 Vogelschutzgebiete.shp"},
]
