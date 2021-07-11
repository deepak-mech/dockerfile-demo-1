import joblib as jb
mind  =  jb.load("marks.pk1")
out = mind.predict([[2]])
print(out)



