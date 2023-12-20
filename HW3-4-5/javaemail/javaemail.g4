grammar javaemail;


EMAIL: '"' (~["\r\n"] | '\\' . | EMAIL_ESCAPE)* '@' (~["\r\n"] | '\\' .)* '.' (~["\r\n"] | '\\' .)* '"';

fragment EMAIL_ESCAPE: '\\' [nrt\\"'] ;
fragment ESC : '\\' . ;

