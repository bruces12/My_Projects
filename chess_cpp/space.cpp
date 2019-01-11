#include "stdafx.h"
#include "space.h"


space::space(int r, int col, bool occ, color clr)
{
	row = r;
	column = col;
	occupied = occ;
	c = clr;
}
space::space()
{
	row = 0;
	column = 0;
	occupied = false;
	c = none;
}
int space::get_column()
{
	return column;
}
int space::get_row()
{
	return row;
}
bool space::get_occ()
{
	return occupied;
}
void space::is_occ()
{
	occupied = true;
}
void space::not_occ()
{
	occupied = false;
}
color space::get_color()
{
	return c;
}
void space::change_color(color colr)
{
	c = colr;
}

