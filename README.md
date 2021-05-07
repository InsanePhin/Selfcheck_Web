# Selfcheck_Web

html flask 공부를 목적으로 만들어졌으며 개발자 사정?으로 인해 오픈소스로 전환하였습니다.

### 시작하게된 동기

> 학교를 다니면서 자가진단을 직접 하기에 너무 귀찮고 짜증이 나서 form 공부를 할겸 만들어봤습니다.

### 주의사항

> 해당 코드는 `학생정보등록`을 위한 코드이며, 자가진단 자동화를 위해서는 코드를 작성하셔야합니다. (조만간 자동화 코드를 올리겠습니다.)

### 작동 원리

1. 학생정보 입력
2. 테스트 자가진단을 통해 학생정보 확인(hcskr 모듈 사용)
3. mysql서버에 입력받은 데이터를 저장
4. 결과 페이지로 이동

### 테스트환경 및 필수 모듈

> 테스트서버에서는 `Apache2`, `wsgi`를 이용하여 호스팅하였습니다. 아파치를 사용하실 예정이라면 (selfcheck.wsgi)[https://github.com/InsanePhin/selfcheck_web/selfcheck.wsgi] 파일에 경로를 설정해주세요.

```
Python 3.8.9 64-bit ("WindowsApps")

pip==21.1
flask==1.1.2
pymysql==0.10.1
hcskr==1.9.2
```

### 사용법

> 개인정보약관을 수정한 후 사용해주시면 감사하겠습니다.

> mysql table 구조
```sql
name, birth, region, school, schooltype, password
```

```
$ pip install -r requirements.txt
$ python garage.py
```
