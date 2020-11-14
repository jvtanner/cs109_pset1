# pset1

 Consider a game, which uses a generator that produces independent random integers between
1 and 100, inclusive. The game starts with a sum S = 0. The first player adds random numbers
from the generator to S until S > 100, at which point they record their last random number
x. The second player continues by adding random numbers from the generator to S until
S > 200, at which point they record their last random number y. The player with the highest
number wins; e.g., if y > x, the second player wins. Write a Python 3 program to simulate
100,000 games and output the estimated probability that the second player wins.
