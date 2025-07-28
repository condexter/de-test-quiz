# app.py
import streamlit as st

# Полные данные в точном порядке, как ты прислал
quiz_data = [
    # === Раздел 3: Git ===
    {
        "section": 3,
        "question": "Что делает git clone https://…?",
        "options": ["Создаёт новую ветку", "Клонирует удалённый репозиторий", "Удаляет файлы под Git", "Инициализирует локальный репозиторий"],
        "answer": 1  # B
    },
    {
        "section": 3,
        "question": "Какой файл указывает Git, какие файлы не отслеживать?",
        "options": [".gitconfig", ".gitignore", "README.md", ".gitinclude"],
        "answer": 1  # B
    },
    {
        "section": 3,
        "question": 'Команда git commit -m "msg":',
        "options": ["Отправляет изменения на сервер", "Создаёт локальный коммит с сообщением", "Обновляет коммит", "Проверяет статус"],
        "answer": 1  # B
    },
    {
        "section": 3,
        "question": "Как переключиться на ветку feature (если она уже существует)?",
        "options": ["git branch feature", "git checkout feature", "git merge feature", "git init feature"],
        "answer": 1  # B
    },
    {
        "section": 3,
        "question": "Что делает git push origin main?",
        "options": ["Отправляет ветку main в удалённый репозиторий origin", "Удаляет ветку main на сервере", "Обновляет статус репозитория", "Перемещает ветку main локально"],
        "answer": 0  # A
    },
    {
        "section": 3,
        "question": "Как объединить ветку feature с веткой main локально?",
        "options": ["git merge main feature", "git rebase feature onto main", "git checkout main → git merge feature", "git switch main feature"],
        "answer": 2  # C
    },
    {
        "section": 3,
        "question": "Что показывает git status?",
        "options": ["Список коммитов", "Статус индекса и рабочих файлов", "Историю веток", "Список удалённых репозиториев"],
        "answer": 1  # B
    },
    {
        "section": 3,
        "question": "git pull делает:",
        "options": ["Только скачивает изменения", "Скачивает и сливает изменения в текущую ветку", "Удаляет удалённые ветки", "Только показывает разницу"],
        "answer": 1  # B
    },
    {
        "section": 3,
        "question": "Что такое .gitconfig?",
        "options": ["Локальный ignore-файл", "Конфигурация пользователя Git", "Сценарий инициирования репозитория", "Скрытый лог команд"],
        "answer": 1  # B
    },
    {
        "section": 3,
        "question": "Как откатить последний коммит (не удаляя изменений)?",
        "options": ["git undo", "git revert HEAD", "git reset HEAD~1", "git delete HEAD"],
        "answer": 2  # C
    },

    # === Раздел 4: Linux ===
    {
        "section": 4,
        "question": "Какая команда показывает текущую директорию?",
        "options": ["ls", "pwd", "cd", "whereami"],
        "answer": 1  # B
    },
    {
        "section": 4,
        "question": "Как перейти в /home/user/docs?",
        "options": ["ls /home/user/docs", "cd /home/user/docs", "pwd /home/user/docs", "goto /home/user/docs"],
        "answer": 1  # B
    },
    {
        "section": 4,
        "question": "Команда ls -la:",
        "options": ["Показывает только скрытые файлы", "Показывает список с подробностями, включая скрытые", "Удаляет файлы", "Создаёт alias"],
        "answer": 1  # B
    },
    {
        "section": 4,
        "question": "Как скопировать файл a.txt в b.txt?",
        "options": ["cp a.txt b.txt", "mv a.txt b.txt", "copy a.txt b.txt", "dup a.txt b.txt"],
        "answer": 0  # A
    },
    {
        "section": 4,
        "question": "Для установки права на выполнение:",
        "options": ["chmod +x filename", "chmod u+x filename", "chown +x filename", "chmod x filename"],
        "answer": 0  # A
    },
    {
        "section": 4,
        "question": "Как посмотреть первые 10 строк файла log.txt?",
        "options": ["head log.txt", "tail log.txt", "cat log.txt", "more log.txt"],
        "answer": 0  # A
    },
    {
        "section": 4,
        "question": "Команда для просмотра процессов:",
        "options": ["jobs", "ps", "top", "grep"],
        "answer": 2  # C
    },
    {
        "section": 4,
        "question": 'grep "pattern" file.txt — это:',
        "options": ["Поиск процессов", "Фильтрация строк по шаблону", "Изменение прав доступа", "Копирование строк"],
        "answer": 1  # B
    },
    {
        "section": 4,
        "question": "Как завершить процесс с PID 1234?",
        "options": ["killall 1234", "kill 1234", "stop 1234", "terminate 1234"],
        "answer": 1  # B
    },
    {
        "section": 4,
        "question": "Что создаёт mkdir -p a/b/c:",
        "options": ["Только папку c", "Все папки a, b, c, включая вложенную структуру", "Удаляет дерево", "Перемещает папки"],
        "answer": 1  # B
    },

    # === Раздел 5: Data Warehouse ===
    {
        "section": 5,
        "question": "Что такое Data Warehouse?",
        "options": ["OLTP-система", "СУБД для аналитической обработки", "NoSQL-база под транзакции", "Хранилище логов"],
        "answer": 1  # B
    },
    {
        "section": 5,
        "question": "Названия схем моделирования:",
        "options": ["Star и Snowflake", "Flake и Cube", "Hub и Spoke", "Simple и Complex"],
        "answer": 0  # A
    },
    {
        "section": 5,
        "question": "Fact-таблица хранит:",
        "options": ["Описательные атрибуты", "Метрические данные (факты) — суммы, счётчики", "Метаданные таблиц", "SQL-запросы"],
        "answer": 1  # B
    },
    {
        "section": 5,
        "question": "Dimension-таблица — это:",
        "options": ["Таблица фактов", "Детали измерения (время, продукт, клиент)", "Журнал транзакций", "Системная таблица"],
        "answer": 1  # B
    },
    {
        "section": 5,
        "question": "ETL расшифровывается как:",
        "options": ["Extract, Transform, Load", "Execute, Test, Launch", "Extract, Transfer, Leave", "Encode, Transmit, Load"],
        "answer": 0  # A
    },
    {
        "section": 5,
        "question": "Разница между OLTP и OLAP:",
        "options": ["OLTP — аналитика, OLAP — транзакции", "OLTP — транзакции, OLAP — аналитика", "Это одно и то же", "OLTP — NoSQL, OLAP — SQL"],
        "answer": 1  # B
    },
    {
        "section": 5,
        "question": "Зачем нужны суррогатные ключи в DWH?",
        "options": ["Уникальность измерений", "Для MongoDB", "Авто‑индексация", "Ускорение пайплайнов"],
        "answer": 0  # A
    },
    {
        "section": 5,
        "question": "Slowly Changing Dimension (SCD) — это:",
        "options": ["Большая таблица измерений", "Подход обработки изменяющихся измерений во времени", "Тип fact-таблицы", "Вид индекса"],
        "answer": 1  # B
    },
    {
        "section": 5,
        "question": "Слой для первичных (raw) данных:",
        "options": ["Presentation", "Raw / Staging", "Business", "Curated"],
        "answer": 1  # B
    },
    {
        "section": 5,
        "question": "OLAP-куб — это:",
        "options": ["Физическое хранилище", "Многомерная модель данных для аналитики", "SQL-таблица", "ETL-инструмент"],
        "answer": 1  # B
    },

    # === Раздел 6: Нормализация ===
    {
        "section": 6,
        "question": "Что такое первая нормальная форма (1NF)?",
        "options": ["Разбиение на таблицы", "Атомарные значения в колонках", "Таблица не должна иметь повторов", "Связь один‑ко‑многим"],
        "answer": 1  # B
    },
    {
        "section": 6,
        "question": "Вторая нормальная форма (2NF):",
        "options": ["Удаление транзитивной зависимости", "Нет частичных зависимостей от составного ключа", "Каждое поле зависит от всего PK", "Только первичный ключ"],
        "answer": 1  # B
    },
    {
        "section": 6,
        "question": "Третья нормальная форма (3NF):",
        "options": ["Нет транзитивных зависимостей", "Атомарные значения", "Полная декомпозиция", "Любая функциональная зависимость разрешена"],
        "answer": 0  # A
    },
    {
        "section": 6,
        "question": "Бойс-Кодда нормальная форма (BCNF):",
        "options": ["Расширяет требования 3NF", "Разрешает транзитивные зависимости", "Только уникальные ключи", "Нужна только для OLAP"],
        "answer": 0  # A
    },
    {
        "section": 6,
        "question": "Транзитивная зависимость — это:",
        "options": ["A → B и B → C, следовательно A → C", "A → B и A → C", "C → B", "Нет зависимости"],
        "answer": 0  # A
    },
    {
        "section": 6,
        "question": "Частичная зависимость означает:",
        "options": ["Атрибут зависит от части составного PK", "Атрибут зависит от всего PK", "Атрибут имеет NULL", "Не влияет на нормальную форму"],
        "answer": 0  # A
    },
    {
        "section": 6,
        "question": "Если таблица с несколькими атрибутами, зависящими только от части составного ключа — она:",
        "options": ["В 1NF", "В 2NF", "Не в 2NF", "В 3NF"],
        "answer": 2  # C
    },
    {
        "section": 6,
        "question": "Зачем нормализовать данные?",
        "options": ["Ускорить SELECT", "Уменьшить повторение данных, избежать аномалий", "Уменьшить сложность", "Только для OLAP"],
        "answer": 1  # B
    },
    {
        "section": 6,
        "question": "Денормализация:",
        "options": ["Всегда плоха", "Улучшает время чтения, может ухудшить консистентность", "Делает данные атомарными", "Применяется только в 1NF"],
        "answer": 1  # B
    },
    {
        "section": 6,
        "question": "Таблица со столбцами A, B, C, где A→B и B→C, но A не напрямую зависит от C — какой нормальной форме она не соответствует?",
        "options": ["1NF", "2NF", "3NF", "BCNF"],
        "answer": 2  # C
    },
]

