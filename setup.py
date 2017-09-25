from setuptools import setup

setup(name='mp3stream',
      packages=['mp3stream'],
      version='0.1',
      description='Download streaming mp3 radio',
      url='http://github.comphilip-iv/mp3stream',
      author='Philip Stephenson',
      author_email='philipstephenson4+mp3stream@gmail.com',
      license='MIT',
      zip_safe=True,
      install_requires=[
          'requests',
      ],)