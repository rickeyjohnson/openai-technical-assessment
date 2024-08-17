import openai
openai.api_key = ""
job_title = input("insert job title: ").lower()
job_dict = {"cloud engineering & infrastructure": "Data Structures and Algorithms, Program Skills, Web Services & API, "
                                                   "Knowledge of Networking, Operating Systems, Web Development, math,"
                                                   " and Parallel and Distributed",
         "cybersecurity": "programming skills, dataStructures+Algorithms, operatingSystems,"
                           "networks+Security, math, parallel+Distributed",
         "data engineering": "programmingSkills, dataStructures+Algorithms, operatingSystems"
                             "databaseManagement, softwareManagement, softwareEngineering"
                             "math, parallel+DistributedComputing, dataAnalysis+Visualization",
         "data science & analytics": "programmingSkills, dataStructures+Algorithms, operatingSystems, "
                                   "databaseManagement, ai+Machine, math, parallel+DistributedComputing, "
                                   "dataAnalysis+Visualization",
         "software engineering": "programmingSkills, dataStructures+Algorithms, operatingSystems,"
                                "systemEngineering, math, parallel+Distributed"}
model_engine = "text-davinci-003"
prompt = "I want you to create a "+job_title+" assessment question for a professional. This should moderately challenge their technical skills relating to"+job_dict[job_title]
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
