import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import plotly.figure_factory as ff
import plotly.express as px
from PIL import Image

#그래프 폰트 설정
# font_path = 'malgun.ttf'
# fontprop = fm.FontProperties(fname=font_path)
# plt.rcParams['font.family'] = fontprop.get_name()
# plt.rcParams['axes.unicode_minus'] = False 

font_path = "./KBO Dia Gothic_medium.ttf"  # 경로 확인
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()  # 전체 기본 폰트 설정

# 웹폰트 로딩용 CSS 정의
# font_css = """
# <style>
# @font-face {
#     font-family: 'KBO Dia Gothic_bold';
#     src: url('./KBO Dia Gothic_bold.ttf') format('truetype');
#     font-weight: 1000;
# }
# @font-face {
#     font-family: 'Malgun';
#     src: url('./malgun.ttf') format('truetype');
#     font-weight: normal;
# }
# </style>
# """

st.markdown("""
<style>
@font-face {
    font-family: 'KBO Dia Gothic';
    src: url('./KBO Dia Gothic_light.ttf') format('truetype');
    font-weight: 300;
}
@font-face {
    font-family: 'KBO Dia Gothic';
    src: url('./KBO Dia Gothic_medium.ttf') format('truetype');
    font-weight: 500;
}
@font-face {
    font-family: 'KBO Dia Gothic';
    src: url('./KBO Dia Gothic_bold.ttf') format('truetype');
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# CSS 삽입
#st.markdown(font_css, unsafe_allow_html=True)

# Webpage Title
#st.title("Streamlit으로 만드는 데이터 앱")
#st.title('“제 2의 김도영이 될래요”... 그들은 어떻게 KBO의 별이 되었을까?')

#st.markdown("### “제 2의 김도영이 될래요”... 그들은 어떻게 KBO의 별이 되었을까?")
# st.markdown("""
# <div style='font-family: "KBO Dia Gothic_bold"; font-size: 24px;'>
# “제 2의 김도영이 될래요”... 그들은 어떻게 KBO의 별이 되었을까?
# </div>
# """, unsafe_allow_html=True)

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 26px;
    font-weight: 700;
    text-align: center;
    line-height: 1.6;
    background-color: #08043c;
    padding: 12px 16px;
    border-radius: 8px;
    color:#ffffff ;
'>
“제 2의 김도영이 될래요”<br>그들은 어떻게 KBO의 별이 되었을까?
</div>
""", unsafe_allow_html=True)

st.write(' ') #enter

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
'>
2025 시즌 이후 한국 프로야구(KBO)는 뜨거운 관심을 받고 있다. 특히 젊은 팬 층의 유입과 함께 선수 개인의 커리어, 성장 과정, 그리고 미래 유망주에 대한 주목도가 크게 증가했다. 그렇다면, 야구 선수는 어떻게 프로가 되는 것일까? KBO 리그에서 선수가 되는 길은 다양하다. 신인 드래프트를 통해 지명을 받는 ‘드래프티’ 외에도, 육성선수로 계약해 2군에서 실력을 쌓은 뒤 1군에 등록하거나, 독립리그 출신 선수, 대학 혹은 실업야구를 거쳐 신고선수로 입단하는 사례도 있다. 다른 팀과 계약이 끝난 뒤 이적하는 자유계약선수(FA), 그리고 외국인 선수도 팀의 핵심 자원으로 활약한다.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
이처럼 진입 경로 중 가장 대표적인 운영 방식은 바로 KBO 신인 드래프트다. 드래프트는 리그의 균형 발전을 도모하고, 유망주에게 프로 진출의 기회를 제공하는 출발선의 제도화된 모습이다. 10개 구단이 정해진 순서대로 선수를 지명해 계약하는 이 제도는, 한 해 수많은 고교 및 대학 선수들의 희망이 걸린 기회의 장이자, 구단의 미래 전략이 응축된 무대이다.
</div>
""", unsafe_allow_html=True)

# st.write(' ')

# st.write('2025 시즌 이후 한국 프로야구(KBO)는 뜨거운 관심을 받고 있다. 특히 젊은 팬 층의 유입과 함께 선수 개인의 커리어, 성장 과정, 그리고 미래 유망주에 대한 주목도가 크게 증가했다. 그렇다면, 야구 선수는 어떻게 프로가 되는 것일까? KBO 리그에서 선수가 되는 길은 다양하다. 신인 드래프트를 통해 지명을 받는 ‘드래프티’ 외에도, 육성선수로 계약해 2군에서 실력을 쌓은 뒤 1군에 등록하거나, 독립리그 출신 선수, 대학 혹은 실업야구를 거쳐 신고선수로 입단하는 사례도 있다. 다른 팀과 계약이 끝난 뒤 이적하는 자유계약선수(FA), 그리고 외국인 선수도 팀의 핵심 자원으로 활약한다.')

# st.write('이처럼 진입 경로 중 가장 대표적인 운영 방식은 바로 KBO 신인 드래프트다. 드래프트는 리그의 균형 발전을 도모하고, 유망주에게 프로 진출의 기회를 제공하는 출발선의 제도화된 모습이다. 10개 구단이 정해진 순서대로 선수를 지명해 계약하는 이 제도는, 한 해 수많은 고교 및 대학 선수들의 희망이 걸린 기회의 장이자, 구단의 미래 전략이 응축된 무대이다.')

st.markdown("- - -")

#st.header('이정후의 휘문 VS 박세웅의 경북! 진짜 야구 명문고를 찾아라!')

#st.markdown('### 이정후의 휘문 VS 박세웅의 경북! 진짜 야구 명문고를 찾아라!')

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 26px;
    font-weight: 700;
    text-align: center;
    line-height: 1.6;
    background-color: #08043c;
    padding: 12px 16px;
    border-radius: 8px;
    color:#ffffff ;
