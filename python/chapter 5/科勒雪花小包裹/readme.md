# 科勒曲线
- 用python绘制科赫曲线(一次科赫曲线转换)
- 三分之一直线 旋转60度，三分之一直线，旋转60度，再有三分之一直线
# 科赫雪花怎么绘制
```python
import turtle
def koch(size,j):
    if j == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
          turtle.left(angle)
          koch(size/3,n-1) 
```
# 绘制科赫雪花
