def rectangle_inator(c, rows, chols):
    for j in range( rows ):
        print(c* chols)

def test_answer(capsys):
    rectangle_inator('_', 1, 4)
    captured = capsys.readouterr()
    assert captured.out == "____\n"

"""Makes a rectangle using a character (c) of rows and chols (columns) (1*4)

>>> rectangle_inator('_', '1', '4')
'____'

"""