'>
이정후의 휘문 VS 박세웅의 경북! 진짜 야구 명문고를 찾아라!
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
KBO 리그의 각 구단이 우승을 위해 치열한 경쟁을 펼친다면, 고교 야구부들도 다양한 대회에서 우승을 차지하기 위해 뜨거운 열정을 불태우고 있다. 고교 야구부들이 이렇게까지 열심히 하는 이유는 물론 고등학교의 위상을 높이기 위해서도 있지만, 더욱 중요한 것은 각 프로구단의 스카우터들에게 강한 인상을 남겨 자교 학생들을 더 많이 프로에 입단시키기 위함이다. 실제로 드래프트는 일종의 입시판이라고 볼 수 있기 때문에, 드래프트에서 좋은 성과를 내기 위해서는 고등학교의 영향을 무시할 수 없다. 그렇기에 야구 역시 좋은 선수들을 많이 배출하는 소위 ‘명문고’도 존재한다. 그렇다면 과연 어떤 고등학교가 야구 명문고일까? 
</div>
""", unsafe_allow_html=True)

#시각화1
#데이터
schools = ['휘문고', '서울고', '장충고', '덕수고', '경남고', '광주제일고', '경북고', '북일고', '경기고', '성남고']
counts = [50, 49, 49, 46, 45, 40, 39, 38, 37, 37]

fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.bar(schools, counts, color='#37bceb')
ax.set_title("드래프티 수(명)", fontsize=14, fontproperties=font_prop)
ax.set_ylabel("명", fontproperties=font_prop)
ax.set_ylim(0, 60)

plt.xticks(fontproperties=font_prop)
plt.yticks(fontproperties=font_prop)

# 눈금선 스타일
ax.grid(axis='y', linestyle='--', alpha=0.5)

# 그래프 출력
plt.tight_layout()
#plt.show()
st.pyplot(fig)


st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
우선 2014년부터 2025년까지의 드래프트 데이터를 바탕으로 가장 많은 드래프티를 배출한 학교는 휘문고등학교였다. 무려 50명의 드래프티를 배출하였고, 실제로 휘문고는 이 기간 동안 메이저리그까지 진출한 이정후나 키움 안우진과 같은 걸출한 1차지명 선수들을 배출하기도 하며 자타가 인정하는 명문고로서의 지위를 공고히 하였다. 또한 휘문고의 뒤를 서울고와 장충고가 각각 49명으로 바짝 뒤쫓았다. 두 학교도 각각 KT 강백호, 기아 박찬호와 같이 프로 무대에서 좋은 활약을 보여주는 선수들을 다수 배출하였다.
</div>
""", unsafe_allow_html=True)

#시각화2
#데이터
schools = ['하마고', '서울고', '장충고', '덕수고', '경남고', '광주일고', '제물포고', '경북고', '경기고', '성남고']
rates = [48, 67, 65, 76, 87, 75, 46, 63, 65, 54]

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(schools, rates, color='#37bceb')

# y축 범위 0~100 고정
ax.set_ylim(0, 100)

# 제목 및 눈금
ax.set_title("1군 데뷔율", fontsize=14, fontproperties=font_prop)
ax.set_ylabel("비율 (%)", fontproperties=font_prop)
plt.xticks(fontproperties=font_prop)
plt.yticks(fontproperties=font_prop)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# 막대 위에 수치 표시
for i, v in enumerate(rates):
    ax.text(i, v + 2, f'{v}%', ha='center', va='bottom', fontsize=9, fontproperties=font_prop)

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
또한 실제 1군에 데뷔한 선수들의 비율 역시 유의미한 평가지표로 작용할 수 있다. 배출한 드래프티들이 전부 1군 무대에 데뷔하는 것은 아니기 때문에 오히려 실제로 1군에 데뷔하는 선수들의 비율을 비교해보는 것도 중요하다. 실제로 1군 데뷔율을 살펴보면, 앞서 가장 많은 드래프티를 배출한 휘문고는 단 48%로, 절반 이상의 선수들이 1군에 데뷔하지 못했다는 것을 확인할 수 있다. 반대로 경남고의 경우, 조사한 기간 내에 배출한 45명의 드래프티 가운데 39명이 1군 무대에 데뷔하며 무려 87%의 1군 데뷔율이라는 압도적인 수치를 보여줬다. 실제로 경남고는 롯데 자이언츠의 영구결번인 최동원과 이대호의 모교로서, 최근에도 한화 노시환, 키움 이주형 등 걸출한 선수들을 배출하며 명문고의 명맥을 유지하고 있음을 확인할 수 있다.
</div>
""", unsafe_allow_html=True)

#시각화3
#데이터
schools = ['하마고', '서울고', '장충고', '덕수고', '경남고', '광주일고', '제물포고', '경북고', '경기고', '성남고']
avg_war = [3.300, 2.530, 1.404, 1.083, 0.998, 1.161, 4.341, 1.114, 0.690, 1.477]

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(schools, avg_war, color='#37bceb')

# y축 설정
ax.set_ylim(0, 7)
ax.set_title("평균 WAR", fontsize=14, fontproperties=font_prop)
ax.set_ylabel("WAR", fontproperties=font_prop)

# 눈금 및 글꼴
plt.xticks(fontproperties=font_prop)
plt.yticks(fontproperties=font_prop)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# 막대 위 숫자 표시
for i, v in enumerate(avg_war):
    ax.text(i, v + 0.2, f'{v:.2f}', ha='center', va='bottom', fontsize=9, fontproperties=font_prop)

plt.tight_layout()
st.pyplot(fig)


st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
하지만 이렇게 각 고등학교들이 배출한 선수들의 수도 중요하지만, 그 선수들이 실제 1군 무대에서 얼마나 큰 활약을 하는지 역시 신경써야 할 지점이다. 배출한 선수는 조금 적을지라도, 그 선수들이 모두 1군 무대에서 중요한 위치를 차지하고 있다고 한다면 결코 무시할 수 없기 때문이다. 이렇게 양보다 질을 중요시하는 고등학교로는 경북고가 있고, 조사 기간 내에 데뷔한 경북고 선수들의 평균 WAR은 무려 4.341로 압도적인 모습이었다. 실제로 이 기간 내에 경북고에서 배출된 선수들로는 롯데 박세웅, 삼성 원태인처럼 각 팀에서 대체 불가능한 토종 1선발들이 자리잡고 있는 것을 확인할 수 있다.
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
이렇게 다양한 기준을 통해 야구 명문고를 분류해보았다. 물론 야구 명문고라고 해서 무조건 좋은 선수들을 많이 배출하는 것도 아니고, 반대의 경우에도 좋은 선수들을 충분히 배출해낼 수 있다. 다만 야구 명문고들은 학교 차원에서 야구부에 대한 지원이 적극적인 경우가 많고, 각 프로 구단의 스카우터들 역시 더 많은 관심을 쏟는 경우가 많다보니 드래프트와도 깊은 관련이 있을 수 밖에 없다. 즉 야구 명문고에 대해 분석해보는 것은 신인 드래프트를 보는 시야를 넓힐 수 있는 계기가 될 것이다. 
</div>
""", unsafe_allow_html=True)

