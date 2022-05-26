[![Python package](https://github.com/lewisresearchgroup/ms-mint/actions/workflows/pythonpackage.yml/badge.svg)](https://github.com/sorenwacker/ms-mint/actions/workflows/pythonpackage.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5178/badge)](https://bestpractices.coreinfrastructure.org/projects/5178)
![](https://github.com/LewisResearchGroup/ms-mint/blob/develop/images/coverage.svg)
[![CodeQL](https://github.com/lewisresearchgroup/ms-mint/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/lewisresearchgroup/ms-mint/actions/workflows/codeql-analysis.yml)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/LewisResearchGroup/ms-mint.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/LewisResearchGroup/ms-mint/context:python)


# MINT (Metabolomics Integrator)

The Metabolomics Integrator (MINT) is a post-processing tool for liquid chromatography-mass spectrometry (LCMS) based metabolomics. 
Metabolomics is the study of all metabolites (small chemical compounds) in a biological sample e.g. from bacteria or a human blood sample. 
The metabolites can be used to define biomarkers used in medicine to find treatments for diseases or for the development of diagnostic tests 
or for the identification of pathogens such as methicillin resistant _Staphylococcus aureus_ (MRSA). 
More information on how to install and run the program can be found in the [Documentation](https://lewisresearchgroup.github.io/ms-mint/).

## News

MINT has been split into the Python library and the app. This repository contains the Python library. For the app follow [this link](https://github.com/LewisResearchGroup/ms-mint-app).

## Contributions

All contributions, bug reports, code reviews, bug fixes, documentation improvements, enhancements, and ideas are welcome.
Before you modify the code please reach out to us using the [issues](https://github.com/LewisResearchGroup/ms-mint/issues) page.


## Code standards

The project follows PEP8 standard and uses Black and Flake8 to ensure a consistent code format throughout the project.


## Example usage

    %pylab inline
    from ms_mint.notebook import Mint
    mint = Mint()

    mint.ms_files = [
        './input/EC_B2.mzXML',
        './input/EC_B1.mzXML',
        './input/CA_B1.mzXML',
        './input/CA_B4.mzXML',
        './input/CA_B2.mzXML',
        './input/CA_B3.mzXML',
        './input/EC_B4.mzXML',
        './input/EC_B3.mzXML',
        './input/SA_B4.mzML',
        './input/SA_B2.mzML',
        './input/SA_B1.mzML',
        './input/SA_B3.mzML'
    ]

    mint.load_targets('/home/swacker/workspace/ms-mint/tests/data/targets/targets_v0.csv')
    
    mint.targets
    >>>   peak_label    mz_mean  mz_width    rt  rt_min  rt_max  intensity_threshold target_filename
        0          1  151.06050         5  None    5.07    5.09                    0  targets_v0.csv
        1          2  216.05040         5  None    3.98    4.39                    0  targets_v0.csv
        2          3  115.00320         5  None    3.45    4.39                    0  targets_v0.csv
        3          4  273.00061         5  None    1.10    2.22                    0  targets_v0.csv

    mint.run()

    mint.results
    >>>

![](https://github.com/LewisResearchGroup/ms-mint/blob/develop/images/results-example.png)

    mint.plot.hierarchical_clustering()


![](https://github.com/LewisResearchGroup/ms-mint/blob/develop/images/hierarchical-clustering.png)