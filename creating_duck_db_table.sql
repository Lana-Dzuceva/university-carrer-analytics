-- Создание последовательности для автоинкрементного id
CREATE SEQUENCE IF NOT EXISTS seq_vacancy_id START 1;

-- Создание таблицы
CREATE TABLE IF NOT EXISTS vacancies (
    id INTEGER DEFAULT nextval('seq_vacancy_id'),
    id_vacancy TEXT,
    name TEXT,
    premium BOOLEAN,
    billing_type TEXT,
    area_id TEXT,
    area_name TEXT,
    salary_from INTEGER,
    salary_to INTEGER,
    salary_currency TEXT,
    salary_gross BOOLEAN,
    type TEXT,
    city TEXT,
    street TEXT,
    building TEXT,
    lat DOUBLE,
    lng DOUBLE,
    experience TEXT,
    schedule TEXT,
    employment TEXT,
    employer_id TEXT,
    employer_name TEXT,
    employer_url TEXT,
    published_at TIMESTAMP,
    description TEXT,
    key_skills TEXT[],
    group_tag TEXT
);
