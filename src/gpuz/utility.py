import re
from typing import List


def normalize_column_name(original_column_name: str) -> str:
    """Normalize a single column name by replacing whitespaces, special characters like '[' and '('"""
    wip = original_column_name.lower()
    wip = re.sub(r"(\([^\)]*\))", "", wip) # replace things like "(MHz)" and "(RPM)"
    wip = re.sub(r"(\[[^\]]*\])", "", wip) # replace things like "[%]" and "[MHz]"
    wip = re.sub(r"([\s]+,[\s]*)", ",", wip) # replace things like "   , " with ","
    wip = re.sub(r"(,[\s]*$)", "", wip) # remove any trailing ","

    wip = wip.strip()
    wip = re.sub(r"[\s#-]+", "_", wip) # replace things like "[%]" and "[MHz]"

    return wip


def normalize_column_names(original_header_line: str) -> str:
    """Normalize all the header names and resolves eventual name conflicts"""
    original_column_names: List[str] = original_header_line.split(",")
    # Remove empty strings (typically due to trailing ",")
    original_column_names[:] = [x for x in original_column_names if x]

    column_name_instances = {}
    def process_column_name(column_name):
        column_name = normalize_column_name( column_name )

        # Manage eventual name conflicts due to the normalization process
        if column_name in column_name_instances:
            n = column_name_instances[column_name] + 1
            column_name_instances[column_name] = n

            column_name = f"{column_name}_{n}"
        else: 
            column_name_instances[column_name] = 1

        return column_name

    column_names = []
    for original_column_name in original_column_names:
        column_name = process_column_name( original_column_name )

        column_names.append(column_name)

    return ",".join(column_names)


def preprocess_gpuz_log_file( input_csv_file: str, output_csv_file: str ) -> None:
    """Process GPU-Z Log file, removing any non-data rows and normalizing header names"""

    print( f"Processing {input_csv_file} into {output_csv_file} ..." )

    header_line_parsed = False
    with open( input_csv_file, "r" ) as input:
        with open( output_csv_file, "w" ) as output:
            for line in input:
                should_write_line = True

                line = line.strip()
                
                if line.startswith( "Date" ):
                    if not header_line_parsed:
                        line = normalize_column_names( line )
                        header_line_parsed = True
                    else:
                        should_write_line = False
                else:
                    # there is a trailing "," for data lines ...
                    line = re.sub(r"(,[\s]*$)", "", line) # remove any trailing ","

                if should_write_line:
                    output.write( line )
                    output.write( "\n" )

    print("Done!")

ZIP_FILE_EXTENSION=".zip"

def preprocess_gpuz_log_file_zipped( input_csv_file: str, output_csv_file: str ) -> None:
    is_input_zipped = input_csv_file.endswith( ZIP_FILE_EXTENSION)
    is_output_zipped = output_csv_file.endswith( ZIP_FILE_EXTENSION)

    # TODO Assume some conventions


if __name__ == "__main__":
    preprocess_gpuz_log_file( "datasets/gpuz_sensor_log.txt", "datasets/clean_gpuz_sensor_log.csv" )