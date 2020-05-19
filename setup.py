from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='scb-payment',
    version='0.1.0',
    description='A Python library for SCB Payment API',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/sang-sakarin/scb-payment',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='scb scb-python scb-python-sdk scb-payment scb-payment-python',
    packages=['scb_payment'],
    install_requires=['requests'],
)
