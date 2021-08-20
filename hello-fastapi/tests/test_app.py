import unittest

from fastapi.testclient import TestClient
from hello_fastapi.main import app


class TestApp(unittest.TestCase):
    def test_customer_info(self):
        client = TestClient(app)
        resp = client.get("/customer/dummy-1234/info")
        self.assertEqual(200, resp.status_code, msg="status code")
        self.assertEqual(
            "application/json", resp.headers["Content-Type"], msg="header content-type"
        )
        self.assertEqual({"customer_id": "dummy-1234"}, resp.json(), msg="data")


if __name__ == "__main__":
    unittest.main()
