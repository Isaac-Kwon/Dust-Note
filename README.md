# Dust-Note
Dust note with python, google gspread

## 필요사항

### 파이썬 인터프리터
* Python 3+

### 필요한 모듈
기본 설정의 파이썬 버전이 3.* 이하인 경우, 모듈을 설치할 때, pip 대신 pip3 를 활용하여야 한다.

If your default python version is lower than 3.*, maybe you have to use 'pip3' instead of 'pip'

* gspread
	* pip install gspread
* OAuth2
	* pip install --upgrade oauth2client

아래 모듈 또한 필요하나, Python 3.6.1 기준, 기본적으로 제공되는 모듈이다.

* json
* datetime



## How to use
기본 설정의 파이썬 버전이 3.* 이하인 경우, 프로그램을 실행할 때 'python' 대신 'python3' 를 활용하여야 한다.

If your default python version is lower than 3.*, maybe you have to use 'python3' instead of 'python'

### 설치

```bash
$ git clone https://github.com/PNU-HIPEx/Dust-Note.git
```

### 초기 설정
#### 구글에서의 설정
##### Autentification
<http://gspread.readthedocs.io/en/latest/oauth2.html>
에서, Using Signed Credentials 섹션에서 1 ~ 3 과정을 진행한다.

##### 스프레드시트
* Google Drive 에서, 새 스프레드시트 파일을 만들고 적절한 이름을 붙인다.
* 다운받은 JSON 파일을 메모장으로 연다.
* ``"client_id":`` 뒤에 표기된 이메일로, 스프레드시트를 공유한다.

#### 내부 설정용 JSON 파일 생성
```bash
$ cd Dust-Note
$ python configure.py
```
처음 프로그램을 사용하는 경우, 스프레드시트를 어떻게 구성할 지 프로그램을 설정하여야 한다.

실험실에서 일반적으로 사용하는 경우는 다음과 같다.

|                | Number |   | # | name   |
|----------------|--------|---|---|--------|
| Location       | 1      |   | 1 | Inside |
|                |        |   |   |        |
| Particle Types | 3      |   | 1 | 0.1    |
|                |        |   | 2 | 0.3    |
|                |        |   | 3 | 5.0    |
|                |        |   |   |        |
| Data Types     | 1      |   | 1 | SUM    |

SpreadSheet Name 은 앞의 과정에서 공유했던 스프레드시트 파일의 이름을 입력한다.

설정 환경이 바뀔때마다 (스프레드시트의 이름, 기록 요소 등) 설정 JSON 파일을 만들어주어야 한다. 이는 ```configure``` 스크립트를 실행하면 된다.

기존에 만들어진 동일한 형식의 ```cfg.json``` 가 있을 경우 내부 파일을 읽어 이전 상태를 보여준 후 설정을 진행하며, 변동사항이 없는 항목은 변경을 생략할 수 있다. (스크립트를 실행할 때 안내된다.)



### 사용 방법
#### 단순 업로드 스크립트
```bash
$ cd Dust-Note
$ python main.py timestamp Data1 Data2 Data3 Data4 ...
```
단순 업로드 스크립트는 위와 같은 입력 변수 양식을 가진다.

입력 변수 양식은, TimeStamp 의 위치를 제외하고는 Configure 파일에서 설정한 방식에 따라 달라지는데, 아래와 같은 커맨드로 어떤 양식으로 입력하는지를 알 수 있다.

```bash
$ cd Dust-Note
$ python main.py -h
OR
$ python main.py --help
```

위와 같은 --help 커맨드를 입력하였을 때, 다음과 같은 입력변수에 대한 안내를 볼 수 있다.

```bash
$ python main.py --help
python main.py timestamp(0 or YYYY/MM/DD-HH:MM) LocationNumber SUMof0.1um SUMof0.3um SUMof5.0um

location numbers
1: Inside
2: Outside
3: Buffer
```


#### 대화형 스크립트
```bash
$ cd Dust-Note
$ python main_interactive.py
```

대화형 프로그램은, 단순 업로드 프로그램에서의 각각의 변수를 순서대로 입력할 수 있도록 한 스크립트이며, 실행하였을 때, 다음과 같은 안내를 볼 수 있다.

```
===================================
Dust Monitoring Data Sending Script
date?
(blank if realtime)
Year:
```
데이터의 연도를 입력하며, 입력하지 않고 Return 키를 누를 경우 현재 시각이 자동으로 입력된다. (표기는 Microseconds 까지 되나, 실제 데이터는 분단위까지 입력된다.)

이후는 스크립트가 제시해주는대로 데이터를 입력하면 단순 업로드 스크립트의 경우와 동일하게 업로드가 진행된다.
