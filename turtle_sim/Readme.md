## turtle sim 예제 실행

### roscore과 rosrun을 통한 실행

```bash
# 마스터 실행
roscore
# turtlesim node 실행
rosrun turtlesim turtlesim_node
# turtlesim을 키도드 방향키로 제어할 수 있는 노드 실행
rosrun turtlesim turtle_teleop_key
# 노드간 통신 시각화
rqt_graph
```
```bash
# 노드 목록 확인
rosnode list
# 토픽 목록 확인
rostopic list
# 토픽 목록 자세히 확인
rostopic list -v
```

### 패키지 생성

```bash
cd ~/ros_ws/src
# init_pkg라는 이름의 패키지를 만들고 std_msgs와 rospy를 담는다는 의미
catkin_create_pkg init_pkg std_msgs rospy 
cd ~/ros_ws
catkin_make
rospack list | grep init
```

### rosrun을 통한 파이썬 코드 실행 -> ~/ros_ws/src/init_pkg/src 폴더 하위에 talker.py, listner.py 생성
```bash
chmod 776 talker.py
chmod 776 listener.py
ls -al talker.py
ls -al listener.py
```
```bash
roscore
rosrun turtlesim turtlesim_node
rosrun init_pkg talker.py
rosrun init_pkg listener.py
rqt_graph
```
<img width="646" height="417" alt="turtle_node" src="https://github.com/user-attachments/assets/3fab5524-2fed-4ce9-8e06-932991453f46" />

### roslaunch를 통한 실행 -> 노드간 통신에 필요한 노드를 launch파일에 저장하여 roscore을 실행하지 않고도 프로그램 실행 가능
```bash
cd ~/ros_ws/src/init_pkg
mkdir launch
# luanch 파일 작성
code talk-listen.launch
roslaunch init_pkg talk-listen.launch
```
<img width="721" height="433" alt="image" src="https://github.com/user-attachments/assets/842403a7-38f8-4259-aba5-df31a0622f1d" />
<img width="577" height="355" alt="image" src="https://github.com/user-attachments/assets/f189d1e4-f5c8-4ec3-9420-33952d80b455" />



