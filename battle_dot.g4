grammar battle_dot;

start: prog | <EOF> ;

prog:  dot_name 
       dot_emoji
       on_stmt+;

dot_name :  'dot_name' ':'  NAME_ID ';';
dot_emoji : 'dot_emoji' ':'  EMOJI ';';
on_stmt : ON_STMT_NAMES ':'  BEHAVIOR_NAMES  '(' (VALUE (',' VALUE)*)?  ')'  ('->' TARGETS)? ';' ;



ON_STMT_NAMES : 'on_start' | 'on_spawn';
BEHAVIOR_NAMES : 'rumba' | 'killer' ;
TARGETS : 'all' | 'new' | 'some';
NAME_ID : ('a'..'z' | 'A'..'Z' | '_')+;
EMOJI : [\p{Emoji}] ;

VALUE   :   ('0'..'9')+ '.' ('0'..'9')+ ;
WS : [ \r\n\t]+ -> skip;
