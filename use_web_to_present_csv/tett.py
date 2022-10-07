import streamlit as st #https://blog.jiatool.com/posts/streamlit/
from st_aggrid import AgGrid 
import pandas as pd 

readPath = "./2022_03_03_22_44_30 time4 PIN 0.txt"
st.success("表格")
df = pd.read_table(  
                        readPath
                        ,sep=' '          #sep=' '中間的空白記得打 要不然會有報錯 
                        ,header=6
                        ,encoding='ANSI'  #看你記事本右下的編碼形式
)
AgGrid(df)

#在cmd 打 streamlit run [檔名] 執行此程式