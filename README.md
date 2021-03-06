# TelemetryTracker
This work represents the game telemetry analysis done as a part of my MSc Thesis

**The TelemetryTracker.py runs on Windows only and is an altered version of [Mouse-n-Key](https://github.com/pablotheissen/Mouse-n-Key)**

## Telemetry Tracker
The Telemetry Tracker tracks mouse and keyboard events and logs them into csv files.

### Setup
1. Install [Python 3.6](https://www.python.org/downloads/)
2. python -m pip install numpy
3. python -m pip install pywin32
4. python -m pip install PyUserInput

### Run
`python telemetrytracker.py`

### Quit
Press ' two times

## Telemetry Analyzer
The Telemetry Analyzer was used to roughly analyze the events in the game in order to note down when a mouse click happened and map it to a certain choice in the game. The analyzer only gives a rough estimate even though sometimes it's spot on. Therefore, a visual comparison with a screen recording of the vide game is necessary. After the visual comparison, make sure there's an event in the mouse event csv file that backs up your time stamp. 

### Run
1. `python telemetryanalyzer.py`
2. Input mouse events csv file, e.g. ./data/7/25022017-144851/00_dump_mouse.csv
3. Input the start time of the game session

## Telemetry Miner
The Telemetry Miner mines the data obtained by the Telemetry Tracker and creates an array including all mouse events that happen 5 seconds before a decisions in the game is made. The miner requires a decision file with timestamps of each decisions. The mined data is logged into a txt file.

### Run
1. `python telemetryminer.py`
2. Input mouse events csv file, e.g. ./data/7/25022017-144851/00_dump_mouse.csv

## Telemetry Compressor
The Telemetry Compressor compresses each of the events in the mined txt file and outputs one array for each event in a txt file.

### Run
1. `python telemetrycompressor.py`
2. Input mined mouse events txt file, e.g. ./data/7/25022017-144851/00_dump_mouse_mined.txt
