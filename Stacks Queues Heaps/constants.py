PARENTHISIS = '('
BRACKET = '{'
SQUARE_BRACKET = '['
PARENTHISIS_END = ')'
BRACKET_END = '}'
SQUARE_BRACKET_END = ']'


def is_start(char):
    start_chars = [BRACKET, PARENTHISIS, SQUARE_BRACKET]
    return char in start_chars


def is_end(char):
    end_chars = [BRACKET_END, PARENTHISIS_END, SQUARE_BRACKET_END]
    return char in end_chars