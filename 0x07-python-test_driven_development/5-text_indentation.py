#!/usr/bin/python3
"""define a function that print text"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
      text (string): The text to be print.

      Raises:
        TypeError: If the text is not a string.
    """

    if not isinstance(text, str):

        raise TypeError("text must be a string")

    i = 0
    txt_len = len(text)
    while i < txt_len and text[i] == ' ':
        i += 1

    while i < txt_len:
        print(text[i], end="")

        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1

            while i < txt_len and text[i] == ' ':
                i += 1
            continue

        i += 1
