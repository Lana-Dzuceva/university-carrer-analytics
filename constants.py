TOKEN = ""


vacancy_titles = [
    """
    (
    C# OR 
    .Net OR
    C# разработчик OR
    .NET Developer OR
    Разработчик WPF/WinForms OR
    Разработчик десктопных приложений C# OR
    ASP.NET разработчик OR
    Fullstack-разработчик C# OR
    C# backend
    )
     AND (NOT UNITY AND NOT "Unreal Engine" AND NOT преподаватель AND NOT учитель)
    """,

    "Flutter",

    """golang OR "go developer" """,

    """
        Web-developer OR
        Веб-разработчик OR
        Frontend-разработчик OR
        Fullstack-разработчик OR
        Веб-программист OR
        Разработчик сайтов OR
        Верстальщик OR
        HTML/CSS-специалист OR
        Веб-мастер OR
        JavaScript-разработчик OR
        React-разработчик OR
        Angular-разработчик OR
        Vue.js-разработчик OR
        Разработчик веб-интерфейсов OR
        Разработчик клиентской части OR
        Инженер веб-приложений OR
        Специалист по CMS OR
        Программист JavaScript OR
        Web-инженер OR
        Frontend-архитектор OR
    """,

    """ 
        ML OR
        "Machine Learning" OR
        "Data Science" OR
        "Data Scientist" OR
        "Data Engineer" OR
        "Data Analyst" OR
        "ML Engineer" OR
        "Machine Learning Engineer" OR
        "Аналитик данных" OR
        "Дата Саентист"
    """,

    "1C OR 1С OR ",#todo finish line

    """
        Сетевой инженер OR
        Системный администратор OR
        Инженер по сетям OR
        Сетевой администратор OR
        Специалист по сетевой безопасности OR
        Инженер по телекоммуникациям OR
        Инженер по IT-инфраструктуре OR
        IT-администратор OR
        Технический специалист по сетям OR
        Техник по обслуживанию сетей OR
        Инженер по компьютерным сетям OR
        Администратор сетевой инфраструктуры OR
        Телекоммуникационный инженер OR
        Специалист по кабельным системам OR
        Специалист по настройке оборудования OR
        Инженер по сетевым решениям OR
        IT-инженер OR
        Специалист по беспроводным сетям OR
        Инженер по поддержке сетей OR
        Мастер по настройке интернета OR
        Техник по сетевому оборудованию OR
        Инженер по обслуживанию сети OR
        Сетевой аналитик OR
        Инженер по WAN/LAN OR
        Инженер связи
    """
]

vacancy_titles.append(f"python AND NOT ({vacancy_titles[4]})")

