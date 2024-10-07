#!/usr/bin/python3
"""
N-Queens Problem Solver
This module solves the N-Queens puzzle using backtracking.
"""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    """Use backtracking to find all solutions to the N-Queens problem."""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

def main():
    """Main function to parse input and solve the N-Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
