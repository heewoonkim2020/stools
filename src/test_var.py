import stools
from io import StringIO
from unittest.mock import patch

def test_variable_set():
    stools.variables.set('case', 'test')
    assert stools.variables.get('case') == 'test', 'Failed to set or get var'

def test_echo_var():
    stream = StringIO()
    with patch('sys.stdout', stream):
        stools.echo('Testing with ($tool)', tool='PyTest')
    tc1 = stream
    del stream
    stream = StringIO()
    stools.variables.set('TEST_TOOL', 'PyTest')
    with patch('sys.stdout', stream):
        stools.echo('Testing with ($TEST_TOOL)')
    tc2 = stream
    del stream
    
    assert tc1.read() == tc2.read()

def test_import():
    from stools import variables
    assert variables
    print('Get variable: [INFO] Success')
    del variables

def test_silentecho():
    retmsg = stools.silent_echo('Testing with ($tool)', tool='PyTest')
    assert retmsg == 'Testing with PyTest'
    assert type(retmsg) is str