import numpy as np

import moments


def test_z_flat_signal_is_zero():
    assert np.all(moments.z([3, 3, 3, 3]) == 0)


def test_z_spike_stands_out():
    out = moments.z([0, 0, 0, 10, 0, 0])
    assert out.argmax() == 3 and out[3] > 1


def test_smooth_keeps_length():
    a = np.arange(20, dtype=float)
    assert len(moments.smooth(a, 5)) == 20
    assert np.allclose(moments.smooth(a, 1), a)


def test_hype_regex():
    assert moments.HYPE.search("NO WAY he did that")
    assert moments.CHAT_HYPE.search("KEKW")
    assert not moments.HYPE.search("calm walk in the park")
