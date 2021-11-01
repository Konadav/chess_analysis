import pandas as pd
import chess
import chess.engine
import dask.dataframe as dd

def evaluate_position(row):
    # Import the engine
    engine = chess.engine.SimpleEngine.popen_uci('/opt/homebrew/Cellar/stockfish/14/bin/stockfish')
    # Create the positions' board
    board = chess.Board(row['fen'])
    # Set the turn's color. the row's color column represnt last turn's color
    if row['color'] == 'White':
        board.turn = chess.BLACK
    else:
        board.turn = chess.WHITE
    # Analyse the position and return white's point of view of the evaluation 
    try:
        n = engine.analyse(board, chess.engine.Limit(time=0.1))['score'].white()
        engine.quit()
        return n
    # Return None if the engine crashed while analysing the position
    except chess.engine.EngineTerminatedError:
        return None

def main():
    # Import data in pandas format, and use dask to evaluate efficiently 
    df = pd.read_csv('/Users/koplo/Documents/Projects/chess_analysis/game_game_moves.csv') 
    ddf = dd.from_pandas(df, npartitions=15)
    res = ddf.map_partitions(lambda df: df.apply((
                                lambda row: evaluate_position(row)), axis=1),
                                meta = 'x').compute()  
    # Add the results to the data and create a new CSV file including the results
    df['evaluation'] = res
    df.to_csv('/Users/koplo/Documents/Projects/chess_analysis/moves_evaluated.csv', index = False, encoding='utf-8')
    
if __name__ == '__main__':
    main()
    
