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

This will run GLAES 10 times for every `pixel_resolution`specified in shared.py, measure the runtime and finally write 
the resulting eligible areas to `output/GLAES_{pixel_resolution}.tif`.
If you are not interested in the runtime evaluation, comment the line containing `timeit.Timer(run).repeat`.

### Running VELEA
Activate the corresponding environment and run `main_velea.py`. 


    cd src
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


    cd src
    conda activate eval-environment-velea
    python main_velea.py

### Running the evaluation
After running VELEA run `iou_lubw.py` to read the results from the previous step and then calculate the resulting area 
sizes and the intersection over union.  The results will be printed to the console. 

    cd src
    conda activate eval-environment-velea
    python iou_lubw.py

## Used data sources
See the [LUBW criteria table](https://www.energieatlas-bw.de/documents/24384/131240/Kriterienkatalog+PV-Freifl%C3%A4chenpotenzial/91272bce-aac1-4010-87fd-92da0854d28f)
(in German).



## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.
