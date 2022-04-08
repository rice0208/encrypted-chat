from distutils.core import setup
from setuptools import find_packages

setup(
    name="encrypted-chat",
    version="0.1.0",
    description="用“加密通话”彻底告别被查聊天记录的黑历史",
    long_description="",
    author="rice0208",
    author_email="riceforever0208@outlook.com",
    url="https://github.com/rice0208/encrypted-chat",
    install_requires=["pydes"],
    license="BSD License",
    packages=find_packages(),
    platforms=["all"],
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
