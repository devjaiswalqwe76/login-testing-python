import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import login_to_site

import pytest
from utils.helpers import login_to_site

@pytest.mark.parametrize("username,password,expected", [
    ("tomsmith", "SuperSecretPassword!", True),      # ✅ Valid login
    ("wronguser", "SuperSecretPassword!", False),    # ❌ Invalid username
    ("tomsmith", "wrongpass", False),                # ❌ Invalid password
    ("", "", False),                                 # ❌ Blank credentials
    ("admin", "admin123", False)                     # ❌ Random credentials
])
def test_login_parametrize(driver, username, password, expected):
    result = login_to_site(driver, username, password)
    assert result == expected