st.markdown("- - -")

#st.header('고졸 강백호 VS 대졸 전준우! 대졸보다 고졸이 선호된다?')

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 26px;
    font-weight: 700;
    text-align: center;
    line-height: 1.6;
    background-color: #08043c;
    padding: 12px 16px;
    border-radius: 8px;
    color:#ffffff ;
'>
고졸 강백호 VS 대졸 전준우! 대졸보다 고졸이 선호된다?
</div>
""", unsafe_allow_html=True)

#st.markdown('### 고졸 강백호 VS 대졸 전준우! 대졸보다 고졸이 선호된다?')

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
한국 프로야구에서 선수들이 프로에 진입하는 시점은 크게 고등학교 졸업 직후 혹은 대학교 졸업 이후로 나뉜다. 일부는 실업팀이나 독립리그를 거치기도 하지만, 대다수의 선수들은 이 두 경로를 통해 드래프트에 참가하게 된다. 이 두 경로는 단순한 출신 배경의 차이를 넘어, 선수 성장의 방향, 구단의 투자 전략, 그리고 성과에 대한 보상 구조까지 연결되는 중요한 기준이 된다.
이에 따라 ‘고졸이 유리한가, 대졸이 유리한가’라는 논쟁은 KBO 리그에서 꾸준히 이어져온 화두 중 하나다. 이 비교는 단순한 출신 배경을 넘어, 선수의 성장 경로와 구단의 육성 전략, 더 나아가 한국 야구 시스템의 구조적 문제까지 함축하고 있기 때문이다.
         
과거에는 선동열, 이종범, 장효조, 양준혁 등 대학을 거쳐 프로에 진출한 전설적인 스타플레이어들이 많았지만, 최근에는 이정후, 강백호, 소형준, 이의리 등 고교 졸업 직후 곧바로 프로에 입단하는 흐름이 주류로 자리잡고 있다. 이는 단순한 선택의 문제가 아니라, KBO 리그 구조와 제도적 환경이 고졸 선수에게 유리하게 작용하고 있기 때문이다.
         
실제로 대학을 거치면 군 복무 문제, FA 취득 지연, 나이 경쟁 등의 불이익이 발생하며, 구단 입장에서도 육성 기간이 짧은 고졸 유망주에게 더 빠르게 투자 수익을 거둘 수 있는 구조가 형성되어 있다.
         
이러한 흐름은 데이터상에서도 명확하게 드러난다. 2001~2012년 드래프트 선수 분석에 따르면, 고졸 출신 선수의 평균 WAR는 3.67로, 대졸 출신 선수의 1.51에 비해 2.4배에 달한다. 2022년 기준으로는 신인 드래프트에서 고졸 선수가 전체의 84%를 차지했고, 2025년 드래프트에서는 그 수치가 85%에 이르렀다. 반면 대졸 선수는 16명에 불과했으며, 대학야구계는 지속적인 지명 축소에 위기의식을 표명하고 있다.
         
따라서 본 분석에서는 선수의 학력(고졸/대졸)에 따른 프로 진출 이후의 성과를 WAR(Wins Above Replacement)와 연봉이라는 주요 지표를 중심으로 비교하고자 한다. WAR은 선수의 경기 기여도를 수치화한 지표로, 팀 승리에 얼마나 기여했는지를 보여주는 대표적인 성능 지표이며, 연봉은 해당 선수가 리그 내에서 어느 정도의 시장 가치를 인정받고 있는지를 반영하는 자료로 사용된다.
         
시각화를 통해 우리는 단순히 "누가 더 성과가 좋았는가"를 넘어서, 구단이 어떤 기준으로 선수를 선발하고 투자하는가, 그리고 학력에 따라 기회의 편차가 존재하는가와 같은 보다 구조적인 질문을 제기하고자 한다.
</div>
""", unsafe_allow_html=True)


#시각화 1

# # 세션 상태 초기화
# if 'show_highschool' not in st.session_state:
#     st.session_state.show_highschool = False
# if 'show_college' not in st.session_state:
#     st.session_state.show_college = False

# # 컬럼 배치
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("대표적인 고졸 선수 🔽"):
#         st.session_state.show_highschool = not st.session_state.show_highschool

# with col2:
#     if st.button("대표적인 대졸 선수 🔽"):
#         st.session_state.show_college = not st.session_state.show_college

# # 이미지 출력
# col1, col2 = st.columns(2)

