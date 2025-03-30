
import streamlit as st
import requests
import time

# API 호출을 위한 캐시 적용 (st.cache_data 사용)
@st.cache_data
def fetch_video_data(channel_url, keyword):
    st.write("Fetching data from API...")
    time.sleep(2)  # 실제 API 호출 시간 모방
    # 실제 API 호출 코드: 예시로 requests.get() 사용
    return {"video_title": "Crypto Update", "video_url": "http://example.com"}

# 버튼 클릭 시에만 데이터 로드
if st.button("Load Video Data"):
    video_data = fetch_video_data("https://example.com", "crypto")
    st.write(f"Video Title: {video_data['video_title']}")
    st.write(f"Video URL: {video_data['video_url']}")
else:
    st.write("Click the button to load data.")
