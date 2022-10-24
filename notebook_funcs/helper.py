#################
### helper.py ###
#################

#################

import pandas as pd
from matplotlib import pyplot as plt
from notebook_funcs.cleaner import *

#
# Instantiate global variables
# (Defined by functions in cleaner.py)
#
global_his = None
unskipped = None
skipped = None

#################

#
# plots top (numtracks) songs by a given artist
#
def plotArtist(artistname, numtracks, export = False):
    plt.rcParams['figure.figsize'] = [20, 8]
    artistdata = unskipped[unskipped['artistName'] == artistname]
    artistdata = artistdata['trackName'].value_counts()
    plt.plot(artistdata.head(numtracks), 'o')
    plt.xticks(rotation = 90)
    plt.title('Most played songs by ' + artistname)
    plt.ylabel('Plays')
    if export:
        # TODO: Figure out png vs svg with react
        plt.savefig("plots/plotArtist.png") # save figure for later use
        plt.show()
    else:
        plt.show()

#################

#
# plot top tracks
#
def plotTopTracks(tracks, numtracks, export = False):
    fig = plt.figure()
    plt.rcParams['figure.figsize'] = [10, 8]
    plt.plot(tracks.head(numtracks), 'o')
    plt.xticks(rotation = 90)
    plt.title('Most Played Tracks')
    plt.ylabel('Plays')
    if export:
        plt.savefig("plots/plotTopTracks.png")
        plt.close(fig)
    else:
        plt.show()
    return

#
# plot top artists
#
def plotTopArtists(artists, numartists, export = False):
    fig = plt.figure()
    plt.rcParams['figure.figsize'] = [10, 8]
    plt.plot(artists.head(numartists), 'o')
    plt.xticks(rotation = 90)
    plt.title('Most Played Artists')
    plt.ylabel('Plays')
    if export:
        plt.savefig("plots/plotTopArtists.png")
        plt.close(fig)
    else:
        plt.show()
    return

#################

#
# List top n songs
#
# TODO - change to output in the form of 'songPlayCount' function 
def topSongPlays(numsongs):
    int(numsongs)
    tracks = unskipped['trackName'].value_counts()
    print('Your top', numsongs, 'songs: ')
    print('Song                       Plays')
    return(tracks.head(numsongs))

#################

#
# Get total playtime (dropping skipped songs)
#
def playtime(his):
    playtime = his['msPlayed'].sum()
    playtime /=  60000
    playtime = int(playtime)
    print("Total minutes listened:", playtime)
    print("Total hours listened:", playtime / 60)
    return(playtime)

#################

# TODO: fix minor issue with displaying the play variable as list instead of int

#
# Get total play count for a given artist
#
def artistPlayCount(artistname):
    plays = unskipped[unskipped['artistName'] == artistname]
    plays = plays.apply(lambda x: x.nunique())
    print("You have listened to", artistname, '\n', plays, "times.")
    return plays[0]
    
#
# Get total play count for a given song 
#
def songPlayCount(trackname):
    plays = unskipped[unskipped['trackName'] == trackname]
    plays = plays.apply(lambda x: x.nunique())
    print("You have listened to", trackname, '\n', plays, "times.")
    return plays[0]

#################

#
# Get top songs since a date
#
def topSongsTimeframe(timestamp, graph = False):
    plt.rcParams['figure.figsize'] = [20, 8]
    # convert input into timestamp format
    element = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element]
    temp = times['trackName'].value_counts() 
    if graph:
        plt.plot(temp.head(100), 'o')
        plt.xticks(rotation = 90)
        plt.title('Top Tracks Since ' + timestamp)
        plt.ylabel('Plays')
        plt.show()
    return(temp.head(10))
    
#
# Get top songs between two dates
#
def topSongsTimeframeBounded(lower, upper, numsongs, graph = False, export = False):
    plt.rcParams['figure.figsize'] = [20, 8]
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element_l] 
    times = times[times['endTime'] <= element_u]
    temp = times['trackName'].value_counts() 
    if graph:
        plt.plot(temp.head(100), 'o')
        plt.xticks(rotation = 90)
        plt.title('Top tracks between ' + lower + ' and ' + upper)
        plt.ylabel('Plays')
        if export:
            plt.savefig('plots/topSongsTimeframeBounded.png')
        else:
            plt.show()
    return (temp.head(numsongs))