# with col1:
#     if st.session_state.show_highschool:
#         st.image("images/2_11.png", use_container_width=True)
#         st.image("images/2_12.png", use_container_width=True)
#         st.image("images/2_13.png", use_container_width=True)
#         st.image("images/2_14.png", use_container_width=True)
#         st.image("images/2_15.png", use_container_width=True)

# with col2:
#     if st.session_state.show_college:
#         st.image("images/2_21.png", use_container_width=True)
#         st.image("images/2_22.png", use_container_width=True)
#         st.image("images/2_23.png", use_container_width=True)
#         st.image("images/2_24.png", use_container_width=True)
#         st.image("images/2_25.png", use_container_width=True)


# 이미지 리스트
high_school_images = ["images/2_11.png", "images/2_12.png", "images/2_13.png", "images/2_14.png", "images/2_15.png"]
college_images = ["images/2_21.png", "images/2_22.png", "images/2_23.png", "images/2_24.png", "images/2_25.png"]

# 세션 상태 초기화
if "high_idx" not in st.session_state:
    st.session_state.high_idx = 0
if "college_idx" not in st.session_state:
    st.session_state.college_idx = 0

# 좌우 분할
col1, col2 = st.columns(2)

# 고졸 영역
with col1:
    #st.markdown("### 고졸 대표 선수")
    st.markdown("""
    <div style='
        font-family: "KBO Dia Gothic";
        font-size: 26px;
        font-weight: 700;
        text-align: center;
        line-height: 1.6;
        background-color: #08043c;
        padding: 12px 16px;
        border-radius: 8px;
        color:#ffffff ;
    '>
    고졸 대표 선수
    </div>
    """, unsafe_allow_html=True)

    # 버튼 클릭 즉시 인덱스 변경
    col_left, col_right = st.columns([1, 1])
    with col_left:
        if st.button("◀", key="high_prev"):
            st.session_state.high_idx = (st.session_state.high_idx - 1) % len(high_school_images)
    with col_right:
        if st.button("▶", key="high_next"):
            st.session_state.high_idx = (st.session_state.high_idx + 1) % len(high_school_images)

    # 이미지 및 현재 인덱스 표시
    st.image(high_school_images[st.session_state.high_idx], use_container_width=True)
    st.markdown(f"**({st.session_state.high_idx + 1} / {len(high_school_images)})**")

# 대졸 영역
with col2:
    #st.markdown("### 대졸 대표 선수")

    st.markdown("""
    <div style='
        font-family: "KBO Dia Gothic";
        font-size: 26px;
        font-weight: 700;
        text-align: center;
        line-height: 1.6;
        background-color: #08043c;
        padding: 12px 16px;
        border-radius: 8px;
        color:#ffffff ;
    '>
    대졸 대표 선수
    </div>
    """, unsafe_allow_html=True)

    # 버튼 클릭 즉시 인덱스 변경
    col_left, col_right = st.columns([1, 1])
    with col_left:
        if st.button("◀", key="college_prev"):
            st.session_state.college_idx = (st.session_state.college_idx - 1) % len(college_images)
    with col_right:
        if st.button("▶", key="college_next"):
            st.session_state.college_idx = (st.session_state.college_idx + 1) % len(college_images)

    # 이미지 및 현재 인덱스 표시
    st.image(college_images[st.session_state.college_idx], use_container_width=True)
    st.markdown(f"**({st.session_state.college_idx + 1} / {len(college_images)})**")

#st.write("다음으로 고졸 선수군과 대졸 선수군의 최근 WAR, 통산 WAR, 그리고 최근 시즌 연봉을 비교할 수 있다. 각 지표는 고졸/대졸 그룹별 평균값 또는 분포로 나타내어, 학력에 따라 나타나는 전반적인 경향을 시각적으로 보여준다. WAR은 선수의 경기 기여도를, 연봉은 시장에서의 평가 가치를 반영하는 지표로 활용되며, 두 지표를 함께 비교함으로써 학력에 따라 프로 진출 이후 성적을 조망할 수 있다.")

st.markdown("""
<div style='
    font-family: "KBO Dia Gothic";
    font-size: 18px;
    font-weight: 300;
    line-height: 1.8;
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 12px;
    color: #2C3E50;
    margin-top: 24px;
'>
다음으로 고졸 선수군과 대졸 선수군의 최근 WAR, 통산 WAR, 그리고 최근 시즌 연봉을 비교할 수 있다. 각 지표는 고졸/대졸 그룹별 평균값 또는 분포로 나타내어, 학력에 따라 나타나는 전반적인 경향을 시각적으로 보여준다. WAR은 선수의 경기 기여도를, 연봉은 시장에서의 평가 가치를 반영하는 지표로 활용되며, 두 지표를 함께 비교함으로써 학력에 따라 프로 진출 이후 성적을 조망할 수 있다.
</div>
""", unsafe_allow_html=True)


#시각화 2

# 데이터
labels = ['인원수', '베스트 WAR', '누적 WAR']
highschool = [49.00, 3.51, 13.86]
college = [13.00, 3.59, 11.95]
y = np.arange(len(labels))

# 스타일
color_hs = '#37bceb'
color_col = '#08043c'

# Figure 및 3개 Axes 생성
fig = plt.figure(figsize=(8, 4))
gs = fig.add_gridspec(nrows=1, ncols=3, width_ratios=[4, 0.8, 4])

# 고졸 그래프 (좌측)
ax1 = fig.add_subplot(gs[0])
ax1.barh(y, highschool, color=color_hs)
ax1.set(title='고졸')
ax1.set_xlim(60, 0)
ax1.set_yticks([])
ax1.tick_params(left=False)
for i, v in enumerate(highschool):
    ax1.text(v + 2, i, f'{v:.2f}', va='center', ha='right', fontsize=9, fontproperties=font_prop)

