grammar email;

fragment LOCAL_SUBPART : [a-zA-Z0-9._%+-]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9.-]+;
EMAIL: LOCAL_SUBPART '@' DOMAIN_SUBPART '.' DOMAIN_SUBPART;

email: EMAIL;

WS: [ \t\r\n]+ -> skip;