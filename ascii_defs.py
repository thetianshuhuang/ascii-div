
"""ASCII Art Definitions

Attributes
----------
LINE_WIDTH : int
    Maximum width, in columns, of each line. Set at 79 for PEP-8 compliance.
COMMENT : dict
    Mappings from file extensions to comment types.
"""

from .pyfiglet import Figlet


LINE_WIDTH = 79

COMMENT = {
    ".py": "#",         # Python
    ".c": "//",         # C
    ".cpp": "//",       # C++
    ".h": "//",         # C/C++ Headers
    ".sh": "#",         # Shell scripts
    ".js": "//",        # JavaScript
    ".java": "//",      # Java
    ".asm": ";",        # Assembly
    ".gitignore": "#",  # .gitignore
    ".": "#",           # default
}


def comment(ending):
    """Get comment type corresponding to a file type

    Parameters
    ----------
    ending : str
        File ending, including the '.'

    Returns
    -------
    str
        Comment header (#, //, etc)
    """
    try:
        return COMMENT[ending]
    except KeyError:
        return COMMENT['.']


def cblock(text, lang):
    """Comment multi-line text block"""

    return '\n'.join([comment(lang) + ' ' + t for t in text.split('\n')])


def pad(text, char, width):
    """Pad text until the line width is reached

    Parameters
    ----------
    text : str
        Original text
    char : char[1]
        Character to pad the line with
    width : int
        Line width

    Returns
    -------
    str
        Text padded with ``char`` to the column limit
    """

    assert len(char) == 1
    return text + char * (width - len(text))


def center(pre, text, width):
    """Center text in a comment

    Parameters
    ----------
    pre : str
        Text that needs to stay left aligned
    text : str
        Text to be centered
    width : int
        Line width

    Returns
    -------
    str
        Centered text ``text``, with left aligned ``pre``
    """

    return (
        pre +
        " " * int((width - len(text) - len(pre)) / 2) +
        text)


def indent(text, indentation):

    return '\n'.join([indentation + t for t in text.split('\n')])


def __trailing_sp(text):

    while len(text) > 1 and text[-1] == ' ':
        text = text[:-1]
    return text


def trailing_sp(text):

    return '\n'.join([__trailing_sp(row) for row in text.split('\n')])


def leading_newline(text):

    while len(text) > 0 and text[0] == '\n':
        text = text[1:]
    return text


def trailing_newline(text):

    while len(text) > 0 and (text[-1] == '\n' or text[-1] == ' '):
        text = text[:-1]
    return text


# -----------------------------------------------------------------------------
#
#                                Divider Types
#
# -----------------------------------------------------------------------------


def div_small(text, lang, padding):

    return indent(
        pad(comment(lang) + ' -- ' + text + ' ', "-", LINE_WIDTH - padding),
        padding * ' ')


def div_medium(text, lang, padding):

    return (
        ' ' * padding + comment(lang) + '\n' +
        div_small(text, lang, padding) + '\n' +
        ' ' * padding + comment(lang))


def div_large(text, lang, padding):

    return indent(
        pad(comment(lang) + ' ', '-', LINE_WIDTH - padding) + '\n' +
        comment(lang) + '\n' +
        center(comment(lang), text, LINE_WIDTH - padding) + '\n' +
        comment(lang) + '\n' +
        pad(comment(lang) + ' ', '-', LINE_WIDTH - padding),
        ' ' * padding
    )


def div_figlet(text, lang, padding, font='small'):

    f = Figlet(font=font)

    return trailing_sp(
        indent(
            cblock(
                leading_newline(trailing_newline(f.renderText(text))),
                lang),
            ' ' * padding))
