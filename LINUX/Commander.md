[1. 우분투 사용 필수 skiils](#1.우분투-사용-필수-Skills-/-지식들)
[1.1 파일거르기, ](#pipe_filter_redirection)
[1.2 프로세스,데몬,서비스 란?](#프로세스,데몬,서비스-란?)
[# 2.commander - 필수 커맨더, 기본 커맨더, 사용자 커맨터](#2.commander:-필수-커맨더,-기본 커맨더,-사용자 커맨터)
# 3. skills, 유저정보확인, 비밀번호 복구(응급복구)
[4. Network 지식](#4-network-지식--넷트워크-연결-오류-해결)

[5. commander - 리눅스 제공 커맨더](#5-commander---리눅스-제공-커맨더)
# 6. Server management and commander
[사용자변경_그룹변경(docker)](#사용자-변경)

[관리자로변경](#관리자-변경)

[root접근권한이없는_사용자에게루트접근권한주기(sudo사용허가하기)](#루트접근불가)

[root관리자비밀번호변경법](#비밀번호변경)

[App설치시모든사용자가사용할수있게하기](#앱설치)

[python라이브러리설치](#python)

[docker설치](#docker설치)


[hardware설치](#hardware설치)

- 한글은  한글\ 게임\ 1.plplpl 처럼 \을 써줘야 인식하나봄. 근데 꼭 그런 것도 아닌가봄.
- cd _: _은 경로, 경로를 이동한다
    - e.g
        1. cd /etc/apt
        2. cd /etc/netplan : ip편집 폴더 이동
- nano : text file 열기용.

- ufw enable : 방화벽 활성, ufw 우분투에서 제공되는 방화벽, 보안상 켜놓는 것이 좋다.
    - apt-y install net-tools 를 다운로드하고 나서 진행했다
- apt update 
- clear : 화면 지우기
- ip addr : id 정보 출력
- mv
- dpkg : dpkg -l ,s 설치된 패키지를 체크하는 것.
- rm : rm -rf root->삭제시 루트파티션삭제로 리눅스재설치, 삭제 커맨더.
- wget : url에 접속해서 파일이 있으면 다운 받음.

- ls : ls sources.list, 있으면 있다 없으면 없다..

- apt : apt update, apt install,

- reboot : 재시작

- exit : 터미널 나가기

- halt -p : 시스템 완전 종료.

- ls -l runlevel?.target : system폴더에 가서 runlevel0.target~runlevel1.target 의 모든 value를 봄. runlavel?.target은 링크파일이라며 각 링크파일이 실제 파일과 연결되어 있다고 한다. runlevel0.target -> poweroff.target 파일을 가르킨다.

+ Linked file(링크 파일)은 윈도우의 바로가기 아이콘과 비슷한 개념이다. 실제 파일이 아닌 다른 파일을 가르키는 것.


# 1.우분투 사용 필수 Skills / 지식들
프로세스, 데몬, 서비스,  (systemd)서비스/소켓
+ Dos key : 이전에 입력했던 것을 위/아래 화살을 사용해 가져오기.

- X window : GNOME,KDE 등이 우분투에 사용된 GUI

- history : 오늘 사용했던 모든 명령어 가져오기
    - 사용예
        1. history -c : 저장된 모든 명령어 삭제
- 자동완성기능 Tap key : 현재 있는 directory에 알파벳/한글 과 일치하는 폴더가 있으면 문자의 첫 몇글자만 치고 tab을 누르면 자동완성.
    1. 비슷한 앞 문자의 폴더 두개 이상 : tab 한 번만 입력해서 완성이 안되는 경우는 비슷한 앞 문자를 가진 경우다. systa 와 sysat인 경우이다. 이 경우 tap 두번을 눌러 어떤 폴더들인 지 확인이 가능하며 문자를 더 명시 해줘야 자동완성이 된다.

- vi/nano/gedit : visual이란 뜻인데, 둘다 텍스터 프로그램이다. 메모장과 같은 것이다. 그래픽 모드에선 gedit이 있는데 text모드에선 사용불가다.
    1. gedit : 어떤 directory에서든 사용가능, gedit/저장경로/file이름 시 열기 가능.
    2. nano : text mode에서도 편리하게 사용가능. ls로 이름을 찾아서 nano file이름 하면 열기가능.
        - nano -? [filename]
            1. c : 커서가 이동할 때마다 행/열 , 문자개수 표시
        - nano 내부 단축키 ctrl + 
            1. c : 커서가 있는 위치가 텍스트 파일의 몇행 몇열이고 총 몇개 문자중에 몇번째 문자에 있는 지 보여줌
    3. vi : root에서 실행
        - Mechanism
            1. vi 실행시 명령모드 상태 돌입.
            2. i/a 클릭시 입력모드, 문서작성을 시작
            2. : 일시 ex mode. 저장(w) q(종료) i(취소) 등 ㅅ ㅜ행
            3. ESC 클릭시 2번의 모든 경우 명령 모드로 이동. EX MODE같은 경우는 ENTER 실행시 명령모드로 돌아간다. 
        - 사용법
            1. EX,라인모드 : ESC 클릭으로 전환. :_ 으로 실행.
                1. :q :vi editor 종류
                2. :wq : write end quit, 저장후 종료
                3. :q! : 기존에 작성한 것을 무시하고 종료
            2. 명령모드 :  TERMINAL vi new.txt 입력. 명령을 기다리는 상태
                1. i/I : 현재 커서의 위치/ 맨 앞에서 부터 입력
                2. a/A : 현재 커서 위치 다음 칸/맨 마지막 부터 입력
                3. o/O : 현재 커서의 다음/이전 줄에 입력
                4. s/S : 현재 커서 위치의 한 글자/줄 를/을 지우고 입력
        - vi editor가 비정상 종료시 생성되는 파일 확인후 조치방법(저장하지 않고 터미널 종료)
            - swqp file : 기존 파일 수정시 자동으로 .new.txt.swap 이 생성되고 정상종료시 자동삭제되는 파일. 파일 앞에 "."은 숨김 파일이란 뜻이다.
            1. 우선 enter 후 :q!입력해서 닫기.
            2. ls -a 로 .swap을 확인
            3. rm -f .new.txt.swp 로 삭제
            4. 정상 편집 가능.

# hardware설치
- mount / umount
    - 장착된 하드웨어(hardware) 확인 법
        - df -h

    1. mkfs : 장착한 하드웨어를 format시키기
    - mount : Hardware를 마음대로 이동시키기/hardware적용시키기. Linux에선 물리적 장치(하드디스크파티션,CD,USB..)를 특정한 위치(보통 폴더)에 연결시키야 함, 이게 마운트.
        - CD/DVD MOUNT

        - 사전지식
            1. 특정 하드웨어는 /dev/sdf 처럼 특정 경로에 존재한다
            2. 이 경로 가 바로 하드웨어가 있는곳이다
            3. ls /dev/sdf -al 로 하면 파일의 상태가 나오는데, -> 의 오른쪽이 실제 장치명이다. 따라서 /dev/sdf 로 simbol되었고 /dev/장치명 으로 해도 된다
        
        - hardward mount
            - sudo mount /dev/sdf /mnt  : /은 바로 모든 경로의 시작이라고 보면된다 , mnt라는 폴더, 경로에 하드웨어 저장소로 만들겠다는 것임. mnt가 없으면 자동 생성
            - /mnt 폴더에 가면 무언가 생겨있다
    - umount : hardware 떄버리기
        - sudo umount /mnt : mount를 통해 hardward가 /mnt경로로 설정되었고 이것을 때버리기 

# pipe_filter_redirection
- pipe , filter, redirection
    1. pipe : |
    2. filter : 필효한 것만 걸러주는 명렁어
        - grep : 일종에 정규표현식 같은 것. 패턴 형식이 같음.
        - tail : 마지막 10개를 default로 보여주기
        - wc : 
        - sort :
        - awk :
        - sed :
    3. redirection : 화면에 출력되는 것을 특정 파일에 넣어서 출력시키는 방법 등.
        - ls -l > list.txt : ls -l 명령어를 .txt 파일에 저장하는데, 기존 내용에 덮어 씌운다
        - ls -l >> list.txt : 기존 내용에 이어서 쓴다
        - sort < list.txt : list.txt 를 sort 해서 화면에 출력
        - sort < list.txt >out.txt : list.txt정렬해서 out.txt에 덮어씌우기.
# 프로세스,데몬,서비스 란?
- 프로세스, 데몬, 서비스 
    1. process
        - cmd
            1. ps : 현재 실행중인 모든 프로세스를 나오게함. processID(PID)
                - ps -ef : PID뿐 아니라 현재 상태를 알려준대.
            2. kill : 프로세스 강제 종료.
                - kill -9 PID : 해당 프로세스를 강제 종료시킨다. 무한루프를 돌 때 사용가능.
            3. pstree : parent process and chile process를 보여줌.
        1. fowarground Process : 
        2. background Process : 모든 커맨더 뒤에 & 을 붙여준다. 해당 커맨더가 실행되는 도중에 terminal을 사용할 수 있게 된다. GUI가 있는 버전에서만 사용이 가능한 듯.
            - ex : gedit & , gedit을 키면서 동시에 
    2. 서비스와 소켓(systemd)서비스/소켓 : systemd라는 서비스  매니저 프로그램으로 작동시키고 관리한다.
        - systemd란? : 운영체제 시작시 가장 시작되는 프로그램 중 하나. systemd manage most service program. https://freedesktop.org/wiki/Software/systemd/ 참고.
        - systemctl : 
        1. 서비스 : Daemon 이라고도 불리는데, 서버프로세스를 의미한다. 웹/네임/DB 서버 등의 프로세스를 지칭한다. 웹 서버 데몬, 네임 서버 데몬 이라고도 불린다.
            - backprocess의 일종.  서비스=데몬=서버 프로세스
            - 평상시에도 늘 가동하는 서버 프로세스
            - 사용EX
                1. systemctl start/stop/restart httpd
                2. ls /lib/systemd/system| grep ^h : 서비스의 실행 스크립트 파일이 들어있는 경로이며, 서비스이름.service 만 존재. 현 시점 347개 있음. 
                    - 이 directory 안에 있는 파일 대부분 systemctl 로 명령 가능.
                    - systemctl list-unit-files로 현재 실행중인 서비스 실행 여부 확인.
                        - 특정 파일 선택 법 : systemctl list-unit-files| grep ^disirable word, 
                        - enable : 사용
                        - disable: 미사용
                        - static : 사용/미사용 설정이 불가, 다른 서비스의 "소켓"에 의존해서 실행됨.
                        - generated/transient : 특별히 신경 꺼도 된대.
        2. 소켓, socket
            - 필요할 때만 작동하는 서버 프로세스.
            - /lib/systemd/system/소켓이름.socket 파일로 존재.



# 2.commander: 필수 커맨더, 기본 커맨더, 사용자 커맨터
- 필수 커맨더(서버구축) 필수 commander
    - unix/linux 에선 소문자 대문자를 명확히 구분한다.

    - man 명렁어 : manual 명렁어, 해당 명령어의 사용법이 담겨 있다. 위 아래는 화살표로, 페이지 단위는 pg up/dn을 사용한다. space / b 도 가능. 종료는 q.
        + man Section : section 1: 명령어, 2~3:프로그래밍 , 4 디바이스, 5 파일형식, 6 게임, 6 기타주제, 8 시스템 관리, 9 커널 관련 설명

    + sudo : 관리자 cmd, 일반사용자가 관리자 권한을 얻으려면 사용한다. root사용자는 생략가능하다.
        - 일반/관리 사용자의 차이 : #는 root , $는 일반
        - root 사용예
            1. sudo su - root : 일반사용자가 관리자 계정으로 가는 것

        - 이외 사용자 sudo : 
            - 사용예
                0. sudo su -root
                1. sudo mv sources.list sources.list.bak[파일이름변경]
                2. sudo apt update : apt라는 폴더를 업데이트.
                3. sudo wget http://~
                4. sudo nano 00-installer-config.yaml : 00~.yaml 파일을 txt파일에서 연 것임! 아하! nano에서 보통 다 변경하나!?
                    - .yaml : XML,C,Python,펄에서 정의된 email양식서 개념얻어 만듦. Yaml ain't makrup language 라는 뜻. 핵심이 마크업이 아닌 데이터 중심에 있음을 공표하기 위함, 오늘 날에 가벼운 마크업 언어로 사용됨 ㅋ
                5. sudo netplan apply : netplan은 ip 주소 설정 파일이 있음. 해당 파일을 적용시켜서 ip 업뎃.
    + 시스템 ON/OFF CMD
        1. OFF : logout/exit, poweroff , shutdown --p now, halt -p, init [RunLevel]
            - shutdown [-?] [time]
                1. -?의 종류
                    1. --p +10/now :poweroff, 10분 후 종료/지금 종료
                    2. -r 22:00/now : reboot, 오후 10시에 재부팅/바로 재부팅
                    3. -c : cancle, 예약된 shutdown 명령 모두 취수
                    4. -k +15 : 현재 접속한 사용자들에게 15분후 종료 메시지만 보내고 실제로 종료는 안함.
                    5. -h +5 : 5분 후에 종료.
            - logout/exit : 자신만 접속을 끊기, 관리자가 끊으면 모든 시스템이 off임으로 사용중인 사용자들이 없도록 주의해서 한다.
        2. init [RunLevel]
            - RunLevel : 0~6의 숫자가 옴. 우분투에선 2,4는 3과 호환위해 동일함.
                1. 0 : power off
                2. 1 : Rescue, 시스템 복구모드
                3. 3 : Multi-User : 텍스트 모드의 다중 사용자 모드.
                4. 5 : Grapical : 그래픽 모드의 다중 사용자 모드. x윈도 사용시 부팅후엔 자동으로 Runlevel 5로 지정된다.
                5. 6 : reboot
            - Example
                1. 현재 설정된 RunLevel 확인
                ```
                cd
                ls -l /lib/systemd/system/default.target
                -> 우분투 server라면 graphcal.target이 뜬다
                ```
                2. 부팅시 text mode로 시작하기
                ```
                ln -sf /lib/systemd/system/multi-user.target /lib/systemd/system/default.target
                ->  file만들어짐. multi-user.target이 default.
                ls -l /lib/systemd/system/default.target
                -> reboot시, textmode로 시작됨.
                -> 그래픽모드로하려면 startx 를하면 x윈도가 가동된다.
                ```
                3. text모드에서 다시 그래픽으로
                ```
                ln -sf /lib/systemd/system/graphical.target /lib/systemd/system/default.target
                -> init 6
                ```
    + Virtual console : ubuntu에선 총 6개 가상콘솔이 제공됨. 부팅시 보이는 화면은 F2.
        1. Ctrl+Alt+F2-F7, chvt 2-7
        2. server 버전은 F1~F6

- 기본 커맨더
    1. ls : 커맨더가 위친 directory의 파일의 목록을 나열
        - ls -l | wc -l : 폴더 내 파일 개수확인, -l로 모든 파일 나열하고 wc -l로 count
        - ls -a : 현재 경로의 숨겨진 파일을 포함해 모두 나열
        - ls /etc/systemd : systemd에 있는 파일 나열
        - ls -a /etc/systemd : systmed에 있는 . 의 숨겨진 파일 모두 나열
        - ls *.conf : .conf인 파일만 모두 나열
        - ls -l /etc/systemd/b* : l은 Linked를 의미, systemd에서 b로시작하는 파일. 끊어 읽어야 한다.
            - 해석 : ls -l (path: root@server)
            ```
            -rw-r--r-- 1 root root    6  5월  3 14:02 ccc.txt
            -rw-r--r-- 1 root root    7  5월  3 14:00 kbs.txt
            drwx------ 3 root root 4096  5월  2 20:20 snap
            drwxr-xr-x 2 root root 4096  4월 27 22:23 공개
            drwxr-xr-x 2 root root 4096  4월 27 22:23 다운로드
            drwxr-xr-x 2 root root 4096  4월 27 22:23 문서
            drwxr-xr-x 2 root root 4096  5월  3 12:40 바탕화면
            drwxr-xr-x 2 root root 4096  4월 27 22:23 비디오
            drwxr-xr-x 2 root root 4096  4월 27 22:23 사진
            drwxr-xr-x 2 root root 4096  4월 27 22:23 음악
            drwxr-xr-x 2 root root 4096  4월 27 22:23 템플릿
            ```
            1. -: 파일유형, -/d/b/c/l 중하나. b/c는 Device를 의미.
                - d : Directory(folder)
                - "-" : 확장자가 있거나 없는 file
                - b : block device, 하드디스크,플로피드스크,CD/DVD의 저장 장치가 있다.
                - c : character device, 마우스,키보드,프린터 등의 입출력 장치
            2. rw-r--r-- : 파일 허가권, 3개씩 끊어서 인식한다. 소유자는 읽고 쓰기가 가능하며 그룹과 이외사용자는 읽기마 가능을 의미. binary로 r:100 w:010 x:001 이며, rwx:111=7로 표현가능
                - rwx : read write excecute 읽쓰실행 가능(실행은.exe란 뜻인가..? 리눅스에선 확장자에 의미가 없다. 단지 .jpg를 .exe로 바꿔 실행시 오류가 날 뿐.)
                - rw- : read write : 읽기 쓰기 실행 불능
                - r-- : read : 읽기만
                1. 첫번째 : USER(소유자)의 파일 접근 권한
                2. 두번째 : 그룹의 파일 전급 권한
                3. 세번째 : 소유자 외 사용자의 파일접근 권한
            3. 1/2/3... : 링크 수
            4. root : 파일 소유자 이름
            5. root : 파일 소유 그룹 이름
            6. 6/7/4096.. : Byte 크기
            7. 5월 3 14:02... : 마지막 변경 날찌.시간
            8. ccc.txt 파일 이름
    2. cd : change directory
        - cd : move to home directory 
        - cd ~ubuntu : ubuntu라는 사용자 이름의 홈 디렉토리이동
        - cd .. : 현재 바로 상위 경로로 이동
        - cd /etc : etc폴더로 이동
        - cd ../systemd : 현재 경로가 netplan에서 /systemd하면 안 가져짐. ../systmed 해야함.
    3. pwd : print woriking directory : 현재 디렉토리의 전체 경로를 화면에 보여준다.
    4. [주의사용]rm : ReMove. root이외엔 권한이 있어야 함. 리눅스에는 휴지통 개념이 있기는 하지만 삭제한 파일이나 폴더 복구가 굉장히 까다롭다.
        - rm abc.txt : 내부적으로 rm -f 연결
        - rm -i abc.txt : 삭제시 정말 삭제할지 메시지 뜸
        - rm -f abc.txt : 삭제 시 그냥 바로 삭제.
        - [주의사용]rm -rf abc : Recursive force , abc 디렉터리와 더불어 그 하위 폴더,파일까지 다 삭제.
        - [글깨진파일삭제] steps
            1. 글깨진 파일|폴더가 있는 경로에서 ls -li , 맨 앞에 써져 있는 번호를 복사한다
            2. find . -inum 번호 -exec rm -f {} \; , 오류면 폴더니까 삭제됐는 지 확인하고 삭제가 안 됐으면 -rf 로 해주면 된다
            - rm -rf abc , abc가 폴더면 그냥 하위까지 다 삭제됨
    5. cp : copy, 파일이나 폴더를 복사. 명령을 읽는 권한이 필요.
        - cd abc.txt cba.txt : abc.txt를 cba.txt라는 이름으로 복사
        - cp -r abc cba : 폴더복사, abc폴더를 cba이름으로 복사
    6. touch : 크기가 0인 파일 생성, 이미 존재하면 수정시간만 현재로 변경
        - touch abc.txt : 내용빈 abc.txt 생성이던가, 기존 파일 시간갱신
    7. mv : MoVe, file,folder의 이름을 변경/다른 폴더로 이동할 때 사용
        - mv abc.txt /etc/systemd/ : systemd로 이동시키기
        - mv aaa bbb ccc ddd : aaa bbb ccc 파일을 '/ddd" folder로 이동
        - mv abc.txt www.txt : www.txt로 이름변경
    6. mkdir : make directory, 새로운 folder생성. 딱 사용한 사용자에게만 생성된다.
        - mkdir abc : 바로 현재 폴더 커맨더가 존재하는 폴더에 abc폴더생성, ls로 확인가능
        - mkdir -p /def/fgh : def,fgh 디렉토리를 생성함. def가 있으면 그냥 통과
    7. rmdir : Remove derectory, 권한이 있어야 하고, 디렉터리 안이 비어있어야함. -r 을 쓰면 깡그리 삭제
        - rmdir -r kbs : kbs폴더 안에 있는 거 다 삭제
    8. cat : concatenate, 어떤 파일인지, 폴더인지를 화면에 보여줌.
        - cat 공개 다운로드 문서 : 공개,다운로드,문서가 파일인지 폴더인지 보여줌
        - ex) cat /etc/NetworkManager/system-connections/유선\ 연결\ 1.nominations
    9. head,tail : 텍스트(nano,vi,gedit)같은 파일의 앞 10행 또는 마지막 10행만 출력
        - head /etc/systemd/user.conf
        - head -3 /etc/systemd/user.conf : 앞 3행만 화면에 보이기
        - tail -5 /etc/systemd/user.conf : 마지막 5행만 화면에 출력
        
    10. more : 텍스트 파일 페이지 단위로 내용을 화면에 출력. spacebar로 다음페이지, b로 이전 페이지 이동. q로 종료
        - more /etc/systemd/system.conf
        - more +10 /etc/systemd/system.conf : 10번행부터 출력
    11. less : more명령어와 용도가 비슷, 화살표키,page up/down 사용가능
        - less /etc/systemd/system.conf
        - less +10 /etc/systemd/system.conf : 10행부터 출력
    12. file : 해당 파일이 어던 인코딩 파일인지 알려줌
        - file /etc/systemd/system.conf : ASCII text
        - file /bin/gzip : gzip은 실행 파일
    13. clear : 현재 터미널 청소

- 사용자 커맨터 (root)

+ 사용자 커맨더: 1대의 사용자에 여러 명이 동시 접속가능 한 리눅스, root는 기본적인 super user.
    - 사용자 커맨더의 존재이유 : 동시에 접속해도 특정 부서에 소속시키는 등의 분류가 필요함. 권한을 주려면 분류가 필요하기 때문임. 자세한 것은 184~185page.
+ 파일 커맨더

    0. 현재 존재 그룹/사용자 보기 : getent group/passwd
    1. adduser : 새로운 사용자 추가, /etc/passwd,/etc/shadow,/etc/group 파일에 새로운 행이 추가됨. 그룹 id가 지정되지 않으면 사용자 이름과 같은 그룹 id가 생성되는데, 이는 즉 그룹을 꼭 지정해야 함을 의미한다.
        - adduser newuser1 : newuser1이라는 이름의 사용자생성
        -> 암호생성 -> 재입력 -> 전체이름입력[생략가능] -> 사무실 번호[생략가능] -> 직장번호[생략가능] -> 집번호[생략가능] -> 기타[생략가능] -> 정보가 올바르요? [Y/n] -> y, enter
        - adduser --uid 111 newuser2 : UserID, newuser2 생성 동시에 사용자 id 111지정
        - adduser --gid 1000 newuser3 : GroupID, newuser3 사용자를 생성, 그룹 id를 사용해서 유저만들기. 고유 id가 1000인 그룹에 newuser3 사용자를 포함시킴
        - adduser --home /newhome newuser4 : HomeDirectory, 생성하면서 홈디렉토리의 이름을 /newhome 지정
        - adduser --shell /bin/csh newuser5 : 기본 셸을 /bin/csh지정
        ## 복수지정도가능.
        - adduser --gid 1997 --uid 1500 lee -> 1997이란 그룹id가 있으면 감. 사전에 미리 만들어둬서 새로운 그룹은 만들어 지지 않음. user id는 1500 이름은 lee로 지정.
            - 단 , gid, uid 모두 이미 존재해야하나봄. 

    2. passwd : 사용자의 비밀번호 변경.
        - passwd newuser1 -> 새 암호, 재입력
        - passwd -> 현재 접속중인 사용자 비번설정
    3. usermod : 사용자 속성 변경
        - user --groups ubuntu newuser1 : newuser1의 보조그룹에 ubuntu추가
        - user --shell /bin/csh newuser1 : newuser1의 기본 셸을 /bin/csh로 변경
    4. userdel : 사용자를 삭제
        - userdel newuser2 : 삭제돼도 홈디렉토리는 삭제 안됨
        - userdel -r newuser3 : Recursive, 삭제하면 홈디렉토리도 삭제
    5. chage : CHange AGE 사용자의 암호를 주기적으로 변경하게하기.
        - chage -l newuser1 : newuser1 사용자에 설정된 사항 확인
        - chage -m 2 newuser1 : 암호 설정/변경후 최소 2일간 사용
        - chage -M 30 newuser1 : 암호 설정/변경후 최대 30일까지만 사용가능
        - chage -E 2026/12/12 newuser1 : 만료날짜 지정
        - chage -W 10 newuser1 : 기본값은 7, 암호사용 만료기간의 몇일 전부터 경고하는 기간.
    6. groups  : 사용자가 소속된 그룹을 보여줌
        - groups : 현재 사용자의 소속 그룹
        - groups newuser1 : 해당 사용자의 소속 그룹
    7. groupadd : 새로운 그룹을 생성
        - groupadd newgroup1 : newgruop1 그룹 생성
        - groupadd --gid 2222 newgroup2 : new~2생성동시에 그룹 아이디를 2222로 지정
    8. groupmod : 그룹의 속성변경
        - groupmod --new -name -mygroup1 newgroup1 : newgroup1 그룹의 이름을 mygroup1으로 변경
    9. groupdel : 그룹을 삭제
        - groupdel newgroup2 : 해당 그룹 삭제, 단 해당 그룹을 main그룹으로 지정한 사용자가 없어야 함. 즉 서브 그룹으로 지정하면 ㄱㅊ.
    10. gpasswd : 그룹의 암호를 설정, 그룹관리 수행
        - gpasswd myg1 : myg1 그룹의 암호 지정
        - gpasswd -A newuser1 mygroup1 : newuser1을 mygroup1 그룹의 관리자로 지정
        - gpasswd -a newuser4 mygroup1 : newuser4를 mygroup1 그룹의 사용자로 추가
        - gpasswd -d newuser4 mygroup1 : newuser4를 mygroup1 그룹의 사용자에서 제거


+ 파일커맨더
    1. chmod : 파일 허가권을 변경. root/해당파일의 소유자만 실행가능. ls -l 설명을 참조해서 파일해석.
        - ex : chmod 777 sample.txt : rwxrwxrwx, 사용자/그룹/이외사용자 모두 읽고쓰고실행가능.
        - 실험
            1. root에서 사용자소유권을 바꾸고, mv 를 사용해 옮긴다음 해당사용자 계정에서 chmod하기 성공. -> 분석결과 root사용자계정에선 파일의 사용자root가 아니더라도 바꾸기가 가능. 단 이외에 사용자들은 오직 그 파일의 소유자만 변경이 가능함. 예를들어 root에서 one,two 파일을 만들고 one은 소유자가 root고 two은 소유자가 lee 임. 유저는 lee와 kim인데 두 파일을 kim에게 보냄. 두 파일 모두 소유자가 다름으로 kim은 
            2. excute 연구, 파일의 사용자가 현재 사용자가 아니더라도 실행이 가능한가? 
                1. kim이란 유저에게서 파일의 소유자는 lee이고 744인 상태로 이동시켜서 실행시 실패.
                2. 같은 조건이지만 441로 실행시 kim에서 실행실패
                3. 같은 조건에 414로 실행시 kim에서 실행실패
                4. 같은 조건인데 777로 했더니 실행성공
                5. 111 실패
                6. 이번에는 사용자를 root와lee로 두번 같이 555로 했더니 실행 성공
                7. root사용자 455 실행성공
                8. root사용자 545 실행성공
                9. lee/root 사용자 554 실행실패.
                10. root사용자 221 실행실패.
                11. root사용자 113 실행실패.
                12. (찾았다.) 117 실행성공. 즉실행을 하려면 rwx가 모두 허용이 되어야 한다.
                13. (찾았다.) --7(007) 실행성공.
                14. root사용자 115 실행성공. 즉 실행을 하려면 읽기가 가능해야하고 실행이 되어야 한다!
                15. (최종결정!)root/lee사용자 --5(005) 실행성공. 역시 실행하려면 읽기가 가능해야하고 실행이 되어야 해. 사용자는 상관이 없다.

    2. 파일 소유권 : 파일을 소유한 사용자/그룹을 의미. 파일은 사용자 외외엔 절대 수정불가. 실험통해 입증.
        1. chown : 파일의 소유자를 변경. 오직 root만이 사용할 수 있다.
            - ex
            ```
            - root에는 kbs,ccc .txt 두개 파일이 있다.
            chown user1 kbs.txt
            ls -l ccc.txt -> -rw-r--r-- 1 user1 root 6  5월  3 14:02 ccc.txt
            ls -l kbs.txt -> -rw-r--r-- 1 root root 7  5월  3 14:00 kbs.txt
            ```

        2. chgrp : 파일의 그룹을 변경하기, 1은 파일의 소유자만 변경한 것.
            - ex
            ```
            tail /etc/group -> 그룹의 종류를 확인, 예제에서 생성한 ubuntuGroup로 지정결정
            ls -l kkk -> -rwxr--r-- 1 user1 root 15  5월  3 15:20 kkk
            chgrp ubuntuGroup kkk
            -> -rwxr--r-- 1 user1 ubuntuGroup 15  5월  3 15:20 kkk
            ```
        3. chown userName.Group fileName : 귀찮으니 사용자와 그룹 한꺼번에 바꾸기
            - ex
            ```
            chown user1.ubuntuGroup text
            ```

- 필수 주소(directory)지식

    1. /etc/skel : 새로운 유저가 생성될 때마다 필수 file들이 /home/이름 로 복사된다.

    2. 

- network 커맨더/파일 : 관련 명령어가 매우 많고 정말 조금만 적는 것임.
    1. nm-connection-editor / nmtui : 넷워크 관련 작업은 대부분 이 두가지로 실행. nm은 Network Manager. nmtui는 Network Manager Text User interface. 
        - 설정내용
            1. 자동 ip주소,고정 ip주소 사용
            2. ip,subnetMask,gateWay 정보 입력
            3. DNS 정보 입력
            4. 넷워크 카드 드라이버 설정
            5. 네트워크 장치(ens32 또는 ens33) 설정

    2. systemctl start/stop/restart/status/enable/disable networking(serviceName)
        1. restart : stop과start옵션을 합한것 1.실행후 내용을 변경하면 반드시 systemctl restart NetworkManager 명령실행을 주입하라.
        2. status : 서비스의 현재 active(enable)/inactive(disable) 상태를 표시.
        3. enable/disable : 서비스 사용/미사용

    3. ifconfig 장치이름: 해당 장치의 IP 주소와 관련 정보를 출력하는 명령어.

    4. ping ip주소/url : ipAdd/url에 해당하는 상대 서버(컴퓨터)가 응답하는 지 테스트하는 간단 유용 명령어.

    5. nslookup : 주소를 수정, 넷워크 연결확인등을 수행할 수 있다. nameserver lookup? the facility for nameserver check maybe...?
        - 내부 cmd
            1. server NewDNS서버의IP주소 : 원래 넷워크가 동작하지 않을 때 체크가능. 임시로 IP주소를 변경하고 본체에는 영향이 가지 않는다.
            ```
            server 8.8.8.8 , googld namerserver
            ```

    - 넷워크 설정 주요 파일
        0. nano /etc/netplan/00-installer-config.yaml, nano /etc/netplan/*.yaml : 둘다 같은 파일. 모든 Address 정보가 담긴 파일. Desktop에도 있기는 한데 server에서 더 자세히 등장해서 Desktop버전에는 어울리지 않음.
        0. nano etc/NetworkManager/system-connections/유선\ 연결\ 1.nmconnection : Desktop에서 주소 정보를 모두 담고 있는 파일.
        0. /etc/resolv.conf : Desktop, Server 버전에 동시 존재. 웹 url이 요청하는 파일. DNS/ HOST 이름이 있음. 넷워크 재시작시 각 버전의 파일에 있는 DNS정보를 덮어씀.
        1. X window version 
            - nm-connection-editor 또는 nmtui 로 Graphic으로 변경.
            - /etc/NetworkManager/system-connections/유선 연결 1.nmconnetion 에 파일의 내용이 변경된다.
                - 유선 연결1 : 넷워크 장치에 설정된 넷워크 정보가 모두 들어 있는 파일. nano/gedit으로 편집이 가능하기는 하나 nm-connection-editor/nmtui가 원래 용도니 사용 권장.
        2. TUI
            - 
            
        3. nm-connection-editor / nmtui : 실험적으로 사용할 게 아니면 2번말고 영구적으로 넷워크를 수정.
        3. /etc/netplan/*.yaml : Ubuntu Server의 네트워크 정보가 설정된 파일. 영구 수정시 사용할 파일.
        4. /etc/hosts : 현 컴터의 호스트 이름과 FQDN이 있는 파일
        5. /etc/resolv.conf : DNS NAME서버가 담겨있는 파일. systemctl restart Net~ 명령이 필없음, 웹 브라우저, nslookup cmd 로 url 조회시 실시간 열어서 사용되기 때문.
        6. /etc/NetworkManager/system-connections/유선 연결 1.nmconnetion : Ubuntu Desktop의 넷워크 정보가 설정되어 있음.
    
    - Example
        1. cat /etc/NetworkManager/system-connections/유선\ 연결\ 1.nmconnection
        - nano /etc/NetworkManager/system-connections/유선\ 연결\ 1.nmconnection : 같음. 단 파일 수정후 컴퓨터를 재부팅해야함.
        ```
        ......
        [ipv4] # 여기를 확인
        address1=192.168.111.55/24,192.168.111.2 -> ip주소/netmask,gateway
        dns=192.168.111.2; -> dns
        dns-search=
        method=manual -> 수동으로 설정했다는 의미. auto는 자동으로 ip주소를 할당 받음을 의미.
        ......
        ```
        2. DNS 서버 변경, 재부팅시 초기화되는 설정. 차라리 서버 재부팅을 먼저 하는 것도 정답.
        ```
        nano /etc/resolv.conf ->
        nameserver 127.0.0.53
        options edns0
        nameserver 8.8.4.4 -> 위에 서버가 작동하지 않으면 이것이 작동. 구글 서버를 사용하는 것.
        ```
# 3. skills, 유저정보확인, 비밀번호 복구(응급복구)

- 사용자생성 및 그룹 관리(지정)
    1. adduser user1 : user1이란 유저를 생성하며, 암호는 자동으로 /etc/shadow에 저장되고, user의 ID는 이전 사용자의 ID에 +1한 숫자인데 tail /etc/passwd로 확인이 가능하다. 2.의 adduser 참고한다.
        - user1:x:1001:1001:,,,:/home/user1:/bin/bash : tail /etc/passwd의 결과이다. 3번 째 열이 User id, 다음이 group id이다. 그룹의 이름이 지정되지 않고 id가 지정이 된다.
        - 홈 디렉터리는 default로 /home/사용자이름 이며, 셸은 기본으로 /bin/bash이다.
        - tail /etc/group : user1:x:1001 로 user1의 이름으로 그룹이 생성됨을 확인가능하다.(소속이 1명) 1001이라는 건 1000이 있다는 뜻이다.
    - 1번처럼 생성시 불편하다. 그룹을 지정해야 관리가 편리하며 있는 그룹에 속하도록 생성하는 것이 바람직하다.
        1. groupadd ubuntuGroup : ubuntuGruop 이란 그룹 생성
            - ubuntuGroup:x:1001: , 란 그룹이 생성됨. 사전에 user1을 userdel했기 때문에 1001이 사라졌기 때문에 1001로 할당 되었다.
        2. adduser --gid 1001 user1 , gid:GroupId, 1001의 그룹아이디에 속한 user1을 추가한다.
        3. tail /etc/passwd : passwd file 확인. 솔직히 비번은 안나와서 왜 passwd인지 모르겠음.
        4. tail /etc/shadow : 실질적인 비번이 담긴 곳, 암호화 되어있어서 볼 수는 없음.
        5. ls -a /home/user1 AND ls -a /etc/skel : 둘 다 동일한 파일이 들어 있음. skel파일의 파일들이 user1 폴더에 복사됨.
    

- root 경로는 drwx------ , 그 어떤 다른 사용자들이 root안에 있는 파일에 접근할 수 없다.
    1. ls -l /root/test s -> root가 아닌 사용자가 root에 접근하려 한다. 절대 불가능하다
    2. ls -ld /root -> id가 아니라 ld이다. 확인해보면 root의 dicrectory는 drwx------ 15 root root 4096 이다.

- 응급복구 : 오랜만에 사용시 비밀번호가 기억나지 않기 일수다. 학습 목적이면 그냥 포맷하고 다시 설치하면 되지만 실무에선 아니다. 비번을 알아낼 수는 없지만 새로 변경은 가능하다.
    1. GRUB 부트로더 : 우분투를 부팅할 때 처음 나오는 선택화면
        - 사용이유와 특징
            1. BOOT정보를 사용자가 임의로 변경해 부팅가능.
            2. 나중에 비밀번호를 잊었을 때 root로 접속해서 비번을 바꿀 수 있는 유일한 수단.
            3. 
        - 사용법
            1. root 사용자로 접속한다.
            2. 
    2. 부팅 시 검은 화면에서 마우스를 클릭하면 ESC를 눌러 "GRUB"의 메뉴 화면을 올리자.ㅈ

# 4. Network 지식 / 넷트워크 연결 오류 해결
1. IP 주소 : 넷워크 상에서 컴터를 구분할 때 유일하게 중복되지 않는 식별자.
1. Port(포트): TCP,UDP 포트의 줄임말. 가상의 논리적 통신 연결변호. IP주소가 정문이면 포트번호는 건물 내부 방번호. 모든 PC엔 0~2^16 만큼의 포트번호가 있음. 일반적으로 0~2^10까지 예약된 포트번호가 많음
2. DNS
    - 4개의 각 8비트 주소를 갖고 있음.
    - 역할 : URL이름을 IP주소로 변경. 웹에서 https://www.nate.com을 입력시 /etc/resolve.conf 파일에 설절된 DNS서버에 해당 URL의 IP유무를 묻는다. 그리고 DNS 서버가 URL의 IP를 찾아내면 웹에 IP를전송시켜 웹에서 접속이 된다.
    - 고장시 IP주소를 알아내서 접속하는 수 밖에는 없다.
    - 공인된 DNS 서버
        1. 8.8.8.8 / 8.8.4.4 : GOOGLE에서 제공하는 DNS서버(NAME서버 : 아마 거의 모든 URL을 갖고있는 서버라서 NAME인듯). 전 세계 어디서든 이 주소를 사용가능.
        2. 168.126.63.1/168.126.63.2 : KT
        3. 219/250.36.130/210.220.163.82 : SK BROAD BAND
        3. 164.126.101.2/203.248.252.2 : LG U+
3. ubuntu network ketword
    1. ens32 : network 장치 이름이 ens32
    2. dhcp4 : 자동 IP의 사용 여부를 지정. no 는 고정 ip를 사용함을 의미.
    3. addresses [ip주소/netMask] : 고정 ip 주소와 넷마스크 값을 지정한다. netMast==24는 255.255.255.0과 동일의미다.
    4. gateweay4 : ip주소 : 게이트웨이 장치의 주소를 지정
    5. nameservers : DNS 서버의 주소를 지정
        - addresses : DNS 서버의 IP주소를 지정함.
4. Desktop 과 Server에서 주소 변경하는 법
    - Desktop,server 공통 파일 : /etc/resolv.conf, 각 버전마다 영구적 주소 변경 파일이 다른데, 유일하게 넷워크에 관한 공통파일
        + resolv.conf 는 실제로 URL을 조회할 때 접근하게 되는 파일이다. DNS정보가 담겨있고 각 버전의 IP주소 파일을 참고해서 REBOOT할 때마다 영구주소 파일의 DNS 정보를 가져와 덮어쓴다.
    - DESKTOP
    ```
    nano /etc/NetworkManager/system-connections/유선\ 연결\ 1.nmconnection 

    ```
    - SERVER
    ```
    nano /etc/netplan/0 +TAP키로 자동완성
    ..->수정
    nano /etc/netplan/*.yaml 
    reboot
    cat /etc/resolv.conf -> 수정된 dns 확인가능.
    ```
- 넷트워크 연결 오류 해결
    0. systemctl restart NetworkManager 로 넷워크 재설정(초기화, 왜냐면 주소파일은 모두 중심주소파일을 덮어씌우는 것이기 때문). 이후에도 안 되면 아래 진행
    1. DNS SERVER 할당 확인 : DNS에서 URL의 주소를 IP로 연결하기 때문에 제일 먼저 확인해본다.
    ```
    1. root@server에서 slookup , 이 예제를 쓸 당시엔 나는 안됨
    2. nano /etc/resolv.conf 에 들어가서 DNS 확인
    nameserver 127.0 -> 가장먼저 연결되는 주소가 이상함. 127.0.0.xx 는 유선 연결1/*.yaml 파일에 설정된 네임서버인 dns=192.168.111.2;를 자동 연결해준다.
    options edns0
    nameserver 8.8.4 -> 제일 첫번째 자리가 비어 있어서 1번 네임서버가 고장나도 2번도 문제가 있어서 갈 곳이 없다.
    ```
    2. ping 사용
    ```
    ping www.naver.com -> 사용시 연결이 된다면 즉각 반응이 오고, 연결이 안 되면 시간이 오래가면서 결국 암 것도 안 나옴.
    ```


# 6. Server USE/management and commander
+ 서버/클라이언트
    - EX): NAVER, 네이버라는 웹서버가 작동되고 사람들은 웹브라우저 , 즉 웹 클라이언트 프로그램(CHROME, FIREFOX, EXPLOREROR)
    - 특징
        1. 서버 접속을 위해선 클라이언트가 필수.
        2. 서버가 리눅스여도 클라이언트는 달라도 됨. THAT IS, 서버 OS,CLIENT OS는 달라도 됨.
        3. 단, 서버프로그램은 특정 클라이언트를 원함
            - 웹 서버 (APACH, IIS), 웹 클라이언트(CHROME,FIREFOX,MOZILLA ..)
            - 텔넷 서버, 텔넷 클라이언트(TELNET)
            - FTP SERVER , FTP CLIENT ...

- 텔넷 server : 보안에 취약하고(오래된 방법이라) 인기는 떨어져도 보편적인 원격접속 방법. 요즘은 텔넷에 보안기능을 더해서 사용.
    - 취약파트 : 서버/클라이언트 사이에 데이터 송수신 중 암호화가 되지 않아 해킹위험에 노출됨. 따라서 아이디/비밀번호 해킹은 매우 단순.
    - 사용조건
        1. Lunux server에 텔넷 서버가 설치되었다면, 원격지 Linux server의 PC도 텔넷 클라이언트 프로그램이 설치되어 있어야 한다.
            - ※그러나 대부분 운영체제에 기본적으로 텔넷클라이언트 프로그램이 내장되어 있어서 큰 문제는 없을 것.
    - 설치과정: #4를 참고
        1. dpkg ls telnetd : 텔넷 패키지 설치 여부 확인. 처음에는 없음
        2. apt -y install xinetd telnetd
        ##### telnet서버 가동 설정 과정
        3. cd /etc/xinetd.d
        4. touch telnet
        5. telnet을 nano/gedit같은 걸로 열기
        6. 아래와 같이 작성한다
        ```
        service telnet
        {
                disable=no
                flags=REUSE
                socket_type=stream
                wait=np
                user=root
                server=/usr/sbin/in.telnetd
                log_on_failure +=USERID
        }
        ```
        7. adduser teluser, 비번은 teluser지정하면 나머지는 default
            - groupadd --gid 1997 telnetork
            - adduser --gid 1997 teluser
        8. systemctl status xinetd , 액티브상태가 active(running)임을 확인.
        9. systemctl restart xinetd
        10. systemctl status xinetd, 액티브는 그대로인데 아래 빨간 줄이 나온 것이 확인된다.
        11. ufw allow 23/tcp, 방화벽에서 텔넷에게 23번 포트를 허용. 포트는 넷트워크 용어 확인
        12. 
- OpenSSH server : 리눅스에서 지원하는 서버, TELNET의 취약점이 보완된 서버이다. 보안강화된 TELNET 서버도 있으나 실무에선 SSH서버를 많이 사용한다.
    - 설치과정 : #4를 참고
        1. system restart ssh
        2. systemctl list-unit-files | grep ^ss : 서비스의 상태 확인.
            - ssh.service : enable
            - ssh@.service : static
            - sshd.service : enable , systemctl disable ssh 하면 사라지는 것 이유는 모름
            - ssh.socket : disable
        3. systemctl enable ssh
        4. systemctl status ssh : 3번과정이 없어도 enable이었음. enable 이라고 초록색이 등장.
        5. ufw allow 22/tcp : 방화벽에서 ssh의 포트인 22번을 허용
- XRDP SERVER : 그래픽지원이 가능한 장점이 있음
# 사용자 변경
- su 를사용 
    1. su - username , 현재 리눅스에 등록된 user의 이름을 적고 pw를 적으면 접속이 된다
- docker 사용위한 사용자 GROUP 변경
    1. docker ps 같은 걸 하면 permission denied 뜸, 
    2. sudo usermod -a -G docker $USER 치고 재접속해서 id 치면 ___(docker) 가 나옴 
# 관리자 변경
- sudo -i 를 사용 , 어떤 유저상태에서도 이걸 사용하면 root로 변경됨
# 루트접근불가
- step
    1. root권한이 있는 ID로 이동한다
        - su name
        - pass -> name의 비번
    2. sudo -i 로 root에 접근한다
    3. nano /etc/sudoers로 들어간다
        - sudoers 에 계정이름이 들어가야 root권한이 생긴다
    4. 맨 아래에 보면 USERNAME ALL=(ALL:ALL) ALL 이 있는데 USERNAME에 SUDO권한을 주고 싶은 유저를 입력하고 저장하면 된다
# 비밀번호변경
- root
    - 다른 사용자에서 
        1. sudo passwd root -> 여기서 변경
# 앱설치
- For all user
    1. root에서 설치하면 됨
# python
- pip 설치
    - python3 을 치고 버전을 한 번 확인하고
    - apt-get install python3-pip 을 해서 설치 ㄱㄱ , python-pip 하면 2.~ 버전이 설치되니까 조심하셈
# docker설치
- google에 ubuntu docker install
- 들어가서 명령어 순서대로 README의 명렁어 더미 실행을 참고해서 모든 명령어를 file에 넣기
- ./file 로 실행하면 ㅇㅋ
