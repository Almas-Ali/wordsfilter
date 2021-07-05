from sys import argv

help = '''This is help for wordsfilter.'''
__version__ = 0.1

try:
    if argv[1] == '--version':
        print(f'version {__version__}')
    else:
        print(help)
except Exception as e:
    print(help)
