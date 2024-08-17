class Employee:
    def __init__(self, lstOfSkills, lstOfScores):
        self.lstOfSkills = lstOfSkills
        self.lstOfScore = lstOfScores

    def findProfiency(self, score):
        if score >= 80:
            return "expert"
        elif score >= 75:
            return "proficient"
        elif score >= 50:
            return "advanced"
        elif score >= 40:
            return "competent"
        else:
            return "beginner"
        
    def technical_skills(self, lstOfSkills, lstOfScores):
        technical_skills_dict = {}
        for i in range(len(lstOfSkills)):
            skill = lstOfSkills[i]
            score = lstOfScores[i]
            technical_skills_dict[skill] = self.findProfiency(score)
        return technical_skills_dict