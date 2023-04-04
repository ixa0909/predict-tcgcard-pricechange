import streamlit as st
# import predict_pricechange

def main():
    st.title('TCG カードの価格変動予測')
    st.sidebar.title("設定")
    choices=["単一のカード","カードセット"]
    choice=st.sidebar.radio("予測の対象選択方法",choices)
    
    if choices.index(choice)==0:
        card_name=st.sidebar.text_input('カード名')
        card_converted_manacost=st.sidebar.text_input('数値換算したマナコスト',key=1)
        card_power=st.sidebar.text_input('攻撃力')
        card_taughness=st.sidebar.text_input('体力')
        card_text_=st.sidebar.text_input('能力')
        has_flavor=st.sidebar.text_input('フレーバテキストの有無')
    else:
        cardset=st.sidebar.text_input('カードセットの略称', max_chars=3)
    
if __name__ == "__main__":
    main()