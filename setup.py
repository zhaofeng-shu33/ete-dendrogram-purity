# only support edit install
# pip install -e .
from setuptools import setup

with open("README.md") as fh:
    long_description = fh.read()
    
if __name__ == '__main__':
    setup(name = 'ete-dendrogram-purity',
          version = '0.1',
          description = 'implement dengram purity for ete.Tree structure',
          author = 'zhaofeng-shu33',
          author_email = '616545598@qq.com',
          url = 'https://github.com/zhaofeng-shu33/ete-dendrogram-purity',
          maintainer = 'zhaofeng-shu33',
          maintainer_email = '616545598@qq.com',
          long_description = long_description,
          long_description_content_type="text/markdown",          
          install_requires = ['ete3'],
          license = 'Apache License Version 2.0',
          py_modules = ['dendrogram_purity'],
          classifiers = (
              "Development Status :: 4 - Beta",
              "Programming Language :: Python :: 3.7",
              "Programming Language :: Python :: 3.6",
              "Operating System :: OS Independent",
          ),
    )