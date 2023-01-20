getTracks <- function(dir) {
    library(tidyverse)
    
    # import his.csv from desired input directory
    # NOTE: file created in Python, maybe convert to R later
    his <- read_csv(paste(c(dir, 'his.csv'), collapse=''), show_col_types=F)

    # create dataframe of unique artists
    tracks <- data.frame(unique(his$trackName))
    colnames(artists) <- c('trackName')

    check_skipped <- function(x, vec = his$msPlayed) {
        if (x > 30000) {
            return(0)
        } else if (x <= 30000) {
            return(1)
        }
    }
    # skipped = 1 | unskipped = 0
    his$skipped <- sapply(his$msPlayed, check_skipped)
    unskipped <- his[which(his$skipped == 0),]
    skipped   <- his[which(his$skipped == 1),]

    return(list(his, tracks, unskipped, skipped))
}

