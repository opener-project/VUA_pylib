import os

from distutils.core import setup

# Get all the directories for the package that lazy way. This way we don't have
# to also manually update that list.
lib_name    = 'VUA_pylib'
directories = [lib_name]

for name in os.listdir(lib_name):
    full_path = os.path.join(lib_name, name)

    if os.path.isdir(full_path):
        directories.append('%s.%s' % (lib_name, name))

setup(
    name         = lib_name,
    version      = '1.5',
    description  = 'Various KAF / NAF python helpers',
    author       = 'Ruben Izquierdo',
    url          = 'https://github.com/cltl/VUA_pylib',
    author_email = 'r.izquierdobevia@vu.nl',
    packages     = directories,
)
