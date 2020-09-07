def filter_words(st):
    while "  " in st:
        st = st.replace("  ", " ")
    return st.lower().capitalize().strip()
