# 0. Hardware 정보
# 1. 하드디스크 장착후 연결

# 0. Hardware 정보
1. SATA SLOT : 메인보드에 케이블을 꽂을 수 있는 홈. 개당 30개 SATA장치를 장착 가능. SATA 0 ... SATA 1 로 표현 가능
2. SCSI : 하드디스크가 주로 사용하는 방식, 컴퓨터 메인보드에 주변기기를 연결할 때 직렬 방식으로 연결하는 표준 방식.
3. SATA : SERIAL ATA, 하드디스크/광학 드라이버 간 데이터 전송 목적의 데이터 BUS의 일종. 전송선 끝이 SIGNAL 파트와 전력 파트가 나뉘어져 있는 형태임.
4. 하드디스크,CD/DVD : IDE(EIDE),SATA 장치들이라고 할 수 있음.
    - 하드D : 서버용으로 SCSI HD,SSD(NVMe,FLASH MEMORY사용가능) 사용이 가능.
    - pc용으로 SATA를 사용하며 서버용으로 SA-SCSI(Serial Attached SCSI)를 주로 사용한다. SCSI는 최대 16개, SA-SCSI는 최대 65,535개까지 연결할 수 있다.

5. 리눅스 SCSI 하드디스크 정보
    - 하드디스크가 장착되면 자동으로 인식된다. abcd..순으로 추가된다.
    - HD directory : /dev
    1. /dev/sda : 리눅스에서 처음 장착된 SCSI하드디스크 이름.
        - 파티션
            1. /dev/sda1 : sda안에 1번 파티션, 예제선 4GB를 할당
            2. /dev/sda2 : 2번 파티션, 예제선 76GB 자동할당
            3. ...
    2. /dev/sdb : 2번쨰
    3. /dev/sdc : 3번째
    4. /dev/sdd : 4번째


# 1. 하드디스크 장착후 연결
1. 하드디스크 추가
    - ※정보 : 리눅스에선 HD추가가 WINDOWS처럼 간단하지 않다.
        1. 용량이 큰 하드디스크 장착하면 포맷하는 시간이 오래 걸림. 
        2. 하드디스크 장착후 최소 1개 이상의 파티션 지정을 해줘야 한다. 특별한 경우가 아니면 1개만 해줘도 된다.
        3. Primary/extended Partition 두개가 존재. HD에 primary 최대 4개 지정가능하고 책에선 
        4. 섹터와 블록
            + 섹터 : 한 섹터당 512 Bytes. 2097152 sectors에 512를 곱하면 1,024MB 1GB 이다. 아래는 하드디스크 접속후 정보를 띄운 것.
            ```
            Device     Boot Start     End Sectors  Size Id Type
            /dev/sdb1        2048 2097151 2095104 1023M 83 Linux
            ```
            + boot start 가 2048 sector(2048*512=1048576Bytes)인 이유는 
            + 블록 : Blocks 의 단위는 1024Bytes
        5. file system : 
        4. 파티션을 만든 다음엔 mount cmd를 사용해서 특정한 티렉토리(폴더)에 마운트 시켜야한다. -> /지정이름 의 mkdir하면 된다.
        
    - 요약순서
        1. 하드디스크 장착
        2. fdisk
        3. 파티션나누기 ->/dev/sdb1
        4. 파일시스템 생성 ->mkfs.ext4
        5. 하디드스크 완성 -> /dev/sdb1
        6. mount
        7. /mydata 라는 directory 로 mount
        8. /etc/fstab에 등록
        9. reboot 하면 끝.
    - 실습
        1. 한개의 primary partition 생성
        