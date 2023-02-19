import re


class Token_regex:
    TOKEN_REGEX = {
        'PALAVRAS_RESERVADAS': r"PROGRAM|INTEGER|BOOLEAN|BEGIN|END|WHILE|DO|READ|VAR|FALSE|TRUE|WRITE",
        'OP_ARITIMETICOS': r"[\+\-\*\/]",
        'OP_LOGICOS': r"[OR|AND]",
    }
