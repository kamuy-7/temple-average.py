import streamlit as st
from PIL import Image

st.title('ポートフォリオ')
st.caption('Python matplotlib グラフ作成')
st.text('概要:気象データをCSVファイルで読み込み１年間の最高気温と\n'
        '最低気温のグラフを作ってみました。')

image = Image.open("kion1.png")
st.image(image, width=800)
image2 = Image.open("kion2.png")
st.image(image2, width=800)
image3 = Image.open("kion3.png")
st.image(image3, width=800)

st.text('感想:姫路市の１年間の最高気温のグラフを作ってみましたが\n'
        '年月の縦書きと文字コードの指定に苦労しました。')