[Hardware설치/메모리해제/할당](#hardware설치)

[설치/다운로드 커멘더](#설치커멘더들)

[commander: 필수 커맨더, 기본 커맨더, 사용자 커맨더](#필수_기본_사용자-커맨더)

- 한글은  한글\ 게임\ 1.plplpl 처럼 \을 써줘야 인식하나봄. 근데 꼭 그런 것도 아닌가봄.


- ufw enable : 방화벽 활성, ufw 우분투에서 제공되는 방화벽, 보안상 켜놓는 것이 좋다.
    - apt-y install net-tools 를 다운로드하고 나서 진행했다
- apt update 



- ls : ls sources.list, 있으면 있다 없으면 없다..

- apt : apt update, apt install

+ Linked file(링크 파일)은 윈도우의 바로가기 아이콘과 비슷한 개념이다. 실제 파일이 아닌 다른 파일을 가르키는 것.


# 설치커멘더들

1. dpkg : 데비안 OS에서 지원되는 패키지의 설치, 삭제, 정보 제공을 위해 사용.
    ```
    dpkg 자체는 저레벨 도구이이고 apt 같은 고급 도구들이 복잡한 패키지 관계를 모두 받아오는 일을 한다.
    ```
    - dpkg -l ,s 설치된 패키지를 체크하는 것.

2. wget <링크주소>: 링크주소 url에 접속해서 파일을 다운받는다.
    - wget https://www.naver.com//~~//mypicture.png 처럼 사용하면 된다.

3. apt-get : Debian이 제공하는 공식 저장소에 접속하여 프로그램 패키지를 다운로드하고 설치하는 명령어. 다운로드 뿐 아니라 자동으로 환경변수 설정, 파일 링크 설정, 데몬 설정이 되기에 매우 편리한다.

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
    2. filter : 필요한 것만 걸러주는 명렁어
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

# 필수_기본_사용자 커맨더

- 필수 커맨더(서버구축) 필수 commander
    [시스템 on/off명령어](#시스템-ON/OFF-CMD)
    - unix/linux 에선 소문자 대문자를 명확히 구분한다.

    1. man : manual 명렁어, 해당 명령어의 사용법이 담겨 있다. 위 아래는 화살표로, 페이지 단위는 pg up/dn을 사용한다. space / b 도 가능. 종료는 q.
        + man Section : section 1: 명령어, 2~3:프로그래밍 , 4 디바이스, 5 파일형식, 6 게임, 6 기타주제, 8 시스템 관리, 9 커널 관련 설명

    2. sudo : 관리자 명령어, "일반사용자가 관리자 권한을 얻을 때 사용한다". root사용자는 생략가능하다.
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
    #### 시스템 ON/OFF CMD
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
        3. halt -p : 시스템 완전 종료.


    + Virtual console : ubuntu에선 총 6개 가상콘솔이 제공됨. 부팅시 보이는 화면은 F2.
        1. Ctrl+Alt+F2-F7, chvt 2-7
        2. server 버전은 F1~F6

- 기본 커맨더
    [텍스트편집 커맨드](#Text-Edit-Cmd)
    
    

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
        - ls -l runlevel?.target : system폴더에 가서 runlevel0.target~runlevel1.target 의 모든 value를 봄. runlavel?.target은 링크파일이라며 각 링크파일이 실제 파일과 연결되어 있다고 한다. runlevel0.target -> poweroff.target 파일을 가르킨다.

    2. cd : change directory
        ```
        기본 사용법
            cd _: _은 경로, 경로를 이동한다
            1. cd /etc/apt
            2. cd /etc/netplan : ip편집 폴더로 이동(확장자가 없으니 폴더임)
        ```
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
        - [주의사용]rm : rm -rf root->삭제시 루트파티션삭제로 리눅스재설치, 삭제 커맨더.
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
    13. clear : 현재 터미널(shell) 화면을 지우고 깔끔한 상태로 만들기
    14. reboot : 재시작
    15. exit : 터미널 나가기
    

    ### Text Edit Cmd
    1. nano : text file 열기용.




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
        - su name or su -l (it's directly change user to sudo)
        - pass -> name의 비번
    2. sudo -i 로 root에 접근한다
    3. nano /etc/sudoers로 들어간다
        - sudoers 에 계정이름이 들어가야 root권한이 생긴다
    4. 맨 아래에 보면 section of "User privilege specification", root ALL=(ALL:ALL) ALL 이 있는데 USERNAME에 SUDO권한을 주고 싶은 유저(leekt)를 입력하고 저장하면 된다
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
