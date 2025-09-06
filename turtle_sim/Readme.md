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

