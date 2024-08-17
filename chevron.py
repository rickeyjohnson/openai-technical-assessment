import openai
import os
import Employee

openai.api_key = ""
model_engine = "text-davinci-003"

def constructPrompt(technical_skills, job):
    prompt = f"write an unbiased appraisal for a {job} who is "
    for skill, level in technical_skills.items():
        prompt += f"{level} in {skill}, "
    prompt += "."

    return prompt

skills = ["java", "C", "math", "data structures"]
scores = [80, 40, 60, 30]
technical_skills = Employee.Employee(skills, scores).technical_skills(skills, scores)

prompt = constructPrompt(technical_skills, "data scientist")
print(f"prompt: {prompt}")


completion = openai.completions.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)

print("-" * 40)