# Заголовок
st.title("📝 Тест по Data Engineering")
st.markdown("Ответьте на вопросы по разделам. В конце — проверка результата.")

score = 0
answers = []

# Проходим по всем вопросам, разделяя по разделам
current_section = None

for i, q in enumerate(quiz_data):
    # Показываем заголовок раздела при смене
    if q["section"] != current_section:
        current_section = q["section"]
        st.header(f"Раздел {current_section}")
        # Можно добавить описание
        if current_section == 3:
            st.markdown("*Git: основы работы с репозиториями*")
        elif current_section == 4:
            st.markdown("*Linux: базовые команды в терминале*")
        elif current_section == 5:
            st.markdown("*Data Warehouse: моделирование и архитектура*")
        elif current_section == 6:
            st.markdown("*Нормализация баз данных*")

    # Номер вопроса в разделе
    section_questions = [x for x in quiz_data if x["section"] == q["section"]]
    section_index = section_questions.index(q) + 1

    st.subheader(f"Вопрос {section_index}")
    st.write(q["question"])

    # Выбор ответа
    choice = st.radio(
        "",
        q["options"],
        key=f"q{i}",
        label_visibility="collapsed"
    )

    # Проверка
    selected_index = q["options"].index(choice)
    is_correct = selected_index == q["answer"]
    answers.append(is_correct)

# Кнопка "Проверить результат"
if st.button("✅ Проверить результат"):
    score = sum(answers)
    total = len(quiz_data)
    percent = (score / total) * 100

    st.balloons()

    if percent >= 80:
        st.success(f"🎉 Отлично! Вы набрали {score} из {total} ({percent:.1f}%)")
    elif percent >= 60:
        st.info(f"👍 Хорошо! {score} из {total} ({percent:.1f}%)")
    else:
        st.error(f"📊 Нужно повторить. {score} из {total} ({percent:.1f}%)")

    # Разбор ошибок
    st.write("### ❌ Ошибки:")
    has_errors = False
    for i, q in enumerate(quiz_data):
        if not answers[i]:
            has_errors = True
            with st.expander(f"Вопрос: {q['question']}"):
                st.markdown(f"**Правильный ответ:** ✅ {q['options'][q['answer']]}")
    if not has_errors:
        st.success("🎉 Вы ответили на все вопросы правильно!")