# 가운데 라벨 축
axc = fig.add_subplot(gs[1])
axc.set_xlim(0, 1)
axc.set_ylim(-0.5, 2.5)
axc.axis('off')  # 눈금 제거
for i, label in enumerate(labels):
    axc.text(0.5, i, label, ha='center', va='center', fontsize=10, fontproperties=font_prop)

# 대졸 그래프 (우측)
ax2 = fig.add_subplot(gs[2])
ax2.barh(y, college, color=color_col)
ax2.set(title='대졸')
ax2.set_xlim(0, 60)
ax2.set_yticks([])
ax2.tick_params(left=False)
for i, v in enumerate(college):
    ax2.text(v + 2, i, f'{v:.2f}', va='center', ha='left', fontsize=9, fontproperties=font_prop)

# 제목
fig.suptitle('고졸 vs 대졸 출신 학력 별 성적 비교', fontsize=13, fontproperties=font_prop)

fig.tight_layout()
st.pyplot(fig)


st.info(
"""
참고자료

기영노, 2021.04.19., 한국스포츠, 본격 ‘학력 파괴시대’ 열려, http://www.newsian.co.kr/news/articleView.html?idxno=48229

김윤일, 2019.08.28., 외면 받은 대졸 신인, 그렇다고 좌절 금지, https://www.dailian.co.kr/news/view/821165/?sc=naver

민경훈, 2022.08.25., ‘46%-> 16%’, 대졸 선수 외면 받는 신인 드래프트, https://isplus.com/article/view/isp202208250058

김은진, 2024.10.04., 110명 중 16명, 그 중 4년제는 6명… “대학야구 심각한 위기의식, 야구협-KBO 협력 촉구”, https://sports.khan.co.kr/article/202410041427003
"""
)

st.markdown("- - -")

#########################################
#st.header('투수 류현진 vs 타자 최형우! 드래프트에서 우선시되는 포지션은?')

st.markdown("### 투수 류현진 vs 타자 최형우! 드래프트에서 우선시되는 포지션은?")

st.write('''
야구 선수를 딱 두 범주로 나눠본다면, 투수와 타자로 나눌 수 있다. 공을 던지는 투수와 그 공을 치는 타자는 야구를 이루는 가장 본질적이고 핵심적인 요소이지만, 또 완전히 구별되는 특성을 지녔기 때문에 이 둘 사이의 비교는 언제나 흥미롭다. 그렇다면 과연 드래프트 과정에서, 그리고 이후 프로 무대에서 투수와 타자는 어떠한 차이가 있는지 알아보자.
         
우선 드래프트 과정에서의 투수와 타자를 비교해보기 위해 2016년부터 2020년까지 총 5년간의 드래프트 데이터를 분석해보았다. 5년 동안 드래프트를 통해 프로에 입단한 투수는 308명이고, 타자는 233명으로, 투수로 입단한 선수가 더 많았음을 확인할 수 있다. 
         
그렇다면 투수와 타자를 뽑는 우선 순위는 어떨까? 드래프트 1라운드부터 5라운드는 상위 라운드, 6라운드부터 그 이하 라운드들은 하위 라운드로 구분하여 프로 구단들이 투수와 타자를 뽑는 순서의 경향성을 분석해보았다.
''')

######################################### 시각화

# 제목
#st.subheader("상위/하위 라운드별 투수·야수 수")
st.markdown("#### 상위/하위 라운드별 투수·야수 수")

# 데이터 정의
labels = ['상위 라운드', '하위 라운드']
pitchers = [169, 140]
batters = [81, 150]

x = np.arange(len(labels))  # x축 라벨 위치
width = 0.35  # 막대 너비

# 그래프 생성
fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, pitchers, width, label='투수', color='skyblue')
bars2 = ax.bar(x + width/2, batters, width, label='야수', color='lightcoral')

# 텍스트 및 스타일 설정
ax.set_ylabel('선수 수',fontproperties=font_prop)
ax.set_title('상위/하위 라운드별 투수·야수 수',fontproperties=font_prop)
ax.set_xticks(x)
ax.set_xticklabels(labels,fontproperties=font_prop)
ax.legend()

# Streamlit에 출력
st.pyplot(fig)

st.write(' 그래프를 통해 알 수 있듯이 상위 라운드에는 확실히 투수들이 선호된다는 것을 확인할 수 있다. 5년간 상위 라운드에서 계약한 투수들은 169명, 타자들은 81명으로 두 배 이상의 차이를 보인다. 전체 드래프트에서 뽑히는 투수의 수가 타자보다 많다는 점을 감안하더라도, 오히려 하위 라운드에서는 타자의 비율이 더 높다는 점을 미루어보았을 때 투수 자원은 보다 상위 라운드에서 뽑는 경향이 있다는 것을 확인할 수 있다.')

