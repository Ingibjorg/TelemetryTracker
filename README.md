# TelemetryTracker

**The TelemetryTracker.py runs on Windows and requires Python 3.6 and is an altered version of [Mouse-n-Key](https://github.com/pablotheissen/Mouse-n-Key)**

## Setup Telemetry Tracker
1. Install [Python 3.6](https://www.python.org/downloads/)
2. python -m pip install numpy
3. python -m pip install pywin32
4. python -m pip install PyUserInput

## Run Telemetry Tracker
`python telemetrytracker.py`

## Quit Telemetry Tracker
Press ' two time

## Run Telemetry Miner
1. `python telemetryminer.py`
2. Input mouse events csv file, e.g. ./data/7/25022017-144851/00_dump_mouse.csv

## Run Telemetry Compressor
1. `python telemetrycompressor.py`
2. Input mined mouse events txt file, e.g. ./data/7/25022017-144851/00_dump_mouse_mined.txt
