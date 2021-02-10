import logging
from typing import Optional, List, Any

import gpuz.utility as utility
from pathlib import Path
import os

import pandas as pd
from pandas.core.frame import DataFrame

import numpy as np
import matplotlib as mp


# Logging configuration only includes the timestamp in human readable format
logging.basicConfig(format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    level=logging.DEBUG)

class DataHelper:
    def __init__(self, root_dir: str) -> None:
        self.root_dir = root_dir
        logging.info( f"DataHelper working on root dir \"{root_dir}\" with"
            f"\n\t - Dataset dir     = {self.data_dir}"
            f"\n\t - Work dataset dir= {self.work_dir}"
         )

        if not self.work_dir.exists():
            logging.debug( f"Work dir {self.work_dir} does not exist: creating it ..." )
            self.work_dir.mkdir()

    @property
    def data_dir(self) -> Path:
        return Path(self.root_dir) / "datasets"

    @property
    def work_dir(self) -> Path:
        return Path(self.root_dir)  / "datasets_work"

    def get_dataset_path(self, dataset_name: str) -> str:
        dataset_path = self.data_dir / dataset_name
        return str(dataset_path)

    def get_work_dataset_path(self, dataset_name: str) -> str:
        dataset_path = self.work_dir / dataset_name
        return str(dataset_path)

    def create_clean_csv_dataset(self, dataset_name: str, clean_dataset_name: str) -> None:
        original_dataset_path =  self.get_dataset_path(dataset_name)
        clean_dataset_path =  self.get_work_dataset_path(clean_dataset_name)

        utility.preprocess_gpuz_log_file(original_dataset_path, clean_dataset_path)

    def load_gpuz_dataset(self, dataset_name: str) -> DataFrame:
        dataset_path = self.get_work_dataset_path(dataset_name)

        df: DataFrame = pd.read_csv( dataset_path )
        # Force the right column data types
        for column in df.columns:
            print( column )
            if str(column) == "date":
                df[column] = pd.to_datetime( df[column], errors="coerce" )
            else:
                df[column] = pd.to_numeric( df[column], errors="coerce" )

        return df

if __name__ == "__main__":
    root_dir = os.getcwd()
    data_helper = DataHelper( root_dir )    
    data_helper.create_clean_csv_dataset( "gpuz_sensor_log.txt", "clean_gpuz_sensor_log.csv" )
