## Catalog

The repo contains a colleciton of methods to manipulate and download earthquake catalogs.

## Installation
The code has been tested on MacOS.


1. Make sure you have the latest version of [`conda`](https://docs.conda.io/en/latest/miniconda.html) installed.
2. Install the dependencies and create a new conda environment.
    ```bash
    conda env create -f environment.yml
    conda activate catalog
    ```

### Usage

``` python 
from earthquake import EarthquakeCatalog

data_directory = "./data"

earthquake_metadata = {
    "starttime": '1990-01-01',
    "endtime": '2023-01-01',
    "latitude_range": [-90,90],
    "longitude_range": [-180,180],
    "minimum_magnitude": 7, 
}

earthquakes = EarthquakeCatalog(
    filename = data_directory + "/global_earthquakes_7.csv",
    kwargs = earthquake_metadata,
)
```

### Ploting

A simple map of earthquakes can be generated as follows

```python
ax = earthquakes.plot_map()
```

