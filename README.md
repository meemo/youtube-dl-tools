# youtube-dl-tools
 A small collection of scripts for use with the files created by [youtube-dl](https://github.com/ytdl-org/youtube-dl).
 See https://github.com/meemo4556/youtube-dl-command
 For a command/config file for [youtube-dl](https://github.com/ytdl-org/youtube-dl)
 
# downloadArchiveConversion.py
 This script will take the output from [youtube-dl](https://github.com/ytdl-org/youtube-dl)'s `--download-archive` option and convert all youtube ids into URLs.
 
 `youtube xxxxxxxxxxx`
 Becomes:
 `https://youtube.com/watch?v=xxxxxxxxxxx`
 
 Usage: `downloadArchiveConversion.py [--download-archive output .txt file] [desired output file name (with .txt)]`
 
 Example usage:
 
 `downloadArchiveConversion.py ids.txt output.txt`
 
# removedVideoFinder.py
 This script will recursively go through a text file with either youtube URLs or the output of a `--download-archive` and use [youtube-dl](https://github.com/ytdl-org/youtube-dl) to test if the videos are still accessible on Youtube. 
 
 Usage:
 `deadVideoFinder.py [name of text file with urls] [output file name (include .txt)] [delay length in seconds]`
 
 Example usage:
 `deadVideoFinder.py ids.txt output.txt 5`
 
 If a delay length is not specified, it defaults to 0 seconds. 
 
 `youtube_dl` module is required for script to run.
 
 Be aware that youtube may block you for excessive requests, wisely choose a delay length and/or use a VPN/proxy.
