from .variables import varlist

def echo(msg: str, **variables) -> None:
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