from os import error
from typing import Any
from dateutil.parser import parse

import gpuz.utility
import pandas as pd
from pandas.core.frame import DataFrame

import numpy as np
import matplotlib as mp

#data_file = "../data/sample.txt"
data_file = "data/clean_gpuz_sensor_log.txt"

df: DataFrame = pd.read_csv( data_file )

for column in df.columns:
    print( column )
    if str(column) == "date":
        df[column] = pd.to_datetime( df[column], errors="coerce" )
    else:
        df[column] = pd.to_numeric( df[column], errors="coerce" )

print( df )

print( type(df) )
print( df.dtypes )
