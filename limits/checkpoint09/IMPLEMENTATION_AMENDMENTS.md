# Implementation amendments

After the initial source freeze, the N=8 computation wrote its cohort arrays but failed when serializing a NumPy boolean in the summary JSON. No numerical results were printed before this error. The frozen source is preserved unchanged in `history/floquet_test_initial.py` and still matches its `FREEZE.json` hash.

The correction adds `.item()` conversion for NumPy scalars to the summary JSON writer. Circuit seeds, gates, predictions, cohort, calculations, and criteria are unchanged. The deterministic run is restarted at the same frozen inputs. This is a serialization repair, not a new scientific protocol or selected rerun.
