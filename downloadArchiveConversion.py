# Converting urls in the output of --download-archive in youtube-dl to youtube URLS
# Only works with youtube
# File should have lines that look like this from the --download-archive option:
# `youtube xxxxxxxxxxx`
# Script converts to
# `https://youtube.com/watch?v=xxxxxxxxxxx`
#
# Usage: `downloadArchiveConversion.py [--download-archive output .txt file] [desired output file name (with .txt)]

import sys

inputFile = open(sys.argv[1])
inputList = []

for i in inputFile:
    inputList.append(i)

# Deduping input
inputList = list(set(inputList))

outputFile = open(sys.argv[2], "w")

for i in inputList:
    if "youtube " in i and len(i) is "19":
        i = "https://youtube.com/watch?v=" + i[-12:]
        outputFile.write(i)
    else:
        print("Input line invalid: " + i)
