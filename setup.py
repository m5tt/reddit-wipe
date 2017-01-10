from setuptools import setup, find_packages

setup(
    name='redditwipe',
    version='0.1.dev',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'reddit-wipe = redditwipe.redditwipe:main'
        ]
    },
    install_requires=['praw'],
    license='MIT',
    url='https://github.com/m5tt/reddit-wipe',
    author='m5tt',
    author_email='arks36@protonmail.com'
)
