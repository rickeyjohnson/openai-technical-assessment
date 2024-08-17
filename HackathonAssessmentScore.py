def isProficient(avggrade):
    if avggrade >= 80:
        return "Expert"
    elif avggrade >= 75:
        return "Proficient"
    elif avggrade >= 50:
        return "Advanced"
    elif avggrade >= 40:
        return "Competent"
    else:
        return "Beginner"

test_scores = {"Skill1_Test1":(5/5)*100,"Skill1_Test2":(4/5)*100,"Skill1_Test3":(5/5)*100,
               "Skill2_Test1":(0/5)*100,"Skill2_Test2":(2/5)*100,"Skill2_Test3":(1/5)*100,
               "Skill3_Test1":(4/5)*100,"Skill3_Test2":(3/5)*100,"Skill3_Test3":(4/5)*100}
Skill1_Average = (test_scores["Skill1_Test1"] + test_scores["Skill1_Test2"] + test_scores["Skill1_Test3"]) / 3
Skill2_Average = (test_scores["Skill2_Test1"] + test_scores["Skill2_Test2"] + test_scores["Skill2_Test3"]) / 3
Skill3_Average = (test_scores["Skill3_Test1"] + test_scores["Skill3_Test2"] + test_scores["Skill3_Test3"]) / 3
print(f'{"Test":^20}|{"Score":^20}')
print("_"*41)
for filler, test in enumerate(test_scores):
    print(f'{test:^20}|{test_scores[test]:^20}')

assessment = {"Skill1":isProficient(Skill1_Average),"Skill2":isProficient(Skill2_Average),"Skill3":isProficient(Skill3_Average)}
for filler, skill in enumerate(assessment):
    print(f'{skill}: {assessment[skill]}')
