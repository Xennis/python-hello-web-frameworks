import unittest

from hello_flask import app


class TestApp(unittest.TestCase):
    def test_customer_info(self):
        client = app.test_client()
        resp = client.get("/customer/dummy-1234/info")
        self.assertEqual(200, resp.status_code, msg="status code")
        self.assertEqual(
            "application/json", resp.headers["Content-Type"], msg="header content-type"
        )
        self.assertEqual(b'{"customer_id":"dummy-1234"}\n', resp.data, msg="data")


if __name__ == "__main__":
    unittest.main()
