TOKEN = ""


VACANCY_TITLES = {
    "c_sharp" : """"
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
       AND (NOT UNITY AND NOT "Unreal Engine" AND NOT преподаватель AND NOT учитель AND NOT Лектор)
      """,

    "flutter" : "Flutter",

    "golang" : """golang OR "go developer" """,

    "web" : """
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
        AND (NOT преподаватель AND NOT учитель AND NOT Лектор)
    """,

    "data_science" : """ 
        ML OR
        "Machine Learning" OR
        "Data Science" OR
        "Data Scientist" OR
        "Data Engineer" OR
        "Data Analyst" OR
        "ML Engineer" OR
        "Machine Learning Engineer" OR
        "Аналитик данных" OR
        "Дата Сайентист"
    """,

    "1c" : """
        "программист 1С" OR
        "разработчик 1С" OR
        "инженер 1С" OR
        "стажер 1С"
    """,

    "system_administrator" : """
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
    """,
    "python": """
    python AND NOT (
        ML OR
        "Machine Learning" OR
        "Data Science" OR
        "Data Scientist" OR
        "Data Engineer" OR
        "Data Analyst" OR
        "ML Engineer" OR
        "Machine Learning Engineer" OR
        "Аналитик данных" OR
        "Дата Сайентист" OR 
        Преподаватель OR
        Лектор OR
        Учитель
    )
    """
}

PROFESSIONAL_ROLES = [
    ('professional_role', '156'),
    ('professional_role', '160'),
    ('professional_role', '10'),
    ('professional_role', '12'),
    ('professional_role', '150'),
    ('professional_role', '25'),
    ('professional_role', '165'),
    ('professional_role', '34'),
    ('professional_role', '36'),
    ('professional_role', '73'),
    ('professional_role', '155'),
    ('professional_role', '96'),
    ('professional_role', '164'),
    ('professional_role', '104'),
    ('professional_role', '157'),
    ('professional_role', '107'),
    ('professional_role', '112'),
    ('professional_role', '113'),
    ('professional_role', '148'),
    ('professional_role', '114'),
    ('professional_role', '116'),
    ('professional_role', '121'),
    ('professional_role', '124'),
    ('professional_role', '125'),
    ('professional_role', '126')
]
