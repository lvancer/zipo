from distutils.core import setup, find_packages


packages = ['zipo']

setup(
    name="zipo",
    version="0.1",
    url="https://github.com/lvancer/zipo",
    author="lvancer",
    author_email="lin029011@163.com",
    license="MIT",
    description="",
    packages=find_packages(exclude=("*examples", "*examples.*", "*tests", "*tests.*")),
)
