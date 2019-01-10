#pragma once
class piece
{
protected:
	int row;
	int column;
	enum type t;
	enum color c;
	bool dead;
	bool move;
public:
	piece(int r, int c, type pt, color pc);//r=row c=column, pt=piece type, pc=piece color
	piece();
	int get_row();
	int get_column();
	enum type get_type();
	void move_piece(int ro, int col);
	enum color get_color();
	void kill();
	bool get_dead();
	bool get_move();
};

