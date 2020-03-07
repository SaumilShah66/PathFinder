# PathFinder

This code is the implementation of Dijkstra's shortest path planning algorithm. Given a start and end point, this code will give you the shortest path a robot can take to move from start point to end point. 

## Dependencies
- python3
- Numpy
- OpenCV
- matplotlib

To find the path with assuming that robot is a point robot and doesn't have any dimentions, use following command.
```
python3 Dijkstra_point.py --Start="[5,5]" --End="[290,190]" --ShowAnimation=1 --Framerate=30
```

To get the optimum execution time of code, please set ```--ShowAnimation=0``` . You can use framerate according to the details of explored path. Low framerate might take longer time to execute because of higher time complexity because of showing more number of frames.

To find the path of robot with given radius and required clearance, use following command.

```
python3 Dijkstra_rigid.py --Start="[5,5]" --End="[290,190]" --RobotRadius=2 --Clearance=2 --ShowAnimation=1 --Framerate=30
```