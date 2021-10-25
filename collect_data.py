import berserk
from converter.pgn_data import PGNData

def main():
  # Use your Lichess API token to get information on your games
    token = 'token'
    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)
    
    my_username = client.account.get()['username']
    
    # Create a list of all my games
    my_games_generator = client.games.export_by_player(my_username, as_pgn = True)
    my_pgn_games = []
    for game in my_games_generator:
        my_pgn_games.append(game)
        
    # Create a pgn file that represents all of my games
    games_string = "\n\n".join(my_pgn_games)
    file = open("/Users/koplo/Documents/Chess/game.pgn", "w")
    file.write(games_string)
     
    # Create two CSV files - one of games data and one of moves data  
    pgn_data = PGNData("/Users/koplo/Documents/Chess/game.pgn")
    result = pgn_data.export()
    result.print_summary()

if __name__ == '__main__':
    main()