st.write('''또한 이 기간 동안 뽑힌 1차 지명자의 비율을 확인해보면 이러한 경향은 더욱 두드러진다. 사실상 해당 연도 드래프트의 주인공이라고도 불리는 1차 지명자들은, 각 구단이 최우선으로 계약하고자 하는 이른바 특급 자원들이다. 하지만 조사한 기간 동안 투수 1차 지명자는 41명, 타자 1차 지명자는 9명으로 무려 4배 이상의 엄청난 차이를 보였다. 확실히 타자보다는 투수에 우선 순위를 두고 드래프트를 진행하는 것을 확인할 수 있다.
         
 그렇다면 이후 프로 무대에서도 이러한 경향이 이어질까? 이번에는 실제로 1군 무대에 데뷔하는 선수들의 비율을 살펴보았다. 조사한 기간 내에 데뷔한 투수는 186명으로, 전체 드래프트에서 선발된 투수 중 60.3%였다. 타자는 155명 데뷔하였고, 이는 전체 드래프트에서 선발된 타자 중 66.5%로 투수보다 높은 비율인 것을 확인할 수 있다. 즉, 드래프트 과정에서 선발된 선수들 중에는 투수가 확연히 높은 비중을 차지하지만, 실제로 1군 무대에 데뷔하는 선수들로만 한정했을 때 투수와 타자의 차이는 훨씬 줄어들었다는 것을 알 수 있다.
         
 또한 투수와 타자가 실제 1군 무대에 데뷔하기까지 걸리는 시간에서도 약간의 차이를 보였다. 실제로 2016년부터 2020년 사이에 드래프트로 선발된 선수가 1군 무대에 데뷔하기까지 투수는 1.01년, 타자는 1.09년 정도 걸렸고, 이는 결국 1군 무대에 적응하기에는 투수가 더 유리하다는 것을 의미한다. 실제 신인왕을 받는 횟수 역시 최근 10년간 투수 7번, 타자 3번으로 투수가 더욱 많았다는 점 역시 이러한 점과 무관하다고 볼 수는 없을 것이다. 즉, 처음 보는 1군 투수들의 공에 타이밍을 맞춰야 하는 타자보다, 우직하게 자기 공을 던질 수 있는 투수들이 초반에는 더 유리할 수 있음을 의미한다.
         
 이렇게 투수와 타자를 비교해보았지만, 이러한 비교에는 한계가 있다. 결국 투수와 타자는 훈련법부터 신경써야 하는 부분까지 전부 다르기 때문이다. 흔히 투수와 타자의 가치를 평가하는데 쓰이는 WAR을 구하는 방식 역시 완전히 다르기 때문에, 두 포지션의 선수들을 단순히 비교하는 것은 사실상 큰 의미가 없다. 본문에서는 드래프트와 그 직후의 과정에서 투수와 타자의 데이터가 어떻게 다른지를 알아본 것 뿐이고, 결국 이후의 프로 무대에서는 투수와 타자의 각 분야에서 어떻게 살아남느냐가 중요하다는 것이다.
''')


st.markdown("- - -")

#########################################

#st.header('문동주 픽한 한화 VS 김택연 픽한 두산! 결국 드래프트에서 웃은 팀은?')
st.markdown('### 문동주 픽한 한화 VS 김택연 픽한 두산! 결국 드래프트에서 웃은 팀은?')

#st.subheader('1. 계약금으로 뽕 뽑기 - 팀별 드래프트 투자 효율 순위는? ')
st.markdown('#### 1. 계약금으로 뽕 뽑기 - 팀별 드래프트 투자 효율 순위는?')

# st.markdown(
# """
# 1. 계약금으로 뽕 뽑기 - 팀별 드래프트 투자 효율 순위는?            
# """)

# 데이터 준비
data = {
    '팀': ['키움', 'LG', 'KT', '기아', 'NC', '삼성', 'SSG', '한화', '두산', '롯데'],
    '1억원 당 WAR': [2.3, 2.1, 1.85, 1.52, 1.3, 1.1, 1.1, 1.1, 0.95, 0.9]
}

team_info = {
    'LG': {
        'players': ['문성주', '홍창기', '문보경', '양석환'],
        'image': 'images/lg.png'
    },
    '롯데': {
        'players': ['배제성', '윤동희', '고승민', '황성빈'],
        'image': 'images/lotte.png'
    },
    '기아': {
        'players': ['김호령', '박찬호', '정해영', '김도영'],
        'image': 'images/kia.png'
    },
    '두산': {
        'players': ['최동현', '이병휘', '곽빈', '최승용'],
        'image': 'images/doosan.png'
    },
    '삼성': {
        'players': ['김지찬', '김현준', '박승규', '원태인'],
        'image': 'images/samsung.png'
    },
    '키움': {
        'players': ['김하성', '김혜성', '송성문', '이정후'],
        'image': 'images/kiwoom.png'
    },
    '한화': {
        'players': ['정은원', '김태연', '주현상', '노시환'],
        'image': 'images/hanwha.png'
    },
    'KT': {
        'players': ['박세웅', '박영현', '심우준', '엄상백'],
        'image': 'images/kt.png'
    },
    'NC': {
        'players': ['신민혁', '서호철', '구창모', '김영규'],
        'image': 'images/nc.png'
    },
    'SSG': {
        'players': ['박성한', '최지훈', '김동엽', '조병현'],
        'image': 'images/ssg.png'
    },
}

#st.subheader("KBO 팀별 드래프트 투자 효율 (통산 WAR / 억 원)")
st.markdown("#### KBO 팀별 드래프트 투자 효율 (통산 WAR / 억 원)")

# 데이터프레임 변환 및 정렬
df = pd.DataFrame(data)
df = df.sort_values(by='1억원 당 WAR', ascending=True)

# 막대그래프 출력
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['팀'], df['1억원 당 WAR'])
ax.set_xlabel('1억원 당 WAR',fontproperties=font_prop)
ax.set_title('KBO 팀별 드래프트 투자 효율',fontproperties=font_prop)
ax.set_yticklabels(df['팀'], fontproperties=font_prop)

st.pyplot(fig)

# 선택 박스 표시
#st.subheader("각 팀 투자 효율 Top 4")
st.markdown("#### 각 팀 투자 효율 Top 4")
selected_team = st.selectbox("팀을 선택하세요", df['팀'])

# 선수 정보 및 이미지 출력
if selected_team in team_info:
    st.image(team_info[selected_team]['image'], width=250)
    st.markdown("**주요 선수:** " + ", ".join(team_info[selected_team]['players']))

# # 그래프 출력
# st.plotly_chart(fig, use_container_width=True)

st.write('각 구단에서 선수를 지명할 때, 1라운드부터 11라운드까지 계약금을 차등 지급합니다. 이때 계약금이란 구단이 해당 선수의 가치를 합리적으로 판단하여 산정한 금액일 것입니다. 이 계약금을 일종의 투자금액이라 생각하면 어떤 구단이 가장 투자 효율이 좋은지를 알아볼 수 있습니다. 아마 모두의 예상대로 결과가 도출된 듯합니다.')

