import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="very_easy_recommendation_engine",
    version="0.0.1",
    author="veryeasyai",
    description="A Very Easy Recommendation Engine for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["very_easy_recommendation_engine"],
    package_dir={'':'very_easy_recommendation_engine'},
    install_requires=[]
)
