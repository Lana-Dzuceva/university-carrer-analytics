TOKEN = ""


vacancy_titles = [
    "(C# OR .Net) AND NOT UNITY ANd NOT \"Unreal Engine\"",
    "Flutter",
    "\"go\" OR golang",
    "web-developer OR веб-программист OR верстальщик OR \"Разработчик сайтов\"",
    "ml OR \"machine learning\" OR \"data science\" OR \"data engineer\" OR \"data analytic\" "
    "OR \"дата саентист\" OR \"аналитик данных\" OR \"ml инженер\"",
    "1C OR 1С",
]

vacancy_titles.append(f"python AND NOT ({vacancy_titles[4]})")

