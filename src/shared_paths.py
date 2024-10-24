input_directory = '../input/RMK'
output_directory = '../output/'

regionPath = f"{input_directory}/base.shp"
excludesPath = f"{input_directory}/exclude"
includesPath = f"{input_directory}/include"

base_area = {"source": regionPath}

# includes = [f"{includesPath}/{file}" for file in os.listdir(includesPath) if file.endswith(".shp")]
includes = [
    {"source": f"{input_directory}/include/Benachteiligte Gebiete.shp", "mode": "include"},
    {"source": f"{input_directory}/include/Deponie.shp", "mode": "include",
     "where": "zustand = '2100' and funktion = '8100'"},
    {
        "source": f"{input_directory}/include/Schienennetz.shp",
        "buffer": 120,
        "mode": "include",
    },
    {"source": f"{input_directory}/include/Tagebau.shp", "mode": "include",
     "where": "zustand = '2100' and art = '3110'"},
]

excludes = [
    {'source': f'{input_directory}/exclude/Alle Straßen.shp',
     'buffer': 2.5},
    {'source': f'{input_directory}/exclude/Schienennetz.shp',
     'buffer': 20},
    {'source': f'{input_directory}/exclude/Biosphaerengebiet Kernzone.shp', 'where': "ZONE = 'Kernzone'"},
    {'source': f'{input_directory}/exclude/Flächenhafte Naturdenkmal.shp'},
    {'source': f'{input_directory}/exclude/Gebäude.shp', 'buffer': 10, "where": "GFK not in ('31001_1313')"},
    {'source': f'{input_directory}/exclude/Nationalparke.shp'},
    {'source': f'{input_directory}/exclude/Naturschutzgebiete.shp'},
    {'source': f'{input_directory}/exclude/Offenlandkartierung Biotope.shp'},
    {'source': f'{input_directory}/exclude/Stehende Gewaesser.shp'},
    {'source': f'{input_directory}/exclude/Straßen.shp',
     'buffer': 22.5},
    {'source': f'{input_directory}/exclude/Waldkartierung Biotope.shp'},
    {'source': f'{input_directory}/exclude/Wasserschutzgebiete.shp', 'where': "ZONE = 'Zone I und II bzw. IIA'"},
    {'source': f'{input_directory}/exclude/Überschwemmungsgebiete HQ100.shp'}
]
