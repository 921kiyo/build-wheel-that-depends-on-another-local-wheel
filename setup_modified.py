from setuptools import find_packages, setup

with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = [x.strip() for x in f]

setup(
    name="project",
    version="1.0.0",
    url="url",
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=install_requires,
)