# This files has to be launched from the same directory:
# $ python3 ./generate_readme.py

from glob import glob
import os
import json

parts = []

# Walk through all sub-folders.
# Generate a README for each folder and memorize the data about the parts.
paths = glob("*/part.json")
for path in paths:
    dir = os.path.dirname(path)
    print("Generating README.md in " + dir + "...")

    part = json.loads(open(path).read())
    if "url" in part:
        desc = "[" + part["desc"] + "](" + part["url"] + ")"
    else:
        desc = part["desc"]
    contents = (
        "# [goBILDA](https://www.gobilda.com/) parts\n"
        + "## "
        + desc
        + "\n\n"
        + "**Patented**\n\n"
        + "<img alt='"
        + part["desc"]
        + "' src='../../../generated_files/parts/gobilda/"
        + dir
        + ".svg'/>\n"
    )
    readme = open(dir + "/README.md", "w+")
    readme.write(contents)
    readme.close()

    part["dir"] = dir
    parts.append(part)

# Now sort the parts to keep the top level README's table normalized.
parts = sorted(parts, key=lambda x: x["dir"])


# Generate the README file in the top level folder.
print("Generating README.md in the current folder...")
contents = """
# openvmp-parts-gobilda

OpenVMP parts that can be purchased from [goBILDA](https://www.gobilda.com/).

See [openvmp-models](https://github.com/openvmp/openvmp-models) for more info.

| Part | Image |
| -- | -- |
"""
readme = open("./README.md", "w+")
readme.write(contents)

for part in parts:
    readme.write(
        "| ["
        + part["desc"]
        + "]("
        + part["dir"]
        + ") | <img alt='"
        + part["desc"]
        + "' src='../../generated_files/parts/gobilda/"
        + part["dir"]
        + ".svg' width='300' /> |\n"
    )

readme.close()
