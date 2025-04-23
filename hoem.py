import streamlit as st

st.set_page_config(page_title="홈", page_icon="🏠")

st.title("🏠 홈 페이지")
st.write("여기는 홈입니다. 좌측 사이드바에서 다른 페이지를 선택하세요.")

st.sidebar.markdown("🏥 page2")
st.sidebar.markdown("💸 page3")

# Define the pages
hoem = st.Page("home.py", title="Main Page", icon="🎈")
page2 = st.Page("page2.py", title="Page 2", icon="❄️")
page3 = st.Page("page3.py", title="Page 3", icon="🎉")


# Set up navigation
pg = st.navigation([home, page2, page3])

# Run the selected page
pg.run()
