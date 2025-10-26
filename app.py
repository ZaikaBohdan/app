import streamlit as st
import pandas as pd

# Заголовок застосунку
st.set_page_config(
    page_title='Methods for modelling the processes of targeted management of complex multi-component information systems for various purposes',
    page_icon=':bar_chart:',
    layout='wide'
)

st.sidebar.header("0. Select app")
app = st.sidebar.selectbox(
    "Select app", 
    [
        "Detection and analysis of cluster structure in complex multidimensional systems", 
        "Entropy approach to detection of anomalies in UAV trajectories", 
        "Spectral feature segmentation"
    ], 
    label_visibility='collapsed'
)
st.title(app)


if app == 'Detection and analysis of cluster structure in complex multidimensional systems':
    img_path = 'imgs/app1'
    # c11, c13, c12 = st.columns([2, 1, 2])
    c11, c13, c12 = st.columns([1, 1, 1.5])  
    c11.write('## Review of loaded data')
    st.sidebar.header("Upload data")
    data_file = st.sidebar.file_uploader("Upload data", type="csv")

    if data_file:
        data = pd.read_csv(data_file)
        c11.dataframe(data, height=350)

        c12.write('## Global network structure')
        c12.image(f'{img_path}/2.jpg', width=620)

        c13.write('### Persistence barcode for Vietoris-Rips complex')
        c13.image(f'{img_path}/3.jpg', width=380)

        c21, c22 = st.columns([3, 2])
        c21.write('### Persistence diagrams of Vietoris-Rips complex')
        c21.write('')
        c21.image(f'{img_path}/4.jpg')

        c22.write('## Ego-networks')
        c22.image(f'{img_path}/1.jpg', width=600) 


if app == 'Entropy approach to detection of anomalies in UAV trajectories':
    img_path = 'imgs/app2'

    c11, c12, c13 = st.columns([1, 1, 1.3])  
    c11.write('## Review of loaded data')
    st.sidebar.header("Upload data")
    data_file = st.sidebar.file_uploader("Upload data", type="csv")

    if data_file:
        data = pd.read_csv(data_file)
        c11.dataframe(data, height=330)

        c12.write('## Q statistics for selected agent and run')
        c12.image(f'{img_path}/1.png')

        c13.write('## Spatial distribution of anomalies on the movement trajectories')
        c13.image(f'{img_path}/2.png')
 
        st.sidebar.header("Select agent and run for visualisations")
        st.sidebar.number_input("Agent №", value=0)
        st.sidebar.number_input("Run №", value=0)
        st.sidebar.button("Generate")

        c21, c22, c23 = st.columns([1, 1, 1])
        c21.write('## Anomaly map: agents vs time')  
        c21.image(f'{img_path}/3.png')
        
        c22.write('### Heatmap of Q-statistics anomaly localization for selected agent')  
        c22.image(f'{img_path}/4.png')
        
        c23.write('### Distribution of Q-statistics: normal and detected anomalous states')  
        c23.image(f'{img_path}/5.png') 

        c31, c32 = st.columns([1, 2.2]) 
        c31.write('### Spatial density of anomalies in all agents and runs')  
        c31.image(f'{img_path}/6.png') 

        res = pd.read_csv('data/result.csv')
        c32.write('## Resulting data with marked anomalies')
        c32.dataframe(res, height=450)

        st.sidebar.header("Download results")
        st.sidebar.download_button(
            label="📥 Download result.csv",
            data=res.to_csv(index=False),
            file_name='result.csv',
            mime='text/csv',
        )


if app == 'Spectral feature segmentation':
    c11, c12 = st.columns([1, 2])  
    c11.write('## 1. Review of loaded data')
    st.sidebar.header("1. Upload data")
    data_file = st.sidebar.file_uploader("Upload data", type="csv")

    if data_file:
        # Зчитування даних
        data = pd.read_csv(data_file)
        # Відображення даних
        c11.dataframe(data, height=270)

        # "Вибір" ознак для відображення карт
        c12.write('## 2. Spatial maps of features')
        st.sidebar.header("2. Choose features for spatial map building")
        features = st.sidebar.multiselect(
            "Show spatial maps for", 
            ['BLUE', 'GREEN', 'RED', 'RE1', 'NIR', 'SWIR1', 'SWIR2', 'NDVI', 'EVI2','NDWI', 'DEM', 'slope', 'aspect', 'SoilMoisture', 'LST'], 
            default=['EVI2', 'LST', 'NDVI']
        )
        st.sidebar.button("Show spatial maps")
        # Відображення карт
        c1, c2, c3 = c12.columns(3)
        c1.image('imgs/app3/2_evi2.png') 
        c2.image('imgs/app3/2_lst.png') 
        c3.image('imgs/app3/2_ndvi.png')

        c21, c22 = st.columns([3, 1])    
        c21.write('## 3. Topological and entropy diagnostics of the ε-graph for spectral feature segmentation')
        c21.write('')
        c21.write('')
        st.sidebar.header("3. Choose ε (dotted line on graphs)")
        eps = st.sidebar.number_input('', value=1.23, step=0.01, label_visibility='collapsed')
        st.sidebar.button("Show ε on graphs")
        c31, c32, c33 = c21.columns(3)
        c31.image('imgs/app3/31.png') 
        c32.image('imgs/app3/32.png')  
        c33.image('imgs/app3/33.png')

        c22.write('## 4. Spectral feature segmentation map')
        st.sidebar.header("4. Genereate spectral feature segmentation map (based on ε)")
        st.sidebar.button("Generate")
        c22.image('imgs/app3/41.png')