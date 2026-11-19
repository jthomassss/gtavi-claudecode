import common


def test_is_url():
    assert common.is_url("https://www.youtube.com/watch?v=abc")
    assert common.is_url("http://twitch.tv/x")
    assert not common.is_url("videos/clip.mp4")
    assert not common.is_url("ftp://example.com/file")


def test_job_dir_is_stable_and_named(tmp_path, monkeypatch):
    monkeypatch.setattr(common, "JOBS", tmp_path / "jobs")
    a = common.job_dir("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    b = common.job_dir("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    assert a == b and a.is_dir()
    assert a.name.startswith("dqw4w9wgxcq-")
    local = common.job_dir("My Stream VOD (part 1).mp4")
    assert local.name.startswith("my-stream-vod-part-1-")
    assert local != a


def test_json_roundtrip(tmp_path):
    p = tmp_path / "x.json"
    common.save_json(p, {"hook": "Ñandú 🔥", "n": [1, 2]})
    assert common.load_json(p) == {"hook": "Ñandú 🔥", "n": [1, 2]}
