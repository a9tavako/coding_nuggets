/*
A Sudoku solver in Kotlin with the approach of keeping 3 2D arrays for tracking the Sudoku conditions. 
Inspired by https://leetcode.com/problems/sudoku-solver/
*/
class Solution {
    private val n = 3
    private val N = n * n
    private val rows = Array(N) { IntArray(N + 1) }
    private val columns = Array(N) { IntArray(N + 1) }
    private val boxes = Array(N) { IntArray(N + 1) }
    private var isSolved = false
    private var board: Array<CharArray> = Array(N) { CharArray(N) }

    fun solveSudoku(board: Array<CharArray>): Unit {
        this.board = board
        for (i in 0 until N) {
            for (j in 0 until N) {
                if (board[i][j] != '.') {
                    val digit = board[i][j].digitToInt()
                    addDigit(i, j, digit)
                }
            }
        }

        explore(0, 0)
    }

    private fun boxId(i: Int, j: Int): Int {
        return (i / n) * n + (j / n)
    }

    private fun addDigit(i: Int, j: Int, digit: Int) {
        val boxId = boxId(i, j)
        rows[i][digit]++
        columns[j][digit]++
        boxes[boxId][digit]++
        board[i][j] = digit.toString().first()
    }

    private fun removeDigit(i: Int, j: Int, digit: Int) {
        val boxId = boxId(i, j)
        rows[i][digit]--
        columns[j][digit]--
        boxes[boxId][digit]--
        board[i][j] = '.'
    }

    private fun canAddDigit(i: Int, j: Int, digit: Int): Boolean {
        val boxId = boxId(i, j)
        return rows[i][digit] + columns[j][digit] + boxes[boxId][digit] == 0
    }

    private fun explore(i: Int, j: Int) {
        if (isSolved) return
        if (i == N) {
            isSolved = true
            return
        }

        if (board[i][j] != '.') {
            if (j != N - 1) {
                explore(i, j + 1)
            } else {
                explore(i + 1, 0)
            }
        } else {
            for (digit in 1..N) {
                if (canAddDigit(i, j, digit)) {
                    addDigit(i, j, digit)
                    if (j != N - 1) {
                        explore(i, j + 1)
                    } else {
                        explore(i + 1, 0)
                    }
                    if (isSolved) return
                    removeDigit(i, j, digit)
                }
            }
        }
    }
}
