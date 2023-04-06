import os
import sys

def restart_app():
    """Restarts the current program, with file objects and descriptors
       cleanup"""
    try:
        p = os.popen(sys.executable + ' ' + __file__)
        return
    except:
        print('Error: Could not restart program')
        return


