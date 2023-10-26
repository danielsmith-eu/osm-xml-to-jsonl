# Convert OSM export data into flattened out JSONL lines

1. install the requirements using pip3, e.g. `pip3 install -r requirements.txt`
2. go to the online map and zoom into an area of interest
3. click "Export" to get a `map.osm`` file
4. cat the json file into the `osm-xml-to-jsonl.py` tool, e.g. `cat map-2023-09-27-London-UK-Soho.osm | python3 osm-xml-to-jsonl.py > map-2023-09-27-London-UK-Soho.jsonl`
5. use the output for whatever, probably via the clipboard, e.g. using `cat map-2023-09-27-London-UK-Soho.jsonl | pbcopy`
