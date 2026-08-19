from __future__ import annotations

import unittest

from testpoietic.f3_identifiability import (
    library_batch_policy,
    run_bitpatch_family,
    serial_fringe_policy,
    wrong_batch_cost_mutant,
)


class F3IdentifiabilityTests(unittest.TestCase):
    def test_exact_costs_and_delivery(self) -> None:
        for n in (1, 2, 4, 8, 16, 32, 64, 128):
            serial = serial_fringe_policy(n)
            batch = library_batch_policy(n)
            self.assertEqual(serial.total_cost, n * n + 2 * n)
            self.assertEqual(batch.total_cost, 3 * n)
            self.assertEqual(serial.delivered_bits, n)
            self.assertEqual(batch.delivered_bits, n)
            self.assertEqual(serial.terminal, batch.terminal)

    def test_policy_classes_overlap(self) -> None:
        result = library_batch_policy(8)
        self.assertTrue(result.uses_failure_fringe)
        self.assertTrue(result.library_local)
        self.assertTrue(result.promotion_shy)

    def test_batch_dominates_at_preregistered_nontrivial_cuts(self) -> None:
        result = run_bitpatch_family()
        self.assertTrue(result["rival_dominates_every_cut"])
        self.assertTrue(result["classes_overlap_every_cut"])
        self.assertEqual(result["protocol_verdict"], "NON-IDENTIFYING")
        self.assertEqual(result["fertility_verdict"], "UNTESTED")

    def test_deliberate_cost_mutant_is_detected(self) -> None:
        for n in (4, 8, 16):
            self.assertNotEqual(wrong_batch_cost_mutant(n), library_batch_policy(n).total_cost)


if __name__ == "__main__":
    unittest.main()
