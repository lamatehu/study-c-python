# pyinstaller库的使用
|参数|描述|
|----|-|
|-h| 查看帮助|
|--clean|清理打包过程中的临时文件|
|-D,-onedir|默认值，生成dist文件夹|
|-F,onefile|在dist文件夹中只生成独立的打包文件|
|-i<图标文件名.ico>|指定打包程序使用的图标(icon)文件|

```python
pyinstaller -i xxx.ico -F xxx.py
```
