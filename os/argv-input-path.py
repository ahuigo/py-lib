import readline, glob
def complete(text, state):
    #buffer = readline.get_line_buffer()
    return (glob.glob(text+'*')+[None])[state]

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
input('file? ')
