import streamlit as st
# import predict_pricechange


def main():
    st.title('TCG カードの価格変動予測')
    st.sidebar.title("設定")
    
    if '画面' not in st.session_state:
        st.session_state["画面"] = "予測の対象"

    choices=["未選択","単一のカード","カードセット"]
    choice="未選択"

    
    choice=st.sidebar.radio("予測の対象",choices)
    
   

    if choices.index(choice)==1:
        card_name=st.sidebar.text_input('カード名')
        card_converted_manacost=st.sidebar.text_input('数値換算したマナコスト',key=1)
        card_power=st.sidebar.text_input('攻撃力')
        card_taughness=st.sidebar.text_input('体力')
        card_text_=st.sidebar.text_input('能力')
        has_flavor=st.sidebar.text_input('フレーバテキストの有無')
    elif choices.index(choice)==2:
        cardset=st.sidebar.text_input('カードセットの略称', max_chars=3,key=2)
    
    
    

    
    
if __name__ == "__main__":
    main()