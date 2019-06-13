class PigGame:
    """
    How PigGame opporates. 
    """

    import randint from random


    class Die:
        """
        The value and behavior of the die. 
        Six(6) sided die, should roll 0-1 times per each player's turn.
        """
        def __init__(self, roll):
            self.roll = roll.random.randint(1,6)


    class Turn:
        """
        Defines each of the three possible outcomes for each turn: Hold/Play/Bust.
        """
        def __init__(self, hold, play, bust):
            self.hold = hold()    
            self.play = play(die.roll)
            self.bust = bust(die.roll) 
        
        def hold(self.hold):
            hold_input = input("To HOLD, enter the letter 'H': ")
                return(f"You are holding, with a current score of: "), score)

        def play(self.play):
            play_input = input("To ROLL, enter the letter 'R': ")
            if self.roll = (2,6):
                return(f"You rolled a", roll, "Your score is now", player_score)
            if self.roll = (1):
                return(f"You rolled a '1'! You lose this round!")


    class Score:
        """  
        Calulates score based on if the player plays/holds/busts.
        """
        total_score = 0

        def __init__(self, add, win):
            self.add = add() 
            self.win = win()

        def add(turn.play):
            num_sum = sum(list())
            return (f"Your current score is", num_sum)

        def win(turn.play):
            num_sum = (sum(list()) > 100)
            return(f"You have", num_sum, "points! You WIN!")

        score.total_score.append
        if score.total_score >= 100
        return (f"You have a current score of", score)
        

    class Player:
        """  
        Define player by player one or two, determine type of turn, and calculate their score.
        """

        def __init__(self, player):
          self.player = player1()
          self.player = player2()
        
        def player1: Player()
            player1.name = input("Type your name here, then press enter. ")
            player1.score = (function needed to collect, sum score)

        def player2: Player()
            player2.name = input("Type your name here, then press enter. ")
            player2.score = (function needed to collect, sum score)
     

    
    def player_instructions:
        """ 
        Specific instructions printed to players on how to opporate the game. 
        """
        Print("ADD INSTRUCTIONS HERE")
        pass
        
    def first_turn:
        """
        Decide first turn of game by each player rolling the die, and player with highest number goes first.
        """
        # I have absolutely no idea how to write this function at this time.
        pass

    def play game:
        """
        Each player alternates turns (by a loop) to roll the die and collect points. 
        Points are based on number rolled, and the first player to collect a minimum of 100 points wins.
        If a player rolls a 1, they lose all points and the other player wins.
        A player may choose to hold their points, instead of rolling, and the other player will continue to roll until win(100+ points) or bust(rolls a 1).
        """
        pass



# NOTES:
# pipenv shell pig_game.py