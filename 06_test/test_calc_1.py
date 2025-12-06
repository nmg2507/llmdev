from calc import add  #calc.py ファイルより

# 加算関数 add のテストコードを defで定義
def test_add():
    result = add(2, 3)
    assert result == 5
# add()関数で2,3を渡したら、結果は5になるはず、
# というのを　キーワードassert　で調べている。
# VSCodeでは、「テスト」メニューで実行し、
# 下ウインドウのテスト結果　欄で”collected 1 item”
# を確認。06_test\test_calc.py .  ←ドット1個ならOK。
# 失敗すると F、スキップされたら S　表示。