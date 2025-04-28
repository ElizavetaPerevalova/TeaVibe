# TeaVibe
### 📋 Инструкция для запуска проекта 

**1. Установи необходимое ПО:**
- [Git](https://git-scm.com/downloads) (отмечай все галочки при установке)
- [Python 3.10+](https://www.python.org/downloads/) (обязательно поставь галочку "Add Python to PATH")
- [VSCode](https://code.visualstudio.com/) (или любой другой редактор кода)

**2. Открой терминал (Bash):**
- На Windows: `Win + R` → введи `cmd` → `OK`
- На Mac: Открой `Terminal` через поиск

**3. Склонируй проект с GitHub:**
```bash
git clone git@github.com:ElizavetaPerevalova/TeaVibe.git
cd TeaVibe/backend
```

**4. Создай виртуальное окружение:**
```bash
python -m venv venv
```

**5. Активируй виртуальное окружение:**
- Windows:
  ```bash
  venv\Scripts\activate
  ```
- Mac/Linux:
  ```bash
  source venv/bin/activate
  ```
*(Теперь в начале строки терминала должно появиться `(venv)`)*

**6. Установи зависимости:**
```bash
pip install -r requirements.txt
```

**7. Настрой базу данных:**
```bash
python manage.py migrate
```

**8. Создай суперпользователя (опционально):**
```bash
python manage.py createsuperuser
```
*(Придумай логин/пароль для админки)*

**9. Запусти сервер:**
```bash
python manage.py runserver
```

**10. Открой проект в браузере:**
Перейди по ссылке, которая появилась в терминале (обычно http://127.0.0.1:8000)

---

### 🔥 Если что-то пошло не так:
1. **Ошибка с Git**: Проверь, что Git установлен. Введи в терминале:
   ```bash
   git --version
   ```
2. **Ошибка с Python**: Убедись, что Python добавлен в PATH. Проверь:
   ```bash
   python --version
   ```
3. **Ошибка с зависимостями**: Попробуй:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

---

### 📌 Полезные команды для работы:
- **Остановить сервер**: `Ctrl + C` в терминале
- **Деактивировать venv**: `deactivate`
- **Запустить админку**: После запуска сервера открой http://127.0.0.1:8000/admin


P.S. [Как работать с Git для начинающих](https://habr.com/ru/articles/541258/)