# 5. Write a simple quote-of-the-day program. The program should contain a list of quotes, and
# when the user runs the program, a randomly selected quote should be printed.

import random
# create a list of random quotes
quotes = ['I\'m not a great programmer; I\'m just a good programmer with great habits.',
          'The best thing about a boolean is even if you are wrong, you are only off by a bit.',
          'The best way to predict the future is to invent it.',
          'How many programmers does it take to change a light bulb? None, that\'s a hardware problem.',
          'The best way to make a large fortune is to have a large head.',
          'The idea of computer programming is to express an idea in some way that is easy to understand, yet hard to implement.',
          'Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.',
          'Dijkstra was a Dutch computer scientist who developed a map-reduce algorithm for finding the shortest path between two points on a graph.',
          'The most important property of a program is whether it accomplishes the intention of its user.',
          'Github Co-pilot is a tool that helps you become more productive, by reminding you when you\'re collaborating on a project.']

quote = random.choice(quotes)
print(quote)
