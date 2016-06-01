import re
import argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np


def findCommonTracks(fileNames):
    """
    Find common tracks in given playlist files,
    and save them to common.txt.
    """
    # a list of sets of trach names
    trackNameSets = []
    for fileName in fileNames:
        # create a new set
        trackNames = set()
        # read in playlist
        plist = plistlib.readPlist(fileName)
        # get the tracks
        tracks = plist['Tracks']
        # iterate through tracks
        for trackId, track in tracks.items():
            try:
                # add name to set
                trackNames.add(track['Name'])
            except:
                # ignore
                pass
            # add to list
            trackNameSets.append(trackNames)
            # get set of common tracks
            commonTracks = set.intersection(*trackNameSets)
            # write to file
            if len(commonTracks) > 0:
                f = open("common.txt", 'wb')
                for val in commonTracks:
                    s = "%s\n" % val
                    f.write(s.encode("UTF-8"))
                f.close()
                print("%d common Tracks found. "
                      "Track names written to common.txt." % len(commonTracks))
            else:
                print("No common Tracks.")

def plotStats(fileName):
	"""
	Plot some statistics by reading rack information from playlist
	"""

	# read in palylist
	
# Gather our code in a main() function
def main():
    # create parser
    descStr = "This program analysez playlist files (.xml) exported from iTunes."

    parser = argparse.ArgumentParser(description=descStr)
    # add a mutually esclusive group of arguments
    group = parser.add_mutually_exclusive_group()

    # add expected arguments
    group.add_argument('--common', nargs='*', dest='plFiles', required=False)
    group.add_argument('--stats', dest='plFile', required=False)
    group.add_argument('--dup', dest='plFileD', required=False)

    # parse args
    args = parser.parse_args()

    if args.plFiles:
            # find common tracks
        findCommonTracks(args.plFiles)
    # elif args.plFile:
    # plot stats
    #     plotStats(args.plFile)
    # elif args.plFileD:
    # find duplicate tracks
    #     findDuplicates(args.plFileD)
    else:
        print("These are not the tracks you are looking for.")

# main method
if __name__ == '__main__':
    main()
