grammar CPPcomment;

// Parser rules
compilationUnit: codeBlock EOF;

codeBlock: (line | block | COMMENT)*;

line: ~[\r\n]* '\r'? '\n';

block: '{' codeBlock '}';

// Lexer rules
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;

WS: [ \t]+ -> skip;

