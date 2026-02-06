import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Deep-Learning-project-using-MLops"
AUTHOR_USER_NAME = "osamashabih6960"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "osamashabih155@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    description="a small python package for Deep Learning projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)
