import os
from ms_mint import Mint
from ms_mint.tools import export_to_excel

def test__export_to_excel(tmp_path):
    filename = os.path.join(tmp_path, 'output.xlsx')
    mint = Mint(verbose=True)
    mint.files = 'tests/data/test.mzXML'
    mint.peaklist_files = 'tests/data/peaklist_v1.csv'
    mint.run()
    mint.export(filename)
    assert os.path.isfile(filename)