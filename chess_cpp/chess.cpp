// chess.cpp : Defines the entry point for the console application.
//
#pragma once
#include "stdafx.h"

//display various pieces
void display_knight(string board[ROWS][COLUMNS], int row, int column, piece p)
{
	string col = " ";
	if (p.get_color() == white)col = "W";
	else col = "B";
	board[1 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "_";
	board[2 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "*";
	board[3 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "*";
	board[2 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "/";
	board[2 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "'";
	board[2 + row*SQUARE_HEIGHT][8 + column*SQUARE_WIDTH] = "\\";
	board[3 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "/";
	board[3 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "\\";
	board[3 + row*SQUARE_HEIGHT][8 + column*SQUARE_WIDTH] = "_";
	board[3 + row*SQUARE_HEIGHT][9 + column*SQUARE_WIDTH] = "\\";
	board[4 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[5 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "/";
	board[5 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = col;
	board[5 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "\\";
	board[6 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "-";
	board[6 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "-";
	board[6 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "-";
	board[6 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "-";
	board[6 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "-";
	return;
}
void display_rook(string board[ROWS][COLUMNS], int row, int column, piece p)
{
	string col = " ";
	if (p.get_color() == white)col = "W";
	else col = "B";
	board[1 + row*SQUARE_HEIGHT][2 + column*SQUARE_WIDTH] = "_";
	board[1 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "_";
	board[1 + row*SQUARE_HEIGHT][8 + column*SQUARE_WIDTH] = "_";
	board[2 + row*SQUARE_HEIGHT][1 + column*SQUARE_WIDTH] = "|";
	board[2 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "|";
	board[2 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "_";
	board[2 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "|";
	board[2 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "_";
	board[2 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "|";
	board[2 + row*SQUARE_HEIGHT][9 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][1 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][2 + column*SQUARE_WIDTH] = "_";
	board[3 + row*SQUARE_HEIGHT][9 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][8 + column*SQUARE_WIDTH] = "_";
	board[4 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "|";
	board[5 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "|";
	board[5 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "|";
	board[6 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "/";
	board[5 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = col;
	board[6 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "_";
	board[6 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "_";
	board[6 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "_";
	board[6 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "\\";
	return;
}
void display_bishop(string board[ROWS][COLUMNS], int row, int column, piece p)
{
	string col = " ";
	if (p.get_color() == white)col = "W";
	else col = "B";
	board[2 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "(";
	board[2 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = ")";
	board[3 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "/";
	board[4 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = col;
	board[4 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "\\";
	board[5 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "|";
	board[5 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "|";
	board[6 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "-";
	board[6 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "-";
	board[6 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "-";
	board[6 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "-";
	return;
}
void display_queen(string board[ROWS][COLUMNS], int row, int column, piece p)
{
	string col = " ";
	if (p.get_color() == white)col = "W";
	else col = "B";
	board[2 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "*";
	board[2 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "(";
	board[2 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = ")";
	board[3 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = col;
	board[4 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[5 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "/";
	board[5 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "\\";
	board[6 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "|";
	board[6 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "|";
	board[6 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "_";
	board[6 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "_";
	board[6 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "_";
	return;
}
void display_king(string board[ROWS][COLUMNS], int row, int column, piece p)
{
	string col = " ";
	if (p.get_color() == white)col = "W";
	else col = "B";
	board[1 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "+";
	board[2 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "(";
	board[2 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "_";
	board[2 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = ")";
	board[3 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = col;
	board[4 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "-";
	board[4 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "-";
	board[5 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "/";
	board[5 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "\\";
	board[6 + row*SQUARE_HEIGHT][3 + column*SQUARE_WIDTH] = "|";
	board[6 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "|";
	board[6 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = "_";
	board[6 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "_";
	board[6 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "_";
	return;
}
void display_pawn(string board[ROWS][COLUMNS], int row, int column, piece p)
{
	string col = " ";
	if (p.get_color() == white)col = "W";
	else col = "B";
	board[2 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "<";
	board[2 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = ">";
	board[3 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "|";
	board[3 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "|";
	board[4 + row*SQUARE_HEIGHT][4 + column*SQUARE_WIDTH] = col;
	board[4 + row*SQUARE_HEIGHT][7 + column*SQUARE_WIDTH] = "\\";
	board[4 + row*SQUARE_HEIGHT][5 + column*SQUARE_WIDTH] = "_";
	board[4 + row*SQUARE_HEIGHT][6 + column*SQUARE_WIDTH] = "_";
	return;
}
void clear_sqaure(string board[ROWS][COLUMNS], int row, int column)
{
	for (int i = 1; i < SQUARE_HEIGHT; i++)
	{
		for (int j = 1; j < SQUARE_WIDTH; j++)
		{
			board[i + SQUARE_HEIGHT*row][j + SQUARE_WIDTH*column]=" ";
		}
	}
}

//initialize board with starting pieces
void board_initialization(string board[ROWS][COLUMNS], piece pieces[32], space spaces[8][8])
{
	int k = 0;
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			if (i < 2)
			{
				space space1(i, j, true, black);
				spaces[i][j] = space1;
				if (k == 0 || k == 7)
				{
					piece piece1(i, j, rook, black);
					pieces[k] = piece1;
				}
				else if (k == 1 || k == 6)
				{
					piece piece1(i, j, knight, black);
					pieces[k] = piece1;
				}
				else if (k == 2 || k == 5)
				{
					piece piece1(i, j, bishop, black);
					pieces[k] = piece1;
				}
				else if (k == 3)
				{
					piece piece1(i, j, queen, black);
					pieces[k] = piece1;
				}
				else if (k == 4)
				{
					piece piece1(i, j, king, black);
					pieces[k] = piece1;
				}
				else
				{
					piece piece1(i, j, pawn, black);
					pieces[k] = piece1;
				}
				k++;
			}
			else if (i >5)
			{
				space space1(i, j, true, white);
				spaces[i][j] = space1;
				if (k == 24 || k == 31)
				{
					piece piece1(i, j, rook, white);
					pieces[k] = piece1;
				}
				else if (k == 25 || k == 30)
				{
					piece piece1(i, j, knight, white);
					pieces[k] = piece1;
				}
				else if (k == 26 || k == 29)
				{
					piece piece1(i, j, bishop, white);
					pieces[k] = piece1;
				}
				else if (k == 27)
				{
					piece piece1(i, j, queen, white);
					pieces[k] = piece1;
				}
				else if (k == 28)
				{
					piece piece1(i, j, king, white);
					pieces[k] = piece1;
				}
				else
				{
					piece piece1(i, j, pawn, white);
					pieces[k] = piece1;
				}
				k++;
			}
			else
			{
				space space1(i, j, false, none);
				spaces[i][j] = space1;
			}
		}
	}
	for (int i = 0; i < ROWS; i++)
	{
		for (int j = 0; j < COLUMNS; j++)
		{
			board[i][j] = " ";
		}
	}
	for (int i = 0; i < ROWS; i++)
	{
		board[i][COLUMNS - 1] = "|";
		board[i][COLUMNS - 15] = "|";
		board[i][COLUMNS - 29] = "|";
		board[i][COLUMNS - 43] = "|";
		board[i][COLUMNS - 57] = "|";
		board[i][COLUMNS - 71] = "|";
		board[i][COLUMNS - 85] = "|";
		board[i][COLUMNS - 99] = "|";
		board[i][COLUMNS - 113] = "|";
	}
	for (int i = 0; i < COLUMNS; i++)
	{
		board[ROWS - 1][i] = "-";
		board[ROWS - 8][i] = "-";
		board[ROWS - 15][i] = "-";
		board[ROWS - 22][i] = "-";
		board[ROWS - 29][i] = "-";
		board[ROWS - 36][i] = "-";
		board[ROWS - 43][i] = "-";
		board[ROWS - 50][i] = "-";
		board[ROWS - 57][i] = "-";
	}
	display_knight(board, pieces[6].get_row(), pieces[6].get_column(), pieces[6]);
	display_knight(board, pieces[1].get_row(), pieces[1].get_column(), pieces[1]);
	display_knight(board, pieces[25].get_row(), pieces[25].get_column(), pieces[25]);
	display_knight(board, pieces[30].get_row(), pieces[30].get_column(), pieces[30]);
	display_rook(board, pieces[31].get_row(), pieces[31].get_column(), pieces[31]);
	display_rook(board, pieces[24].get_row(), pieces[24].get_column(), pieces[24]);
	display_rook(board, pieces[0].get_row(), pieces[0].get_column(), pieces[0]);
	display_rook(board, pieces[7].get_row(), pieces[7].get_column(), pieces[7]);
	display_bishop(board, pieces[2].get_row(), pieces[2].get_column(), pieces[2]);
	display_bishop(board, pieces[5].get_row(), pieces[5].get_column(), pieces[5]);
	display_bishop(board, pieces[26].get_row(), pieces[26].get_column(), pieces[26]);
	display_bishop(board, pieces[29].get_row(), pieces[29].get_column(), pieces[29]);
	display_queen(board, pieces[3].get_row(), pieces[3].get_column(), pieces[3]);
	display_queen(board, pieces[27].get_row(), pieces[27].get_column(), pieces[27]);
	display_king(board, pieces[4].get_row(), pieces[4].get_column(), pieces[4]);
	display_king(board, pieces[28].get_row(), pieces[28].get_column(), pieces[28]);
	display_pawn(board, pieces[8].get_row(), pieces[8].get_column(), pieces[8]);
	display_pawn(board, pieces[9].get_row(), pieces[9].get_column(), pieces[9]);
	display_pawn(board, pieces[10].get_row(), pieces[10].get_column(), pieces[10]);
	display_pawn(board, pieces[11].get_row(), pieces[11].get_column(), pieces[11]);
	display_pawn(board, pieces[12].get_row(), pieces[12].get_column(), pieces[12]);
	display_pawn(board, pieces[13].get_row(), pieces[13].get_column(), pieces[13]);
	display_pawn(board, pieces[14].get_row(), pieces[14].get_column(), pieces[14]);
	display_pawn(board, pieces[15].get_row(), pieces[15].get_column(), pieces[15]);
	display_pawn(board, pieces[16].get_row(), pieces[16].get_column(), pieces[16]);
	display_pawn(board, pieces[17].get_row(), pieces[17].get_column(), pieces[17]);
	display_pawn(board, pieces[18].get_row(), pieces[18].get_column(), pieces[18]);
	display_pawn(board, pieces[19].get_row(), pieces[19].get_column(), pieces[19]);
	display_pawn(board, pieces[20].get_row(), pieces[20].get_column(), pieces[20]);
	display_pawn(board, pieces[21].get_row(), pieces[21].get_column(), pieces[21]);
	display_pawn(board, pieces[22].get_row(), pieces[22].get_column(), pieces[22]);
	display_pawn(board, pieces[23].get_row(), pieces[23].get_column(), pieces[23]);
	return;
}

//display the board in the terminal
void display_board(string board[ROWS][COLUMNS])
{
	int k = 0;
	for (int i = 0; i < ROWS; i++)
	{
		for (int j = 0; j < COLUMNS; j++)
		{
			cout << board[i][j];
		}
		if (((i + 3) % 7) == 0)
		{
			cout << k;
			k++;
		}
		cout << endl;
	}
	cout << "      0             1             2             3             4             5             6             7";
	cout << endl;
}
//see if a king is in check mate
bool mate(piece king, space ks, piece pieces[32], space all_spaces[8][8]);//ks=king spot, where is the king at or planning on moving to/through
vector<space> get_move_options(space all_spaces[8][8], piece moving_piece, piece mover_king, piece pieces[32])
{
	vector<space> move_options;
	switch (moving_piece.get_type())
	{
	case rook:
	{
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() + i < 8)
			{
				if (all_spaces[moving_piece.get_row()][moving_piece.get_column() + i].get_color()!=moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row()][moving_piece.get_column() + i]);
					if (all_spaces[moving_piece.get_row()][moving_piece.get_column() + i].get_occ()) i=9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() - i > -1)
			{
				if (all_spaces[moving_piece.get_row()][moving_piece.get_column() - i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row()][moving_piece.get_column() - i]);
					if (all_spaces[moving_piece.get_row()][moving_piece.get_column() - i].get_occ())i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_row() + i < 8)
			{
				if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column()].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() + i][moving_piece.get_column()]);
					if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column()].get_occ())i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_row() - i > -1)
			{
				if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column()].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() - i][moving_piece.get_column()]);
					if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column()].get_occ()) i = 9;

				}
				else i = 9;
			}
			else i = 9;
		}
		break;
	}
	case knight:
	{
		if (moving_piece.get_row() + 2 < 8 && moving_piece.get_column() + 1 < 8 && all_spaces[moving_piece.get_row() + 2][moving_piece.get_column() + 1].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() + 2][moving_piece.get_column() + 1]);
		}
		if (moving_piece.get_row() + 2 < 8 && moving_piece.get_column() - 1 > -1 && all_spaces[moving_piece.get_row() + 2][moving_piece.get_column() - 1].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() + 2][moving_piece.get_column() - 1]);
		}
		if (moving_piece.get_row() - 2 > -1 && moving_piece.get_column() - 1 > -1 && all_spaces[moving_piece.get_row() - 2][moving_piece.get_column() - 1].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() - 2][moving_piece.get_column() - 1]);
		}
		if (moving_piece.get_row() - 2 > -1 && moving_piece.get_column() + 1 < 8 && all_spaces[moving_piece.get_row() - 2][moving_piece.get_column() + 1].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() - 2][moving_piece.get_column() + 1]);
		}
		if (moving_piece.get_row() - 1 > -1 && moving_piece.get_column() + 2 < 8 && all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() + 2].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() + 2]);
		}
		if (moving_piece.get_row() - 1 > -1 && moving_piece.get_column() - 2 > -1 && all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() - 2].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() - 2]);
		}
		if (moving_piece.get_row() + 1 < 8 && moving_piece.get_column() - 2 > -1 && all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() - 2].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() - 2]);
		}
		if (moving_piece.get_row() + 1 < 8 && moving_piece.get_column() + 2 < 8 && all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() + 2].get_color() != moving_piece.get_color())
		{
			move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() + 2]);
		}
		break;
	}
	case bishop:
	{
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() + i < 8 && moving_piece.get_row() + i < 8)
			{
				if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() + i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() + i][moving_piece.get_column() + i]);
					if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() + i].get_occ())i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() - i > -1 && moving_piece.get_row() - i > -1)
			{
				if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() - i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() - i][moving_piece.get_column() - i]);
					if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() - i].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() + i < 8 && moving_piece.get_row() - i >-1)
			{
				if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() + i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() - i][moving_piece.get_column() + i]);
					if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() + i].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() - i > -1 && moving_piece.get_row() + i < 8)
			{
				if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() - i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() + i][moving_piece.get_column() - i]);
					if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() - i].get_occ()) i = 9;

				}
				else i = 9;
			}
			else i = 9;
		}
		break;
	}
	case queen:
	{
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() + i < 8 && moving_piece.get_row() + i < 8)
			{
				if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() + i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() + i][moving_piece.get_column() + i]);
					if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() + i].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() - i > -1 && moving_piece.get_row() - i > -1)
			{
				if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() - i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() - i][moving_piece.get_column() - i]);
					if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() - i].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() + i < 8 && moving_piece.get_row() - i > -1)
			{
				if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() + i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() - i][moving_piece.get_column() + i]);
					if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column() + i].get_occ())i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() - i > -1 && moving_piece.get_row() + i < 8)
			{
				if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() - i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() + i][moving_piece.get_column() - i]);
					if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column() - i].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() + i < 8)
			{
				if (all_spaces[moving_piece.get_row()][moving_piece.get_column() + i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row()][moving_piece.get_column() + i]);
					if (all_spaces[moving_piece.get_row()][moving_piece.get_column() + i].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_column() - i > -1)
			{
				if (all_spaces[moving_piece.get_row()][moving_piece.get_column() - i].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row()][moving_piece.get_column() - i]);
					if (all_spaces[moving_piece.get_row()][moving_piece.get_column() - i].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_row() + i < 8)
			{
				if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column()].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() + i][moving_piece.get_column()]);
					if (all_spaces[moving_piece.get_row() + i][moving_piece.get_column()].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (moving_piece.get_row() - i > -1)
			{
				if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column()].get_color() != moving_piece.get_color() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() - i][moving_piece.get_column()]);
					if (all_spaces[moving_piece.get_row() - i][moving_piece.get_column()].get_occ()) i = 9;
				}
				else i = 9;
			}
			else i = 9;
		}
		break;
	}
	case king:
	{
		if (moving_piece.get_row() - 1 > -1)
		{
			if (all_spaces[moving_piece.get_row() - 1][moving_piece.get_column()].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column()]);
			}
		}
		if (moving_piece.get_row() + 1 < 8)
		{
			if (all_spaces[moving_piece.get_row() + 1][moving_piece.get_column()].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column()]);
			}
		}
		if (moving_piece.get_column() + 1 < 8)
		{
			if (all_spaces[moving_piece.get_row()][moving_piece.get_column() + 1].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row()][moving_piece.get_column() + 1]);
			}
		}
		if (moving_piece.get_column() - 1 > -1)
		{
			if (all_spaces[moving_piece.get_row()][moving_piece.get_column() - 1].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row()][moving_piece.get_column() - 1]);
			}
		}
		if (moving_piece.get_column() + 1 < 8 && moving_piece.get_row() + 1 < 8)
		{
			if (all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() + 1].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() + 1]);
			}
		}
		if (moving_piece.get_column() - 1 > -1 && moving_piece.get_row() - 1 > -1)
		{
			if (all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() - 1].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() - 1]);
			}
		}
		if (moving_piece.get_row() - 1 > -1 && moving_piece.get_column() + 1 < 8)
		{
			if (all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() + 1].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() + 1]);
			}
		}
		if (moving_piece.get_row() + 1 < 8 && moving_piece.get_column() - 1 > -1)
		{
			if (all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() - 1].get_color() != moving_piece.get_color())
			{
				move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() - 1]);
			}
		}
		break;
	}
	case pawn:
	{
		if (moving_piece.get_color() == white)
		{
			if (!all_spaces[moving_piece.get_row() - 1][moving_piece.get_column()].get_occ() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
			{
				move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column()]);
				if (moving_piece.get_row() == 6 && !all_spaces[moving_piece.get_row() - 2][moving_piece.get_column()].get_occ() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() - 2][moving_piece.get_column()]);
				}
			}
			if (all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() - 1].get_color() == black && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
			{
				move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column()-1]);
			}
			if (all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() + 1].get_color() == black && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
			{
				move_options.push_back(all_spaces[moving_piece.get_row() - 1][moving_piece.get_column() + 1]);
			}

		}
		if (moving_piece.get_color() == black)
		{
			if (!all_spaces[moving_piece.get_row() + 1][moving_piece.get_column()].get_occ() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
			{
				move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column()]);
				if (moving_piece.get_row() == 1 && !all_spaces[moving_piece.get_row() + 2][moving_piece.get_column()].get_occ() && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
				{
					move_options.push_back(all_spaces[moving_piece.get_row() + 2][moving_piece.get_column()]);
				}
			}
			if (all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() - 1].get_color() == white && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
			{
				move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() - 1]);
			}
			if (all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() + 1].get_color() == white && !mate(mover_king, all_spaces[mover_king.get_row()][mover_king.get_column()], pieces, all_spaces))
			{
				move_options.push_back(all_spaces[moving_piece.get_row() + 1][moving_piece.get_column() + 1]);
			}
		}
		break;
	}

	}
	return move_options;
}

