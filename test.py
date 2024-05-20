from badword_check import BadWord

model = BadWord.load_badword_model()
data = BadWord.preprocessing("ㅅㅂ")
print(model.predict(data))

#확인용
if(model.predict(data) >= 0.65):
    print("욕설입니다.")
else:
    print("욕설이 아닙니다.")