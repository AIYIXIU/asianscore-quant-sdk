import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

from asianscore_quant import (
    brier_score,
    devig_multiplicative,
    devig_power,
    dixon_coles_probs,
    kelly_fraction,
)


class QuantModelsTest(unittest.TestCase):
    def test_devig_sums_to_one(self):
        p1 = devig_multiplicative([1.95, 3.50, 4.10])
        p2 = devig_power([1.95, 3.50, 4.10])
        self.assertAlmostEqual(sum(p1), 1.0, places=6)
        self.assertAlmostEqual(sum(p2), 1.0, places=6)
        self.assertGreater(p2[0], p1[0])  # favorite gets higher weight under power devig

    def test_kelly(self):
        self.assertAlmostEqual(kelly_fraction(0.55, 2.0, scale=1.0), 0.10, places=6)
        self.assertEqual(kelly_fraction(0.45, 2.0), 0.0)

    def test_dixon_coles(self):
        probs = dixon_coles_probs(1.65, 1.05, rho=-0.05)
        self.assertAlmostEqual(probs["home"] + probs["draw"] + probs["away"], 1.0, places=4)
        self.assertGreater(probs["home"], probs["away"])

    def test_brier(self):
        self.assertAlmostEqual(brier_score([([0.7, 0.2, 0.1], 0)]), (0.09 + 0.04 + 0.01) / 3, places=6)


if __name__ == "__main__":
    unittest.main()
