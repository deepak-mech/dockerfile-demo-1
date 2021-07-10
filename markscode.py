import joblib as jb
mind  =  jb.load("marks.pk1")
inp_exp = float(input("Enter Total Exp: "))
output = mind.predict([[inp_exp]])
print(output)