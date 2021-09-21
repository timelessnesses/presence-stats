from setuptools import setup
 
classifiers = []
 
setup(
  name='pypresence-stats',
  version='1.2',
  description='Presence-stats but you can make python script and launch it.',
  long_description=open("README.md").read(),
  long_description_content_type='text/markdown',
  url='https://github.com/dumb-stuff/Meta-search',  
  author='Rukchad Wongprayoon',
  author_email='contact@biomooping.tk',
  license='MIT', 
  classifiers=classifiers,
  keywords='Tools', 
  packages=["presencestats"],
  install_requires=["pypresence","psutil"],
  entry_points={
    'console_scripts': ['pypresence=pypresence.__init__:launcharg']
  }
)