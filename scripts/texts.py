import pygame
from scripts.utils import Text


def texts(surf,context,level=None):
    if context == 'game_menu':
        if level == 1:
            Text('Did you know?', 30, 'black', surf, (30, 30))
            Text('The US creates over', 20, 'black', surf, (30, 80))
            Text('624,000 metric tons', 20, 'black', surf, (30, 110))
            Text('of waste per day.', 20, 'black', surf, (30, 140))
            Text('press any key to continue',10,'black',surf,(30,180))


        elif level == 2:
            Text('Did you know?', 30, 'black', surf, (30, 30))
            Text('The US threw out ', 20, 'black', surf, (30, 80))
            Text('over 292 million ', 20, 'black', surf, (30, 110))
            Text('tons of trash in 2018.', 20, 'black', surf, (30, 140))
            Text('press any key to continue', 10, 'black', surf, (30, 180))
        elif level == 3:
            Text('Did you know?', 30, 'black', surf, (30, 30))
            Text('Roughly 80% of the ', 20, 'black', surf, (30, 80))
            Text('items in landfills ', 20, 'black', surf, (30, 110))
            Text('could be recycled.', 20, 'black', surf, (30, 140))
            Text('press any key to continue', 10, 'black', surf, (30, 180))
        elif level == 4:
            Text('Did you know?', 30, 'black', surf, (30, 30))
            Text('Plastic takes more ', 20, 'black', surf, (30, 80))
            Text('than 400 years ', 20, 'black', surf, (30, 110))
            Text('to degrade.', 20, 'black', surf, (30, 140))
            Text('press any key to continue', 10, 'black', surf, (30, 180))
        elif level == 5:
            Text('Did you know?', 30, 'black', surf, (30, 30))
            Text('The US generates more ', 20, 'black', surf, (30, 80))
            Text('plastic trash than ', 20, 'black', surf, (30, 110))
            Text('any other nation.', 20, 'black', surf, (30, 140))
            Text('press any key to continue', 10, 'black', surf, (30, 180))
        elif level == 6:
            Text('Did you know?', 30, 'black', surf, (30, 30))
            Text('There are still 50 bil ', 20, 'black', surf, (30, 80))
            Text('pieces of litter on ', 20, 'black', surf, (30, 110))
            Text('the ground in America.', 20, 'black', surf, (30, 140))
            Text('press any key to continue', 10, 'black', surf, (30, 180))