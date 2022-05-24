import pandas as pd

from ms_mint.Mint import Mint
from ms_mint.standards import MINT_RESULTS_COLUMNS

from paths import TEST_MZML, TEST_MZXML, TEST_TARGETS_FN, TEST_TARGETS_FN_V0


mint = Mint(verbose=True)
mint_b = Mint(verbose=True)


class TestClass:
    def run_without_files(self):
        mint.run()

    def test__add_experimental_data(self):
        assert mint.n_files == 0, mint.n_files
        mint.ms_files = [TEST_MZXML]
        assert mint.n_files == 1, mint.n_files
        assert mint.ms_files == [TEST_MZXML]

    def test__mint_run_standard(self):
        mint.run()

    def test__results_is_dataframe(self):
        results = mint.results
        assert isinstance(results, pd.DataFrame), "Results is not a DataFrame"

    def test__results_lenght(self):
        actual = len(mint.results)
        expected = len(mint.targets) * len(mint.ms_files)
        assert (
            expected == actual
        ), f"Length of results ({actual}) does not equal expected length ({expected})"

    def test__results_columns(self):
        expected = MINT_RESULTS_COLUMNS
        actual = mint.results.columns
        assert (expected == actual).all(), actual

    def test__crosstab_is_dataframe(self):
        ct = mint.crosstab()
        assert isinstance(
            ct, pd.DataFrame
        ), f"Crosstab is not a DataFrame ({type(ct)})."

    def test__mint_run_parallel(self):
        mint.ms_files = [TEST_MZML, TEST_MZXML]
        mint.targets_files = TEST_TARGETS_FN
        mint.run(nthreads=2)

    def test__mzxml_equals_mzml(self):
        mint1 = Mint()
        mint2 = Mint()

        mint1.load_targets(TEST_TARGETS_FN)
        mint1.ms_files = [TEST_MZML]

        mint2.load_targets(TEST_TARGETS_FN)
        mint2.ms_files = [TEST_MZXML]

        assert mint1.results.equals(mint2.results)

    def test__target_v0_equals_v1_results(self):
        mint1 = Mint()
        mint2 = Mint()

        mint1.load_targets(TEST_TARGETS_FN_V0)
        mint1.ms_files = [TEST_MZXML]

        mint2.load_targets(TEST_TARGETS_FN)
        mint2.ms_files = [TEST_MZXML]

        assert mint1.results.equals(mint2.results)

    def test__status(self):
        mint.status == "waiting"

    def test__run_returns_none_without_target(self):
        mint.reset()
        mint.ms_files = [TEST_MZXML]
        assert mint.run() is None

    def test__run_returns_none_without_ms_files(self):
        mint.reset()
        mint.targets_files = TEST_TARGETS_FN
        assert mint.run() is None
