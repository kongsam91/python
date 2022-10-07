# physupport(暫定) 

physupport 是個物理系ip被動監測程式，目前不具有主動改變任何事的功能🙂 

## 目前檔案

- phycr.py

    library，裡面只裝其他檔案會呼叫到的class

- chronos.py
    
    chronos 科羅諾斯為古希臘中掌管時間之神。
    
    此程式會生生不息的運行直到時間終止那刻，我們把這種程式叫做 deamon

    chronos 會進入cisco主機並詢問目前有多少主機在cisco的mactable裡面，
    接著把有出現的主機的當下時間更新到ipdb裡面

- legoman.py
    
    cli - command line interface 讓你可以用指令列來顯示資料💕


## bugs and problems
### 主要問題
我主要的想法是希望能擴展ipdb的功能，甚至擴展到監測流量，事實上網管的權限比你想像中的大很多的

我認為用 deamon 監測ip狀態應該是個不錯的方法，網頁的主要功能已經12年惹(從2006 timdream 一個很猛的學長和他的好夥伴做出來之後就好像沒什麼功能更新)

利用 deamon 把抓到的資料塞回db中，再利用web做分析會是個比較好的做法，因為cli的上手難度比較高，真心推薦😉


### 不重要的問題
目前legoman 還不具有抓ipdb中資料的功能，他只能依賴舊的 palamedes.py 產出的devices file來解析


