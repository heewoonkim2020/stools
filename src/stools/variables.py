'''
Support for variables in sTools.
'''

varlist = {}

def set(variable: str, content) -> None:
    '''
    Set a variable.

    :param variable: (str) The name of the variable.
    :param content: (Any) The content to put.
    '''

    global varlist

    varlist[variable] = content
    return None

def get(variable: str):
    '''
    Return a variable.

    :param variable: (str) The name of the variable.

    :return: (Any) The content of the variable given.
    '''

    return varlist[variable]