import requests

url_ddg = "https://api.duckduckgo.com"
resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
rsp_data = resp.json()
topics = rsp_data["RelatedTopics"]
texts = ""
for x in topics:
    texts += x["Text"]


def test_Washington():
    assert 'Washington' in texts


def test_Adams():
    assert 'Adams' in texts


def test_Jefferson():
    assert 'Jefferson' in texts


def test_Madison():
    assert 'Madison' in texts


def test_Monroe():
    assert 'Monroe' in texts


def test_Jackson():
    assert 'Jackson' in texts


def test_Buren():
    assert 'Buren' in texts


def test_Harrison():
    assert 'Harrison' in texts


def test_Tyler():
    assert 'Tyler' in texts


def test_Polk():
    assert 'Polk' in texts


def test_Taylor():
    assert 'Taylor' in texts


def test_Fillmore():
    assert 'Fillmore' in texts


def test_Pierce():
    assert 'Pierce' in texts


def test_Buchanan():
    assert 'Buchanan' in texts


def test_Lincoln():
    assert 'Lincoln' in texts


def test_Johnson():
    assert 'Johnson' in texts


def test_Grant():
    assert 'Grant' in texts


def test_Hayes():
    assert 'Hayes' in texts


def test_Garfield():
    assert 'Garfield' in texts


def test_Arthur():
    assert 'Arthur' in texts


def test_Cleveland():
    assert 'Cleveland' in texts


def test_McKinley():
    assert 'McKinley' in texts


def test_Roosevelt():
    assert 'Roosevelt' in texts


def test_Taft():
    assert 'Taft' in texts


def test_Wilson():
    assert 'Wilson' in texts


def test_Harding():
    assert 'Harding' in texts


def test_Coolidge():
    assert 'Coolidge' in texts


def test_Hoover():
    assert 'Hoover' in texts


def test_Truman():
    assert 'Truman' in texts


def test_Eisenhower():
    assert 'Eisenhower' in texts


def test_Kennedy():
    assert 'Kennedy' in texts


def test_Nixon():
    assert 'Nixon' in texts


def test_Ford():
    assert 'Ford' in texts


def test_Carter():
    assert 'Carter' in texts


def test_Reagan():
    assert 'Reagan' in texts


def test_Bush():
    assert 'Bush' in texts


def test_Clinton():
    assert 'Clinton' in texts


def test_Obama():
    assert 'Obama' in texts


def test_Trump():
    assert 'Trump' in texts


def test_Biden():
    assert 'Biden' in texts
