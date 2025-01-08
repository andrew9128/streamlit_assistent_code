import streamlit as st 
import google.generativeai as genai 
import os 
 
# Установка переменной окружения GOOGLE_APPLICATION_CREDENTIALS 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/MyDrive/gen/global-brook-412118-4bbce82b657c.json" 
 
# Настройка модели Gemini 
gemini_model = genai.GenerativeModel(model_name="gemini-pro") 
 
# Создание интерфейса веб-приложения 
# Вывод названия приложения 
st.title("Помощник по кодированию") 
 
# Создание поля ввода кода 
code = st.text_area("Введите код:", height=300) 
 
# Кнопка "Отправить" 
if st.button("Отправить"): 
    # Выполнение автодополнения и отображение результатов 
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
            except TypeError as e: 
                st.text("Произошла ошибка при обработке кода. Код не распознан.") 
 
# Сохранение истории кодирования 
if st.button("Сохранить историю"): 
    try: 
        # Открытие файла "history.txt" в режиме добавления 
        with open("history.txt", "a") as f: 
            # Запись введенного кода в файл 
            f.write(code) 
    except NameError: 
        st.text("Ошибка: код нельзя экспортировать") 
 
# Экспорт кода 
if st.button("Экспортировать код"): 
    try: 
        # Скачивание кода в виде файла "code.py" 
        st.download_button("Скачать код", code, "code.py") 
    except NameError: 
        st.text("Ошибка: код нельзя экспортировать") 
 
# Подключение CSS файла 
with open("/content/drive/MyDrive/gen/style.css", "r") as f: 
    css = f.read() 
 
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True) 
 
