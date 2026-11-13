"""Regression for a shared source frame lost by union-based selection."""
import unittest
from verify_frame_mapping import audit_mapping, compare_count


class FrameMappingTests(unittest.TestCase):
    def test_shared_frame_must_appear_twice(self):
        rows = [dict(start=0, end=106, **{'in': 2533, 'out': 2639}),
                dict(start=106, end=156, **{'in': 2638, 'out': 2688})]
        report = audit_mapping(rows)
        self.assertEqual(report['sourceReuseClipIndices'], [1])
        compare_count(report, 156)
        with self.assertRaisesRegex(ValueError, 'expected 156, decoded 155'):
            compare_count(report, 155)

    def test_reordered_and_reused_windows_are_valid(self):
        rows = [dict(start=0, end=5, **{'in': 10, 'out': 15}),
                dict(start=5, end=10, **{'in': 0, 'out': 5}),
                dict(start=10, end=15, **{'in': 10, 'out': 15})]
        self.assertEqual(audit_mapping(rows)['expectedVideoFrames'], 15)

    def test_reject_gap_and_time_transform(self):
        for row in [dict(start=1, end=6, **{'in': 0, 'out': 5}),
                    dict(start=0, end=6, **{'in': 0, 'out': 5})]:
            with self.assertRaises(ValueError):
                audit_mapping([row])


if __name__ == '__main__':
    unittest.main()
