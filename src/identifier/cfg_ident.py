import os

from staticfg import CFGBuilder

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'quick_sort.py')

cfg = CFGBuilder().build_from_file('quick_sort', file_path)
cfg.build_visual('quick_sort', 'png')
