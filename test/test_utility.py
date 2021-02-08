import sys
print( sys.path )
# content of test_expectation.py
import pytest
from pathlib import Path
import gpuz.utility as utility


@pytest.mark.parametrize( "test_input,expected", [
    ("        Date        ,", "date"),
    ("GPU Clock [MHz] , Memory Clock [MHz] , GPU Temperature [C] ", "gpu_clock,memory_clock,gpu_temperature" )
])
def test_normalize_column_name(test_input: str, expected: str) -> None:
    result = utility.normalize_column_name(test_input)

    assert result == expected


@pytest.mark.parametrize( "test_input,expected", [
    ("        Date        , GPU Clock [MHz] , Memory Clock [MHz] , GPU Temperature [C] , Fan Speed (%) [%] , Fan Speed (RPM) [RPM] , Memory Used [MB] , GPU Load [%] , Memory Controller Load [%] , Video Engine Load [%] , Bus Interface Load [%] , Board Power Draw [W] , GPU Chip Power Draw [W] , MVDDC Power Draw [W] , PCIe Slot Power [W] , PCIe Slot Voltage [V] , 8-Pin #1 Power [W] , 8-Pin #1 Voltage [V] , Power Consumption (%) [% TDP] , PerfCap Reason [] , GPU Voltage [V] , CPU Temperature [C] , System Memory Used [MB] ,",
     "date,gpu_clock,memory_clock,gpu_temperature,fan_speed,fan_speed_2,memory_used,gpu_load,memory_controller_load,video_engine_load,bus_interface_load,board_power_draw,gpu_chip_power_draw,mvddc_power_draw,pcie_slot_power,pcie_slot_voltage,8_pin_1_power,8_pin_1_voltage,power_consumption,perfcap_reason,gpu_voltage,cpu_temperature,system_memory_used")
])
def test_make_clean_header(test_input: str, expected: str) -> None:
    result = utility.normalize_column_names( test_input )

    assert result == expected

def test_preprocess(tmpdir):
    tmpfile =  p = Path(tmpdir) / "cleaned.csv"
    utility.preprocess_gpuz_log_file( "test/data/sample.txt", tmpfile )

    with open(tmpfile, "r") as processed:
        with open("test/data/expected_cleaned_sample.csv", "r") as expected:
            same = set(processed).intersection(expected)

    assert len(same) == 9 # rows expected
