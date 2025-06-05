#!/usr/bin/env python

from reqlint import ReqLint

from glob import glob


class TestGood:
    @staticmethod
    def get_good_files():
        return glob("test_data/good*.py")

    def test(self):
        for f in self.get_good_files():
            print(f"{f}: ", end="")
            with open(f, "r") as file:
                code = file.read()
            assert ReqLint.has_lint_errors(code) is False
            print("Passed")


class TestBad:
    @staticmethod
    def get_bad_files():
        return glob("test_data/bad*.py")

    def test(self):
        for f in self.get_bad_files():
            print(f"{f}: ", end="")
            with open(f, "r") as file:
                code = file.read()
            assert ReqLint.has_lint_errors(code) is True
            print("Passed")


if __name__ == "__main__":
    TestGood().test()
    TestBad().test()
