// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include "targetver.h"

#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <sstream>
#include <vector>
#include "piece.h"
#include "space.h"
const int ROWS = 57;
const int COLUMNS = 113;
const int SQUARE_WIDTH = 14;
const int SQUARE_HEIGHT = 7;
enum type { rook, knight, bishop, queen, king, pawn };
enum color{ black, white, none };

using namespace std;




// TODO: reference additional headers your program requires here
