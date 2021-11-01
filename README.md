# Chess Analysis: Project Overview

* Collected over 6500 games using Python and Lichess API
* Cleaned the data to make it usable
* Created visualizations of statistics about chess games

## Code and Resources

**Python Version:** 3.8.10             
**Packages:** pandas, matplotlib, csv, dask, berserk, chess, pgn2data              
**Eco to Opening Key:** https://docs.google.com/spreadsheets/d/1CehtdBIt5cOkRy6mbgMJlLjvfK1StGsqiKVCkeh9uqQ/edit#gid=0
**Lichess API Token:** https://lichess.org/account/oauth/token                 
**Berserk Documentation:** https://berserk.readthedocs.io/en/master/               
**Pgn2data Github:** https://github.com/zq99/pgn2data                 
**Stockfish:** https://stockfishchess.org

## Data collection

Used Berserk, a Python client for Lichess API to collect above 6500 games I played on https://lichess.org into a PGN file - A file that uses standard plain text format for recording chess games (both the moves and related data), then used pgn2data to convert the pgn file to two csv files - one of games related data, and one of the moves related data. Then, used Stockfish engine to give an evaluation to every move. With each game some of the data we got is:

* Game id
* Event 
* White elo (elo is a rating system for chess)
* Black elo
* Winner
* Loser
* Eco (a key that represents the name of the opening)

And with each move some of the data we got is:

* Game id
* Player
* Move
* Evaluation
* Fen (A code that represents the current state of the board)
* Color

## Data Cleaning

After collecting the data, I needed to clean it up so it was usable for our purposes. I made the following changes and created the following variables:

* Removed games with non-relevant events
* Converted white elo, black elo, winner elo and loser elo to numeric data
* Converted evaluation to numeric data and calculated white and black average evaluation
* Added to the games dataset columns for opening, result type, openings played with white/black, my elo, my color, white and black average evaluation and elo and evaluation difference between the players
* Added to the games dataset columns for elo and evaluation difference range for visualizations purposes

## Data Analysis

 looked at the distributions of the data and the value counts for various categorical variables. Below are a few highlights from the pivot tables.

<img src="https://github.com/Konadav/chess_analysis/blob/main/Elo_by_time.png" width="300" height="250">            <img src="https://github.com/Konadav/chess_analysis/blob/main/Winrate_by_color.png" width="300" height="250">

<img src="https://github.com/Konadav/chess_analysis/blob/main/Winrate_by_elo_difference.png" width="300" height="250">
















