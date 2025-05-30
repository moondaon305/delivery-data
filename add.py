import streamlit as st
import pandas as pd

st.title("Delivery Data Visualization")

# CSV 파일 이름 주의: 저장소 파일 이름과 똑같이 적기
data = pd.read_csv("Delivery (1).csv")

st.write(data)

# 간단한 차트 (숫자형 컬럼 이름을 실제 컬럼명으로 바꾸세요)
# 예를 들어, 'Quantity'라는 컬럼이 있다면 아래처럼
# st.bar_chart(data["Quantity"])
