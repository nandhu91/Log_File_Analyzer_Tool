import unittest
import os
from analyzer_utils import parse_logs, analyze_logs


class TestLogFileAnalyzer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Create a temporary log file for testing
        """
        cls.test_log_file = "test_sample.log"
        with open(cls.test_log_file, "w") as f:
            f.write(
                "2026-01-21 10:00:00 192.168.1.10 GET 404\n"
                "2026-01-21 10:01:00 192.168.1.20 POST 500\n"
                "2026-01-21 10:02:00 192.168.1.10 GET 403\n"
                "INVALID LOG ENTRY\n"
            )

    @classmethod
    def tearDownClass(cls):
        """
        Remove temporary log file after tests
        """
        if os.path.exists(cls.test_log_file):
            os.remove(cls.test_log_file)

    # ---------------- TEST CASES ----------------

    def test_parse_logs_total_lines(self):
        logs, total_lines, corrupted = parse_logs(self.test_log_file)
        self.assertEqual(total_lines, 4)

    def test_parse_logs_corrupted_lines(self):
        logs, total_lines, corrupted = parse_logs(self.test_log_file)
        self.assertEqual(corrupted, 1)

    def test_parse_logs_valid_entries(self):
        logs, total_lines, corrupted = parse_logs(self.test_log_file)
        self.assertEqual(len(logs), 3)

    def test_analyze_logs_total_errors(self):
        logs, _, _ = parse_logs(self.test_log_file)
        result = analyze_logs(logs)
        self.assertEqual(result["total_errors"], 3)

    def test_error_code_frequency(self):
        logs, _, _ = parse_logs(self.test_log_file)
        result = analyze_logs(logs)

        self.assertEqual(result["error_counts"][404], 1)
        self.assertEqual(result["error_counts"][500], 1)
        self.assertEqual(result["error_counts"][403], 1)

    def test_top_ip_addresses(self):
        logs, _, _ = parse_logs(self.test_log_file)
        result = analyze_logs(logs)

        self.assertEqual(result["top_ips"]["192.168.1.10"], 2)

    def test_no_crash_on_empty_file(self):
        empty_file = "empty.log"
        open(empty_file, "w").close()

        logs, total_lines, corrupted = parse_logs(empty_file)
        self.assertEqual(total_lines, 0)
        self.assertEqual(corrupted, 0)
        self.assertEqual(len(logs), 0)

        os.remove(empty_file)


if __name__ == "__main__":
    unittest.main()
