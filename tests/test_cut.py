import pytest

import cut


def test_ts_formats_ass_timestamps():
    assert cut.ts(0) == "0:00:00.00"
    assert cut.ts(61.5) == "0:01:01.50"
    assert cut.ts(3725.25) == "1:02:05.25"
    assert cut.ts(-3) == "0:00:00.00"


def test_clean_masks_swears_by_default():
    assert cut.clean("what the fuck bro") == "what the f*** bro"
    assert cut.clean("Shit happens") == "S*** happens"


def test_clean_keeps_swears_when_allowed():
    assert cut.clean("what the fuck bro", profanity=True) == "what the fuck bro"


def test_clean_always_masks_slurs():
    assert cut.clean("you retard", profanity=True) == "you r*****"




@pytest.mark.parametrize("word", ["class", "hello", "scrapping", "Shiba"])
def test_clean_leaves_ordinary_words(word):
    assert cut.clean(word) == word


# Known bug: the swear/slur patterns match word prefixes, so ordinary words get masked.
# Remove the xfail once the patterns in cut.py are tightened.
@pytest.mark.xfail(strict=True, reason="prefix matching masks ordinary words")
@pytest.mark.parametrize("word", ["Dickens", "spicy", "spice"])
def test_clean_overmasks_ordinary_words(word):
    assert cut.clean(word) == word


def test_esc_strips_ass_override_chars():
    assert cut.esc("a{b}\\c\nd") == "a(b)c d"


def test_wrap():
    assert cut.wrap("the hidden car nobody found", 12) == ["the hidden", "car nobody", "found"]
    assert cut.wrap("", 10) == []
    assert cut.wrap("supercalifragilistic", 5) == ["supercalifragilistic"]


def test_even():
    assert all(cut.even(n) % 2 == 0 for n in [0, 1, 2, 7, 731.6])


def test_build_ass_has_header_and_dialogue():
    words = [{"s": 10.0, "e": 10.4, "w": "no"}, {"s": 10.4, "e": 11.0, "w": "way"}]
    ass = cut.build_ass(words, 10.0, 15.0, "Nobody noticed this", cut.CAP_Y["blur"])
    assert "[Script Info]" in ass
    assert "PlayResX: 1080" in ass and "PlayResY: 1920" in ass
    assert "Dialogue:" in ass
