#pragma once
class space
{
private:
	int row;
	int column;
	bool occupied;
	color c;
public:
	space(int r, int col, bool occ, color clr);
	space();
	bool get_occ();
	int get_row();
	int get_column();
	void is_occ();
	void not_occ();
	enum color get_color();
	void change_color(color colr);
};

