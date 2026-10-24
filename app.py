import streamlit as st

st.set_page_config(page_title="Мій Супер-Додаток", page_icon="https://img.icons8.com/nolan/1200/bongo-cat.jpg", layout="wide")

st.title("Ласкаво просимо до мого додатку! 🚀")

tab1, tab2 = st.tabs(["Про мене", "Мій інструмент"])

with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn.wcs.org/2024/03/13/21/14/05/2d2c6f1b-71c4-4390-b7e2-deb21a0bc11f/shutterstock_2331893385.jpg", width=400)
    with col2:
        st.subheader("Привіт, я майбутній Python Developer!")
        st.write("Я навчаюсь в Малій Компютерній Академії IT STEP. Створюю круті веб-додатки та вивчаю Streamlit")

        with st.container():
            st.info("Контакти для зв`язку")
            st.markdown("- GitHub: [Мій профіль](https://github.com)")
            st.markdown("- E-Mail: teacher@itstep.org")

with tab2:
    st.info("У процессі розробки")