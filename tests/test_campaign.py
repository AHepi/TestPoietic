from __future__ import annotations

import unittest

from testpoietic.campaign import _git_tag_commit


class CampaignProvenanceTests(unittest.TestCase):
    def test_semantic_freeze_resolves_from_the_available_repository_ref(self) -> None:
        self.assertEqual(
            _git_tag_commit(),
            "d04bd2273121427166cd4fe9442ff595db959fbd",
        )


if __name__ == "__main__":
    unittest.main()
