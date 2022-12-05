[윈도우에서-리눅스로_파일전송방법](#window_linuxfiletransfering)

[리눅스에서윈도우로파일전송방법](#linux_windowtransfering)

[관리자자동접속법](#Administrator)
[가상머신IP확인및ip설정](#vm-machine)
[tmux사용법](#tmux)

# Window_LinuxFileTransfering
- steps
    1. 설치
    - On ubuntu
        1. root로 접속하던가 아니면 sudo를 사용해서 진행
        2. (sudo) apt install openssh-server
        3. (설치완료시)
            - (sudo) service ssh status
            - Active 에서 active(running을 쳌)
            - (만약 running이 아니면) (sudo) service ssh start
        4. (Option) 매번 시작할 때 작동시키고 싶다면 
            - (sudo) service ssh enable
        5. (sudo) apt install net-tools : 왜 필요한 지 모르겠지만, 자신의 op를 확인하기 위해 사용
        6. ifconfig : net-tools가 없으면 사용이 안됨
            - enp0s3에서 inet 을 확인
    - On window
        1. SSH client - PUTTY 다운로드 , PSCP는 PUTTY설치시 자동으로 실행이래요. cmd에서 pscp 쳐서 뭐 나오면 ㅇㅋ
        2. cmd에서 putty 또는 putty 아이콘으로 putty 열기
        3. (가상머신일시)가상머신IP확인및IP설정이 모두 완료시키기 
        4. PUTTY에서 HOSTIP와 포트번호를 적고 SAVE
    2. 실행
        1. window - cmd , pscp ~ window경로 리눅스에등록된사용자이름@hostip:linux경로(/home/사용자이름)~ 적는다
            - 만약 access denied 일시
                1. 리눅스에등록된사용자이름이 정확리 Linux에 등록된 user 인 지 체크한다
                1. Linux에서 /etc/ssh/sshd_config 에서 PermitRootLogin 옆에 prohibit-password을 yes로 바꾼다 (이 때 반드시 사용자는 root 사용 권한이 있어야 한다)
            - 만약 is not regular file 이라고 뜨는 이유는 경로를 사용할 땐 -r 을 써주는 게 필수다 (위에 일부러 쓰지 않은 것은 내가 분명 까먹을 것이기 때문이다)
                - pscp -r window경로 리눅등록user@HOSTIP:/home/리눅등록user/~ 을 해주면 끝난다
        2. pw 를 적으라하는데 리눅스에등록된사용자이름의 비밀번호를 적으면 된다

        + 윈도우 경로의 끝이 폴더라면 폴더 그 자체가 복사가 된다
        + 윈도우에서 보낼 파일의 이름이 kbs이고 window에 kbs라는 이름의 폴더가 " 있는 경로 " 에다가 해버리면 자동으로 덮어쓰기가 될까?
            -  YES , 된다

# linux_windowtransfering

- On window cmd , (p)scp -P 16022 -r ubuntu@14.49.44.206:/home/ubuntu/VR_SICK_made_leekt/vr_sickness\Park_vr_sickness_predictor C:\Users\leekt\Desktop
    - 윈도우 cmd에서 실행시 , 자신의 port와 ip를 알기 때문에 아주 손쉽게 옮길 수가 있다.


# Administrator
- 방법
    1. sudo -i : 바로 관리자 root로 terminal 실행하는 방법


# VM-MACHINE

- from window cmd
    1. cmd
    2. ipconfig /all
    3. 설명 옆에 적힌 나의 Vm이름을 찾기
    4. IPv4 주소 확인

- from Vm 환경 ip 설정
    - on Oracle VM virtualBox
        1. Tools - > Network Manager 
        2. VirtualBox Host~ 라 적힌거 누르고 아래 IPv4 Address 잘 기억, 적어두던가 
        3. Linux에 들어가서 ifconfig 한 후 현재 가상머신으로부터 할당받은 ip를 확인 "10.0.2.15"
        4. 확인 후 리눅스를 닫고 리눅스 셋팅 - > network
        5. Adapter 1 에서 아래 Advanced를 클릭해서 "Port Forwarding"을 클릭한다, 포트포워딩은 기본지식.md에서 참고한다
        6. 옆에 +를 누르고 Name은 아무거나 치고 Host Ip에는 " Vm머신의 ip " 를 Guest iP에는 가상머신으로 부터 할당받은 ip를 입력한다(10.0.2.15)
            - Host ip는 사실상 가상머신임으로 " port number " 가 중요한가?
                1. Host port를 22로 적지않고 3214로 적어본다 - > connection Refused
                2. 22(ssh의 약속된 port)로 적어본다 - > Okay
        7. 리눅스는 켜져야 putty 접속이 되나 안 되나?
            1. 리눅스가 꺼진 상태로 Host ip 를 putty에 Host ip로 접근 - > connection Refused
            2. 리눅스가 켜진 채로 - > Okay
        8. login as 가 뜬다
            - 리눅스에서 adduser 된 상태의 user이름으로 접속한다 , 나는 Linux에서 adduser leekt 로 하고 pw 는 anna1234로 했다
            - login as leekt
            - pw anna1234
        
# tmux
- tmux : terminal multiplexer, 여러개 터미널을 각각 독립적으로 사용할 수 있게 하는 유틸리티
    - 장점
        1. 한 개 터미너렝서 화면을 분할해서 사용이 가능함
        2. 영구적인 "session" 이라는 걸 제공해서 작업중 ssh서버와 연결이 끊겨도 작업중인 것이 사라지지 않음
    - 구조
        1. session : 
    - 사용법
        - session
            1. tmux new -s 세션이름 , 새로운 세션 생성
            2. tmux new -s 세션이름 -n 윈도우이름 , 세션 만들면서 윈도우랑 같이 생성
            3. exit , 세션 종료
            4. tmux ls , 현재 생성된 모든 세션 목록
            5. tmux attach -t 세션번호 , 세션 다시 시작하기 불러오기
            6. (ctrl+b) +d , 세션 중단하기 ? 
        - window
            1. (ctrl + b ) + c , 새 윈도우 생성
            2. (ctrl + b ) + b + 숫자 , 숫자로 적힌 윈도우로 이동
        1. tmux 타입
        2. 하나의 새로운 윈도우를 가지는 새로운 세션을 만듦
        3. 