import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Button_pb2 import Button
import time


st.title('Streamlit 超入門')
# st.write('DataFrame')
st.write('Display Image')

st.write('プログレスバーの表示')
'start!'


latest_iteraction = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteraction.text(f'Iteraction {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)






left_column, right_colume = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button :
    right_colume.write('ここは右カラム')



expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容1の内容')

expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容2の内容')

expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ内容3の内容')


option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は',option,'です。'



text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は',text,'です。'


condition = st.slider('あなたの調子は？',0,100,50)
'コンディション',condition


if st.checkbox('Show Image'):
    img = Image.open('kiyomizu.jpeg')
    st.image(img, caption='清水寺', use_column_width=True)











# option = st.selectbox(
#     'あなたが好きな数字を教えて',
#     list(range(1,11))
# )









# if st.checkbox('Show Image'):
#     img = Image.open('prof.png')
#     st.image(img, caption='Taiko', use_column_width=True)




# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """












# df = pd.DataFrame(
#  np.random.rand(20, 3),
#  columns=['a', 'b', 'c']
# )


# 折れ線
# st.line_chart(df)

# 折れ線色埋め
# st.area_chart(df)

# 棒グラフ
# st.bar_chart(df)









# df = pd.DataFrame(
#  np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
#  columns=['lat', 'lon']
# )

# st.map(df)









