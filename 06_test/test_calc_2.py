from calc import add  #calc.py ファイルより
import pytest  # pytestを使う

# 同じ関数について、異なる入力をタプルのリストで指定して
# 繰り返しテストできるようにする

#テスト関数に複数入力をさせるための「デコレータ」。
# テストのパラメータ化という装飾がされている。
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, 5, 15),
])

def test_add_param(a, b, expected): #タプルの中身
    assert add(a, b) == expected