st.write('*선수의 주요 활동팀이 아닌 지명팀을 기준으로 산정하였습니다. 다른 팀으로 이적하여 활약하더라도, 결국 그 선수의 가치를 첫눈에 알아본 것은 지명팀의 능력입니다.')

st.write('*선수별 입단 연도가 달라도 통산 WAR을 기준으로 계산했습니다. 오랫동안 꾸준히 잘하는 선수는 팀을 먹여 살린 것과 같으니까요.')


# st.markdown(
# """
# 2. 드래프트의 묘미는 예측불가능성에 있다           
# """)

#st.subheader('2. 드래프트의 묘미는 예측불가능성에 있다 ')
st.markdown("#### 2. 드래프트의 묘미는 예측불가능성에 있다")

st.write('드래프트 지명 순위가 반드시 리그에서의 성공을 보장하지는 않습니다. LG의 문성주, 롯데의 배제성 선수처럼 하위라운드에 지명되어 폭풍성장을 겪은 선수들도 있습니다. 그럼 2014년부터 올해까지 가장 높은 투자 효율을 보여준 경우, 그리고 그 반대의 경우를 살펴 봅시다.')

st.title("KBO 드래프트 투자 효율 분석")
st.subheader("WAR 기준 상위 / 하위 10명")

# 상위 10명 데이터
top_df = pd.DataFrame({
    "이름": ["문성주", "배제성", "홍창기", "김하성", "김혜성", "송성문", "문보경", "박성한", "김호령", "박찬호"],
    "팀": ["LG", "롯데", "LG", "키움", "키움", "키움", "LG", "SSG", "기아", "기아"],
    "연도": [2018, 2016, 2016, 2014, 2015, 2015, 2019, 2017, 2015, 2014],
    "계약금 (억)": [0.3, 0.3, 0.8, 1.0, 1.3, 0.8, 0.3, 1.0, 0.7, 0.7],
    "통산 WAR": [12.6, 12.6, 30.8, 37.0, 32.5, 19.4, 19.1, 21.8, 20.6, 15.0]
})

# 하위 10명 데이터
bottom_df = pd.DataFrame({
    "이름": ["김주형", "정보근", "허관회", "노태형", "권민석", "백승민", "강동수", "황경태", "김한별", "조한민"],
    "팀": ["키움", "롯데", "한화", "한화", "두산", "삼성", "롯데", "두산", "NC", "한화"],
    "연도": [2019, 2018, 2019, 2014, 2018, 2017, 2016, 2016, 2020, 2019],
    "계약금 (억)": [0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.4],
    "통산 WAR": [-0.8, -1.0, -0.8, -0.7, -0.8, -0.7, -1.4, -2.6, -0.5, -0.7]
})


top_df.index = top_df.index + 1
bottom_df.index = bottom_df.index + 1

st.markdown("### 🥇 투자 효율 상위 10명")
st.dataframe(top_df, use_container_width=True)

st.markdown("### 🥵 투자 효율 하위 10명")
st.dataframe(bottom_df, use_container_width=True)


st.subheader('3. 우리 팀은 드래프트 전략을 잘 세우는가?')

st.write('선수들이 구단에 기여한 정도를 살펴 보았으니, 이제 구단별 신인 기용 능력을 알아봅시다.')

st.markdown("- - -")

# 제목
st.markdown("## 지난 12년간의 신인 드래프트에서")

# 양쪽 열로 분할
col1, col2 = st.columns(2)

# with col1:
#     st.markdown("### <div style='text-align: center;'>가장 많은 계약금을 지불한 팀</div>", unsafe_allow_html=True)
#     st.markdown("<div style='text-align: center;'><img src='images/kiwoom.png' width='180'></div>", unsafe_allow_html=True)
#     st.markdown("### <div style='text-align: center;'>약 87억 원</div>", unsafe_allow_html=True)

# with col2:
#     st.markdown("### <div style='text-align: center;'>가장 적은 계약금을 지불한 팀</div>", unsafe_allow_html=True)
#     st.markdown("<div style='text-align: center;'><img src='images/nc.png' width='180'></div>", unsafe_allow_html=True)
#     st.markdown("### <div style='text-align: center;'>약 61억 원</div>", unsafe_allow_html=True)

with col1:
    st.markdown("### 가장 많은 계약금을 지불한 팀", unsafe_allow_html=True)
    st.image("images/kiwoom.png", width=180)
    st.markdown("### 약 87억 원", unsafe_allow_html=True)

with col2:
    st.markdown("### 가장 적은 계약금을 지불한 팀", unsafe_allow_html=True)
    st.image("images/nc.png", width=180)
    st.markdown("### 약 61억 원", unsafe_allow_html=True)

st.subheader("KBO 팀별 드래프트 효율/비용 사분면 분석")

# 팀별 좌표 정의 (x: 비용, y: 효율)
teams = {
    "KT 위즈": (-1.3, 1.2),
    "LG 트윈스": (-1.3, 1),
    "NC 다이노스": (-1.3, 0.8),
    "키움 히어로즈": (0.7, 1),
    "두산 베어스": (0.7, -0.7),
    "삼성 라이온즈": (0.7, -0.9),
    "한화 이글스": (0.7, -1.1),
    "롯데 자이언츠": (0.7, -1.3),
    "SSG 랜더스": (-1.3, -1),
}

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 8))

# 축 그리기
ax.axhline(0, color='royalblue', linewidth=1)
ax.axvline(0, color='royalblue', linewidth=1)

# 화살표 그리기
ax.arrow(0, 0, 1.9, 0, head_width=0.1, head_length=0.1, fc='royalblue', ec='royalblue')
ax.arrow(0, 0, 0, 1.9, head_width=0.1, head_length=0.1, fc='royalblue', ec='royalblue')


