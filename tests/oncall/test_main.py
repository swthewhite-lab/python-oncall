from unittest.mock import patch
from io import StringIO
import os

import pytest

from oncall.main import main


def run_io_fun(inputs):
    with patch("builtins.input", side_effect=inputs):
        buffer = StringIO()
        with patch("sys.stdout", new=buffer):
            main()
        outputs = buffer.getvalue()
    return outputs


line_separator = os.linesep


def test_예외_테스트():
    outputs = run_io_fun(
        [
            "0,일",
            "4,토",
            "허브,쥬니,말랑,라온,헤나,우코,에단,수달,파워,히이로,마코,슬링키,모디,연어,깃짱,리오,고니,박스터,달리,조이,노아이즈,도이,도치,홍고,스캇,폴로,해시,로지,첵스,아이크,우가,푸만능,애쉬,로이스,오션",
            "오션,로이스,애쉬,푸만능,우가,아이크,첵스,로지,해시,폴로,스캇,홍고,도치,도이,노아이즈,조이,달리,박스터,고니,리오,깃짱,연어,모디,슬링키,마코,히이로,파워,수달,에단,우코,헤나,라온,말랑,쥬니,허브",
        ]
    )
    assert all(
        expected_output in outputs
        for expected_output in [
            "[ERROR]",
            "4월 1일 토 오션" + line_separator,
            "4월 2일 일 로이스" + line_separator,
            "4월 3일 월 허브" + line_separator,
            "4월 4일 화 쥬니" + line_separator,
            "4월 5일 수 말랑" + line_separator,
        ]
    )


def test_기능_테스트():
    outputs = run_io_fun(
        [
            "4,토",
            "허브,쥬니,말랑,라온,헤나,우코,에단,수달,파워,히이로,마코,슬링키,모디,연어,깃짱,리오,고니,박스터,달리,조이,노아이즈,도이,도치,홍고,스캇,폴로,해시,로지,첵스,아이크,우가,푸만능,애쉬,로이스,오션",
            "오션,로이스,애쉬,푸만능,우가,아이크,첵스,로지,해시,폴로,스캇,홍고,도치,도이,노아이즈,조이,달리,박스터,고니,리오,깃짱,연어,모디,슬링키,마코,히이로,파워,수달,에단,우코,헤나,라온,말랑,쥬니,허브",
        ]
    )
    assert all(
        expected_output in outputs
        for expected_output in [
            "4월 1일 토 오션" + line_separator,
            "4월 2일 일 로이스" + line_separator,
            "4월 3일 월 허브" + line_separator,
            "4월 4일 화 쥬니" + line_separator,
            "4월 5일 수 말랑" + line_separator,
            "4월 6일 목 라온" + line_separator,
            "4월 7일 금 헤나" + line_separator,
            "4월 8일 토 애쉬" + line_separator,
            "4월 9일 일 푸만능" + line_separator,
            "4월 10일 월 우코" + line_separator,
            "4월 11일 화 에단" + line_separator,
            "4월 12일 수 수달" + line_separator,
            "4월 13일 목 파워" + line_separator,
            "4월 14일 금 히이로" + line_separator,
            "4월 15일 토 우가" + line_separator,
            "4월 16일 일 아이크" + line_separator,
            "4월 17일 월 마코" + line_separator,
            "4월 18일 화 슬링키" + line_separator,
            "4월 19일 수 모디" + line_separator,
            "4월 20일 목 연어" + line_separator,
            "4월 21일 금 깃짱" + line_separator,
            "4월 22일 토 첵스" + line_separator,
            "4월 23일 일 로지" + line_separator,
            "4월 24일 월 리오" + line_separator,
            "4월 25일 화 고니" + line_separator,
            "4월 26일 수 박스터" + line_separator,
            "4월 27일 목 달리" + line_separator,
            "4월 28일 금 조이" + line_separator,
            "4월 29일 토 해시" + line_separator,
            "4월 30일 일 폴로",
        ]
    )
