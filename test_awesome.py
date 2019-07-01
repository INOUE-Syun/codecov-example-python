import awesome
from awesome import hoge, fuga


def test_smile():
    assert awesome.smile() == ":)"


def test_frown():
    assert awesome.frown() == ":("


def test_poker_face():
    assert awesome.poker_face() == ":|"


def test_japanese_emoji_smile():
    assert awesome.japanese_emoji_smile() == "^_^"


def test_japanese_emoji_sleep():
    assert awesome.japanese_emoji_sleep() == "-_- zzz"


def test_hoge():
    assert hoge.hoge() == "hoge"


def test_fuga():
    assert hoge.fuga() == "fuga"


# def test_piyo():
#     assert hoge.piyo() == "piyo"


# def test_fugafuga():
#     assert fuga.fuga() == "fuga"
