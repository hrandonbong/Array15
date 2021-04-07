#Author: Brandon Hong
#Date: 2/9/21
#Description: This code takes a list of numbers and returns if the following game is beatable or not.
#each number it lands on is the number of spaces the player can move. If the game is solvable then the
#player wins. If the player can't move to the right most 0 square, the player loses.

def row_puzzle(list,memo=None,index=0):
    """This program takes a list of integers as its parameters. It returns a true or false
    statement. If the list of numbers can be solved for the row puzzle return value is true. If no it
    is false."""
    #If the row is a winner, this if statement is passed.
    if index == len(list)-1 and list[index]==0:
        return True

    #if the index is out of range, False
    if index < 0 or  index >= len(list):
        return False

    #If not none, means true
    if not memo:
        memo = {}

    pos = list[index]

    #Checks if the index has already been visited
    if index not in memo:
        memo[index] = list[index:]
        #In a true or false return, the true statement is returned
        return row_puzzle(list,memo,index-pos) or row_puzzle(list,memo,index+pos)
    return False

# x = [2, 4, 5, 3, 1, 3, 1, 4, 0]
# x =  [1, 3, 2, 1, 3, 4, 0]
# # x = [1,2,3,0]
# print(row_puzzle(x))