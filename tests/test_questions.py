import questions


def test_is_question():
    assert questions.is_question("Where is the hidden garage?")
    assert questions.is_question("how do I get the boat")
    assert not questions.is_question("nice clip")
    assert not questions.is_question("why?")  # too short
    assert not questions.is_question("x" * 400 + "?")


def test_sentences_keeps_only_questions():
    body = "Great stream today. How do I unlock the airport? Also love the music!\nWhere is the stash"
    assert questions.sentences(body) == ["How do I unlock the airport?", "Where is the stash"]


def test_tokens_drop_stopwords_and_links():
    toks = questions.tokens("How do I unlock the airport? https://example.com/x")
    assert "airport" in toks and "unlock" in toks
    assert "the" not in toks and "example" not in toks


def test_howto_title():
    assert questions.howto_title("How do I unlock the airport in GTA 6?") == "HOW TO UNLOCK THE AIRPORT IN GTA 6"
    assert questions.howto_title("how to get a boat") == "HOW TO GET A BOAT IN GTA 6"
