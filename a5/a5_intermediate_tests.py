
##The following is a reasonable way to check your find_most_constrained_cell
##   method. Comment out the end entire end of your code starting with the
##   line if __name__ == "__main__": to the end of the file. Notice that in the
##   "format" menu, there is a "comment out region" command that you can use
##   to comment out some highlighted code.

first_moves = [
        (0, 1, 7),
        (0, 7, 1),
        (1, 2, 9),
        (1, 3, 7),
        (1, 5, 4),
        (1, 6, 2),
        (2, 2, 8),
        (2, 3, 9),
        (2, 6, 3),
        (3, 1, 4),
        (3, 2, 3),
        (3, 4, 6),
        (4, 1, 9),
        (4, 3, 1),
        (4, 5, 8),
        (4, 7, 7),
        (5, 4, 2),
        (5, 6, 1),
        (5, 7, 5),
        (6, 2, 4),
        (6, 5, 5),
        (6, 6, 7),
        (7, 2, 7),
        (7, 3, 4),
        (7, 5, 1),
        (7, 6, 9),
        (8, 1, 3),
        (8, 7, 8),
    ]

#Create a sudoku board.
b = Board()
#Place the 28 assignments in first_moves on the board.
for trip in first_moves:
    b.rows[trip[0]][trip[1]] = trip[2]
#NOTE - the above code only *puts* the numbers on the board, but doesn't
#   do the work that update does (remove numbers from other lists, etc).

#I'm going to now alter 3 lists on the board to make them shorter (more
#   constrained. 
remove_if_exists(b.rows[0][0], 8)
remove_if_exists(b.rows[0][0], 7)
remove_if_exists(b.rows[0][0], 3)
remove_if_exists(b.rows[0][0], 2)
remove_if_exists(b.rows[4][8], 8)
remove_if_exists(b.rows[4][8], 1)
remove_if_exists(b.rows[4][8], 2)
remove_if_exists(b.rows[4][8], 3)
remove_if_exists(b.rows[4][8], 4)
remove_if_exists(b.rows[6][7], 2)
remove_if_exists(b.rows[6][7], 3)
remove_if_exists(b.rows[6][7], 5)
remove_if_exists(b.rows[6][7], 6)
#we removed 5 items from positions (4,8) so that should now be the most
#  constrained.
assert b.find_most_constrained_cell() == (4,8), "find most constrained cell test 1"
assert b.failure_test() == False, "failure test test 1"
assert b.goal_test() == False, "goal test test 1"

b.rows[4][3] = []
assert b.find_most_constrained_cell() == (4,3), "find most constrained cell test 2"
assert b.failure_test() == True, "failure test test 2"
print("All part 1 tests passed!")

##Now, let's write some quick tests to check update!
#Create a sudoku board.
g = Board()
#Place the 28 assignments in first_moves on the board.
for trip in first_moves:
    g.update(trip[0],trip[1],trip[2])

g.print_pretty()
#From the above print statement, you can see which numbers
#  have been assigned to the board, and then create test
#  cases by looking at the board and listing what values are
#  still possible for a specific cell. I have created
#  2 such test cases like that for you. 
assert g.rows[0][2] == [2,5,6], "update test 1"
assert g.rows[5][5] == [3,7,9], "update test 2"
assert g.num_nums_placed == 28, "update test 3"
assert g.find_most_constrained_cell() == (1,7), "fmc test"
assert g.failure_test() == False, "failure test test"
assert g.goal_test() == False, "goal test test"
g.num_nums_placed = 81
assert g.goal_test() == True, "goal test test"

print("All part 2 tests passed!")