#
# Get top artists since a data
#
def topArtistsTimeframe(timestamp, graph = False):
    plt.rcParams['figure.figsize'] = [20, 8]
    element = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element]
    temp = times['artistName'].value_counts()
    if graph:
        plt.plot(temp.head(100), 'o')
        plt.xticks(rotation = 90)
        plt.title('Top Artists Since ' + timestamp)
        plt.ylabel('Plays')
        plt.show()
    return(temp.head())

#
# Get top artists between two dates
#
def topArtistsTimeframeBounded(lower, upper, numartists, graph = False, export = False):
    plt.rcParams['figure.figsize'] = [20, 8]
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element_l]
    times = times[times['endTime'] <= element_u]
    temp = times['artistName'].value_counts()
    if graph:
        plt.plot(temp.head(100), 'o')
        plt.xticks(rotation = 90)
        plt.title('Top Artists Between ' + lower + ' and ' + upper)
        plt.ylabel('Plays')
        if export:
            plt.savefig('plots/topArtistsTimeframeBounded.png')
        else:
            plt.show()
    return(temp.head(numartists))

#################

# TODO - fix end of month bounds

#
# find listening time for a given month
#
def listeningTimeMonth(month_num, year):
    # define bounds for month
    lower = str(year) + "-" + str(month_num) + "-01"
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    upper = str(year) + "-" + str(month_num) + "-31"
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    
    # narrow data to fit parameters
    df_params = unskipped[unskipped['endTime'] >= element_l]
    df_params = df_params[df_params['endTime'] <= element_u]
    total = df_params['msPlayed'].sum()
    #calculate hours listened
    total = total / 1000 / 60 / 60
    
    return(total)

#################

#
# Get the listening time for an individual artist
#
def listeningTimeArtist(artist):
    df_params = unskipped[unskipped['artistName'] == artist]
    return(df_params['msPlayed'].sum() / 1000 / 60 / 60)


################

#
# histogram of average time listened to songs
# (skipped songs are dropped)
#
def avgTrackLength():
    plt.rcParams['figure.figsize'] = [10, 8]
    plt.hist(unskipped['msPlayed'], 
             bins = [0, 50000, 100000, 150000, 200000, 250000, 
                 300000, 350000, 400000, 450000, 500000, 550000])
    plt.xlabel("Song Playtime (ms)")
    plt.ylabel("Number of plays")
    plt.title("Average Song Length")
    plt.show()

################

#
# Get most skipped songs between two dates
#
def mostSkippedArtistsTimeframeBounded(lower, upper, numartists, export = False, graph = False):
    plt.rcParams['figure.figsize'] = [10, 8]
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    times = skipped[skipped['endTime'] >= element_l] 
    times = times[times['endTime'] <= element_u]
    temp = times['artistName'].value_counts() 
    if graph:
        plt.plot(temp.head(numsongs), 'o')
        plt.xticks(rotation = 90)
        plt.title('Top tracks between ' + lower + ' and ' + upper)
        plt.ylabel('Plays')
        if export:
            plt.savefig("plots/mostSkippedTimeframeBounded.png")
        else:
            plt.show()
    return (temp.head(numsongs))

#
# Get most skipped songs between two dates
#
def mostSkippedTimeframeBounded(lower, upper, numsongs, graph = False, export = False):
    fig = plt.figure()
    plt.rcParams['figure.figsize'] = [10, 8]
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    times = skipped[skipped['endTime'] >= element_l] 
    times = times[times['endTime'] <= element_u]
    temp = times['trackName'].value_counts() 
    if graph:
        plt.plot(temp.head(numsongs), 'o')
        plt.xticks(rotation = 90)
        plt.title('Top tracks between ' + lower + ' and ' + upper)
        plt.ylabel('Plays')
        if export:
            plt.savefig("plots/mostSkippedTimeframeBounded.png")
            plt.close(fig)
        else:
            plt.show()
    return (temp.head(numsongs))

################

# TODO: Potential improvements
# image exports for all graph functions -> txt file export for others?
# daily song/artist charts and numbers
# desktop app allowing changing of graphs and lists
# graph of playtime per month (general, artists, songs?)
# api calls for current top songs/artists/genres
# genre graphs - requires api calls and track ids (computationally heavy)
# make cleaner and helper into classes to store multiple sets of data at a time
# all time data (multiple datasets) vs current year (jan-dec) data

