#让级算机试错出正确答案
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 5 in [4,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor = dayfactor + 0.001

print("当每天努力{:.4f}时，才能和天天努力的人一样".format(dayfactor))
