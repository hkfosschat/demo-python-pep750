# PEP 750 - Template Strings 使用示簵

這個源碼庫放了 YouTube 頻道「[我哋講開][hkfosschat]」內
[其中一集][hkfosschat-episode]使用的指令及代碼。


## 檔案

這些檔案包含影片示範大的代碼，新的 t-string 需要用 Python 3.14
（或者它的 rc 版本）運行：

- [demo1.py](demo1.py)：示範基本的 string formatting
- [demo2.py](demo2.py)：示範使用 f-string 處理 SQL 的問題
- [demo3.py](demo3.py)：示範使用 t-string 處理 SQL 的一個解法


## 如何使用 Docker 執行 Python 3.14rc

如果你懂得安裝及使用 [Docker][docker-get-started], 你可以
使用 Docker 去執行官方發佈的 Python 3.14rc image：

```bash
docker run -it --rm python:"3.14-rc"
```

由於使用了 `--rm` 選項，這個執行環境會在你關閉或離開 Python 的
[REPL 互動介面][python-repl]時自動刪除。

若果想在環境內使用 pip 安裝額外的套件，可以指定使用 [bash][bash]
指令，以進入 bash 的環境執行其他指令：

```bash
docker run -it --rm python:"3.14-rc" bash
```

## 如何安裝 sqlescapy

[demo2.py](demo2.py) 及 [demo3.py](demo3.py) 需要使用 [sqlescapy][sqlescapy]
套件（目前的版本是 1.0.1），pip 安裝指令：

```bash
pip install sqlescapy
```

或者指定版本安裝：

```bash
pip install sqlescapy==1.0.1
```

[hkfosschat]: https://www.youtube.com/@hkfosschat
[hkfosschat-episode]: https://youtu.be/Gyr3sluwUJE
[pep-750]: https://peps.python.org/pep-0750/
[docker-get-started]: https://www.docker.com/get-started/
[python-repl]: https://realpython.com/python-repl/
[bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[sqlescapy]: https://pypi.org/project/sqlescapy/
