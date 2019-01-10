#include "stdafx.h"
#include "piece.h"


piece::piece(int r, int col, type pt, color pc)
{
	row = r;
	column = col;
	t = pt;
	c = pc;
	dead = false;
	move = false;
}
piece::piece()
{
	row = 0;
	column = 0;
	t = pawn;
	c = white;
	dead = false;
	move = false;
}
int piece::get_row()
{
	return row;
}
int piece::get_column()
{
	return column;
}
void piece::move_piece(int ro, int col)
{
	row = ro;
	column = col;
	move = true;
	return;
}

type piece::get_type()
{
	return t;
}
color piece::get_color()
{
	return c;
}
void piece::kill()
{
	row = -2;
	column = -2;
	dead = true;
}
bool piece::get_dead()
{
	return dead;
}
bool piece::get_move()
{
	return move;
}
