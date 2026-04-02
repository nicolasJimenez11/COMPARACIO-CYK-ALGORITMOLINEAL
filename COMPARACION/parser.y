%{
#include <stdio.h>
#include <time.h>

void yyerror(const char *s);
int yylex();
%}

%token NUM
%left '+'

%%
input: exp;
exp: NUM | exp '+' NUM;
%%

void yyerror(const char *s) {}

int main() {
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    yyparse();

    clock_gettime(CLOCK_MONOTONIC, &end);
    double time_ms = (end.tv_sec - start.tv_sec) * 1e3 + (end.tv_nsec - start.tv_nsec) / 1e6;
    printf("%f", time_ms); 
    return 0;
}
