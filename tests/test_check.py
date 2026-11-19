import check


def test_parse_campaign_defaults_when_missing(tmp_path):
    rules, found = check.parse_campaign(tmp_path / "nope.md")
    assert not found
    assert rules == {"min": 7.0, "max": 60.0, "tags": [], "mention": None}


def test_parse_campaign_reads_rules(tmp_path):
    p = tmp_path / "campaigns.md"
    p.write_text("min_seconds: 15\nMax_Seconds: 45.5\nrequired_hashtags: #GTA6 #ad\nrequired_mention: @streamer\n")
    rules, found = check.parse_campaign(p)
    assert found
    assert rules == {"min": 15.0, "max": 45.5, "tags": ["#GTA6", "#ad"], "mention": "@streamer"}


def test_fps_of():
    assert check.fps_of("30/1") == 30.0
    assert abs(check.fps_of("30000/1001") - 29.97) < 0.01
    assert check.fps_of("0/0") == 0.0
    assert check.fps_of("garbage") == 0.0


def test_banned_in():
    assert check.banned_in("Free Download link in bio") == ["free download"]
    assert check.banned_in("the hidden car nobody found") == []
