import pytest


class TestDependent:
    def test_open_app(self):
        print("Opening the application")
        assert True

    @pytest.mark.depends(on=['TestDependent::test_open_app'])
    def test_login_app(self):
        print("Logging to the application")
        assert False

    @pytest.mark.depends(on=['TestDependent::test_login_app'])
    def test_count_anchor_tags(self):
        print("Count of anchor tags are 20")
        assert True

    @pytest.mark.depends(on=['TestDependent::test_login_app'])
    def test_count_image_tags(self):
        print("Count of image tags are 10")
        assert True

    @pytest.mark.depends(on=['TestDependent::test_login_app'])
    def test_logout(self):
        print("Logout is successful")
        assert True
