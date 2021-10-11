from setuptools import setup, find_packages

setup(name='mne_qt_browser',
      version='0.0.1',
      author='marsipu',
      author_email='dev@earthman-music.de',
      description='A new backend based on pyqtgraph for the 2D-Data-Browser '
                  'in MNE-Python.',
      license='License :: OSI Approved :: BSD License',
      url='https://github.com/marsipu/mne_pg_browser',
      project_urls={'Bug Tracker':
                    'https://github.com/marsipu/mne_pg_browser/issues'},
      classifiers=['Programming Language :: Python :: 3',
                   'License :: OSI Approved :: BSD License',
                   'Operating System:: OS Independent'],
      packages=find_packages(),
      install_requires=['numpy',
                        'scipy',
                        'matplotlib',
                        'PyQt5',
                        'qtpy',
                        'mne',
                        'pyqtgraph@git+https://git@github.com/pyqtgraph/pyqtgraph@master#egg=pyqtgraph',  # noqa: E501
                        'pyopengl'],
      entrypoints={'console_scripts':
                       ['mne_qt_browser = mne_qt_browser.__main__:main']}
      )
