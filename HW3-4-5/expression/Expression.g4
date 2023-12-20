grammar Expression;

expression : additiveExpression EOF;

additiveExpression : multiplicativeExpression ( ('+' | '-') multiplicativeExpression )*;

multiplicativeExpression : primaryExpression ( ('*' | '/') primaryExpression )*;

primaryExpression : NUMBER | '(' expression ')';

NUMBER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
