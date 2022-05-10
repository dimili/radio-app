import streamlit as st


#@st.experimental_memo
def m3u_to_list(filename):
    name = []
    url = []
    with open(filename) as fh:
        for line in fh.read().split("\n"):
            line = line.strip()
            if not line.startswith("#"):
                url.append(line)
            else:
                name.append(line)
    return name, url

n,u = m3u_to_list("athens-radio.m3u")
lst = [e[10:] for e in n[1:]]


stations = dict(zip(lst,u))

st.write(
    """
    ### Radio streaming
    """
)

s = st.selectbox('Select radio station', options=list(stations.keys()))

st.audio(stations[s])
    

# Run
# !streamlit run streamlit_app.py