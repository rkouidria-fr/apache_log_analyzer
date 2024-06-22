import unittest
from scripts.analyze_logs import get_datas_from_user_input

class TestLogAnalysis(unittest.TestCase):
    """ Test the log analysis function. """
    def setUp(self):
        self.mock_logs_path = 'test/mock_datas/mock_logs.log'

    def test_log_analysis(self):
        """ Test the log analysis function. """
        result_df = get_datas_from_user_input(log_file_path=self.mock_logs_path)
        print(result_df.head())
        self.assertFalse(result_df.empty, "Le DataFrame résultant est vide.")
        expected_columns = ['ip', 'date_time', 'request', 'status', 'size']
        self.assertListEqual(list(result_df.columns), expected_columns,
                              "Les colonnes du DataFrame ne correspondent"
                              " pas aux attentes.")

        self.assertEqual(result_df['status'].dtype, int, "Le type de la "
                         "colonne 'status' doit être int.")
        self.assertEqual(result_df['size'].dtype, int, "Le type de la colonne "
                         "'size' doit être int.")
        self.assertEqual(result_df['date_time'].dtype, 'datetime64[ns]', "Le "
                         "type de 'date_time' doit être datetime64[ns].")
        self.assertTrue(result_df['date_time'].notnull().all(), "La colonne "
                        "'date_time' ne doit pas contenir de valeurs nulles.")
        self.assertTrue(result_df['ip'].notnull().all(), "La colonne 'ip' ne "
                        "doit pas contenir de valeurs nulles.")
        self.assertTrue(result_df['request'].notnull().all(), "La colonne "
                        "'request' ne doit pas contenir de valeurs nulles.")
        self.assertTrue(result_df['status'].notnull().all(), "La colonne "
                        "'status' ne doit pas contenir de valeurs nulles.")
        self.assertTrue(result_df['size'].notnull().all(), "La colonne 'size' "
                        "ne doit pas contenir de valeurs nulles.")


if __name__ == '__main__':
    unittest.main()
