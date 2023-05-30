from caverphone2 import caverphone2

def test_Thompson() :
    assert caverphone2("Thompson") == "TMPSN11111"

def test_Lee() :
    assert caverphone2("Lee") == "LA11111111"

def test_Stevenson() :
    assert caverphone2("Stevenson") == "STFNSN1111"

def test_Peter() :
    assert caverphone2("Peter") == "PTA1111111"

def test_able() :
    assert caverphone2("able") == "APA1111111"

def test_ready() :
    assert caverphone2("ready") == "RTA1111111"

def test_social() :
    assert caverphone2("social") == "SSA1111111"

def test_Dyun() :
    assert caverphone2("Dyun") == "TN11111111"

def test_Karleen() :
    assert caverphone2("Karleen") == "KLN1111111"

def test_Tedder() :
    assert caverphone2("Tedder") == "TTA1111111"

def test_Tudor() :
    assert caverphone2("Tudor") == "TTA1111111"