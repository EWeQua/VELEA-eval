# VELEA-eval


## Description
This is the evaluation repo for VELEA - Vector-based Land Eligibility Analysis for Renewable Energy Sources.
See the [VELEA repo](https://github.com/EWeQua/VELEA) for further information on the purpose and functionality of VELEA.
This repo recreates the [open-field photovoltaic potential cadastre](https://www.energieatlas-bw.de/sonne/freiflachen/potenzial-freiflachenanlage) 
from the Baden-Württemberg State Institute for the Environment (German: Landesanstalt für Umwelt Baden-Württemberg, in 
short LUBW) using VELEA and [GLAES](https://github.com/FZJ-IEK3-VSA/glaes).
Then the results (runtime and eligible areas) are compared.

## Preparation

This repo requires the use of the [conda](https://docs.conda.io/en/latest/) package manager. conda can be obtained by installing the 
[Anaconda Distribution](https://www.anaconda.com/distribution/), or [miniconda](https://docs.anaconda.com/miniconda/). See the [Conda installation docs](https://conda.io/docs/user-guide/install/download.html>) for more information.

### Acquire geodata
TODO
    
### Installing dependencies
Due to incompatibility of GLAES with newer Python versions, we decided to create two separate conda environments,
one for running GLAES (`eval-environment-glaes`) and one for running VELEA and the evaluation (`eval-environment-velea`).
To create the required environments run:

    cd velea-eval
    conda env create --file=environment-velea.yml
    conda env create --file=environment-glaes.yml

## Comparison between VELEA and GLAES

### Running GLAES
Activate the corresponding environment and run `main_glaes.py`.

    cd src
    conda activate eval-environment-glaes
    python main_glaes.py

This will run GLAES 10 times for every `pixel_resolution` specified in shared.py, measure the runtime and finally write 
the resulting eligible areas to `output/GLAES_{pixel_resolution}.tif`.
If you are not interested in the runtime evaluation, comment the line containing `timeit.Timer(run).repeat`.

### Running VELEA
Activate the corresponding environment and run `main_velea.py`. 


    conda activate eval-environment-velea
    python main_velea.py

This will run VELEA 10 times, measure the runtime and finally write the resulting eligible areas to 
`output/VELEA-eligible.gpkg`.
If you are not interested in the runtime evaluation, comment the line containing `timeit.Timer(run).repeat`.

### Running the evaluation
After running GLAES and VELEA, activate the eval-environment-velea environment and run `iou.py` to read the results from
the previous steps and then calculate the resulting area sizes and the intersection over union.

    cd src
    conda activate eval-environment-velea
    python iou.py

## Comparison between VELEA and LUBW cadastre

### Running VELEA
Edit `main_velea.py` and set the sliver threshold to 100 by adding `sliver_threshold=100`:
````python
return EligibilityAnalysis(
        shared.base_area,
        shared.includes,
        shared.excludes,
        shared.restricted,
        sliver_threshold=100,
        crs="EPSG:25832",
    ).execute()
````
Also comment the line containing `timeit.Timer(run).repeat` to reduce runtime.

Activate the corresponding environment and run `main_velea.py`.


    conda activate eval-environment-velea
    python main_velea.py

### Running the evaluation
After running VELEA run `iou_lubw.py` to read the results from the previous step and then calculate the resulting area 
sizes and the intersection over union.  The results will be printed to the console. 

    conda activate eval-environment-velea
    python iou_lubw.py

## Used data sources
As mentioned in the paper, only parts of the used data for the LUBW cadastre are available as open data.
We filled the gaps with open data available. See the following list for the used data sources:

|                                                                           | Data source                                                                                                                                                             | License / Terms of use                                                               |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Landuse (in German: Landnutzung)                                          | https://www.lgl-bw.de/Produkte/Landschaftsmodelle/Landnutzung/index.html                                                                                                | https://www.govdata.de/dl-de/by-2-0                                                  |
| Buildings (in German: Gebäude)                                            | https://www.lgl-bw.de/Produkte/3D-Produkte/3D-Gebaeudemodelle/LoD2/                                                                                                     | https://www.govdata.de/dl-de/by-2-0                                                  |
| Roads and rail network (in German: Straßen- und Schienennetz)             | OpenStreetMap, see [osm_data_acquisition.py](/src/osm_data_acquisition.py)                                                                                              | https://opendatacommons.org/licenses/odbl/                                           |
| Biosphere area (in German: Biosphärengebiet)                              | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=c8bba771-0985-4f46-9ce4-44d6d9a7ff2c&q=Biosph%C3%A4ren&f=                                                         | https://www.govdata.de/dl-de/zero-2-0                                                |
| National parks (in German: Nationalparke)                                 | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=f596d907-1316-470d-a81e-418fb8b0f24d&q=nationalpark&f=                                                            | https://www.govdata.de/dl-de/zero-2-0                                                |
| Nature Reserve (in German: Naturschutzgebiete)                            | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=1a6a350d-97b6-4c73-8558-704d9fe8a29e&q=naturschutzgebiet&f=                                                       | https://www.govdata.de/dl-de/zero-2-0                                                |
| Natura 2000 bird protection (in German: Natura 2000 Vogelschutz)          | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=73f3dfdc-6c6e-4edc-b6fe-1d557ab10001&q=natura+2000&f=                                                             | https://www.govdata.de/dl-de/zero-2-0                                                |
| Natura 2000 FFH                                                           | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=2e5c0d70-f6d7-4c90-83a9-12fafed44b0e&q=natura+2000&f=                                                             | https://www.govdata.de/dl-de/zero-2-0                                                |
| Flood zones(in German: Überschwemmungsgebiete)                            | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=6a76f60b-d2ca-433e-80fb-6a0a708aea50                                                                              | https://www.lubw.baden-wuerttemberg.de/umweltinformationssystem/nutzungsvereinbarung |
| Natural monuments (in German: Naturdenkmal)                               | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=9a1e76ff-5481-435a-8841-67b03e98dca8&q=naturdenkmal&f=                                                            | https://www.lubw.baden-wuerttemberg.de/umweltinformationssystem/nutzungsvereinbarung |
| Water protection (in German: Wasserschutzgebiete)                         | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=19db48dd-576f-498c-bafa-083b200baad5&q=wasserschutz&f=                                                            | https://www.lubw.baden-wuerttemberg.de/umweltinformationssystem/nutzungsvereinbarung |
| Protected landscapes (in German: Landschaftsschutzgebiete)                | https://rips-metadaten.lubw.de/trefferanzeige?docuuid=e60e94f0-d7b5-4289-aea2-aed7280068c3&q=landschaftsschutz&f=                                                       | https://www.lubw.baden-wuerttemberg.de/umweltinformationssystem/nutzungsvereinbarung |
| Disadvantaged areas (in German: Benachteiligte Gebiete)                   | https://www.energieatlas-bw.de/documents/24384/128501/Benachteiligte_Gebiete_BW_1986_1997/098eb322-dde8-46d6-b60f-74c9205681ba                                          |                                                                                      |
| Biotopes, wildlife trails (in German: Biotopverbund, Generalwildwegeplan) | https://udo.lubw.baden-wuerttemberg.de/public/navigatorurl/show?globalId=naturLand.Biotopverbund.nais%3A%24SYSTEM%7BUDO_GEODOWNLOAD_URL%7Dnais%2FBV_Offenland_2020.html |                                                                                      |

See also the [LUBW criteria table](https://www.energieatlas-bw.de/documents/24384/131240/Kriterienkatalog+PV-Freifl%C3%A4chenpotenzial/91272bce-aac1-4010-87fd-92da0854d28f)
(in German).

## Authors and acknowledgment
This work was funded by the Bavarian State Ministry of Science and the Arts to promote applied research and development 
at universities of applied sciences and technical universities.
