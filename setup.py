import setuptools

setuptools.setup(
    name="baldrick_circleci",
    version="0.1.0",
    url="https://github.com/Cadair/baldrick-circleci",

    author="Stuart Mumford",
    author_email="stuart@cadair.com",

    description="A plugin for baldrick for listening to circleci webhooks.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
