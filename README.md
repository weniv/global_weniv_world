# weniv_world

* 실행 URL : https://weniv.github.io/weniv_world/
* 위니브 월드 레파지토리가 2개 있습니다. 스터디인 프로젝트가 이전 이름이 위니브 월드입니다. 이 프로젝트는 Python과 JavaScript를 실행하게 하는 교육용 서비스 제작 repo입니다.(우선 Python으로만 진행됩니다.)
* 남은 과업
   * 경현: 벽 구현
   * 유진: UI 구현
   * 호준: 스토리 작성, 스토리 마크다운 구현, 애러 해결, 주피터 노트북 업로드 구현, 월드 데이터 업로드 구현
   * 경림: 캐릭터 위, 아래 모습, 아이템, 스토리 이미지 작성
   * 나영: 내년 초 버전에서 번역
* threejs
   * 지도 화면 구성
   * 모델 불러오기
   * 모델 움직이기 (W 점프, E 이동, R 회전)
* 애러(아래 코드를 2번 실행했을 경우 맵을 벗어나지 않았음에도 벗어난다고 하는 애러)
   ```python
   move()
   turn_left()
   turn_left()
   turn_left()
   attack()
   move()
   ```
  - move 함수 내 오류

    - 0(동, 오른쪽), 1(북), 2(서, 왼쪽), 3(남)
    - directions = 0 일 때, 기존 x+1 이 아닌 y+1로 수정 
    - directions = 1 일 때, 기존 y-1 이 아닌 x-1로 수정 
    - directions = 2 일 때, 기존 x-1 이 아닌 y-1로 수정 
    - directions = 3 일 때, 기존 y+1 이 아닌 x+1로 수정