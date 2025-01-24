### 6차시 실습

- 이번 실습에서는 postgres를 파이썬에 연결하는 방법에 대한 실습을 진행합니다.
- 실습파일은 [postgres-python.pdf](./postgres-python.pdf) 입니다.

- 실습에 사용되는 예제 파일들은 pg-python 폴더에 업로드 해놨습니다.

#### 실행 방법
1. 로컬 환경에서 파이썬을 실행할 수 있는 ide 를 실행합니다. (e.g. visual studio code, pycharm)
2. postgres가 실행되고 있는지 확인합니다. (mac에서는 postgres application 실행 시 "Running" 표시가 떠있으면 정상 동작 상태입니다. 윈도우에서는 작업관리자에서 postgres가 실행중인지 확인하시면 됩니다.)
3. ide에서 [pg-python](./pg-python) directory 내에 있는 파일들을 복사/붙여넣기하여 생성합니다. 
4. 각 파일안에서 postgres 연결 설정을 확인합니다. (만약 postgres 초기 설정 시, 포트 번호나 비밀번호를 바꾸셨다면 connection 정보에 바꾸신 값을 입력합니다.)
5. ide 터미널 창에서 `python <파일명>`을 입력하여 실행합니다.
