import CSP_6_03_Writing_to_files as HW
list0 = ['swing', 'your', 'arms', 'from', 'side', 'to', 'side']
list1 = ['swing your arms', 'from', 'side to side']
list2 = []

def test_writeFile():
    assert HW.writeFile(list0, 'doTheMario0.txt') == 'swing\nyour\narms\nfrom\nside\nto\nside\n'
    assert HW.writeFile(list1, 'doTheMario1.txt') == 'swingyourarms\nfrom\nsidetoside\n'

def test_sortNames():
    assert HW.sortNames("names.txt","namesNew.txt") == 'Daisy\nLuigi\nMario\nPeach\nToad\nWaluigi\nWario\n'

def test_highScore():
    assert HW.highScore(14) == 50
