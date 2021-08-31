from setuptools import setup
import re

pakage_name = 'async_fateslist'
requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

version = ''
with open(f'{pakage_name}/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
with open('README.rst') as f:
    readme = f.read()

extras_require = {
    'widgets': ['Pillow>=3.7'],
}

packages = [
    pakage_name,
    f'{pakage_name}.client',
    f'{pakage_name}.errors',
]

setup(name=pakage_name,
      author='Dhruva Shaw',
      url='https://github.com/Fates-List/async-fateslist',
      project_urls={
        "Documentation": "https://discordpy.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/Fates-List/async-fateslist/issues",
      },
      version=version,
      packages=packages,
      license='GNU GENERAL PUBLIC LICENSE',
      description='A Python wrapper for the FatesList API',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      extras_require=extras_require,
      python_requires='>=3.7',
      classifiers=[
        'Development Status :: 5 - Production/UnStable',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
      ]
)