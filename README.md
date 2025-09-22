# cra_250922
Code Review Agent 공통과제 - 2025 10차

# 요구사항 체크 리스트
## D1 o
- 함수 레벨 리팩토링
## D2 o
- Regression Test를 위한 Unit Test 개발
- <img width="1051" height="372" alt="image" src="https://github.com/user-attachments/assets/fb3a4db1-db85-4d80-9142-7a8502b67629" />
- mission2/test 하위 테스트 스크립트 작성 (pytest)
## D3 o
- 확장성을 고려한 설계, 정책과 등급이 추가되더라도 Client Code에 변경이 없도록 한다.
- Player 등급별 심플팩토리패턴을 적용하여 등급 변경 시 클래스를 추가/변경하여 등급별 Player 객체를 다룰 수 있다.
## D4 o
- 리팩토링에 디자인 패턴을 적용한다.
- PlayerManager 클래스를 싱글턴으로 만들어 ID 생성 시 오류가 없도록 작성
- D3 와 동일하게 심플팩토리패턴을 적용한 항목
## D5 o
- 리팩토링이 끝난 코드에, 코드 커버리지가 100% 되어야 한다.
<img width="1013" height="869" alt="image" src="https://github.com/user-attachments/assets/da7cf19e-8682-4d7e-9284-8bed3d3106c9" />


# env
```
py -3.12 -m venv venv
venv\Scripts\activate

python.exe -m pip install --upgrade pip
pip install pytest
```
