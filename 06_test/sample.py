# VScodeのデバッグ機能テスト用
def calcurate_score(score):
    if score >=90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    return grade

score = 85 # 任意のスコア
result = calcurate_score(score)
print(f"成績は{result}です")