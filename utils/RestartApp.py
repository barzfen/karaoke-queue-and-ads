import os
import sys

def restart_app():
    """
    Restarts the current Python program.
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)


