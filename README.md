# ROS

## ROS의 개념
- 로봇 소프트웨어를 개발하는데 필요한 소프트웨어의 집합체
- 각종 센서와 모터를 프로그래머가 편하게 사용할 수 있도록 지원
- 표준화된 통신 프로토콜을 따르는 이기종간의 메시지 교환이 가능
- 통신의 topic의 publish 및 subscribe 기반의 메시지 교환 방식으로 진행

## ROS 용어
- Master : node 사이의 통신을 총괄 관리
- node : 실행 가능한 최소 단위의 프로세스로써, topic을 주고 받는 통신주체
- message : node간에 통신할 수 있는 채널(1:1, 1:N 통신가능)
- publisher(발행자) : topic을 만들어 보내는 노드
- subscriber(구독자) : topic을 받는 노드
- package(패키지) : 하나 이상의 노드와 노드 실행을 위한 정보들은 묶어놓은 것

## 워크 스페이스 생성 및 빌드
```bash
mkdir -p ~/${work_space_name}/src # mkdir -p ~/ros_ws/src
cd ~/${work_space_name} # cd ~/ros_ws
catkin_make
ls # build, devel폴더 확인
```

## ./bashrc에 빌드 경로 추가
```bash
nano ~/.bashrc

alias cm='cd ~/ros_ws&& catkin_make'
alias cs='cd ~/ros_ws/src'
source /opt/ros/melodic/setup.bash
source ~/ros_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost

source ~/.bashrc


