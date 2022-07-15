import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = [
  "django>=2.2",
]

VERSION = "0.0.1.1"
URL = "https://veryeasyai.com/"

setuptools.setup(
    name="very_easy_recommendation_engine",
    version=VERSION,
    author="veryeasyai",
    url=URL,
    description="A Very Easy Recommendation Engine for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords="django, AI, artificial-intelligence, veryeasyai, machine-learning, neural-networks, recommendation-systems",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["very_easy_recommendation_engine"],
    package_dir={'':'very_easy_recommendation_engine'},
    install_requires=REQUIRES
)
