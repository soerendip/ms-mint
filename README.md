![](docs/image/MINT-logo.png)

# MINT (Metabolomics Integrator)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5178/badge)](https://bestpractices.coreinfrastructure.org/projects/5178)
![](images/coverage.svg)
[![Github All Releases](https://img.shields.io/github/downloads/sorenwacker/ms-mint/total.svg)]()


The Metabolomics Integrator (MINT)) is a post-processing tool for liquid chromatography-mass spectrometry (LCMS) based metabolomics. 
Metabolomics is the study of all metabolites (small chemical compounds) in a biological sample e.g. from bacteria or a human blood sample. 
The metabolites can be used to define biomarkers used in medicine to find treatments for diseases or for the development of diagnostic tests 
or for the identification of pathogens such as methicillin resistant _Staphylococcus aureus_ (MRSA). 
More information on how to install and run the program can be found in the [Documentation](https://sorenwacker.github.io/ms-mint/).

![](./docs/image/distributions.png)

## Python API for metabolomics

    from ms_mint.notebook import Mint
    mint.ms_files = glob('/path/to/files/*mzML')
    mint.peaklist_files = '/path/to/peaklist/file/peaklist.csv'
    mint.run()
    mint.results

![Mint Jupyter Results](./docs/image/jupyter_results.png "Mint Jupyter Results")

More information in the documentation.

# Errors, Feedback, Feature Requests
If you encounter an error, if you have a request for a new feature, or for general feedback, please open a new ticket at the [issue tracker](https://github.com/sorenwacker/ms-mint/issues).

# Contributions are welcome
If you want to contribute to MINT please send me a notification. 

In general I will ask you to followowing steps:

1. fork the repository
1. implement the new feature or bug-fix
1. add corresponding tests
2. run `flake8`
3. submit a pull request

## Code standards
Before submitting a pull request please run `flake8`.


# Contributors
This project would not be possible without the help of the open-source community. 
The tools and resources provided by GitHub, Docker-Hub, the Python Package Index, as well the answers from dedicated users on [Stackoverflow](stackoverflow.com)
and the [Plotly community](https://community.plotly.com/) forums and of course all the packages and tools used are the fuel of this project that translates 
computer science and data science into the hands of metabolomics researchers to hopefully contribute to better and faster science. Beside this, several people have made direct contributions to the codebase and we are extremely grateful for that. 

- @rokm refactored the specfile for `Pyinstaller` to create a windows package. 
- @bucknerns helped with the configuration of the `versioneer` file.

Last but not least, we want to thank all the users and early adopters that drive the development with feature requests and bug reports.

