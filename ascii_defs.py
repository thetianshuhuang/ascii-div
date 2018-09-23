
"""ASCII Art Definitions

Attributes
----------
LINE_WIDTH : int
    Maximum width, in columns, of each line. Set at 79 for PEP-8 compliance.
COMMENT : dict
    Mappings from file extensions to comment types.
"""

LINE_WIDTH = 79

COMMENT = {
    ".py": "#",     # Python
    ".c": "//",     # C
    ".cpp": "//",   # C++
    ".h": "//",     # C/C++ Headers
    ".sh": "#",     # Shell scripts
    ".js": "//",    # JavaScript
    ".java": "//",  # Java
    ".asm": ";",    # Assembly
}


def pad(text, char):
    """Pad text until the line width is reached

    Parameters
    ----------
    text : str
        Original text
    char : char[1]
        Character to pad the line with

    Returns
    -------
    str
        Text padded with ``char`` to the column limit
    """

    assert len(char) == 1
    return text + char * (LINE_WIDTH - len(text)) + "\n"


def center(pre, text):
    """Center text in a comment

    Parameters
    ----------
    pre : str
        Text that needs to stay left aligned
    text : str
        Text to be centered

    Returns
    -------
    str
        Centered text ``text``, with left aligned ``pre``
    """

    return (
        pre +
        " " * int((LINE_WIDTH - len(text) - len(pre)) / 2) +
        text + "\n")


# -----------------------------------------------------------------------------
#
#                                Divider Types
#
# -----------------------------------------------------------------------------
DIVIDERS = {
    "small": lambda text, lang: (
        pad(COMMENT[lang] + " -- " + text + " ", "-")
    ),
    "large": lambda text, lang: (
        pad(COMMENT[lang] + " ", "-") +
        COMMENT[lang] + "\n" +
        center(COMMENT[lang], text) +
        COMMENT[lang] + "\n" +
        pad(COMMENT[lang] + " ", "-")
    )
}
