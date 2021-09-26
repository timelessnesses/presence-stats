from setuptools import setup
 
classifiers = []
 
setup(
  name='pypresence-stats',
  version='1.6',
  description='Presence-stats but you can make python script and launch it.',
  long_description=open("README.md").read(),
  long_description_content_type='text/markdown',
  url='https://redirect.biomooping.tk/HOB1UlWkCg',  
  author='Rukchad Wongprayoon',
  author_email='contact@biomooping.tk',
  license='MIT', 
  classifiers=classifiers,
  keywords='Tools', 
  packages=["presencestats"],
  install_requires=["pypresence","psutil"],
  entry_points={
    'console_scripts': ['pypresence=presencestats.__init__:launcharg']
  }
)
