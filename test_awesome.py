import awesome


def test_smile():
    assert awesome.smile() == ":)"


def test_frown():
    assert awesome.frown() == ":("


def test_poker_face():
    assert awesome.poker_face() == ":|"


def test_smile():
    assert awesome.japanese_emoji_smile() == "^_^"


def test_sleep():
    assert awesome.japanese_emoji_sleep() == "-_- zzz"
