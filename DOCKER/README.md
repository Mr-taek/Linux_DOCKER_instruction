# 최초 설치후 docker permission denied 가 뜨면, /var/run/docker.sock 의 파일 소유자 확인하자

[Docker의 용도](#What-is-docker)

[Docker 설치](#Install)

[Docker My Account](#개인정보)

[Docker Engine, Docker의 기본이자 모든 것](#Docker-engine)

[Docker Network 연결및 다루기](#docker-network)

[Docker compose](#도커-컴포즈)


# What is docker
- Go 언어로 개발된 '여러 개발환경'을 성능 손실 없이 줄이기 위한 툴
 - 한 호스트 아래 여러 개의 운영체제는 가상머신 단위로 불리며, 우분투/CentOs 등이 존재함
 - 'Hypervisor', 호스트와 가상머신간 소통하기 위한 중간 단계. Hypervisor에의해 생성/관리되는 것을 Guest 운영체제라 함
 - 여러 Guest os는 다른 게스트 os와 완전히 독립된 공간과 시스템 자원을 할당받음 (Vmware)
 - 가상머신은 또 guest os를 사용하기 위한 라이브러리, 커널 등을 전부 포함해서 크기가 큼. 다만, 완벽한 운영체제를 생성할 수 있다는 장점이 있고 성능손실이 있음
- Docker는 '프로세스 단위'의 환경을 만듦. 필요한 커널은 호스트의 커널을 사용하고 사용하는 애플리케이션의 라이브러리 및 실행 파일만이 존재함. 즉 크기가 작아짐
 - 이는 배포시간이 가상머신에 비해 빠르고 가상화된 공간에서의 성능 손실도 거의 없음

- Docker는 어떻게 쓰나
    1. 호스트os는 일반적으로 서버를 부팅할때 실행되는 운영체제를 의미하며
    2. docker의 컨테이너, 즉 docker의 가상 머신은 호스트 os 바로 다음 단계에 실행이 됨
    3. 컨테이너에 어떤 소프트웨어를 설치하고 설정 파일을 수정해도 호스트 os에는 영향이 안 감.
    4. 컨테이너에서 작업을 마치고 실질적인 운영환경에 배포할 때 컨테이너를 docker image를 로 만들어서 서버에 전달하면 됨.

# Install
- install website : https://docs.docker.com/engine/install/ubuntu/
- steps
    1. 위 웹사이트에서 차근 차근 따라가면됨
    2. 본인은 Ubuntu 20.04(LTS)를 사용했음
    3. give perbission to use docker for a user , sudo usermod -a -G docker $USER
# Docker engine
- 사용 툴
    1. CLI : command line interface, 도커가 기본적으로 제공하는 도커 엔진 접근 툴
    2. Kitematic : 도커사용을 위한 GUI TOOL
- 구성단위
    1. image : Base file , 컨테이너 생성하기 위한
        - 기억할 내용
            1. 이미지의 이름형식 : _이미지가저장된장소이름_(옵션,지정되지않으면DOCKER-HUB의공식이미지를의미)/_이미지이름_(필수,저장소에서IMAGE이름에맞는것을찾음):_TAG_(이미지의Tag에맞는것을찾음. 보통 버전을 의미, 명시되지 않으면 latest로 지정)
            - e.g  : docker run -i -t ubuntu:18.04 , 만약 우분투의 18.04 버전이 local에 없으면 자동으로 docker 홈페이지 docker hub서 다운받으러 감
                - local에 없는경우 나오는 Text
                    ```
                    Unalble to find image "ubuntu:18.02" locally
                    ```
    2. container : image에서 복사한 것
        - 기억할 내용
            1. 이미지에서 변경된 사항만 저장. 컨테이너에서 조작한 것은 이미지에 무관
            2. 생성된 컨테이너는 "독립된" 공간임으로 컨테이너 자체가 시스템이 된다 (약간 virtual machine 같은 개념)

- 사용법
    [이미지생성](#이미지-생성)
    [컨테이너생성](#컨테이너-생성)
    [생성된컨테이너작동법 참고](#생성된컨테이너작동-foreground-backgrond|생성된컨테이너config변경)
    [컨테이너 외부 상호작용 허용하기](#컨테이너-외부노출)
    [컨테이너나가기](#컨테이너-들어|나가기)
    [컨테이너정보확인하기](#컨테이너정보)
    [컨테이너삭제하기](#컨테이너삭제)
    [명령어들](#명령어)
    ### 이미지 생성
        - 기본설명
            - 이미지 : 도커는 local에 없는 이미지를 도커의 중앙 이미지 저장소인 도커 허브(Docker Hub)에서 이미지를 내려받음.
            - 도커 이미지 검색하기
                1. docker search ubuntu : 도커 허브사이트에서 ubuntu와 관련된 이미지를 보여줌
                    - starts 피쳐 : 해당 name의 이미지가 도커 사용자로부터 얼마나 즐겨찾기(star)됐는 지를 나타냄.
                2. docker search docker.io/ubuntu : 도커 허브의 이미지를 명시하기위해 docker.io/ 를 사용할 수 도 있으나 , 없으면 자동으로 docker hub의 이미지로 인식함
            - 도커 이미지의 이해
                1. 어떤 이미지를 바탕으로 컨테이너를 만들고 또 그 컨테이너로 이미지를 만들면 Layer 항목이 증가한다.
                2. 이 Layer는 일종에 이미지의 역사를 기록한 것이며, 최종적으로 만들어낸 이미지의 크기는 최초이미지의 용량+생성된 데이터들의 총용량 이다.
                3. 이미지를 사용하고 있는 컨테이너가 존재한다면, 이미지는 삭제가 불가능하다. 이미지를 사용했던 컨테이너를 모두 삭제해야 이미지도 삭제할 수 있다.
        1. docker pull _image정보_ : 이미지를 내려받기
        2. docker images : 현재 내 docker에 저장되어 있는 image들 보기.
        3. docker history 저장소이름:태그 : 해당 저장소이름:태그 이미지가 어떤 레이어로 구성되어 있는지를 볼 수 있음
        4. docker rmi 저장소이름:태그 : 해당 이미지를 삭제함

        - 컨테이너를 이미지로 만들기
            - docker commit _option_ _컨테이너 이름_ _생성될 이미지의 저장소이름_:_이미지태그이름_
                - option
                    - -a : author란 뜻, 이미지 작성자의 meta data를 이미지에 포함시킴. 
                        - e.g) docker commit -a "imtek" , 이미지 작성자 데이터는 "imtek" 으로 설정
                    - -m : commit message, 이미지에 포함될 부가 설명
                        - e.g) docker commit -m "Hello world"
                - 컨테이너 이름 : 생성한 컨테이너의 이름, e.g) docker create --name myubuntu , docker commit -a myubuntu
                - _생성될 이미지의 저장소이름_:_이미지태그이름_ : 저장소이름:latest(디폴트이름) , 저장소의 태그 이름을 지정하지않으면 latest로 설정됨
        - 이미지 삭제하기
            - 설명
                1. 하위 이미지가 존재하는 상위 이미지를 삭제하면 이미지는 실제로 삭제되지 않고 저장소이름:태그 만 삭제된다.
                
    ### 컨테이너 생성
        1. [기본사용법]docker run -i -t _image정보_ : 실행완료시 이미지생성 - >컨테이너 생성 - >  컨테이너 내부로 이동 (shell 사용자와 호스트이름이 변경됨을 확인가능)
            - docker run -it _image정보_ , 처럼 사용이 가능
            - 컨테이너 기본 사용자 : root
            - 호스트 이름 : 무작위 16진수 해시값. 컨테이너의 고유 ID
            - "-i" : 상호 입출력 , 이게 없으면 shell을 정상적으로 사용 불능
            - "-t" : tty 활성 , bash shell 사용하도록 컨테이너를 설정 , 이게 없으면 shell을 정상적으로 사용 불능
            - -i -t 가 없으면 
            - mechanism
                1. docker pull (이미지가 없으면)
                2. docker create (이미지 기반 컨테이너 생성, 컨테이너 name이 자동생성 됨)
                3. docker start _컨테이너 name_ : (생성된컨테이너작동법 foreground backgrond 참고)컨테이너 작동시작
                4. docker attach _컨테이너 name_ : (생성된컨테이너작동법 foreground backgrond 참고)-i -t 옵션이 들어갔을 때 자동으로 컨테이너에 들어가게 됨
        2. [기본사용법]docker run -d _image정보_ : Docker container runs in background of my terminal and it does not receive input or display output
            - backgroud : CLI와 상호작용이 불가능한 장소.
            - detach로 설정된 컨테이너 CLI 작동시키는 법
                - docker exec -i -t _컨테이너이름_ /bin/bash
            - docker ps -a 하면, 생성과 동시에 바로 종료되기 때문에 STATUS가 Exited (0) dlek

        3. [기본사용법]docker create -i -t --name _컨테이너이름_ _image정보_ : image정보에 맞는 컨테이너를 생성한다, 마찬가지로 저장소 없다면 docker hub에서 내려 받는다
            - "--name _컨테이너이름_ " : 컨테이너의 이름을 지정한다, 만약 지정하지 않으면 컨테이너 이름이 자동으로 생성돼버린다
            - detach 옵션인 -d를 사용할 수 없음, run만 사용이 가능.
            - mechanism
                1. docker pull
                2. docker create
            - e.g
                1. -i -t를 지정 안해줬더니.. background모드가 default인 가봄 -> default가 맞음. 2번 특징을 참고
                    ```
                    docker create --name test_ubuntu ubuntu:18.04 -> docker start 시켜도 반응 안옴
                    docker create -i -t ~ -> 이제서야 start가 됨
                    ```
                2. 특징
                    1. docker ps -a 하면 STATUS가 created이고, start 시키면 Exited (1) 로 되어 있음. 이것은 "-d"옵션과 아주 똑같은 과정임.

        4. [포트포워딩]docker run/create -i -t -p 3307:3306 ubuntu:18.04 : 생성한 컨테이너에 외부에서 접근할 수 있는 port를 지정해준 것. 호스트의 3307포트에서 컨테이너의 3306포트로 접근이 가능
            - ※주의※ 만약 80번 포트로 진입한 경우만 서비스를 제공하도록 내부적으로 설정되어 있는 것에 81번으로 포드포워딩 해버리면 정상적으로 작동이 안된다
            
            - 특정 IP만 접근이 가능하게 하는법 : docker run/create -i -t -p 192.168.0.100:7777:80 ubuntu:18.04
            - 여러 포트에서 진입이 가능하게 하는 법 : docker run/create -i -t -p 192.168.0.100:653:80 -p 3306:3306 ubuntu:18.04
            - 만약 -p 80 만 쓰면 ? -> 컨테이너의 80번 포트를 쓸 수 있는 호스트의 포트 중 하나와 자동 연결. docker ps 로 컨테이너의 ports를 확인해야함.
                - docker ps -> PORTS에 "0.0.0.0:32769->80/tcp"과 같이 나오는데, 0.0.0.0은 호스트에서 사용가능한 모든 넷트워크 ? 에서 32769번 포트를 80번으로 포드포워딩 했음을 의미
        5. 컨테이너 생성 여러 옵션

            - [컨테이너 환경변수] docker -e _변수이름_ : 컨테이너 내부의 환경변수를 설정.
            
            - docker --link _컨테이너이름_:별명 : 컨테이너에 별명붙이기 ? 

            - [메모리제한] docker run --memory="1g(기가)"또는"4m(메가)" , 이거 없이 ubuntu 만들면 0memory 할당됨
                - docker inspect _컨테이너이름_ | grep \"Momory\" -> 할당된 메모리 크기를 반환
            - [메모리제한] docker run --memory-swap=200m 또는 500m
                - docker inspect _컨테이너이름_ | grep \"Momory\" -> 할당된 메모리 크기를 반환

            - [CPU사용량제한] docker run --cpu-shares 1024 , 반드시 기억할 것은 사용량은 " 비율 " 개념으로 할당하며, 1024는 1(100%)의 비중을 의미하며 설정하지 않으면 자동으로 1024가 default임
                - 만약 다른 컨테이너가 --cpu-shares 512 이면 1024:512 = 2:1 의 비율이기 때문에 할당량이 분할 된다

            - [CPU사용량제한] docker --cpuset-cpus=숫자 , 컨테이너가 특정 CPU만 사용하도록 설정.
                - 추가 사용 매뉴얼
                    1. 숫자를 지정해야하기 때문에 현재 사용하는 CPU별로 번호를 볼 수 있는 방법
                        - htop , 따로 설치가 필요함. 1,2..Mem,Swp 가 있으며 1은 0번 2는 1번으로 인식된다
                    2. htop을 통해 본 결과 1,2,3,4 가 적혀있다면 0,1,2,3으로 --cpuset-cpus=0~3 을 적으면 된다

                - 여러개 cpu사용시키는 법
                    1. --cpuset-cpus="0,3" -> 1번 4번 cpu를 사용
                    2. --cpuset-cpus="0-2"

                    3. 만약 1,2, 만있는데 번호를 2로 사용하면 error가 뜸

    ### 생성된컨테이너작동 foreground backgrond|생성된컨테이너config변경
        - 기본 참고사항
            1. foreground : User와 interact할 수 있는 상황. 터미널에서 컨테이너의 출력값을 볼수 있음...?
                - -d로 설정된 녀석이 여기서 돌아간다고 함. -d를 사용하면 foreground에서 동작한대. 
                - exit 하여 나와도 작동이 멈추지 않는(start가 유지되는) 상태.

            2. background : 터미널에서 컨테이너의 출력값을 볼 수 없음. 즉 CLI을 통해서 컨테이너에게 명령 내리기가 불가능.
                - 컨테이너 생성시 -d 모드 또는 -i -t 없이 하면 start 컨네이너 를 시켜도 start가 안 됨.
            3. 컨테이너 생성시 -i -t가 없으면 default로 background 모드가 된다.
        - 컨테이너 작동방법
            1. docker start _컨테이너이름1_ _컨테이너이름2_ _컨테이너이름3_ ... : 컨테이너를 " background " 에서 작동시킴. docker stop _컨테이너이름_ 하지않으면 멈추지 않고 계속 실행
                
            2. docker attach _컨테이너이름1_ _컨테이너이름2_ _컨테이너이름3_ ... : 컨테이너의 상황을 CLI로 볼 수 있음. 터미널이 닫히면 자동으로 컨테이너도 종료함. 테스트에서 사용할 때

            3. docker stop _컨테이너이름1_ _컨테이너이름2_ _컨테이너이름3_ ... : 컨네이너작동을 다 중지시킴.

            ※ docker run -i -t 를 하면 자동으로 start - > attach 가 되는 이유를 상기하자
        - 컨테이너 config update
            1. 기존에 있는 것을 변경
                - docker update {변경할 resource(cpu,process 개수 등) {컨테이너 이름}}
    ### 컨테이너 외부노출
        - 정보
            1. 컨테이너는 가상 IP주소를 할당받음
            2. 컨테이너에 172.17.0.X의 IP를 순차적으로 할당함. 컨테이너 생성후 ifconfig를 통해 eth0 ip 확인이 가능.
            3. 이 컨테이너는 외부에서 접근이 불가능하며, 오직 DOCKER가 설치된 HOST만 접근할 수 있음
            4. 따라서 포드포워딩(호스트의 특정port에 들어오면 자동으로 연결된 어떤 port로 즉시 연결시켜주는 것)을 설정해야하며, 컨테이너 생성 section의 3번을 사용하면 된다
                - ※주의 만약 80번 포트로 진입한 경우만 서비스를 제공하도록 내부적으로 설정되어 있는 것에 81번으로 포드포워딩 해버리면 정상적으로 작동이 안된다
    ### 컨테이너 들어|나가기
        - 들어가기
            1. docker start _컨테이너이름_ 또는 Container ID 2~3글자(docker ps -a 을 통해 찾기)
                - Container ID 찾기 : docker inspect 
            2. docker attach _컨테이너 이름_ 또는 Container ID 2~3글자(docker ps -a 을 통해 찾기)
        - 나가기
            1. 동시에 컨테이너 정지시키기
                - exit 를 셸에 입력 , ctrl+d
            2. 컨테이너 셸에서만 나오고 컨테이너 작동은 지속하기
                - ctrl + p -> q
    ### 컨테이너정보
        - 컨테이너 configuration 얻기
            1. docker inspect _컨테이너이름_
                - docker inspect myubuntu | grep \"Memory\" : myubuntu에 할당된 메모리 크기 얻기
        - 컨테이너 상태 얻기
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
            5. 컨테이너 정보 해석
                ```
                CONTAINER ID    IMAGE   COMMAND     CREATED     STATUS      PORTS       NAMES
                ```
                - CONTAINER ID : 컨테이너에게 자동으로할당 되는 고유 ID.    
                - IMAGE : 컨테이너에 시용된 이미지
                - COMMAND : IMAGE 에 내장된 COMMAND. 컨테이너가 시작될 때 실행시킬 CMD를 설정. /bin/bash 가 실행되어야만 입출력이 가능한 shell 사용가능.
                    - docker run -i -t ubuntu:18.04 echo hello world : image 안에 /bin/bash cmd를 echo hello world 바꿔버림(덮어씌우기). 즉 컨테이너를 생성하는데 이 컨테이너는 shell접근을 하지 않아서 hello world 만 echo 하고 끝나버리는 무용지물 컨테이너가 완성됨
                - CREATED : 컨테이너 생성후 지난 시간
                - STATUS : UP/PAUSE/Exited , 실행중/중지된/종료된
                - PORTS : 컨테이너에 접근 가능한 PORTS 번호와 해당 번호를 연결한 HOST의 포트번호 (결론 : HOST의 특정 PORT 번호로 진입하면 컨테이너에 접근 가능). 빈칸은 아무것도 설정되지 않음
                - NAMES : 컨테이너 생성때 주어지면 주어진 이름으로 , 없으면 DOCKER에서 자동으로 컨테이너 이름을 생성
        - 컨테이너 이름 변경
            - docker rename _컨테이너이름_ _바꿀이름_
    ### 컨테이너삭제
        - 주의
            1. 반드시 컨테이너는 stop된 상태여야 한다 , docker stop _container_ 로 실행한다.
            2. 실행중인 컨테이너 삭제법
             - docker rm -f _컨테이너 이름_
        - 모든 컨테이너 제거하기
            - docker rm $(docker ps -aq) : 책에선 -a -q, docker ps -a -q 는 모든 컨테이너의 id를 출력시킴. 여기에 해당되는 컨테이너들을 다 삭제
            - docker container prune : 연습용으로 만든 컨테이너가 너무 많을 때 다 삭제.
        - 단일 삭제
            - docker rm _컨테이너 이름_
    ### 명령어
     1. docker stop _container_ : 컨테이너의 작동을 중지시킴
      - 모든 컨테이너 작동 중지 : dockor stop $(docker ps -a -q)

# docker network
- 명령어
    - 기본구조 : docker network _ _ : 도커의 넷트워크를 다루는 명령어는 docker network 로 시작
    - ls : 도커에서 기본적으로 사용가능한 네트워크를 리턴
# 도커 컴포즈
- 용도
    1. 여러 container와 정의할 option command가 많을 때 사용
