# imports
library(ggplot2)
library(tidyverse)

# change working directory
setwd('~/Documents/projects/SpotiPy-Wrapped')

# load local files
source("statistical_analysis/artists.R")
source("statistical_analysis/tracks.R")

# set data directory
dir <- 'input/20221105/'

# load other dataframes
artists <- getArtists(dir)
artists$plays <- as.factor(artists$plays)

tracksTuple <- getTracks(dir)
his <- tracksTuple[[1]]
tracks <- tracksTuple[[2]]
skipped <- tracksTuple[[3]]
unskipped <- tracksTuple[[4]]

############

fit <- lm(uniqueSongs ~ plays, data = artists)
ggplot(artists, aes(x=log(uniqueSongs), y=log(plays))) +
    geom_point(color = 'blue')


#############

# TODO: Future plans
# model for listening time artists and songs
# plot avg number of songs listened to by artist vs artist plays
# plot of timeframes listened to artists (likely only top artists to prevent clutter)
    # boxplot/scatterplot?
# kmeans clustering on artist genres/moods
# most listened to playlists (might need live logger for this info)



