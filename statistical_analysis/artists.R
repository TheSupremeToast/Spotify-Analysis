getArtists <- function(dir) {
    library(tidyverse)
    
    # import his.csv from desired input directory
    # NOTE: file created in Python, maybe convert to R later
    his <- read_csv(paste(c(dir, 'his.csv'), collapse=''), show_col_types=F)

    # create dataframe of unique artists
    artists <- data.frame(unique(his$artistName))
    colnames(artists) <- c('artistName')
    artists$msPlayed <- c(rep(0, length(artists$artistName)))
    artists$plays <- c(rep(0, length(artists$artistName)))
    artists$uniqueSongs <- c(rep(0, length(artists$artistName)))

    # TODO: add ability to use timeframe bounds


    # create table of occurences per artist
    occurences <- table(his$artistName)

    # iterate through history to find total artist playtime and number of plays
    i <- 1
    for (artist in unique(his$artistName)) {
        artists$msPlayed[i] <- sum(his$msPlayed[which(his$artistName == artist)])
        # FIX: filter out skipped?
        artists$plays[i] <- occurences[artist]
        artists$uniqueSongs[i] <- length(unique(his$trackName[which(his$artistName == artist)]))
        i=i+1
    }
    rm(occurences)

    return(artists)
}

