## `python` 가상환경 사용 방법 (vscode)

- vscode에서 터미널을 켠다

- 우선 가상환경을 만든다
  - python -m venv 가상환경이름
- 만들어진 가상환경에 접속한다
  - .\myenv\Scripts\activate
  - 가상 환경을 실행하면 (myenv) PS C:\~~ 이런 꼴로 바뀐다
  - 만약 `에러`가 난다면?
    - windows powershell을 관리자 권한으로 실행한다
    - Set-ExecutionPolicy RemoteSigned 명령어 실행
    - 실행 규칙 변경 여부를 물어보면 Y입력후 엔터
    - vscode로 돌아와서 .\myenv\Scripts\activate 다시 실행
- 여기서 pip list를 실행해보면 2개만 존재한다
- vscode 오른쪽 아래를 클릭해서 Select Interpreter창을 띄운다
- 내 가상환경에 해당하는 인터프리터를 선택해준다 ('myenv':venv)가 포함된 인터프리터
- 가상 환경에서 나가려면
  - 터미널에서 deactivate
  - 인터프리터도 원래로 바꿔주면 된다
- 현재 가상환경에 깔린 패키지 목록들을 파일로 저장하고 싶다면
  - pip freeze > requirements.txt

