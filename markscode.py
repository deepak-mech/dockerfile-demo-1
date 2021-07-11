import joblib as jb
mind  =  jb.load("marks.pk1")

output = mind.predict([[2]])
print(output)
