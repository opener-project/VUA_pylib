from distutils.core import setup


setup(name='VUA_pylib',
      version='1.1',
      description = 'Various KAF / NAF python helpers',
      author = 'Ruben Izquierdo',
      url = 'https://github.com/cltl/VUA_pylib',
      author_email = 'r.izquierdobevia@vu.nl',
      package_dir = {'':''},
      packages = ['lexicon','common','io','corpus_reader'],
      )
