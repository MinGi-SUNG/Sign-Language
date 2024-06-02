# 딥러닝 기반 양방향 수어 번역 시스템
농인과 청인 간의 실시간 소통을 위해 양방향 번역 서비스를 제공하는 수어 번역 애플리케이션을 개발
<br>

## 🖥️ 프로젝트 목표
농인과 청인 사이의 원활한 의사소통을 위한 수어 번역 애플리케이션 개발 프로젝트로 
현재 존재하는 단방향 수어 번역 애플리케이션과 달리 양방향 번역 서비스를 제공
<br>

## 🖥️ 프로젝트 내용
‘사회적 약자를 위한 애플리케이션을 개발해보면 어떨까?’하고 브레인스토밍을 통하여 회의를 하던 중 농인과 청인 사이의 원활한 의사소통을 위해 필요하다고 생각되는 양방향 수어 번역 시스템을 개발하기로 결정하였다. 문제 관련 정보 수집 을 통해 시중에 출시되어 있는 애플리케이션들과의 차별성에 대해 살펴보았다. 시 중의 애플리케이션들은 수어에서 한국어로 번역을 해주거나 한국어에서 수어로 번 역을 해주는 단방향 번역 서비스만을 제공하였다. 우리가 개발한 애플리케이션은 양방향 번역 서비스를 제공한다는 점에서 차별성이 있다고 판단된다. 애플리케이션 의 주요 기능은 다음과 같다. 애플리케이션에서 청인이 음성을 입력하게 되면 번역 시스템에서 음성을 텍스트로 변환 후 텍스트를 기반으로 아바타가 수어를 보여준 다. 또한 반대로 수어를 카메라에 입력하면 수어를 인식하고 음성으로 변환하여 번 역 결과를 나타낸다. 이 프로젝트에서 사용한 기술은 딥러닝 기술인 LSTM과, Blender 아바타, STT, 안드로이드 스튜디오와 AI HUB 데이터 셋인 한국 수어를 사용하였다.
<br>

## 🕰️ 개발 기간
* 23.03.09일 - 23.06.22일
  
### 🧑‍🤝‍🧑 맴버구성
 - 이재현 : 프로젝트 총괄, 서버 개발 및 관리, 웹 연동
 - 박지수 : 애플리케이션 개발, STT API 연동, 수어 데이터 관리
 - 성민기 : AI 모델 학습, 데이터 수집 및 전처리, 웹 연동
 - 정세연 : 자연어 처리, 아바타 모델링, 수어 애니메이션 생성

### ⚙️ 개발 환경
- **Language** : Python, Java
- **AI 모델 개발 및 아바타** : MediaPipe, TensorFlow, OpenCV, Blender
- **서버구축** : AWS EC2, AWS S3, Nginx, Flask
- **개발도구** : Pycharm, Blender, Android Studio
  
## 📌 주요 기능

### 시스템 구성도
<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/73b1529c-2fdc-448c-b169-d409346c614b" height="70%" width="70%">

### 기능 설명
<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/54313ac0-7e28-4573-a592-17d6d8449d66" height="70%" width="70%">
<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/3bf4a2f0-db81-4916-b248-fb2339123edc" height="70%" width="70%">

### AI 모델 (LSTM)
- 장단기 기억 모델 LSTM 사용
- 수어 공공데이터에서 Mediapipe holistic을 활용하여 키포인트 추출 및 한 단어당 100개의 데이터 저장
- AI 모델 인식률 및 결과 추출
<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/16d7bc49-6c5f-4a0d-af3d-39da4c6d7ec3" height="70%" width="70%">
<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/dffa1aa0-03b9-4345-ad8a-f9abaac8278c" height="70%" width="70%">

### 수어 애니메이션 생성
- Mediapipe holistic을 활용하여 키포인트 추출
- 아바타 모델에 키 포인트 대입
- Blender를 활용하여 수어 번역 애니메이션 캐릭터 생성

### 수어 특징 분석
- 한국 수어의 특징 : 수어는 조사와 어미가 존재X (ex, 문제가 너무 어려웠다 -> 문제 + 너무 + 어렵다)
- 수어 문장 변환
    - 형태소 분석 후 불필요한 품사 제거
    - 분류된 단어들과 수어 아바타를 매핑 후 각 단어에 해당하는 아바타의 행동을 한 영상으로 병합

### 애플리케이션 개발
<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/bafa2619-1e9f-430b-9b0a-0861b75e15a3" height="70%" width="70%">

## 📃 논문 📃
딥러닝 기반 양방향 수어 번역 시스템(Two-Way Sign Language Translation System Based on Deep Learning)

- https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11485611<br>


## 🏆 프로젝트 결과 정리 🏆
<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/538e69d9-d3e5-4b2d-b881-d632b2e02ee1" height="30%" width="30%">

<img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/a881a164-c131-488e-94ac-094ee93beb1d" height="32.2%" width="32.2%"><img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/80faf63e-55f2-4315-86d3-bc635c7fa0e7" height="32.2%" width="32.2%"><img src="https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/761f948b-1937-4c90-aab9-3008d1823a7b" height="32.2%" width="32.2%">






<!-- # Sign-Language
![d3test3(0515_20h54m)](https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/f814a961-1410-4de6-9322-e4226652f1e9)
![d3test3_loss(0515_20h54m)](https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/c9826382-27ca-4323-8ddc-51a909a41ae1)
![d3test3_matrix(0515_20h54m)](https://github.com/MinGi-SUNG/Sign-Language/assets/89721794/985513a1-9ebd-4f99-9a56-3cdd275fed93) -->