ax.text(2.1, 0, "비용", va='center', ha='left', fontsize=12, fontproperties=font_prop)
ax.text(0, 2.1, "효율", va='bottom', ha='center', fontsize=12, fontproperties=font_prop)

# 팀 위치 마킹
for team, (x, y) in teams.items():
    ax.text(x, y, team, fontsize=11, fontproperties=font_prop)

# 스타일
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
ax.set_facecolor("white")
st.pyplot(fig)


# 제목 출력
st.subheader("📊 팀별 투자 효율 요약")

# 데이터프레임 생성
data = {
    "팀": ["KT", "LG", "NC", "SSG", "기아", "두산", "롯데", "삼성", "키움", "한화"],
    "총계약금": [70.6, 71.2, 61.6, 64.4, 70.3, 76.3, 78.8, 76.5, 87.0, 78.1],
    "총 WAR": [131.8, 148.4, 81.3, 76.9, 107.4, 71.9, 66.6, 91.5, 190.4, 86.3],
    "평균계약금": [1.04, 1.03, 0.91, 0.96, 1.03, 1.11, 1.16, 1.05, 1.14, 1.17],
    "평균 WAR": [1.94, 2.15, 1.20, 1.15, 1.58, 1.04, 0.98, 1.26, 2.51, 1.29],
    "분류": [
        "저비용 고효율", "저비용 고효율", "저비용 고효율", "저비용 저효율", "저비용 고효율",
        "고비용 저효율", "고비용 저효율", "고비용 저효율", "고비용 고효율", "고비용 저효율"
    ]
}

df = pd.DataFrame(data)

# 표 출력
st.dataframe(df, use_container_width=True)

st.markdown("- - -")

#########################################

st.header("결국 중요한 것은 예측을 불허하는 야구의 ‘낭만’")

st.image("images/4_1.png")
st.image("images/4_2.png")

st.write('휘문고, 북일고, 광주일고, 경남고… 매년 신인 드래프티 명단에는 익숙한 고등학교 출신의 선수들이 눈에 띄게 보였다. 유소년 시기부터 뛰어난 역량을 발휘한 선수가 명문고 야구부에 입학한다는 것을 고려하면, 좋은 인풋이 좋은 아웃풋을 만들어낸다고 볼 수 있다.')

st.write('한편으로는, 명문고라는 라벨이 드래프티로 선발되기 위한 밑거름이 될 수 있다. 야구와 같은 구기종목은 팀 전체의 역량이 승패를 좌우하는 경향이 크다. 따라서 좋은 학교에 입학할수록 좋은 기록을 얻을 확률이 더 높아진다. 특히 예선을 통과해야만 출전 자격이 주어지는 고교야구 메이저 대회의 경우, 선수 개인의 실력이 좋아도 충분한 이닝 수나 타석 수를 채우지 못해 진흙 속의 진주로 남아 있게 된다.')

st.write('그렇다고 해서 대학 야구도 같은 경향을 띠는 건 아니었다. 연세대와 고려대처럼 명문 야구부가 있는 학교로 알려져 있다 해도, 신인 드래프트에 선발될 가능성은 점점 희박해지고 있었다. 대학야구에서 중요한 것은, 학교의 네임밸류보다 선수의 기량이었다. 어느 스포츠에서든 신체나이가 중요하기에 대학 선수는 육성 단계를 최소화하고 바로 경기에 투입할 수 있는 즉시전력감으로 선발하는 경우가 대부분이다. 하지만 고교 선수와 대학 선수의 통산 WAR을 비교해보니 유의미한 차이가 있었다. 또, 얼리드래프트를 포함한 대학 선수 선발 추이는 꾸준히 감소하고 있다. 이에 한국야구학회 회장을 역임하고 있는 서울대학교 통계학과 장원철 교수는, ‘신인으로 선발되어도 1군 리그에서 게임을 뛰려면 엔트리에 자리가 나야 하는데, 한국 야구에는 나이가 들어도 실력을 유지하는 선수들이 많다는 것‘을 이유로 들었다. 즉, 대학 선수로서 신인 드래프트에 선발되려면 즉시 현역 엔트리에 등록될 정도의 기량을 갖추고 있어야 한다는 말이다.')


st.info(
"""
출처: SBS 뉴스 [정진구의 해피베이스볼] 야구특기생 입시를 둘러싼 오해와 진실

https://news.sbs.co.kr/news/endPage.do?news_id=N1003921630&plink=COPYPASTE&cooper=SBSNEWSEND
"""
)

st.image("images/4_3.png")

st.write("이처럼 선수들을 줄 세워 가격표를 붙이는 것이 마치 경매장의 모습을 보는 듯하지만, KBO의 신인 드래프트에서는 낙찰가가 평생의 가치를 보장하지는 않는다. 야구선수에게는 숫자로 드러나지 않는 무수한 가능성들이 기다리고 있기 때문이다.")

st.write("앞서, 상위라운드로 선발된 선수일수록 KBO 리그에서의 승리 기여도가 더 높을 수 있다는 점을 살펴 보았다. 다만 이는 경향성에 불과하다. 투자효율 상위, 하위 Top10을 떠올려 보자. 고교시절 날고 기던 선수가 입단 이후 끝내 데뷔하지 못하고 방출되기도 하며, ‘하위라운드의 반란‘으로 표현할 수 있는 폭풍성장형 선수들이 나타나기도 한다. 이처럼 선수들의 잠재력을 알아보는 것이 각팀 스카우터들에게 복잡한 과제로 남아 있다.")

st.write("하루에도 몇 번의 예측불허 경기를 만들어내는 대한민국 프로야구, 흥미로운 데이터 뒤에 숨은 제각각의 이야기들. 이것이 천만 관중의 비결이 아닐까 싶다.")


