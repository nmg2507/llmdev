# テストコード　ファイル test_authenticator.py として保存
import pytest
from authenticator import Authenticator

@pytest.fixture  # テスト前後処理　テスト間で状態が混ざらないように（要らない？）
def authenticator():
    auth = Authenticator()
    yield auth   #後処理は記述なしでいい・・？

# register() メソッドで、ユーザーが正しく登録されるか
def test_register_rightly(authenticator):
    authenticator.register("taro","abcd0123")
    assert authenticator.users["taro"] == "abcd0123" #辞書だからキーでアクセス

# register() メソッドで、すでに存在するユーザー名で
# 登録を試みた場合に、エラーメッセージが出力されるか
def test_register_overlap(authenticator):
    authenticator.register("taro","abcd0123") #１つめをまず登録
    with pytest.raises(ValueError,match="エラー: ユーザーは既に存在します。"):
        authenticator.register("taro","test0000")

# login() メソッドで、正しいユーザー名とパスワードでログインできるか
def test_login_success(authenticator):
    authenticator.register("taro","abcd0123") #１つめをまず登録
    assert authenticator.login("taro","abcd0123") == "ログイン成功"

# login() メソッドで、誤ったパスワードでエラーが出るか
def test_login_wrongpass(authenticator):
    authenticator.register("taro","abcd0123") #１つめをまず登録
    with pytest.raises(ValueError,match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("taro","test0000")