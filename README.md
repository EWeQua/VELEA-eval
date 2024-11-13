# VELEA-eval


## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Usage

This repo requires the use of the [conda](https://docs.conda.io/en/latest/) package manager. conda can be obtained by installing the 
[Anaconda Distribution](https://www.anaconda.com/distribution/), or [miniconda](https://docs.anaconda.com/miniconda/). See the[Conda installation docs](https://conda.io/docs/user-guide/install/download.html>)for more information.

### Acquire geodata
TODO
    
### Installing dependencies
Due to incompatibility of GLAES with newer Python versions, we decided to create two different conda environments,
one for running GLAES (`eval-environment-glaes`) and one for running VELEA and the evaluation (`eval-environment-velea`).
To create the required environments:

    cd velea-eval
    conda env create --file=environment-velea.yml
    conda env create --file=environment-glaes.yml

### Running GLAES
    cd src
    conda activate eval-environment-glaes
    python main_glaes.py

### Running VELEA
    cd src
    conda activate eval-environment-velea
    python main_velea.py

### Running the evaluation
    cd src
    conda activate eval-environment-velea
    python iou.py

## Used data sources
See the [LUBW criteria table](https://www.energieatlas-bw.de/documents/24384/131240/Kriterienkatalog+PV-Freifl%C3%A4chenpotenzial/91272bce-aac1-4010-87fd-92da0854d28f)
(in German).



## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.
