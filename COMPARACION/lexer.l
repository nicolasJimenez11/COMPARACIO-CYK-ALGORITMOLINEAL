%{
#include "parser.tab.h"
%}

%%
[0-9]+      { return NUM; }
"+"         { return '+'; }
"*"         { return '*'; }
[ \t\n]     { ; } /* Ignorar espacios */
.           { return yytext[0]; }
%%

int yywrap() { return 1; }
