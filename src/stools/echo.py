from .variables import varlist

def echo(msg: str, **variables) -> None:
    '''
    Print a message to `sys.stdout` with the variables provided.

    :param msg: (str) The message to convert.
    :param variables: (dict, auto) The variables.
    '''

    message = msg
    pmessage = msg
    for val in varlist:
        pmessage = pmessage.replace('(${})'.format(val), str(varlist[val]))

    for val in variables:
        message = message.replace('(${})'.format(val), str(variables[val]))
    else:
        message = pmessage
    print(message)
    return None

def silent_echo(msg: str, **variables) -> None:
    '''
    Like echo, but returns the message instead of printing.

    :param msg: (str) The message to convert.
    :param variables: (dict, auto) The variables.
    '''
    
    message = msg
    pmessage = msg
    for val in varlist:
        pmessage = pmessage.replace('(${})'.format(val), str(varlist[val]))

    for val in variables:
        message = message.replace('(${})'.format(val), str(variables[val]))
    else:
        message = pmessage
    return message