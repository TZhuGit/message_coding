from message import encode, decode

def test_message():
    assert decode("th3s 3s 1 m2ss1g2.") == "this is a message."
    assert encode("another message here!") == "1n4th2r m2ss1g2 h2r2!"