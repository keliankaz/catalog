from __future__ import annotations
import pandas as pd
import os
from pathlib import Path
from src.data import EarthquakeCatalog

base_dir = Path(__file__).parents[2]


class ESTEarthquakeCatalog(EarthquakeCatalog):
    def __init__(self) -> EarthquakeCatalog:
        self.dir_name = os.path.join(
            os.path.join(base_dir, "Datasets/Seismicity_datasets/Japan")
        )
        self.file_name = "est2016-20.dat"
        _catalog = self.read_catalog(self.dir_name, self.file_name)

        super().__init__(_catalog)

    @staticmethod
    def read_catalog(dir_name, file_name):
        """
        Reads in a EST catalog and returns a pandas dataframe. Read each file in
         directory and concatenate them into one dataframe.
        """
        full_file_name = os.path.join(dir_name, file_name)

        column_names = [
            "datetime",
            "y",
            "m",
            "d",
            "H",
            "M",
            "S",
            "f",
            "lat",
            "lon",
            "dep",
            "mag",
            "meca_type",
            "repeater_idx",
            "event_idx",
            "event_idx_JMA",
            "event_idx_meca",
            "event_idx_repeater",
            "lat_JMA",
            "lon_JMA",
            "dep_JMA",
        ]

        df = pd.read_csv(
            full_file_name,
            header=None,
            sep=" ",
            names=column_names,
        )

        df["time"] = pd.to_datetime(
            df[["y", "m", "d", "H", "M", "S", "f"]].astype(str).agg("-".join, axis=1),
            format="%Y-%m-%d-%H-%M-%S-%f",
        )

        df["depth"] = df["dep"]

        return df


# class JMAEarthquakeCatalog(EarthquakeCatalog):
#     def __init__(self) -> EarthquakeCatalog:
#         self.dir_name = os.path.join(
#             os.path.join(base_dir, "Datasets/Seismicity_datasets/Japan")
#         )
#         self.file_name = "JMA.csv"
#         self.url = "https://www.data.jma.go.jp/eqev/data/bulletin/hypo_e.html"


#         # _catalog = self.read_catalog(self.dir_name, self.file_name)


#         # super().__init__(_catalog)

#     @staticmethod
#     def query_catalog(dir_name, file_name, url):
#         # Gets all the files in the web directory:
#         # https://www.data.jma.go.jp/eqev/data/bulletin/data/hypo/
#         # and downloads them to the local directory


#     @staticmethod
#     def read_catalog(dir_name, file_name):
#         """
#         Reads in a EST catalog and returns a pandas dataframe. Read each file in
#          directory and concatenate them into one dataframe.
#         """
#         full_file_name = os.path.join(dir_name, file_name)

#         column_names = [
#             "datetime",
#             "lat",
#             "lon",
#             "depth",
#             "mag",
#             "hypoflag_est",
#             "dotime_est",
#             "dolat_est",
#             "dolon_est",
#             "dodep_est",
#             "std_ditp_est",
#             "std_dits_est",
#             "ppick_est",
#             "19_est",
#             "20_est",
#             "bothps_est",
#             "22_est",
#             "23_est",
#             "24_est",
#             "pspicknear_est",
#             "26_est",
#             "27_est",
#             "fname_est",
#             "event_idx_est",
#             "event_idx_man",
#             "datetime_man",
#             "lat_man",
#             "lon_man",
#             "dep_man",
#             "mag_man",
#             "dt",
#             "dlat",
#             "dlon",
#             "dho",
#             "ddep",
#             "dmag",
#         ]

#         df = pd.read_csv(
#             full_file_name,
#             header=0,
#             sep=",",
#             skiprows=1,
#             names=column_names,
#             engine="python",
#         )

#         df["time"] = pd.to_datetime(df.datetime)

#         return df
