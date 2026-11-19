import secrets_map as sm


def test_next_id():
    assert sm.next_id([]) == "S001"
    assert sm.next_id([{"id": "S001"}, {"id": "S012"}, {"id": "junk"}]) == "S013"


def test_link_at():
    assert sm.link_at("https://youtu.be/abc", 75.9) == "https://youtu.be/abc?t=75s"
    assert sm.link_at("https://www.youtube.com/watch?v=abc", 10) == "https://www.youtube.com/watch?v=abc&t=10s"
    assert sm.link_at("local.mp4", 5) == "local.mp4#t=5"


def test_mmss():
    assert sm.mmss(0) == "0:00"
    assert sm.mmss(125.7) == "2:05"


def test_categorize():
    assert sm.categorize("a rare car spawns behind the docks") == "car"
    assert sm.categorize("there is a cash stash under the pier") == "money"
    assert sm.categorize("nothing special") == "other"


def test_similar_dedupes_near_duplicates():
    a = {"name": "Hidden garage", "where": "behind the docks"}
    b = {"name": "hidden garage!", "where": "Behind the docks"}
    c = {"name": "Golden statue", "where": "mountain top"}
    assert sm.similar(a, b)
    assert not sm.similar(a, c)
