import os
rootdir = os.path.dirname(__file__)

with open(os.path.join(rootdir, 'VERSION')) as vf:
    __version__ = vf.read().strip()
