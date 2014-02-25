from distutils.core import setup

setup(name='VUA_pylib',
      version='1.0',
      description = 'Various KAF / NAF python helpers',
      author = 'Ruben Izquierdo',
      author_email = 'r.izquierdobevia@vu.nl',
      packages = ['VUA_pylib.lexicon','VUA_pylib.common',
        'VUA_pylib.io','VUA_pylib.corpus_reader']
      )
