# 최초 설치후 docker permission denied 가 뜨면, /var/run/docker.sock 의 파일 소유자 확인하자
[Docker My Account](#개인정보)


[Docker Engine](#Docker-engine)

[Docker compose](#도커-컴포즈)



# Docker engine
- 사용 툴
    1. CLI : 도커가 기본적으로 제공하는 도커 엔진 접근 툴
    2. Kitematic : 도커사용을 위한 GUI TOOL
- 구성단위
    1. image : Base file , 컨테이너 생성하기 위한
        - 기억할 내용
            1. 이미지의 이름형식 : _이미지가저장된장소이름_(옵션,지정되지않으면DOCKER-HUB의공식이미지를의미)/_이미지이름_(필수,저장소에서IMAGE이름에맞는것을찾음):_TAG_(이미지의Tag에맞는것을찾음. 보통 버전을 의미, 명시되지 않으면 latest로 지정)
    2. container : image에서 복사한 것
        - 기억할 내용
            1. 이미지에서 변경된 사항만 저장. 컨테이너에서 조작한 것은 이미지에 무관
            2. 생성된 컨테이너는 "독립된" 공간임으로 컨테이너 자체가 시스템이 된다 (약간 virtual machine 같은 개념)

- 사용법
    [이미지생성](#이미지-생성)
    [컨테이너생성](#컨테이너-생성)
    [컨테이너나가기](#컨테이너-들어|나가기)
    [컨테이너정보확인하기](#컨테이너정보)
    [컨테이너삭제하기](#컨테이너삭제)
    ### 이미지 생성
        1. docker pull _image정보_ : 이미지를 내려받기
    ### 컨테이너 생성
        1. docker run -i -t _image정보_ : 실행완료시 이미지생성 - >컨테이너 생성 - >  컨테이너 내부로 이동 (shell 사용자와 호스트이름이 변경됨을 확인가능)
            - 컨테이너 기본 사용자 : root
            - 호스트 이름 : 무작위 16진수 해시값. 컨테이너의 고유 ID
            - "-i" : 상호 입출력 , 이게 없으면 shell을 정상적으로 사용 불능
            - "-t" : tty 활성 , bash shell 사용하도록 컨테이너를 설정 , 이게 없으면 shell을 정상적으로 사용 불능
            - mechanism
                1. docker pull (이미지가 없으면)
                2. docker create (이미지 기반 컨테이너 생성, 컨테이너 name이 자동생성 됨)
                3. docker start _컨테이너 name_ : 컨테이너 작동시작
                4. docker attach _컨테이너 name_ : -i -t 옵션이 들어갔을 때 자동으로 컨테이너에 들어가게 됨
        2. docker create -i -t --name _컨테이너이름_ _image정보_ : image정보에 맞는 컨테이너를 생성한다, 마찬가지로 저장소 없다면 docker hub에서 내려 받는다
            - "--name _컨테이너이름_ " : 컨테이너의 이름을 지정한다, 만약 지정하지 않으면 컨테이너 이름이 자동으로 생성되버린다\
            - mechanism
                1. docker pull
                2. docker create
    ### 컨테이너 들어|나가기
        - 들어가기
            1. docker start _컨테이너이름_ 또는 Container ID 2~3글자(docker ps -a 을 통해 찾기)
            2. docker attach _컨테이너 이름_ 또는 Container ID 2~3글자(docker ps -a 을 통해 찾기)
        - 나가기
            1. 동시에 컨테이너 정지시키기
                - exit 를 셸에 입력 , ctrl+d
            2. 컨테이너 셸에서만 나오고 컨테이너 작동은 지속하기
                - ctrl + p -> q
    ### 컨테이너정보
        - 컨테이너 정보 얻기
            1. 작동중인 것만
                - docker ps
            2. 모든 것
                - docker ps -a
            3. 원하는 정보만 얻기
                - docker ps --format "table {{.ID}}\n{{.Status}}\t{{.Image}}" : id,현재상태,밑바탕이미지 정보만 가져오기
            4. 컨테이너 정보 해석
                1. Container ID : 컨테이너에 자동 할당된 ID
                    - 전체 ID 확인 : docker inspect _container name_ | grep Id
                2. IMAGE : 컨테이너가 가져온 IMAGE 이름
                3. COMMAND : 컨테이너가 시작될 때 실행할 명령어. 대부분 이미지에 미리 내장되어 있음.
                4. NAMES : 컨테이너 고유 이름, 생성시 --name 옵션으로 지정하지 않으면 엔진이 무작위로 생성. 변경을 위해선 docker rename _컨테이너이름_ _바꿀이름_ 으로 변경해야함
            
        - 컨테이너 이름 변경
            - docker rename _컨테이너이름_ _바꿀이름_
    ### 컨테이너삭제
        - 주의
            1. 반드시 컨테이너는 stop된 상태여야 한다
        
        - 모든 컨테이너 제거하기
            - docker rm $(docker ps -aq) : 책에선 -a -q, docker ps -a -q 는 모든 컨테이너의 id를 출력시킴. 여기에 해당되는 컨테이너들을 다 삭제
        - 단일 삭제
            - docker rm _컨테이너 이름_
# 도커 컴포즈
- 용도
    1. 여러 container와 정의할 option command가 많을 때 사용