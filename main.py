import streamlit as st

st.write('---')
st.title('1.버튼')
st.write('---')

if st.button("클릭하세요"):
    st.write("버튼이 눌렸습니다!")

feedback = st.text_area("자유롭게 의견을 남겨주세요.")
height=150

score = st.number_input("점수를 입력하세요.",
min_value=0, max_value=100, value=50, step=5)

from datetime import date
birthday = st.date_input("생년월일 선택")
period = st.date_input("기간 선택.",
value=[date(2025,1,1), date(2025,12,31)])

color = st.color_picker("테마 색상을 선택하세요", value="#00ff00")

uploaded_file = st.file_uploader("파일을 업로드하세요", type=["csv", "xlsx"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
with st.form("my_form"):
    name = st.text_input("이름")
    age = st.number_input("나이", 0, 100)
    submitted = st.form_submit_button("제출")
if submitted:
    st.write(f"{name} ({age}세) 제출 완료!")

with st.expander("추가 정보 보기", expanded=False):
    st.write("여기에 세부 정보를 넣어요.")

import time
with st.spinner("처리 중입니다..."):
    time.sleep(3)
st.success("완료!")

import time
my_bar = st.progress(0)
for percent in range(100):
    time.sleep(0.05)
    my_bar.progress(percent + 1)
    
col1, col2 = st.columns(2)
with col1:
    st.write("왼쪽 열")
with col2:
    st.write("오른쪽 열") 

option = st.sidebar.selectbox("사이드바 메뉴",["홈", "설정","정보"])






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
