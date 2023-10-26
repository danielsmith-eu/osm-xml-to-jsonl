import xmltodict
import sys
import json

data = xmltodict.parse(sys.stdin.read())

for node in list(filter(lambda n: "tag" in n, data["osm"]["node"])):
    out = dict()

    for key in node.keys():
        if key[0] == "@":
            out[key.lstrip("@")] = node[key]
        elif key == "tag":

            tag = node[key]
            if type(tag) == dict:
                out["tag-" + tag["@k"]] = tag["@v"]
            elif type(tag) == list:
                for subtag in tag:
                    if ("@k" in subtag and "@v" in subtag):
                        out["tag-" + subtag["@k"]] = subtag["@v"]
            else:
                raise Exception("cant handle key: " + key)

    print(json.dumps(out))
