
import streamlit as st
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import time

# API 호출을 위한 캐시 적용 (st.cache_data 사용)
@st.cache_data
def fetch_video_data(channel_id, keyword):
    # Google API를 사용하여 유튜브 데이터 검색
    youtube = build("youtube", "v3", developerKey="YOUR_YOUTUBE_API_KEY")

    # 1주일 전 날짜 계산
    one_week_ago = datetime.now() - timedelta(weeks=1)
    published_after = one_week_ago.isoformat() + "Z"

    # API 호출: '코인' 키워드가 포함된 제목의 영상만 검색
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        q=keyword,
        type="video",
        publishedAfter=published_after,
        order="date",  # 최신 영상
        maxResults=5  # 최대 5개 영상
    )
    response = request.execute()

    video_data = []
    for item in response['items']:
        title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        description = item['snippet']['description']

        video_data.append({
            "title": title,
            "url": video_url,
            "description": description
        })
    
    return video_data

# 채널 ID와 키워드 설정 (강환국 채널, '코인' 키워드)
channel_id = "UC5gB48k0RzG3T18_m1HlKfw"
keyword = "코인"

# 버튼 클릭 시에만 데이터 로드
if st.button("Load Video Data"):
    video_data_list = fetch_video_data(channel_id, keyword)
    
    if video_data_list:
        for video_data in video_data_list:
            st.write(f"**Video Title:** {video_data['title']}")
            st.write(f"**Video URL:** {video_data['url']}")

            # 영상 설명을 10줄로 요약
            video_description = video_data['description']
            description_lines = video_description.split('\n')
            summary = '\n'.join(description_lines[:10])  # 10줄로 자르기
            st.write("**Video Description (Summary):**")
            st.write(summary)
    else:
        st.write("No videos found with the keyword '코인' uploaded in the last week.")
else:
    st.write("Click the button to load the latest videos with '코인' keyword.")
