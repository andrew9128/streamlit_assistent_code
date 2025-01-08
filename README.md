# streamlit_assistent_code

Данный проект представляет собой простое веб-приложение, разработанное с использованием **Streamlit** и модели **Gemini** от Google Generative AI. Основная цель приложения — предоставление пользователю удобного интерфейса для автодополнения кода, его экспорта и управления историей.

---

## **Функциональность**

1. **Автодополнение кода**  
   Пользователь вводит код в текстовое поле, а модель **Gemini** генерирует предсказания или дополнения для введенного текста.

2. **Сохранение истории**  
   Весь введенный код может быть сохранен в локальный файл `history.txt`.

3. **Экспорт кода**  
   Возможность скачать введенный код в виде файла `.py`.

4. **Настраиваемый интерфейс**  
   Приложение поддерживает кастомизацию интерфейса через подключение пользовательских стилей CSS.

---

## **Описание кода**

### **1. Импорт библиотек**

- `streamlit` — для создания веб-приложения.  
- `google.generativeai` — для работы с моделью **Gemini**.  
- `os` — для работы с переменными окружения и файловой системой.

```python
import streamlit as st
import google.generativeai as genai
import os
```

### **2. Настройка Google Generative AI**

- Установка переменной окружения для авторизации через JSON-файл ключей:  

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/MyDrive/gen/global-brook-412118-4bbce82b657c.json"
```

- Инициализация модели **Gemini**:  

```python
gemini_model = genai.GenerativeModel(model_name="gemini-pro")
```

### **3. Основные функции интерфейса**

#### **Поле для ввода кода**

```python
code = st.text_area("Введите код:", height=300)
```

Пользователь может вставить код (до 300 строк) в текстовое поле.

#### **Кнопка "Отправить"**

Запускает автодополнение кода с помощью модели Gemini:

```python
if st.button("Отправить"):
    result = autocomplete(code)
    if result is None:
        st.text("Произошла ошибка при обработке кода. Код не распознан.")
    elif result and result[0] == "Введенный код пуст":
        st.text(result[0])
    else:
        for i, prediction in enumerate(result):
            try:
                prediction_text = extract_text(prediction)
                st.code(prediction_text, language="plaintext")
            except TypeError:
                st.text("Произошла ошибка при обработке кода. Код не распознан.")
```

#### **Кнопка "Сохранить историю"**

Сохраняет введенный код в локальный файл `history.txt`:

```python
if st.button("Сохранить историю"):
    try:
        with open("history.txt", "a") as f:
            f.write(code)
    except NameError:
        st.text("Ошибка: код нельзя экспортировать")
```

#### **Кнопка "Экспортировать код"**

Позволяет пользователю скачать введенный код в формате `.py`:

```python
if st.button("Экспортировать код"):
    try:
        st.download_button("Скачать код", code, "code.py")
    except NameError:
        st.text("Ошибка: код нельзя экспортировать")
```

#### **Подключение пользовательского CSS**

```python
with open("/content/drive/MyDrive/gen/style.css", "r") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
```

---

## **Как запустить проект**

### **1. Установка зависимостей**

Убедитесь, что у вас установлены необходимые библиотеки:

```bash
python -m pip install streamlit google-generative-ai
```

### **2. Запуск приложения**

Запустите приложение с помощью следующей команды:

```bash
streamlit run app.py
```

### **3. Подготовка ключей Google Generative AI**

1. Создайте проект в Google Cloud Platform.
2. Включите API для Generative AI.
3. Скачайте JSON-файл ключей и поместите его в соответствующую директорию.

---

С помощью **Streamlit** и **Google Generative AI** вы можете быстро разработать простое и удобное веб-приложение, подходящее как для начинающих, так и для опытных программистов.
