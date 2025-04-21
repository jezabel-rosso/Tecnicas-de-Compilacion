grammar MiLenguaje;

// Reglas del parser
program         : statement* EOF ;

statement
    : ifStatement
    | expressionStatement
    ;

ifStatement
    : 'if' '(' expression ')' block ('else' block)?
    ;

block
    : '{' statement* '}'
    ;

expressionStatement
    : expression ';'
    ;

expression
    : operand (OPERATOR operand)* // muy simplificado
    ;

operand
    : ID
    | INTEGER
    | FLOAT
    | STRING
    | BOOLEAN
    | '(' expression ')'
    ;

// Lexer rules (reglas léxicas)
// Identificadores
ID          : [a-zA-Z][a-zA-Z0-9_]* ;

// Literales
INTEGER     : [0-9]+ ;
FLOAT       : [0-9]+ '.' [0-9]+ ;
STRING      : '"' (~["\r\n] | '\\"')* '"' ;
BOOLEAN     : 'true' | 'false' ;

// Palabras clave
KEYWORD     : 'var' | 'if' | 'else' | 'print' | 'while' | 'function' | 'return' ;

// Operadores
OPERATOR    : '+' | '-' | '*' | '/' | '%' | '=' | '==' | '!=' | '<' | '>' | '<=' | '>=' | '&&' | '||' | '!' ;

// Separadores
SEPARATOR   : ';' | '(' | ')' | '{' | '}' | ',' | '.' ;

// Ignorar espacios en blanco y comentarios
WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip ;
