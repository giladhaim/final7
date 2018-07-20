print("how many km did you run today?")
kms = input()
mls= float(kms)/1.6093
mls= round(mls,3)
print("so you ran today {} miles!".format(mls))