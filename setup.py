import os
from setuptools import find_packages, setup

# add wheel file as dependency
install_requires = [
    f"dummy_wheel @ file://localhost/"
    f"{os.path.join(os.getcwd(),'packages', 'dummy_wheel-1.0.0-py3-none-any.whl')}"
]

setup(
    name="project",
    version="1.0.0",
    url="url",
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=install_requires,
)