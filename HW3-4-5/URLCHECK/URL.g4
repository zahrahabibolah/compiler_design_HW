grammar URL;

url: httpURL | httpsURL;

httpURL: 'http://' host port? path?;
httpsURL: 'https://' host port? path?;

host: DOMAIN | IP_ADDRESS;
port: ':' DIGIT+;
path: '/' SEGMENT*;

DOMAIN: [a-zA-Z0-9.-]+;
IP_ADDRESS: DIGIT '.' DIGIT '.' DIGIT '.' DIGIT;

SEGMENT: [a-zA-Z0-9_-]+;
DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;
