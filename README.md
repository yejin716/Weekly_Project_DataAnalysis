## Airbnb 리뷰데이터 분석을 통한 좋은 숙소의 조건 분석 - 파리/런던의 고객 만족도 결정 요인 분석을 중심으로

> 포스트 코로나 시대의 새로운 트렌드와 수요가 증가로 호텔보다는 에어비앤비와 같은 숙박 업체를 이용하는 비율이 증가. 따라서 기존 호스트 및 예비 호스트에게 새로운 트렌드에 맞춘 좋은 숙소의 기준을 제공하고자 함

### 데이터 수집 
- 올리브영 **스킨케어 제품** (스킨, 로션, 크림, 미스트, 에센스) 화장품 정보(이름, 브랜드, 가격, 성분, 사진, 링크, 리뷰) 크롤링
- AIhub 한국인 피부상태 측정 데이터 <https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71645>
### NLP 
- 리뷰 데이터 전처리, EDA, 감성분석 진행

### 이미지 처리 
- Yolov5를 이용한 얼굴 7가지 부위별 탐지 학습 (전이학습)
  - 이미지 데이터 + 라벨링 데이터(class, bbox)
- Resnet50, Densenet201 + VGG19 (Ensemble model)를 이용한 이미지 분류
  - 피부과 전문의가 분류한 등급 라벨링 데이터 + 이미지 데이터 전이학습

### LLM을 이용한 챗봇 구현 
1. VectorDB (chromadb) 이용 - 화장품 정보, 리뷰 데이터 
2. LLM 모델 (gpt-4o-mini)
3. agent

- 전이학습한 yolo와 Ensemble model 연결하여 결과값 (관리 필요 유무) - json 파일
- json 파일 결과 - LLM에게 전달 - 답변 생성

### Streamlit 구현 
- 챗봇 개발
- sidebar + navigation 활용
- 이미지 분석 후 추천 관리 제공 + 기본 채팅 구성
  - session_state를 통해 기존 내용 history에 담아서 구성 
