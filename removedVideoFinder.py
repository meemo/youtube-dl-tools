# Usage:
# deadVideoFinder.py [name of text file with urls] [output file name (include .txt)] [delay length in seconds]
# Default delay is 0 seconds

import youtube_dl
import sys
import time

inputFile = open(sys.argv[1])
inputList = []
for i in inputFile:
    inputList.append(i)

outputFile = open(sys.argv[2], "w")

delayLength = sys.argv[3]
if delayLength.isdigit() is not True:
    delayLength = 0

yt_dl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})  # need the stuff in {}? pretty sure no.


def checkVideo(videoURL):
    with yt_dl:
        try:
            yt_dl.extract_info(videoURL, download=False)
            print("URL Successful: " + videoURL)
        except youtube_dl.utils.DownloadError:
            outputFile.write(videoURL)
            print("URL Failed: " + videoURL)


print("Warning: use a VPN so you don't get blocked by Youtube!")
time.sleep(2)
print("Starting URL Checking")
for i in inputList:
    if "youtube " in i and len(i) is "19":
        i = "https://youtube.com/watch?v=" + i[-12:]
        checkVideo(i)
        time.sleep(delayLength)
    elif "https://youtube.com/watch?v=" in i and len(i) is "39":
        checkVideo(i)
        time.sleep(delayLength)
    else:
        print("Entry in input file invalid: " + i)
