from setuptools import setup
import re

requirements = []
with open('requirements.txt', encoding='utf-8') as f:
  requirements = f.read().splitlines()

version = ''
with open('discord_py_ext_tasks_loop_group/__init__.py', encoding='utf-8') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')


readme = ''
with open('README.md', encoding='utf-8') as f:
    readme = f.read()


packages = [
    'discord_py_ext_tasks_loop_group'
]

setup(name='dpy-ext-tasks-loop-group',
      author='AomiVel',
      url='https://github.com/Req-kun/d.py-ext-tasks-loop-group',
      project_urls={},
      version=version,
      packages=packages,
      license='MIT',
      description='Discord.pyのext.tasks.loopの拡張',
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.8.0',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet'
      ]
)
