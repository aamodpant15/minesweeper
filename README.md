# minesweeper

## Usage

Run the `minesweeper.py` file using, `python3 minesweeper.py`.  

### Controls
1. To select a cell and uncover it, type in `[row]<space>[column]`.  
2. To flag a cell, type `f<space>[row]<space>[column]`.

## Computer Science Concepts used:
1. DFS: When an empty cell is chosen, the entire connected area of empty cells must be uncovered. To accomplish this, Depth First Search is started from the chosen cell, till a number cell is found. This reveals an area of neighbouring empty cells. Then, we go around the boundary of this area, revealing a layer of numbers around it. 