//allows a player to choose a move
int choose_move(vector<space> move_options)
{
	int j = 1;
	int k = 0;
	do
	{
		cout << "Select the choice of row and column you wish to move to: \n";
		for (int i = 0; i < move_options.size(); i++)
		{
			cout << i << " : row- " << move_options[i].get_row() << " , column- " << move_options[i].get_column() << endl;
		}
		cin >> k;
		if (move_options.size()<=k)
		{
			j = 0;
		}
		else j = 1;
	}
	while (j==0);
	return k;
}

//where the actual game is played
void play_game(string board[ROWS][COLUMNS], piece pieces[32], space spaces[8][8])
{
	bool game_over = false;
	bool white_turn = true;
	piece mover_king = pieces[28];
	while (!game_over)
	{
		vector<space> move_options;
		int row_choice = 0;
		int column_choice = 0;
		int piece_choice = 0;
		int k = 0;
		int l = 0;
		int n = 0;
		while (k == 0 || l == 0 || n==0)
		{
			if (white_turn)
			{
				cout << "White: Choose a row: ";
				cin >> row_choice;
				cout << "White: Choose a column: ";
				cin >> column_choice;
			}
			else
			{
				cout << "Black: Choose a row: ";
				cin >> row_choice;
				cout << "Black: Choose a column: ";
				cin >> column_choice;
			}
			for (int i = 0; i < 32; i++)
			{
				if (pieces[i].get_row() == row_choice && pieces[i].get_column() == column_choice)
				{
					k = 1;
					piece_choice = i;
					if (white_turn && pieces[piece_choice].get_color() == white)n = 1;
					else if (!white_turn && pieces[piece_choice].get_color() == black)n = 1;
				}
			}
			move_options = get_move_options(spaces, pieces[piece_choice], mover_king, pieces);
			if (move_options.size()>0) l = 1;
		}
		clear_sqaure(board, pieces[piece_choice].get_row(), pieces[piece_choice].get_column());
		int m = choose_move(move_options);
		if (move_options[m].get_occ())
		{
			for (int i = 0; i < 32; i++)
			{
				if (pieces[i].get_row() == move_options[m].get_row() && pieces[i].get_column() == move_options[m].get_column())
				{
					pieces[i].kill();
					i = 32;
				}
			}
		}
		clear_sqaure(board, move_options[m].get_row(), move_options[m].get_column());
		spaces[pieces[piece_choice].get_row()][pieces[piece_choice].get_column()].not_occ();
		spaces[pieces[piece_choice].get_row()][pieces[piece_choice].get_column()].change_color(none);
		pieces[piece_choice].move_piece(move_options[m].get_row(), move_options[m].get_column());
		spaces[pieces[piece_choice].get_row()][pieces[piece_choice].get_column()].is_occ();
		spaces[pieces[piece_choice].get_row()][pieces[piece_choice].get_column()].change_color(pieces[piece_choice].get_color());
		if (pieces[piece_choice].get_type() == rook)
		{
			display_rook(board, pieces[piece_choice].get_row(), pieces[piece_choice].get_column(), pieces[piece_choice]);
			display_board(board);
		}
		else if (pieces[piece_choice].get_type() == knight)
		{
			display_knight(board, pieces[piece_choice].get_row(), pieces[piece_choice].get_column(), pieces[piece_choice]);
			display_board(board);
		}
		else if (pieces[piece_choice].get_type() == bishop)
		{
			display_bishop(board, pieces[piece_choice].get_row(), pieces[piece_choice].get_column(), pieces[piece_choice]);
			display_board(board);
		}
		else if (pieces[piece_choice].get_type() == queen)
		{
			display_queen(board, pieces[piece_choice].get_row(), pieces[piece_choice].get_column(), pieces[piece_choice]);
			display_board(board);
		}
		else if (pieces[piece_choice].get_type() == king)
		{
			display_king(board, pieces[piece_choice].get_row(), pieces[piece_choice].get_column(), pieces[piece_choice]);
			display_board(board);
		}
		else
		{
			display_pawn(board, pieces[piece_choice].get_row(), pieces[piece_choice].get_column(), pieces[piece_choice]);
			display_board(board);
		}
		if (white_turn)
		{
			white_turn = false;
			mover_king = pieces[4];
		}
		else
		{
			white_turn = true;
			mover_king = pieces[28];
		}
		if (pieces[4].get_dead())
		{
			cout << "White wins! Game over\n";
			game_over = true;
		}
		else if (pieces[28].get_dead())
		{
			cout << "Black wins! Game over\n";
			game_over = true;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	piece pieces[32];
	space spaces[8][8];
	string board[ROWS][COLUMNS];
	board_initialization(board, pieces, spaces);
	display_board(board);
	system("pause");
	play_game(board, pieces, spaces);
	system("pause");
	return 0;
}
bool mate(piece king, space ks, piece pieces[32], space all_spaces[8][8])
{
	int row_orig;
	int col_orig;
	bool mate = false;
	vector<piece> enemies;
	for (int i = 0; i < 32; i++)
	{
		if (king.get_color() != pieces[i].get_color() && !pieces[i].get_dead()) enemies.push_back(pieces[i]);
	}
	for (int j = 0; j<enemies.size(); j++)
	{
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_row() + i > 7)i = 9;
			if (ks.get_row() + i == enemies[j].get_row() && ks.get_column() == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == rook)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row() + i][ks.get_column()].get_occ())i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_row() - i < 0)i = 9;
			if (ks.get_row() - i == enemies[j].get_row() && ks.get_column() == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == rook)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row() - i][ks.get_column()].get_occ())i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_column() - i < 0)i = 9;
			if (ks.get_row()== enemies[j].get_row() && ks.get_column()-i == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == rook)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row()][ks.get_column() - i].get_occ())i = 9;
		}		
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_column() + i > 7)i = 9;
			if (ks.get_row() == enemies[j].get_row() && ks.get_column() - i == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == rook)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row()][ks.get_column() - i].get_occ())i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_column() + i > 7 || ks.get_row() + i > 7)i = 9;
			if (ks.get_row() + i == enemies[j].get_row() && ks.get_column() + i == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == bishop)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row() + i][ks.get_column() + i].get_occ())i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_column() + i > 7 || ks.get_row() -i < 0)i = 9;
			if (ks.get_row() + i == enemies[j].get_row() && ks.get_column() - i == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == bishop)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row() + i][ks.get_column() - i].get_occ())i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_column() - i < 0 || ks.get_row() - i < 0)i = 9;
			if (ks.get_row() - i == enemies[j].get_row() && ks.get_column() - i == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == bishop)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row() - i][ks.get_column() - i].get_occ())i = 9;
		}
		for (int i = 1; i < 8; i++)
		{
			if (ks.get_column() - i < 0 || ks.get_row() + i > 7)i = 9;
			if (ks.get_row() - i == enemies[j].get_row() && ks.get_column() + i == enemies[j].get_column())
			{
				if (enemies[j].get_type() == queen || enemies[j].get_type() == bishop)
				{
					mate = true;
					i = 9;
					j = 17;
				}
			}
			if (all_spaces[ks.get_row() - i][ks.get_column() + i].get_occ()) i = 9;
		}
		if (ks.get_column() + 2 == enemies[j].get_column() && ks.get_row() + 1 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_column() + 2 == enemies[j].get_column() && ks.get_row() - 1 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_column() - 2 == enemies[j].get_column() && ks.get_row() + 1 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_column() - 2 == enemies[j].get_column() && ks.get_row() - 1 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_column() + 1 == enemies[j].get_column() && ks.get_row() + 2 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_column() + 1 == enemies[j].get_column() && ks.get_row() - 2 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_column() - 1 == enemies[j].get_column() && ks.get_row() + 2 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_column() - 1 == enemies[j].get_column() && ks.get_row() - 2 == enemies[j].get_row() && enemies[j].get_type() == knight)
		{
			mate = true;
			j = 17;
		}
		if (ks.get_row() - 1 == enemies[j].get_row() && ks.get_column() + 1 == enemies[j].get_column())
		{
			if (enemies[j].get_type() == pawn && king.get_color() ==white)
			{
				mate = true;
				j = 17;
			}
		}
		if (ks.get_row() - 1 == enemies[j].get_row() && ks.get_column() - 1 == enemies[j].get_column())
		{
			if (enemies[j].get_type() == pawn && king.get_color() == white)
			{
				mate = true;
				j = 17;
			}
		}
		if (ks.get_row() + 1 == enemies[j].get_row() && ks.get_column() + 1 == enemies[j].get_column())
		{
			if (enemies[j].get_type() == pawn && king.get_color() == black)
			{
				mate = true;
				j = 17;
			}
		}
		if (ks.get_row() + 1 == enemies[j].get_row() && ks.get_column() - 1 == enemies[j].get_column())
		{
			if (enemies[j].get_type() == pawn && king.get_color() == black)
			{
				mate = true;
				j = 17;
			}
		}

	}
	return mate;
}

