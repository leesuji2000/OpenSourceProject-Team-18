## 데모 링크:
 link 적어주세요

## 최종 발표 자료 링크:
[https://youtu.be/-VfLoHE5HW8?si=UfoGIWWr3TbAz9Vo]
 
## 주요 특징
어린이에게 영단어 암기법을 제공하는 서비스입니다. 
사용자가 입력한 영단어가 어린이에게 적합한 단어인 지 확인하고 적절한 프롬프트를 활용하여 암기법을 제공합니다.

### 1. 상황별 다른 프롬프트 생성
1. 사용자 입력 단어에 접두사가 있는 경우
<img width="1695" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/163505867/877e5039-cb87-4140-9c2c-aa29743300dc">
   (1) 해당하는 접두사를 활용하여 영단어 암기법을 추천합니다.
   #
<img width="1647" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/163505867/ba29ca56-802a-4345-84ec-03390f91d1c0">

   (2) 사진과 같이 un- 접두사가 사용되었지만 뜻을 사용하지 않는 경우는 DB에 따로 저장하여 관리합니다.

3. 사용자가 입력한 단어와 비슷한 철자의 단어가 교과서DB에 존재하는 경우
<img width="1647" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/163505867/2015fbff-3a45-4e4b-9c8e-bd443ce54507">



   - 교과서에서 어떤 단어를 사용하였는 지 명시해줍니다.
   - 교과서에서 찾은 단어를 활용하여 연상암기법을 설명합니다.
   - 설명한 내용을 토대로 쉬운 영어 예문을 작성합니다.
   - 예문에 사용된 두 단어는 볼딩처리해서 뚜렷하게 만들었습니다.
  

4. 두 케이스 모두 아닌 경우 (일반적인 경우)
<img width="1647" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/163505867/d51bc42d-27e3-42c2-a410-1b36c314406a">

   gpt를 통해 암기법을 추천받고, 추천한 암기법을 활용하여 답변을 제공합니다.

### 2. 모더레이션 강화
1. 입력단어와 출력결과에 대한 필터링
   1. 입력한 단어가 자주 사용되는 욕인 경우 : 정규표현을 통한 필터링
   2. 입력한 단어가 모더레이션 조건을 통과하지 못하는 경우 :
      (교과서DB 영어 욕DB에 맞춰 모더레이션 임계치 조정 완료)
   3. 두 조건 모두 충족하지만 부적절한 단어인 경우 : 프롬프트 단에서 답변 거부
      (필터링 결과는 아래에서 확인 가능)

2. 예시사진
- 아래 사진은 fuck (자주 사용하는 욕설)을 입력한 결과 뜨는 팝업창입니다.
<img width="471" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/163505867/f6305b63-1027-4db7-8e3d-45faa980aa2f">



- 아래 사진은 흑인비하 발언 niggar를 입력하였을때, 모더레이션을 이용하여 필터링된 팝업창입니다.
<img width="471" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/163505867/e1fc70a8-eaca-461c-a1d6-3c20717ec444">


- 아래 사진은 출력된 결과에 욕설이 있는 경우 프롬프트에서 답변을 거부한 결과입니다.
<img width="1647" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/163505867/a78e6312-0dad-426a-bc55-046db0a9684f">




 
## 사용 설명

### 사용자
- 이 서비스는 어린이를 대상으로 한 영어 단어 암기 서비스 입니다.
- 외워야할 단어장이 있다는 전제하에 연상기억법을 제공함으로써 영어단어를 좀 더 기억에 남기 위한 도움을 주는 서비스입니다.


### 서비스 이용 방법
1. 첫페이지: 단어 입력창
- 링크를 타고 들어가시면, **단어**를 입력하는 창이 있습니다. 사용자가 외워야할 **단어**를 입력하시면 됩니다.
- 아래는 review 입력 예시입니다.
  
  <img width="422" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/0ee98540-8bbc-4371-a71e-4b82abc62282">

 2. 단어 뜻 페이지: 원하는 단어 뜻 선택
- 입력한 단어에 따라서 사전 크롤링을 통해서 가져온 단어의 뜻이 출력됩니다.
- 외우고 싶은 단어를 선택합니다.
- 아래는 review를 입력했을떄, 나오는 단어의 뜻입니다.

  <img width="262" alt="image" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/54c8cf86-f662-43f3-adab-460e91bb5e21">


 3. 연상 기억법 및 암기법 출력 페이지: 단어별로 다른 프롬프트 적용
- 만일 **입력한 단어와 뜻**이 DB에 있는 경우, DB에 저장되어 있는 연상기억법을 출력합니다.
- 만일 **입력한 단어**가 DB에 없는 경우, GPT가 입력한 단어와 뜻을 기반으로 연상기억법을 생성해줍니다.
- 아래는 review 단어의 복습 뜻을 눌렀을때 출력된 결과입니다.

  ![image](https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/9d529f10-dcb1-4c94-b881-5d006e4c42d1)

- 단어에 따라서 다른 프롬프팅이 적용되며 그에 대한 내용은 위의 주요 특징에서 설명드렸으니 참고하시길 바랍니다.
- 페이지 하단에서 텍스트를 이용하여 피드백을 남기실 수도 있습니다.
  

### 서비스 이용 참고사항
- 어린이를 대상으로 하는 영어단어 서비스이기 때문에, 어린어 영단어를 중심으로 DB를 구성하였습니다. 어린이 영단어에는 띄어쓰기가 필요 없기 때문에, 띄어쓰기가 포함된 입력은 알림을 통해서 제한하였습니다.

  <img width="436" alt="127 0 0 15000 내용" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/4157184f-4c27-40a1-b9b5-0685703132a3">

- 영어입력창과 한글입력창에 목적과 다른 단어를 입력하면 알림을 통하여 제한하였습니다. 아래는 뜻 입력창에 영어를 썼을때의 알림입니다.

  <img width="436" alt="127 0 0 15000 내용" src="https://github.com/leesuji2000/OpenSourceProject-Team-18/assets/64798587/5bc45e32-35bc-4cdc-837e-132dbf7e77df">





