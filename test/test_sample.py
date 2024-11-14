import pytest


class TestSample:

    @pytest.mark.sample
    def test_example(self):
        print("run text")

    @pytest.mark.xfai
    def test_example1(self):
        print("example1")

    @pytest.mark.sample2
    def test_example2(self):
        pass
