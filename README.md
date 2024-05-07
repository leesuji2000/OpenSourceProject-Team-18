## 데모링크

https://4fa1-211-117-79-45.ngrok-free.app/

## 사용설명

### 사용자
- 이 서비스는 어린이를 대상으로 한 영어 단어 암기 서비스 입니다.
- 외워야할 단어장이 있다는 전제하에 연상기억법을 제공함으로써 영어단어를 좀 더 기억에 남기 위한 도움을 주는 서비스입니다.


### 서비스 이용 방법
- 링크를 타고 들어가시면, **단어**와 **뜻**을 입력하는 창이 있습니다. 사용자가 외워야할 **단어**와 **뜻**을 입력하시면 됩니다.
  
  <img width="716" alt="Pasted Graphic" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/25ae8a51-033b-4a4f-864f-175898ae7b8b">

- 만일 **입력한 단어**가 DB에 있는 경우, DB에 저장되어 있는 연상기억법을 출력합니다.
- 만일 **입력한 단어**가 DB에 없는 경우, GPT가 입력한 단어와 뜻을 기반으로 연상기억법을 생성해줍니다.
- 아래는 apple 입력 예시입니다.
  
  <img width="814" alt="Pasted Graphic 1" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/fde82946-c50e-4b67-896a-715a68121e0b">
- 연상기억법이 출력된 후에 피드백을 남기실 수 있습니다.

  <img width="540" alt="• Not bad" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/d1558108-5242-46f2-a7fc-383f2609b365">

### 서비스 이용 참고사항
- 어린이를 대상으로 하는 영어단어 서비스이기 때문에, 어린어 영단어를 중심으로 DB를 구성하였습니다. 어린이 영단어에는 띄어쓰기가 필요 없기 때문에, 띄어쓰기가 포함된 입력은 알림을 통해서 제한하였습니다.

  <img width="436" alt="127 0 0 15000 내용" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/4157184f-4c27-40a1-b9b5-0685703132a3">

- 영어입력창과 한글입력창에 목적과 다른 단어를 입력하면 알림을 통하여 제한하였습니다. 아래는 뜻 입력창에 영어를 썼을때의 알림입니다.

  <img width="441" alt="127 0 0 15000 내용" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/5bc45e32-35bc-4cdc-837e-132dbf7e77df">

- 욕설을 적는 경우에는 gpt moderation을 이용하여 연상기억법을 제공하지 않도록 하였습니다.

  <img width="435" alt="Pasted Graphic 5" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/8e43625d-f5b7-405d-a25f-8125e52da2e4">

### 구현 계획
- 보다 기억하기 쉬운 연상기억법 DB 구축
- 신뢰가능한 moderation
- 영단어 오타에 대한 유사도 검증

