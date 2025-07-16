# 🏧 ATM Controller

이 프로젝트는 카드 삽입부터 PIN 인증, 계좌 선택, 잔액 조회/입금/출금까지의 ATM 내부 로직을 구현한 컨트롤러입니다.  
UI나 네트워크는 포함하지 않고, 순수한 비즈니스 로직만 포함되어 있습니다.

---

## 📁 프로젝트 구조

atm-controller/
├── atm/
│ ├── controller.py # ATMController 클래스 (핵심 로직)
│ └──  models.py # Card, Account 모델 클래스
├── tests/
│ └── test_controller.py # 단위 테스트
├── main.py # 흐름을 직접 실행해볼 수 있는 예제
├── README.md
└── venv/ # 가상환경

---

## 🚀 실행 방법

### 1. 가상환경 설정 (최초 1회)
python -m venv venv
source venv/Scripts/activate   # Windows(Git Bash)

### 2. 테스트 실행(tests/test_controller.py 에서 단위 테스트를 확인할 수 있습니다.)
python -m unittest discover tests

### 3. 직접 실행 예제(ATM 흐름을 콘솔에서 따라가면서 테스트할 수 있습니다.)
python main.py

## 🧪 포함된 테스트
- 카드 삽입 및 PIN 인증
- 계좌 선택 후 입금 / 출금 / 잔액 확인
- 인증 실패, 잔액 부족, 계좌 미존재 등 예외 처리

## 📌 주의사항
본 코드는 실제 은행 시스템이나 ATM 하드웨어와는 연동되어 있지 않습니다.
향후 REST API 또는 UI와 통합 가능한 구조로 설계되었습니다.