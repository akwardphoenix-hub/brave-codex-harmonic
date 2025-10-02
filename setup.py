from setuptools import setup, find_packages

setup(
    name="brave_codex_harmonic",
    version="0.1.0",
    description="A foundation for Harmonic Math and safer kernel runtime hooks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Christopher Ryan Martin",
    author_email="akwardphoenix@gmail.com",
    url="https://github.com/akwardphoenix-hub/brave-codex-harmonic",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.7",
    install_requires=[],  # Add dependencies here, if any
    entry_points={
        "console_scripts": [
            "chattyg-checksum=hnum.checksum:main",
            "chattyg-kernel-hooks=hnum.kernel_hooks:main",
        ],
    },
)