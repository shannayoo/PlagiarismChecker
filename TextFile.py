from typing import List

class TextFile:
    """ A text file to check plagiarism.
    """

    # === Private Attributes ===
    # _num_lines:
    #   The number of lines that this file contains.
    # _curr_lines:
    #   The line of text file that the program is currently pointing at.
    #   Set as None if text file is empty
    # _all_lines:
    #   A list of every line in the text file in order.
    _num_lines: int
    _curr_lines: str
    _all_lines: List[str]

    def __init__(lines_lst: List[str]) -> None:
        """ Initialize this text file as described in description.
        """
        self._num_lines = len(lines_lst)
        self._all_lines = lines_lst
        
        # set _curr_lines if file is empty, otherwise set it to the first line
        if len(lines_lst) == 0:
            self._curr_lines = None
        else:
            self._curr_lines = lines_lst[0]

    def get_num_lines() -> int:
        """ Return the number of lines that this file contains.
        """
        return self._num_lines

    def get_curr_lines() -> str:
        """ Return the line of text file that the program is currently pointing at.
        """
        return self._curr_lines

    def get_all_lines() -> List[str]:
        """ Return a list of every line in the text file in order.
        """
        return self._all_lines

    def is_empty() -> bool:
        """ Return whether this text file is an empty file.
        """
        return _curr_lines == None
