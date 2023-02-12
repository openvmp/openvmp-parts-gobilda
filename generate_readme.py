# This files has to be launched from the same directory:
# $ python3 ./generate_readme.py

from glob import glob
import os
import json

paths = glob("*/part.json")
for path in paths:
    dir = os.path.dirname(path)
    print("Generating README.md in " + dir + "...")

    part = json.loads(open(path).read())
    contents = (
        "# [goBILDA](https://www.gobilda.com/) parts\n"
        + "## ["
        + part["desc"]
        + "]("
        + part["url"]
        + ")\n\n"
        + "**Patented**\n\n"
        + "![The preview image only works from within https://github.com/openvmp/openvmp/](../../../generated_files/parts/gobilda/"
        + dir
        + ".svg)\n"
    )
    readme = open(dir + "/README.md", "w+")
    readme.write(contents)
    readme.close()
