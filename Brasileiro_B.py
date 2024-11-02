import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
#from PIL import image
import numpy as np
import pandas as pd
#from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
import plotly.express as px
import io
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
from sklearn.decomposition import PCA
from PIL import Image
import seaborn as sns
from matplotlib import cm


df = pd.read_csv("jogadores.csv")
df1 = pd.read_csv("jogador.csv")


with st.sidebar:

    jogadores = df["Atleta"]
    choose = option_menu("Galeria de Apps", ["Melhores do Brasileirão-2024", "Ranking de Jogadores", "Compare Jogadores"],
                         icons=['sort-numeric-down', 'graph-up-arrow', 'question-lg'],
                         menu_icon="universal-access", default_index=0, 
                         styles={
                         "container": {"padding": "5!important", "background-color": "#fafafa"},
                         "icon": {"color": "orange", "font-size": "25px"},
                         "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                         "nav-link-selected": {"background-color": "#02ab21"},    
                         })

if choose == "Melhores do Brasileirão-2024":
    
    #CABEÇALHO DO FORM
    st.markdown("<h1 style='text-align: center;'>Melhores do Brasileirão até a Rodada 25</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>app by @JAmerico1898</h6>", unsafe_allow_html=True)
    st.markdown("---")

    df6 = pd.read_csv("Posições.csv")

    #ligas = ("MG", "RJ", "RS", "SP")
    posições = df6["Posição"]
    #temporada = 2024
    #liga = st.selectbox("Escolha a Liga", options=ligas, index=None)
    #posição = st.selectbox("Escolha a posição", options=posições, index=None)
    posição = st.radio("Escolha a Métrica Posição", options=posições, label_visibility="visible")
    import pandas as pd
    import numpy as np
    import streamlit as st

    if posição == "Goleiro":
        st.markdown("<h4 style='text-align: center;'>5 Goleiros Clássicos Mais Bem Ranqueados</h4>", unsafe_allow_html=True)
        tabela_3 = pd.read_csv("1_Role_Goleiro.csv")
        tabela_3 = tabela_3.iloc[:, np.r_[1, 30, 3, 10:12, 18:25]]
        tabela_3 = tabela_3.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Posição_Wyscout':'Posição', 'Versão_Temporada':'Janela de Análise', 'Interceptações.1':'Interceptações'})
        tabela_3 = tabela_3.sort_values(by='Rating', ascending=False)
        tabela_31 = tabela_3.iloc[:, np.r_[0:5]]
        tabela_31 = tabela_31.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_31.iloc[:, 1] = tabela_31.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_32 = tabela_3.iloc[:, np.r_[0, 5:12]]
        tabela_32 = tabela_32.rename(columns={'Atleta':'Métricas'})
        tabela_32 = tabela_32.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_32.columns = tabela_32.iloc[0]
        tabela_32 = tabela_32.drop(tabela_32.index[0])
    #    tabela_32 = tabela_32.rename(columns={'Atleta': 'Métricas'})
        # Create the new "Métricas" column with the specified content
    #    new_metrica_column = ["Duelos_Aéreos_Ganhos", "Defesas", "Gols_Evitados", "Saídas", "Interceptações", "xG_Evitado", "Finalizações_por_Gol_Sofrido"]

        # Insert the new column after the first "Métricas" column
    #    tabela_32.insert(0, 'Métricas', new_metrica_column)    

    #    tabela_33 = tabela_32.reset_index().rename(columns={'index': 'Métricas'})
        
        # Format the values in the metrics table
        tabela_32.iloc[:, 0:7] = tabela_32.iloc[:, 0:7].applymap('{:.2f}'.format)
        
        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.reset_index(drop=True)
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Center headers except first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px', 'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            styled_html = style_table(tabela_31).to_html(index=False, escape=False)
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            '''  # Properly close the div tag
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'>Métricas dos 5 Goleiros Clássicos Mais Bem Ranqueados</h4>", 
                        unsafe_allow_html=True)

            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_32).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)
            
        

        st.markdown("<h4 style='text-align: center;'><br>5 Goleiros Líberos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_4 = pd.read_csv("2_Role_Goleiro_Líbero.csv")
    #    tabela_4 = tabela_4[(tabela_4['Liga']==liga)&(tabela_4['Versão_Temporada']==temporada)]
        tabela_4 = tabela_4.iloc[:, np.r_[1, 33, 3, 10:12, 18:28]]
        tabela_4 = tabela_4.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Posição_Wyscout':'Posição', 'Versão_Temporada':'Janela de Análise', 'Interceptações.1':'Interceptações'})
        tabela_4 = tabela_4.sort_values(by='Rating', ascending=False)
        tabela_41 = tabela_4.iloc[:, np.r_[0:5]]
        tabela_41 = tabela_41.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_41.iloc[:, 1] = tabela_41.iloc[:, 1].map('{:.3f}'.format)
        
        # Step 1: Select the required columns and transpose the dataframe
        tabela_42 = tabela_4.iloc[:, np.r_[0, 5:15]]
        tabela_42 = tabela_42.rename(columns={'Atleta':''})
        tabela_42 = tabela_42.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_42.columns = tabela_42.iloc[0]
        tabela_42 = tabela_42.drop(tabela_42.index[0])
        #tabela_42 = tabela_42.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 2 decimal places
        tabela_42.iloc[:, 0:10] = tabela_42.iloc[:, 0:10].map('{:.2f}'.format)
        
        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index and display it
            styled_html = style_table(tabela_41).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Goleiros Líberos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
                #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                #df = df.reset_index(drop=True)
                
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_42).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

    elif posição == "Lateral Direito":
        st.markdown("<h4 style='text-align: center;'>5 Laterais Direitos Defensivos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_3 = pd.read_csv("3_Role_Lateral_Defensivo.csv")
        tabela_3 = tabela_3[(tabela_3['Pé']=='right')]
        tabela_3 = tabela_3.iloc[:, np.r_[1, 29, 3, 10:12, 18:23]]
        tabela_3 = tabela_3.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_3 = tabela_3.sort_values(by='Rating', ascending=False)
        tabela_31 = tabela_3.iloc[:, np.r_[0:5]]
        tabela_31 = tabela_31.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_31.iloc[:, 1] = tabela_31.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_32 = tabela_3.iloc[:, np.r_[0, 5:10]]
        tabela_32 = tabela_32.rename(columns={'Atleta':''})
        tabela_32 = tabela_32.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_32.columns = tabela_32.iloc[0]
        tabela_32 = tabela_32.drop(tabela_32.index[0])
        #tabela_32 = tabela_32.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_32.iloc[:, 0:6] = tabela_32.iloc[:, 0:6].map('{:.2f}'.format)
    
        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            styled_html = style_table(tabela_31).to_html(index=False, escape=False)
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            '''  # Properly close the div tag
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Laterais Direitos Defensivos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)

            # Assuming your DataFrame is ready and you want to apply the colormap
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_32).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)


        st.markdown("<h4 style='text-align: center;'>5 Laterais Direitos Ofensivos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_4 = pd.read_csv("4_Role_Lateral_Ofensivo.csv")
        tabela_4 = tabela_4[(tabela_4['Pé']=='right')]
        tabela_4 = tabela_4.iloc[:, np.r_[1, 38, 3, 10:12, 18:33]]
        tabela_4 = tabela_4.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_4 = tabela_4.sort_values(by='Rating', ascending=False)
        tabela_41 = tabela_4.iloc[:, np.r_[0:5]]
        tabela_41 = tabela_41.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_41.iloc[:, 1] = tabela_41.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_42 = tabela_4.iloc[:, np.r_[0, 5:20]]
        tabela_42 = tabela_42.rename(columns={'Atleta':''})
        tabela_42 = tabela_42.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_42.columns = tabela_42.iloc[0]
        tabela_42 = tabela_42.drop(tabela_42.index[0])
        #tabela_42 = tabela_42.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_42.iloc[:, 0:16] = tabela_42.iloc[:, 0:16].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_41).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Laterais Direitos Ofensivos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_42).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Laterais Direitos Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_5 = pd.read_csv("5_Role_Lateral_Equilibrado.csv")
        tabela_5 = tabela_5[(tabela_5['Pé']=='right')]
        tabela_5 = tabela_5.iloc[:, np.r_[1, 41, 3, 10:12, 18:36]]
        tabela_5 = tabela_5.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_5 = tabela_5.sort_values(by='Rating', ascending=False)
        tabela_51 = tabela_5.iloc[:, np.r_[0:5]]
        tabela_51 = tabela_51.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_51.iloc[:, 1] = tabela_51.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_52 = tabela_5.iloc[:, np.r_[0, 5:23]]
        tabela_52 = tabela_52.rename(columns={'Atleta':''})
        tabela_52 = tabela_52.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_5 as its values
        tabela_52.columns = tabela_52.iloc[0]
        tabela_52 = tabela_52.drop(tabela_52.index[0])
        #tabela_52 = tabela_52.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_52.iloc[:, 0:19] = tabela_52.iloc[:, 0:19].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            styled_html = style_table(tabela_51).to_html(index=False, escape=False)
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            '''  # Properly close the div tag
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique!")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Laterais Direitos Equilibrados Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                
                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
                #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                #df = df.reset_index(drop=True)
                
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_52).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)


    elif posição == "Lateral Esquerdo":
        st.markdown("<h4 style='text-align: center;'>5 Laterais Esquerdos Defensivos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_3 = pd.read_csv("3_Role_Lateral_Defensivo.csv")
        tabela_3 = tabela_3[(tabela_3['Pé']=='left')]
        tabela_3 = tabela_3.iloc[:, np.r_[1, 29, 3, 10:12, 18:23]]
        tabela_3 = tabela_3.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_3 = tabela_3.sort_values(by='Rating', ascending=False)
        tabela_31 = tabela_3.iloc[:, np.r_[0:5]]
        tabela_31 = tabela_31.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_31.iloc[:, 1] = tabela_31.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_32 = tabela_3.iloc[:, np.r_[0, 5:10]]
        tabela_32 = tabela_32.rename(columns={'Atleta':''})
        tabela_32 = tabela_32.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_32.columns = tabela_32.iloc[0]
        tabela_32 = tabela_32.drop(tabela_32.index[0])
        #tabela_32 = tabela_32.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_32.iloc[:, 0:6] = tabela_32.iloc[:, 0:6].map('{:.2f}'.format)
    
        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            styled_html = style_table(tabela_31).to_html(index=False, escape=False)
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            '''  # Properly close the div tag
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Laterais Esquerdos Defensivos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)

            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_32).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)


        st.markdown("<h4 style='text-align: center;'>5 Laterais Esquerdos Ofensivos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_4 = pd.read_csv("4_Role_Lateral_Ofensivo.csv")
        tabela_4 = tabela_4[(tabela_4['Pé']=='left')]
        tabela_4 = tabela_4.iloc[:, np.r_[1, 38, 3, 10:12, 18:33]]
        tabela_4 = tabela_4.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_4 = tabela_4.sort_values(by='Rating', ascending=False)
        tabela_41 = tabela_4.iloc[:, np.r_[0:5]]
        tabela_41 = tabela_41.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_41.iloc[:, 1] = tabela_41.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_42 = tabela_4.iloc[:, np.r_[0, 5:20]]
        tabela_42 = tabela_42.rename(columns={'Atleta':''})
        tabela_42 = tabela_42.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_42.columns = tabela_42.iloc[0]
        tabela_42 = tabela_42.drop(tabela_42.index[0])
        #tabela_42 = tabela_42.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_42.iloc[:, 0:16] = tabela_42.iloc[:, 0:16].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_41).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Laterais Esquerdos Ofensivos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_42).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Laterais Esquerdos Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_5 = pd.read_csv("5_Role_Lateral_Equilibrado.csv")
        tabela_5 = tabela_5[(tabela_5['Pé']=='left')]
        tabela_5 = tabela_5.iloc[:, np.r_[1, 41, 3, 10:12, 18:36]]
        tabela_5 = tabela_5.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_5 = tabela_5.sort_values(by='Rating', ascending=False)
        tabela_51 = tabela_5.iloc[:, np.r_[0:5]]
        tabela_51 = tabela_51.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_51.iloc[:, 1] = tabela_51.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_52 = tabela_5.iloc[:, np.r_[0, 5:23]]
        tabela_52 = tabela_52.rename(columns={'Atleta':''})
        tabela_52 = tabela_52.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_5 as its values
        tabela_52.columns = tabela_52.iloc[0]
        tabela_52 = tabela_52.drop(tabela_52.index[0])
        #tabela_52 = tabela_52.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_52.iloc[:, 0:19] = tabela_52.iloc[:, 0:19].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            styled_html = style_table(tabela_51).to_html(index=False, escape=False)
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            '''  # Properly close the div tag
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique!")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Laterais Esquerdos Equilibrados Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
                #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                #df = df.reset_index(drop=True)
                
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_52).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)







    elif posição == "Zagueiro":
        st.markdown("<h4 style='text-align: center;'>5 Zagueiros Clássicos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_6 = pd.read_csv("6_Role_Zagueiro_Defensivo.csv")
    #    tabela_6 = tabela_6[(tabela_6['Liga']==liga)&(tabela_6['Versão_Temporada']==temporada)]
        tabela_6 = tabela_6.iloc[:, np.r_[1, 29, 3, 10:12, 18:23]]
        tabela_6 = tabela_6.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_6 = tabela_6.sort_values(by='Rating', ascending=False)
        tabela_61 = tabela_6.iloc[:, np.r_[0:5]]
        tabela_61 = tabela_61.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_61.iloc[:, 1] = tabela_61.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_62 = tabela_6.iloc[:, np.r_[0, 5:10]]
        tabela_62 = tabela_62.rename(columns={'Atleta':''})
        tabela_62 = tabela_62.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_6 as its values
        tabela_62.columns = tabela_62.iloc[0]
        tabela_62 = tabela_62.drop(tabela_62.index[0])
        #tabela_62 = tabela_62.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_62.iloc[:, 0:7] = tabela_62.iloc[:, 0:7].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.reset_index(drop=True)
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Center headers except first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px', 'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            styled_html = style_table(tabela_61).to_html(index=False, escape=False)
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            '''  # Properly close the div tag
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'>Métricas dos 5 Goleiros Clássicos Mais Bem Ranqueados</h4>", 
                        unsafe_allow_html=True)

            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_62).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Zagueiros Construtores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_7 = pd.read_csv("7_Role_Zagueiro_Construtor.csv")
    #    tabela_7 = tabela_7[(tabela_7['Liga']==liga)&(tabela_7['Versão_Temporada']==temporada)]
        tabela_7 = tabela_7.iloc[:, np.r_[1, 33, 3, 10:12, 18:28]]
        tabela_7 = tabela_7.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_7 = tabela_7.sort_values(by='Rating', ascending=False)
        tabela_71 = tabela_7.iloc[:, np.r_[0:5]]
        tabela_71 = tabela_71.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_71.iloc[:, 1] = tabela_71.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_72 = tabela_7.iloc[:, np.r_[0, 5:15]]
        tabela_72 = tabela_72.rename(columns={'Atleta':''})
        tabela_72 = tabela_72.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_7 as its values
        tabela_72.columns = tabela_72.iloc[0]
        tabela_72 = tabela_72.drop(tabela_72.index[0])
        #tabela_72 = tabela_72.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_72.iloc[:, 0:11] = tabela_72.iloc[:, 0:11].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.reset_index(drop=True)
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Center headers except first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px', 'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            styled_html = style_table(tabela_71).to_html(index=False, escape=False)
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            '''  # Properly close the div tag
            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'>Métricas dos 5 Zagueiros Construtores Mais Bem Ranqueados</h4>", 
                        unsafe_allow_html=True)

            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_72).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)


        st.markdown("<h4 style='text-align: center;'>5 Zagueiros Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_8 = pd.read_csv("8_Role_Zagueiro_Equilibrado.csv")
    #    tabela_8 = tabela_8[(tabela_8['Liga']==liga)&(tabela_8['Versão_Temporada']==temporada)]
        tabela_8 = tabela_8.iloc[:, np.r_[1, 36, 3, 10:12, 18:32]]
        tabela_8 = tabela_8.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_8 = tabela_8.sort_values(by='Rating', ascending=False)
        tabela_81 = tabela_8.iloc[:, np.r_[0:5]]
        tabela_81 = tabela_81.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_81.iloc[:, 1] = tabela_81.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_82 = tabela_8.iloc[:, np.r_[0, 5:18]]
        tabela_82 = tabela_82.rename(columns={'Atleta':''})
        tabela_82 = tabela_82.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_8 as its values
        tabela_82.columns = tabela_82.iloc[0]
        tabela_82 = tabela_82.drop(tabela_82.index[0])
        #tabela_82 = tabela_82.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_82.iloc[:, 0:14] = tabela_82.iloc[:, 0:14].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

    # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_81).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique!")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Zagueiros Equilibrados Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_82).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

    elif posição == "Primeiro Volante":
        st.markdown("<h4 style='text-align: center;'>5 Primeiros Volantes Defensivos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_12 = pd.read_csv("9_Role_Volante_Defensivo.csv")
    #    tabela_12 = tabela_12[(tabela_12['Liga']==liga)&(tabela_12['Versão_Temporada']==temporada)]
        tabela_12 = tabela_12.iloc[:, np.r_[1, 27, 3, 10:12, 18:22]]
        tabela_12 = tabela_12.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_12 = tabela_12.sort_values(by='Rating', ascending=False)
        tabela_121 = tabela_12.iloc[:, np.r_[0:5]]
        tabela_121 = tabela_121.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_121.iloc[:, 1] = tabela_121.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_122 = tabela_12.iloc[:, np.r_[0, 5:9]]
        tabela_122 = tabela_122.rename(columns={'Atleta':''})
        tabela_122 = tabela_122.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_122.columns = tabela_122.iloc[0]
        tabela_122 = tabela_122.drop(tabela_122.index[0])
        #tabela_122 = tabela_122.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_122.iloc[:, 0:6] = tabela_122.iloc[:, 0:6].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_121).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Primeiros Volantes Defensivos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_122).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Primeiros Volantes Construtores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_13 = pd.read_csv("10_Role_Volante_Construtor.csv")
    #    tabela_13 = tabela_13[(tabela_13['Liga']==liga)&(tabela_13['Versão_Temporada']==temporada)]
        tabela_13 = tabela_13.iloc[:, np.r_[1, 32, 3, 10:12, 18:27]]
        tabela_13 = tabela_13.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_13 = tabela_13.sort_values(by='Rating', ascending=False)
        tabela_131 = tabela_13.iloc[:, np.r_[0:5]]
        tabela_131 = tabela_131.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_131.iloc[:, 1] = tabela_131.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_132 = tabela_13.iloc[:, np.r_[0, 5:14]]
        tabela_132 = tabela_132.rename(columns={'Atleta':''})
        tabela_132 = tabela_132.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_132.columns = tabela_132.iloc[0]
        tabela_132 = tabela_132.drop(tabela_132.index[0])
        #tabela_132 = tabela_132.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_132.iloc[:, 0:11] = tabela_132.iloc[:, 0:11].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            #df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

    # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_131).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique!")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 5 Primeiros Volantes Construtores Mais Bem Ranqueados Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Styling DataFrame using Pandas
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_132).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Primeiros Volantes Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_14 = pd.read_csv("11_Role_Volante_Equilibrado.csv")
    #    tabela_14 = tabela_14[(tabela_14['Liga']==liga)&(tabela_14['Versão_Temporada']==temporada)]
        tabela_14 = tabela_14.iloc[:, np.r_[1, 34, 3, 10:12, 18:29]]
        tabela_14 = tabela_14.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_14 = tabela_14.sort_values(by='Rating', ascending=False)
        tabela_141 = tabela_14.iloc[:, np.r_[0:5]]
        tabela_141 = tabela_141.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_141.iloc[:, 1] = tabela_141.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_142 = tabela_14.iloc[:, np.r_[0, 5:16]]
        tabela_142 = tabela_142.rename(columns={'Atleta':''})
        tabela_142 = tabela_142.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_142.columns = tabela_142.iloc[0]
        tabela_142 = tabela_142.drop(tabela_142.index[0])
        #tabela_142 = tabela_142.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_142.iloc[:, 0:17] = tabela_142.iloc[:, 0:17].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_141).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Primeiros Volantes Equilibrados Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_142).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

    elif posição == "Segundo Volante":
        st.markdown("<h4 style='text-align: center;'>5 Segundos Volantes Box-to-Box Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_12 = pd.read_csv("12_Role_Segundo_Volante_Box_to_Box.csv")
    #    tabela_12 = tabela_12[(tabela_12['Liga']==liga)&(tabela_12['Versão_Temporada']==temporada)]
        tabela_12 = tabela_12.iloc[:, np.r_[1, 36, 3, 10:12, 18:31]]
        tabela_12 = tabela_12.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_12 = tabela_12.sort_values(by='Rating', ascending=False)
        tabela_121 = tabela_12.iloc[:, np.r_[0:5]]
        tabela_121 = tabela_121.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_121.iloc[:, 1] = tabela_121.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_122 = tabela_12.iloc[:, np.r_[0, 5:18]]
        tabela_122 = tabela_122.rename(columns={'Atleta':''})
        tabela_122 = tabela_122.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_122.columns = tabela_122.iloc[0]
        tabela_122 = tabela_122.drop(tabela_122.index[0])
        #tabela_122 = tabela_122.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_122.iloc[:, 0:14] = tabela_122.iloc[:, 0:14].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_121).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Segundos Volantes Box-to-Box Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_122).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Segundos Volantes Organizadores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_13 = pd.read_csv("13_Role_Segundo_Volante_Organizador.csv")
    #    tabela_13 = tabela_13[(tabela_13['Liga']==liga)&(tabela_13['Versão_Temporada']==temporada)]
        tabela_13 = tabela_13.iloc[:, np.r_[1, 33, 3, 10:12, 18:28]]
        tabela_13 = tabela_13.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_13 = tabela_13.sort_values(by='Rating', ascending=False)
        tabela_131 = tabela_13.iloc[:, np.r_[0:5]]
        tabela_131 = tabela_131.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_131.iloc[:, 1] = tabela_131.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_132 = tabela_13.iloc[:, np.r_[0, 5:15]]
        tabela_132 = tabela_132.rename(columns={'Atleta':''})
        tabela_132 = tabela_132.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_132.columns = tabela_132.iloc[0]
        tabela_132 = tabela_132.drop(tabela_132.index[0])
        #tabela_132 = tabela_132.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_132.iloc[:, 0:11] = tabela_132.iloc[:, 0:11].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_131).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Segundos Volantes Organizadores Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_132).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Segundos Volantes Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_14 = pd.read_csv("14_Role_Segundo_Volante_Equilibrado.csv")
    #    tabela_14 = tabela_14[(tabela_14['Liga']==liga)&(tabela_14['Versão_Temporada']==temporada)]
        tabela_14 = tabela_14.iloc[:, np.r_[1, 36, 3, 10:12, 18:31]]
        tabela_14 = tabela_14.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_14 = tabela_14.sort_values(by='Rating', ascending=False)
        tabela_141 = tabela_14.iloc[:, np.r_[0:5]]
        tabela_141 = tabela_141.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_141.iloc[:, 1] = tabela_141.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_142 = tabela_14.iloc[:, np.r_[0, 5:18]]
        tabela_142 = tabela_142.rename(columns={'Atleta':''})
        tabela_142 = tabela_142.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_142.columns = tabela_142.iloc[0]
        tabela_142 = tabela_142.drop(tabela_142.index[0])
        #tabela_142 = tabela_142.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_142.iloc[:, 0:14] = tabela_142.iloc[:, 0:14].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_141).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique!")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Segundos Volantes Equilibrados Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_142).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

    elif posição == "Meia":
        st.markdown("<h4 style='text-align: center;'>5 Meias Organizadores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_15 = pd.read_csv("15_Role_Meia_Organizador.csv")
    #    tabela_15 = tabela_15[(tabela_15['Liga']==liga)&(tabela_15['Versão_Temporada']==temporada)]
        tabela_15 = tabela_15.iloc[:, np.r_[1, 33, 3, 10:12, 18:28]]
        tabela_15 = tabela_15.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_15 = tabela_15.sort_values(by='Rating', ascending=False)
        tabela_151 = tabela_15.iloc[:, np.r_[0:5]]
        tabela_151 = tabela_151.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_151.iloc[:, 1] = tabela_151.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_152 = tabela_15.iloc[:, np.r_[0, 5:15]]
        tabela_152 = tabela_152.rename(columns={'Atleta':''})
        tabela_152 = tabela_152.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_152.columns = tabela_152.iloc[0]
        tabela_152 = tabela_152.drop(tabela_152.index[0])
        #tabela_152 = tabela_152.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_152.iloc[:, 0:11] = tabela_152.iloc[:, 0:11].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

    # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_151).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Meias Organizadores Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                
                
                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_152).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Meias Atacantes Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_16 = pd.read_csv("16_Role_Meia_Atacante.csv")
    #    tabela_16 = tabela_16[(tabela_16['Liga']==liga)&(tabela_16['Versão_Temporada']==temporada)]
        tabela_16 = tabela_16.iloc[:, np.r_[1, 40, 3, 10:12, 18:35]]
        tabela_16 = tabela_16.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_16 = tabela_16.sort_values(by='Rating', ascending=False)
        tabela_161 = tabela_16.iloc[:, np.r_[0:5]]
        tabela_161 = tabela_161.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_161.iloc[:, 1] = tabela_161.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_162 = tabela_16.iloc[:, np.r_[0, 5:22]]
        tabela_162 = tabela_162.rename(columns={'Atleta':''})
        tabela_162 = tabela_162.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_162.columns = tabela_162.iloc[0]
        tabela_162 = tabela_162.drop(tabela_162.index[0])
        #tabela_162 = tabela_162.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_162.iloc[:, 0:18] = tabela_162.iloc[:, 0:18].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

    # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_161).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Meias Atacantes Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_162).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)


    elif posição == "Extremo":
        st.markdown("<h4 style='text-align: center;'>5 Extremos Organizadores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_17 = pd.read_csv("17_Role_Extremo_Organizador.csv")
    #    tabela_17 = tabela_17[(tabela_17['Liga']==liga)&(tabela_17['Versão_Temporada']==temporada)]
        tabela_17 = tabela_17.iloc[:, np.r_[1, 36, 3, 10:12, 18:31]]
        tabela_17 = tabela_17.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_17 = tabela_17.sort_values(by='Rating', ascending=False)
        tabela_171 = tabela_17.iloc[:, np.r_[0:5]]
        tabela_171 = tabela_171.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_171.iloc[:, 1] = tabela_171.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_172 = tabela_17.iloc[:, np.r_[0, 5:18]]
        tabela_172 = tabela_172.rename(columns={'Atleta':''})
        tabela_172 = tabela_172.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_3 as its values
        tabela_172.columns = tabela_172.iloc[0]
        tabela_172 = tabela_172.drop(tabela_172.index[0])
        #tabela_172 = tabela_172.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_172.iloc[:, 0:14] = tabela_172.iloc[:, 0:14].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)

            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_171).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Extremos Organizadores Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_172).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)
            
        st.markdown("<h4 style='text-align: center;'>5 Extremos Táticos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_18 = pd.read_csv("18_Role_Extremo_Tático.csv")
    #    tabela_18 = tabela_18[(tabela_18['Liga']==liga)&(tabela_18['Versão_Temporada']==temporada)]
        tabela_18 = tabela_18.iloc[:, np.r_[1, 30, 3, 10:12, 18:25]]
        tabela_18 = tabela_18.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_18 = tabela_18.sort_values(by='Rating', ascending=False)
        tabela_181 = tabela_18.iloc[:, np.r_[0:5]]
        tabela_181 = tabela_181.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_181.iloc[:, 1] = tabela_181.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_182 = tabela_18.iloc[:, np.r_[0, 5:12]]
        tabela_182 = tabela_182.rename(columns={'Atleta':''})
        tabela_182 = tabela_182.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_18 as its values
        tabela_182.columns = tabela_182.iloc[0]
        tabela_182 = tabela_182.drop(tabela_182.index[0])
        #tabela_182 = tabela_182.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_182.iloc[:, 0:8] = tabela_182.iloc[:, 0:8].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_181).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Extremos Táticos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_182).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Extremos Agudos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_19 = pd.read_csv("19_Role_Extremo_Agudo.csv")
    #    tabela_19 = tabela_19[(tabela_19['Liga']==liga)&(tabela_19['Versão_Temporada']==temporada)]
        tabela_19 = tabela_19.iloc[:, np.r_[1, 36, 3, 10:12, 18:31]]
        tabela_19 = tabela_19.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_19 = tabela_19.sort_values(by='Rating', ascending=False)
        tabela_191 = tabela_19.iloc[:, np.r_[0:5]]
        tabela_191 = tabela_191.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_191.iloc[:, 1] = tabela_191.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_192 = tabela_19.iloc[:, np.r_[0, 5:18]]
        tabela_192 = tabela_192.rename(columns={'Atleta':''})
        tabela_192 = tabela_192.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_19 as its values
        tabela_192.columns = tabela_192.iloc[0]
        tabela_192 = tabela_192.drop(tabela_192.index[0])
        #tabela_192 = tabela_192.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_192.iloc[:, 0:14] = tabela_192.iloc[:, 0:14].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_191).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique!")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Extremos Agudos Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_192).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

    elif posição == "Atacante":
        st.markdown("<h4 style='text-align: center;'>5 Atacantes Referência Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_17 = pd.read_csv("20_Role_Atacante_Referência.csv")
    #    tabela_17 = tabela_17[(tabela_17['Liga']==liga)&(tabela_17['Versão_Temporada']==temporada)]
        tabela_17 = tabela_17.iloc[:, np.r_[1, 33, 3, 10:12, 18:28]]
        tabela_17 = tabela_17.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_17 = tabela_17.sort_values(by='Rating', ascending=False)
        tabela_171 = tabela_17.iloc[:, np.r_[0:5]]
        tabela_171 = tabela_171.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_171.iloc[:, 1] = tabela_171.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_172 = tabela_17.iloc[:, np.r_[0, 5:15]]
        tabela_172 = tabela_172.rename(columns={'Atleta':''})
        tabela_172 = tabela_172.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_17 as its values
        tabela_172.columns = tabela_172.iloc[0]
        tabela_172 = tabela_172.drop(tabela_172.index[0])
        #tabela_172 = tabela_172.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_172.iloc[:, 0:11] = tabela_172.iloc[:, 0:11].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_171).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Atacantes Referência Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_172).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)
            
        st.markdown("<h4 style='text-align: center;'>5 Atacantes Móveis Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_18 = pd.read_csv("21_Role_Atacante_Móvel.csv")
    #    tabela_18 = tabela_18[(tabela_18['Liga']==liga)&(tabela_18['Versão_Temporada']==temporada)]
        tabela_18 = tabela_18.iloc[:, np.r_[1, 32, 3, 10:12, 18:27]]
        tabela_18 = tabela_18.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_18 = tabela_18.sort_values(by='Rating', ascending=False)
        tabela_181 = tabela_18.iloc[:, np.r_[0:5]]
        tabela_181 = tabela_181.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_181.iloc[:, 1] = tabela_181.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_182 = tabela_18.iloc[:, np.r_[0, 5:14]]
        tabela_182 = tabela_182.rename(columns={'Atleta':''})
        tabela_182 = tabela_182.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_18 as its values
        tabela_182.columns = tabela_182.iloc[0]
        tabela_182 = tabela_182.drop(tabela_182.index[0])
        #tabela_182 = tabela_182.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_182.iloc[:, 0:10] = tabela_182.iloc[:, 0:10].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_181).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Atacantes Móveis Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_182).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

        st.markdown("<h4 style='text-align: center;'>5 Segundos Atacantes Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_19 = pd.read_csv("22_Role_Segundo_Atacante.csv")
    #    tabela_19 = tabela_19[(tabela_19['Liga']==liga)&(tabela_19['Versão_Temporada']==temporada)]
        tabela_19 = tabela_19.iloc[:, np.r_[1, 36, 3, 10:12, 18:31]]
        tabela_19 = tabela_19.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_19 = tabela_19.sort_values(by='Rating', ascending=False)
        tabela_191 = tabela_19.iloc[:, np.r_[0:5]]
        tabela_191 = tabela_191.head(5)
        # Format the second column (index 1) to display with 3 decimal places
        tabela_191.iloc[:, 1] = tabela_191.iloc[:, 1].map('{:.3f}'.format)

        # Step 1: Select the required columns and transpose the dataframe
        tabela_192 = tabela_19.iloc[:, np.r_[0, 5:18]]
        tabela_192 = tabela_192.rename(columns={'Atleta':''})
        tabela_192 = tabela_192.head(5).T

        # Step 2: Set the first column as "Métricas" and use the original column labels from tabela_19 as its values
        tabela_192.columns = tabela_192.iloc[0]
        tabela_192 = tabela_192.drop(tabela_192.index[0])
        #tabela_192 = tabela_192.reset_index().rename(columns={'index': 'Métricas'})
        # Format the second column (index 1) to display with 3 decimal places
        tabela_192.iloc[:, 0:14] = tabela_192.iloc[:, 0:14].map('{:.2f}'.format)

        # Styling DataFrame using Pandas
        def style_table(df):
            df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
            df = df.reset_index(drop=True)
            
            # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
            return df.style.set_table_styles(
                [{
                    'selector': 'thead th',
                    'props': [('font-weight', 'bold'),
                            ('border-style', 'solid'),
                            ('border-width', '0px 0px 2px 0px'),
                            ('border-color', 'black')]
                }, {
                    'selector': 'thead th:not(:first-child)',
                    'props': [('text-align', 'center')]  # Centering all headers except the first
                }, {
                    'selector': 'thead th:last-child',
                    'props': [('color', 'black')]  # Make last column header black
                }, {
                    'selector': 'td',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'center')]
                }, {
                    'selector': 'th',
                    'props': [('border-style', 'solid'),
                            ('border-width', '0px 0px 1px 0px'),
                            ('border-color', 'black'),
                            ('text-align', 'left')]
                }]
            ).set_properties(**{'padding': '2px',
                                'font-size': '15px'})

        # Displaying in Streamlit
        def main():
            # Convert the styled DataFrame to HTML without the index
            styled_html = style_table(tabela_191).to_html(index=False, escape=False)

            # Wrap the HTML table in a div with a center alignment
            centered_html = f'''
            <div style="display: flex; justify-content: center;">
                {styled_html}
            
            '''

            st.markdown(centered_html, unsafe_allow_html=True)

        if __name__ == '__main__':
            main()

        
        mais_dados = st.button("Quer ver as métricas? Clique!")
        if mais_dados:
            st.markdown("<h4 style='text-align: center;'><br>Métricas dos 5 Segundos Atacantes Mais Bem Ranqueados<br></h4>", unsafe_allow_html=True)
        
            # Assuming your DataFrame is ready and you want to apply the colormap
            def highlight_ranked_metrics(row):
                # Ensure that the row values are treated as numeric
                row = pd.to_numeric(row)                

                # Get the ranked positions (ascending order of ranking)
                ranked = row.argsort()[::1].argsort()  
                
                # Normalize the ranked values between 0 and 1 to map to the colormap
                normalized_rank = (ranked / (len(row) - 1))/2
                
                # Generate colors using the 'coolwarm' colormap
                colors = plt.cm.Blues(normalized_rank)
                
                # Convert the colors to the CSS format (background-color: rgba(...))
                color_css = ['background-color: rgba({}, {}, {}, {})'.format(int(c[0]*255), int(c[1]*255), int(c[2]*255), c[3]) for c in colors]
                
                # Apply the colors to the cells
                return color_css

            # Styling DataFrame using Pandas
            def style_table(df):
    #            df = df.reset_index(drop=True)
                return df.style.apply(highlight_ranked_metrics, subset=df.columns[0:], axis=1).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                    ('border-style', 'solid'),
                                    ('border-width', '0px 0px 2px 0px'),
                                    ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Center headers except first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                    ('border-width', '0px 0px 1px 0px'),
                                    ('border-color', 'black'),
                                    ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px'})

            def main():
                styled_html = style_table(tabela_192).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Maior', '', '', '', 'Menor']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

elif choose == "Ranking de Jogadores":
    
    #CABEÇALHO DO FORM
    st.markdown("<h1 style='text-align: center;'>Melhores do Brasileirão até a Rodada 25</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>app by @JAmerico1898</h6>", unsafe_allow_html=True)
    st.markdown("---")

    
    st.markdown("<h2 style='text-align: center;'>Ranking de Jogadores</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Série A - 2024</h3>", unsafe_allow_html=True)
    st.markdown("---")
    jogadores = st.selectbox("Digite o nome de seu jogador. A grafia deve ser exata!", options=jogadores, index=None, placeholder="Jogador")
    temporada = 2024
    liga = 'BRA1'
    if jogadores:
        df3 = df.loc[(df['Atleta']==jogadores)]
        posição = df3['Posição'].unique()
        posição = st.selectbox("Escolha a Posição", options=posição)
        if posição == ("Goleiro"):
            #####################################################################################################################
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################
            # GOLEIRO CLÁSSICO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_1.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[9, 14, 26, 30:34, 28, 32, 11]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==0)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 9]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            #####################################################################################################################
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_1.csv")
            tabela_a = tabela_a.iloc[:, np.r_[9, 11, 15:21, 22:25, 14, 26, 28]]
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==0)&(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                df = df.reset_index(drop=True)
                
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(index=False, escape=False)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            #####################################################################################################################
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'><br>GOLEIRO CLÁSSICO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('1_Role_Goleiro.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:25, 6, 25, 27]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==0)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2  = tabela_2.iloc[:, np.r_[0:8]]
            tabela_2 = tabela_2.rename(columns={'Interceptações.1':'Interceptações'})
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('1_Role_Goleiro.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:25, 6, 25, 27]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==0)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:8, 9]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_b = tabela_b.rename(columns={'Interceptações.1':'Interceptações'})
            tabela_c = (tabela_b.groupby('Liga')[['Duelos_Aéreos_Ganhos', 'Defesas', 'Gols_Evitados', 'Saídas', 'Interceptações', 'xG_Evitado', 'Finalizações_por_Gol_Sofrido']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_1.csv')
            tabela_d = tabela_d.iloc[:, np.r_[48:55, 9, 14, 26, 28]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==0)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:7]]
            tabela_d = tabela_d.rename(columns={'Duelos_Aéreos_Ganhos_Percentil':'Duelos_Aéreos_Ganhos', 'Defesas_Percentil': 'Defesas', 
                                                'Gols_Evitados_Percentil':'Gols_Evitados', 'Saídas_Percentil': 'Saídas', 
                                                'Interceptações.1_Percentil': 'Interceptações', 'xG_Evitado_Percentil': 'xG_Evitado', 
                                                'Finalizações_por_Gol_Sofrido_Percentil': 'Finalizações_por_Gol_Sofrido'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada<br></h4>", unsafe_allow_html=True)


            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}

                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(

                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)



            #####################################################################################################################
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_1_Mean_Charts = pd.read_csv('1_Role_Goleiro.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_1_Mean_Charts.iloc[:, np.r_[1, 3, 25, 27, 18:25]]
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Duelos_Aéreos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Aéreos_Ganhos'].mean()
            Role_x_Mean_Charts['Defesas_LM'] = Role_x_Mean_Charts['Defesas'].mean()
            Role_x_Mean_Charts['Gols_Evitados_LM'] = Role_x_Mean_Charts['Gols_Evitados'].mean()
            Role_x_Mean_Charts['Saídas_LM'] = Role_x_Mean_Charts['Saídas'].mean()
            Role_x_Mean_Charts['Interceptações_LM'] = Role_x_Mean_Charts['Interceptações.1'].mean()
            Role_x_Mean_Charts['xG_Evitado_LM'] = Role_x_Mean_Charts['xG_Evitado'].mean()
            Role_x_Mean_Charts['Finalizações_por_Gol_Sofrido_LM'] = Role_x_Mean_Charts['Finalizações_por_Gol_Sofrido'].mean()
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts = Role_y_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})

            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_1_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:11]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[11:18]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Duelos_Aéreos_Ganhos_LM':'Duelos_Aéreos_Ganhos', 'Defesas_LM': 'Defesas', 
                                                        'Gols_Evitados_LM':'Gols_Evitados', 'Saídas_LM': 'Saídas',  
                                                        'Interceptações_LM': 'Interceptações', 'xG_Evitado_LM': 'xG_Evitado', 
                                                        'Finalizações_por_Gol_Sofrido_LM': 'Finalizações_por_Gol_Sofrido'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            Role_1_Mean_Charts = Role_1_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    
            #Concatenating Dataframes
            Role_1_Mean_Charts = pd.concat([Role_1_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_1_Mean_Charts = Role_1_Mean_Charts.append(League_Mean).reset_index()
            Role_1_Mean_Charts = Role_1_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    
            # Preparing the Graph
            params = list(Role_1_Mean_Charts.columns)
            params = params[1:]

            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_1_Mean_Charts['Atleta'])):
                if Role_1_Mean_Charts['Atleta'][x] == jogadores:
                    a_values = Role_1_Mean_Charts.iloc[x].values.tolist()
                if Role_1_Mean_Charts['Atleta'][x] == 'Média da Liga':
                    b_values = Role_1_Mean_Charts.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'
            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison.png', dpi=600, bbox_inches="tight")

            #####################################################################################################################
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################
            # GOLEIRO LÍBERO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_2.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[12, 17, 29, 33:37, 31, 35, 14]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==0)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 9]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'>GOLEIRO LÍBERO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_2_Mean_Charts = pd.read_csv('2_Role_Goleiro_Líbero.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_2_Mean_Charts.iloc[:, np.r_[1, 3, 28, 30, 18:28]]
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]
            
            Role_x_Mean_Charts['Duelos_Aéreos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Aéreos_Ganhos'].mean()
            Role_x_Mean_Charts['Passes_Curtos_Médios_Certos_LM'] = Role_x_Mean_Charts['Passes_Curtos_Médios_Certos'].mean()
            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Defesas_LM'] = Role_x_Mean_Charts['Defesas'].mean()
            Role_x_Mean_Charts['Gols_Evitados_LM'] = Role_x_Mean_Charts['Gols_Evitados'].mean()
            Role_x_Mean_Charts['Saídas_LM'] = Role_x_Mean_Charts['Saídas'].mean()
            Role_x_Mean_Charts['Interceptações_LM'] = Role_x_Mean_Charts['Interceptações.1'].mean()
            Role_x_Mean_Charts['xG_Evitado_LM'] = Role_x_Mean_Charts['xG_Evitado'].mean()
            Role_x_Mean_Charts['Finalizações_por_Gol_Sofrido_LM'] = Role_x_Mean_Charts['Finalizações_por_Gol_Sofrido'].mean()

            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts = Role_y_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})

            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_2_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:14]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[14:24]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Duelos_Aéreos_Ganhos_LM':'Duelos_Aéreos_Ganhos', 'Passes_Curtos_Médios_Certos_LM':'Passes_Curtos_Médios_Certos', 
                                                    'Passes_Longos_Certos_LM': 'Passes_Longos_Certos', 'Passes_Progressivos_Certos_LM': 'Passes_Progressivos_Certos',
                                                    'Defesas_LM': 'Defesas', 'Gols_Evitados_LM':'Gols_Evitados', 'Saídas_LM': 'Saídas',  
                                                    'Interceptações_LM': 'Interceptações', 'xG_Evitado_LM': 'xG_Evitado', 
                                                    'Finalizações_por_Gol_Sofrido_LM': 'Finalizações_por_Gol_Sofrido'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            Role_2_Mean_Charts = Role_2_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    
            #Concatenating Dataframes
            Role_2_Mean_Charts = pd.concat([Role_2_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_2_Mean_Charts = Role_2_Mean_Charts.append(League_Mean).reset_index()
            
            # Preparing the Graph
            params = list(Role_2_Mean_Charts.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_2_Mean_Charts['Atleta'])):
                if Role_2_Mean_Charts['Atleta'][x] == jogadores:
                    a_values = Role_2_Mean_Charts.iloc[x].values.tolist()
                if Role_2_Mean_Charts['Atleta'][x] == 'Média da Liga':
                    b_values = Role_2_Mean_Charts.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison.png', dpi=600, bbox_inches="tight")
#################################################################################################################################
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:14]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

                ###############################################################################################################################
                ###############################################################################################################################
                ###############################################################################################################################
                ###############################################################################################################################

        elif posição == ("Lateral Direito"):
            ##################################################################################################################### 
            #####################################################################################################################
            # LATERAL DEFENSIVO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_3.csv')
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==1)&
                                (tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)
                                &(tabela_1['Pé']=='right')]
            tabela_1  = tabela_1.iloc[:, np.r_[8, 13, 25, 29:33, 27, 10]]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_3.csv")
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==1)
                                &(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)
                                &(tabela_a['Pé']=='right')]
            tabela_a = tabela_a.iloc[:, np.r_[8, 10, 14:20, 21:24, 13, 25, 27]]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)
            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format().set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            ##################################################################################################################### 
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'><br>LATERAL DIREITO DEFENSIVO</b></h3>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: center;'>(Laterais D/E são ranqueados em conjunto)</b></h6>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # LATERAL DIREITO OFENSIVO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_4.csv')
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==1)
                                &(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)
                                &(tabela_1['Pé']=='right')]
            tabela_1  = tabela_1.iloc[:, np.r_[17, 22, 34, 38:42, 36, 19]]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>LATERAL DIREITO OFENSIVO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # LATERAL DIREITO EQUILIBRADO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_5.csv')
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==1)
                                &(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)
                                &(tabela_1['Pé']=='right')]
            tabela_1  = tabela_1.iloc[:, np.r_[20, 25, 37, 41:45, 39, 22]]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>LATERAL DIREITO EQUILIBRADO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('5_Role_Lateral_Equilibrado.csv')
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==1)
                                &(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)
                                &(tabela_2['Pé']=='right')]
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:36, 6, 36, 38]]
            tabela_2  = tabela_2.iloc[:, np.r_[0:19]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('5_Role_Lateral_Equilibrado.csv')
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==1)&(tabela_b['Versão_Temporada']==temporada)
                                &(tabela_b['Liga']==liga) &(tabela_b['Pé']=='right')]
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:36, 6, 36, 38]]
            tabela_b = tabela_b.iloc[:, np.r_[1:19, 20]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos', 
                                                    'Passes_Longos_Certos', 'Passes_Progressivos_Certos', 'Passes_Laterais_Certos', 'Ações_Ofensivas_BemSucedidas', 
                                                    'Duelos_Ofensivos_Ganhos', 'Pisadas_Área', 'Dribles_BemSucedidos', 'Corridas_Progressivas', 
                                                    'Acelerações', 'xA', 'Assistência_Finalização', 'Passes_TerçoFinal_Certos', 'Deep_Completions', 
                                                    'Deep_Completed_Crosses', 'Passes_ÁreaPênalti_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_5.csv')
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==1)
                                &(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)
                                &(tabela_d['Pé']=='right')]
            tabela_d = tabela_d.iloc[:, np.r_[81:99, 20, 25, 37, 39]]
            tabela_d = tabela_d.iloc[:, np.r_[0:18]]
            tabela_d = tabela_d.rename(columns={'Ações_Defensivas_BemSucedidas_Percentil':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_Percentil':'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos_Percentil':'Duelos_Aéreos_Ganhos', 'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 'Passes_Progressivos_Certos_Percentil':'Passes_Progressivos_Certos',
                                                    'Passes_Laterais_Certos_Percentil':'Passes_Laterais_Certos', 'Ações_Ofensivas_BemSucedidas_Percentil':'Ações_Ofensivas_BemSucedidas', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 
                                                    'Pisadas_Área_Percentil':'Pisadas_Área', 'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 'Corridas_Progressivas_Percentil':'Corridas_Progressivas', 'Acelerações_Percentil':'Acelerações', 
                                                    'xA_Percentil':'xA', 'Assistência_Finalização_Percentil':'Assistência_Finalização', 'Passes_TerçoFinal_Certos_Percentil':'Passes_TerçoFinal_Certos', 'Deep_Completions_Percentil':'Deep_Completions',
                                                    'Deep_Completed_Crosses_Percentil':'Deep_Completed_Crosses', 'Passes_ÁreaPênalti_Certos_Percentil':'Passes_ÁreaPênalti_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)


            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'




            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
    
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)


            ##################################################################################################################### 
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################

            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_5_Mean_Charts = pd.read_csv('5_Role_Lateral_Equilibrado.csv')
            Role_5_Mean_Charts = Role_5_Mean_Charts[(Role_5_Mean_Charts['Versão_Temporada']==temporada)
                                                    &(Role_5_Mean_Charts['Liga']==liga)
                                                    &(Role_5_Mean_Charts['Pé']=='right')]
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_5_Mean_Charts.iloc[:, np.r_[1, 3, 36, 38, 18:36]]
            
            Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Defensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Defensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Duelos_Aéreos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Aéreos_Ganhos'].mean()
            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Laterais_Certos_LM'] = Role_x_Mean_Charts['Passes_Laterais_Certos'].mean()
            Role_x_Mean_Charts['Ações_Ofensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Ofensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Pisadas_Área_LM'] = Role_x_Mean_Charts['Pisadas_Área'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Corridas_Progressivas_LM'] = Role_x_Mean_Charts['Corridas_Progressivas'].mean()
            Role_x_Mean_Charts['Acelerações_LM'] = Role_x_Mean_Charts['Acelerações'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Passes_TerçoFinal_Certos_LM'] = Role_x_Mean_Charts['Passes_TerçoFinal_Certos'].mean()
            Role_x_Mean_Charts['Deep_Completions_LM'] = Role_x_Mean_Charts['Deep_Completions'].mean()
            Role_x_Mean_Charts['Deep_Completed_Crosses_LM'] = Role_x_Mean_Charts['Deep_Completed_Crosses'].mean()
            Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos_LM'] = Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_5_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:22]]
            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[22:40]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Ações_Defensivas_BemSucedidas_LM':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_LM':'Duelos_Defensivos_Ganhos', 
                                                    'Duelos_Aéreos_Ganhos_LM':'Duelos_Aéreos_Ganhos', 'Passes_Longos_Certos_LM': 'Passes_Longos_Certos', 'Passes_Progressivos_Certos_LM': 'Passes_Progressivos_Certos',
                                                    'Passes_Laterais_Certos_LM': 'Passes_Laterais_Certos', 'Ações_Ofensivas_BemSucedidas_LM':'Ações_Ofensivas_BemSucedidas', 
                                                    'Duelos_Ofensivos_Ganhos_LM': 'Duelos_Ofensivos_Ganhos', 'Pisadas_Área_LM':'Pisadas_Área', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos',  
                                                    'Corridas_Progressivas_LM':'Corridas_Progressivas', 'Acelerações_LM': 'Acelerações', 'xA_LM':'xA', 'Assistência_Finalização_LM':'Assistência_Finalização',
                                                    'Passes_TerçoFinal_Certos_LM': 'Passes_TerçoFinal_Certos', 'Deep_Completions_LM':'Deep_Completions', 'Deep_Completed_Crosses_LM':'Deep_Completed_Crosses',
                                                    'Passes_ÁreaPênalti_Certos_LM':'Passes_ÁreaPênalti_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_5_Mean_Charts = pd.concat([Role_5_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_5_Mean_Charts = Role_5_Mean_Charts.append(League_Mean).reset_index()
            #Splitting Columns
            Role_5_Mean_Charts_1 = Role_5_Mean_Charts.iloc[:, np.r_[0, 1:10]]
            Role_5_Mean_Charts_2 = Role_5_Mean_Charts.iloc[:, np.r_[0, 10:19]]
            # Preparing Graph 1
            # Get Parameters
            params = list(Role_5_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_5_Mean_Charts_1['Atleta'])):
                if Role_5_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_5_Mean_Charts_1.iloc[x].values.tolist()
                if Role_5_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_5_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_5_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_5_Mean_Charts_2['Atleta'])):
                if Role_5_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_5_Mean_Charts_2.iloc[x].values.tolist()
                if Role_5_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_5_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            ##########################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:22]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

                #####################################################################################################################
                #####################################################################################################################
                ##################################################################################################################### 
                #####################################################################################################################

        elif posição == ("Lateral Esquerdo"):
            ##################################################################################################################### 
            #####################################################################################################################
            # LATERAL DEFENSIVO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_3.csv')
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==1)&
                                (tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)
                                &(tabela_1['Pé']=='left')]
            tabela_1  = tabela_1.iloc[:, np.r_[8, 13, 25, 29:33, 27, 10]]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_3.csv")
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==1)
                                &(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)
                                &(tabela_a['Pé']=='left')]
            tabela_a = tabela_a.iloc[:, np.r_[8, 10, 14:20, 21:24, 13, 25, 27]]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)
            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format().set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            ##################################################################################################################### 
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'><br>LATERAL ESQUERDO DEFENSIVO</b></h3>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: center;'>(Laterais D/E são ranqueados em conjunto)</b></h6>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # LATERAL ESQUERDO OFENSIVO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_4.csv')
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==1)
                                &(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)
                                &(tabela_1['Pé']=='left')]
            tabela_1  = tabela_1.iloc[:, np.r_[17, 22, 34, 38:42, 36, 19]]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>LATERAL ESQUERDO OFENSIVO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # LATERAL ESQUERDO EQUILIBRADO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_5.csv')
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==1)
                                &(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)
                                &(tabela_1['Pé']=='left')]
            tabela_1  = tabela_1.iloc[:, np.r_[20, 25, 37, 41:45, 39, 22]]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>LATERAL ESQUERDO EQUILIBRADO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('5_Role_Lateral_Equilibrado.csv')
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==1)
                                &(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)
                                &(tabela_2['Pé']=='left')]
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:36, 6, 36, 38]]
            tabela_2  = tabela_2.iloc[:, np.r_[0:19]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('5_Role_Lateral_Equilibrado.csv')
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==1)&(tabela_b['Versão_Temporada']==temporada)
                                &(tabela_b['Liga']==liga) &(tabela_b['Pé']=='left')]
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:36, 6, 36, 38]]
            tabela_b = tabela_b.iloc[:, np.r_[1:19, 20]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos', 
                                                    'Passes_Longos_Certos', 'Passes_Progressivos_Certos', 'Passes_Laterais_Certos', 'Ações_Ofensivas_BemSucedidas', 
                                                    'Duelos_Ofensivos_Ganhos', 'Pisadas_Área', 'Dribles_BemSucedidos', 'Corridas_Progressivas', 
                                                    'Acelerações', 'xA', 'Assistência_Finalização', 'Passes_TerçoFinal_Certos', 'Deep_Completions', 
                                                    'Deep_Completed_Crosses', 'Passes_ÁreaPênalti_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_5.csv')
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==1)
                                &(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)
                                &(tabela_d['Pé']=='left')]
            tabela_d = tabela_d.iloc[:, np.r_[81:99, 20, 25, 37, 39]]
            tabela_d = tabela_d.iloc[:, np.r_[0:18]]
            tabela_d = tabela_d.rename(columns={'Ações_Defensivas_BemSucedidas_Percentil':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_Percentil':'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos_Percentil':'Duelos_Aéreos_Ganhos', 'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 'Passes_Progressivos_Certos_Percentil':'Passes_Progressivos_Certos',
                                                    'Passes_Laterais_Certos_Percentil':'Passes_Laterais_Certos', 'Ações_Ofensivas_BemSucedidas_Percentil':'Ações_Ofensivas_BemSucedidas', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 
                                                    'Pisadas_Área_Percentil':'Pisadas_Área', 'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 'Corridas_Progressivas_Percentil':'Corridas_Progressivas', 'Acelerações_Percentil':'Acelerações', 
                                                    'xA_Percentil':'xA', 'Assistência_Finalização_Percentil':'Assistência_Finalização', 'Passes_TerçoFinal_Certos_Percentil':'Passes_TerçoFinal_Certos', 'Deep_Completions_Percentil':'Deep_Completions',
                                                    'Deep_Completed_Crosses_Percentil':'Deep_Completed_Crosses', 'Passes_ÁreaPênalti_Certos_Percentil':'Passes_ÁreaPênalti_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)



            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'



            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
    
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################

            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_5_Mean_Charts = pd.read_csv('5_Role_Lateral_Equilibrado.csv')
            Role_5_Mean_Charts = Role_5_Mean_Charts[(Role_5_Mean_Charts['Versão_Temporada']==temporada)
                                                    &(Role_5_Mean_Charts['Liga']==liga)
                                                    &(Role_5_Mean_Charts['Pé']=='left')]
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_5_Mean_Charts.iloc[:, np.r_[1, 3, 36, 38, 18:36]]
            
            Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Defensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Defensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Duelos_Aéreos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Aéreos_Ganhos'].mean()
            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Laterais_Certos_LM'] = Role_x_Mean_Charts['Passes_Laterais_Certos'].mean()
            Role_x_Mean_Charts['Ações_Ofensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Ofensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Pisadas_Área_LM'] = Role_x_Mean_Charts['Pisadas_Área'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Corridas_Progressivas_LM'] = Role_x_Mean_Charts['Corridas_Progressivas'].mean()
            Role_x_Mean_Charts['Acelerações_LM'] = Role_x_Mean_Charts['Acelerações'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Passes_TerçoFinal_Certos_LM'] = Role_x_Mean_Charts['Passes_TerçoFinal_Certos'].mean()
            Role_x_Mean_Charts['Deep_Completions_LM'] = Role_x_Mean_Charts['Deep_Completions'].mean()
            Role_x_Mean_Charts['Deep_Completed_Crosses_LM'] = Role_x_Mean_Charts['Deep_Completed_Crosses'].mean()
            Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos_LM'] = Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_5_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:22]]
            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[22:40]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Ações_Defensivas_BemSucedidas_LM':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_LM':'Duelos_Defensivos_Ganhos', 
                                                    'Duelos_Aéreos_Ganhos_LM':'Duelos_Aéreos_Ganhos', 'Passes_Longos_Certos_LM': 'Passes_Longos_Certos', 'Passes_Progressivos_Certos_LM': 'Passes_Progressivos_Certos',
                                                    'Passes_Laterais_Certos_LM': 'Passes_Laterais_Certos', 'Ações_Ofensivas_BemSucedidas_LM':'Ações_Ofensivas_BemSucedidas', 
                                                    'Duelos_Ofensivos_Ganhos_LM': 'Duelos_Ofensivos_Ganhos', 'Pisadas_Área_LM':'Pisadas_Área', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos',  
                                                    'Corridas_Progressivas_LM':'Corridas_Progressivas', 'Acelerações_LM': 'Acelerações', 'xA_LM':'xA', 'Assistência_Finalização_LM':'Assistência_Finalização',
                                                    'Passes_TerçoFinal_Certos_LM': 'Passes_TerçoFinal_Certos', 'Deep_Completions_LM':'Deep_Completions', 'Deep_Completed_Crosses_LM':'Deep_Completed_Crosses',
                                                    'Passes_ÁreaPênalti_Certos_LM':'Passes_ÁreaPênalti_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_5_Mean_Charts = pd.concat([Role_5_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_5_Mean_Charts = Role_5_Mean_Charts.append(League_Mean).reset_index()
            #Splitting Columns
            Role_5_Mean_Charts_1 = Role_5_Mean_Charts.iloc[:, np.r_[0, 1:10]]
            Role_5_Mean_Charts_2 = Role_5_Mean_Charts.iloc[:, np.r_[0, 10:19]]
            # Preparing Graph 1
            # Get Parameters
            params = list(Role_5_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_5_Mean_Charts_1['Atleta'])):
                if Role_5_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_5_Mean_Charts_1.iloc[x].values.tolist()
                if Role_5_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_5_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_5_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_5_Mean_Charts_2['Atleta'])):
                if Role_5_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_5_Mean_Charts_2.iloc[x].values.tolist()
                if Role_5_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_5_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            ##########################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:22]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

                #####################################################################################################################
                #####################################################################################################################
                ##################################################################################################################### 
                #####################################################################################################################



        elif posição == ("Zagueiro"):
            ##################################################################################################################### 
            #####################################################################################################################
            # ZAGUEIRO CLÁSSICO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_6.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[8, 13, 25, 29:33, 27, 10]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==4)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_6.csv")
            tabela_a = tabela_a.iloc[:, np.r_[8, 10, 14:20, 21:24, 13, 25, 27]]
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==4)&(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                formatter = {"Idade": "{:.0f}"}
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format(formatter).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            ##################################################################################################################### 
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'><br>ZAGUEIRO CLÁSSICO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # ZAGUEIRO CONSTRUTOR
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_7.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[12, 17, 29, 33:37, 31, 14]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==4)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>ZAGUEIRO CONSTRUTOR</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # ZAGUEIRO EQUILIBRADO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_8.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[15, 20, 32, 36:40, 34, 17]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==4)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>ZAGUEIRO EQUILIBRADO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('8_Role_Zagueiro_Equilibrado.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==4)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2  = tabela_2.iloc[:, np.r_[0:14]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('8_Role_Zagueiro_Equilibrado.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==4)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:14, 15]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos', 
                                                    'Finalizações_Bloqueadas', 'Interceptações_Ajustadas_a_Posse', 'Passes_Longos_Certos', 
                                                    'Passes_Frontais_Certos', 'Passes_Progressivos_Certos', 'Passes_Laterais_Certos', 'Duelos_Ofensivos_Ganhos', 
                                                    'Dribles_BemSucedidos', 'Corridas_Progressivas', 'Passes_TerçoFinal_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_8.csv')
            tabela_d = tabela_d.iloc[:, np.r_[66:79, 15, 20, 32, 34]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==4)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:13]]
            tabela_d = tabela_d.rename(columns={'Ações_Defensivas_BemSucedidas_Percentil':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_Percentil':'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos_Percentil':'Duelos_Aéreos_Ganhos',
                                                'Finalizações_Bloqueadas_Percentil':'Finalizações_Bloqueadas', 'Interceptações_Ajustadas_a_Posse_Percentil':'Interceptações_Ajustadas_a_Posse', 'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 
                                                'Passes_Frontais_Certos_Percentil':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_Percentil':'Passes_Progressivos_Certos', 'Passes_Laterais_Certos_Percentil':'Passes_Laterais_Certos', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 
                                                'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 'Corridas_Progressivas_Percentil':'Corridas_Progressivas', 'Passes_TerçoFinal_Certos_Percentil':'Passes_TerçoFinal_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()
            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'


            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################

            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_8_Mean_Charts = pd.read_csv('8_Role_Zagueiro_Equilibrado.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_8_Mean_Charts.iloc[:, np.r_[1, 3, 31, 33, 18:31]]
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Defensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Defensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Duelos_Aéreos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Aéreos_Ganhos'].mean()
            Role_x_Mean_Charts['Finalizações_Bloqueadas_LM'] = Role_x_Mean_Charts['Finalizações_Bloqueadas'].mean()
            Role_x_Mean_Charts['Interceptações_Ajustadas_a_Posse_LM'] = Role_x_Mean_Charts['Interceptações_Ajustadas_a_Posse'].mean()
            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Frontais_Certos_LM'] = Role_x_Mean_Charts['Passes_Frontais_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Laterais_Certos_LM'] = Role_x_Mean_Charts['Passes_Laterais_Certos'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Corridas_Progressivas_LM'] = Role_x_Mean_Charts['Corridas_Progressivas'].mean()
            Role_x_Mean_Charts['Passes_TerçoFinal_Certos_LM'] = Role_x_Mean_Charts['Passes_TerçoFinal_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)

            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_8_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:17]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[17:30]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Ações_Defensivas_BemSucedidas_LM':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_LM':'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos_LM':'Duelos_Aéreos_Ganhos',
                                                'Finalizações_Bloqueadas_LM':'Finalizações_Bloqueadas', 'Interceptações_Ajustadas_a_Posse_LM':'Interceptações_Ajustadas_a_Posse', 'Passes_Longos_Certos_LM':'Passes_Longos_Certos', 
                                                'Passes_Frontais_Certos_LM':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_LM':'Passes_Progressivos_Certos', 'Passes_Laterais_Certos_LM':'Passes_Laterais_Certos', 'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 
                                                'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 'Corridas_Progressivas_LM':'Corridas_Progressivas', 'Passes_TerçoFinal_Certos_LM':'Passes_TerçoFinal_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_8_Mean_Charts = pd.concat([Role_8_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_8_Mean_Charts = Role_8_Mean_Charts.append(League_Mean).reset_index()

            #Splitting Columns
            Role_8_Mean_Charts_1 = Role_8_Mean_Charts.iloc[:, np.r_[0, 1:8]]
#                        st.dataframe(Role_8_Mean_Charts_1)
            Role_8_Mean_Charts_2 = Role_8_Mean_Charts.iloc[:, np.r_[0, 8:14]]
#                        st.dataframe(Role_8_Mean_Charts_2)

            # Preparing Graph 1
            # Get Parameters

            params = list(Role_8_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_8_Mean_Charts_1['Atleta'])):
                if Role_8_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_8_Mean_Charts_1.iloc[x].values.tolist()
                if Role_8_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_8_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_8_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_8_Mean_Charts_2['Atleta'])):
                if Role_8_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_8_Mean_Charts_2.iloc[x].values.tolist()
                if Role_8_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_8_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            ##########################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:17]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

                #####################################################################################################################
                #####################################################################################################################
                ##################################################################################################################### 
                #####################################################################################################################
        elif posição == ("Primeiro Volante"):
            ##################################################################################################################### 
            #####################################################################################################################
            # PRIMEIRO VOLANTE DEFENSIVO
            ##################################################################################################################### 
            #####################################################################################################################
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_9.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[6, 11, 23, 27:31, 25, 8]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==7)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_9.csv")
            tabela_a = tabela_a.iloc[:, np.r_[6, 8, 12:18, 19:22, 11, 23, 25]]
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==7)&(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                formatter = {"Idade": "{:.0f}"}
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format(formatter).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            ##################################################################################################################### 
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'><br>PRIMEIRO VOLANTE DEFENSIVO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################

            # PRIMEIRO VOLANTE CONSTRUTOR
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_10.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[11, 16, 28, 32:36, 30, 13]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==7)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>PRIMEIRO VOLANTE CONSTRUTOR</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # PRIMEIRO VOLANTE EQUILIBRADO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_11.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[13, 18, 30, 34:38, 32, 15]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==7)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>PRIMEIRO VOLANTE EQUILIBRADO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('11_Role_Volante_Equilibrado.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:29, 6, 29, 31]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==7)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2  = tabela_2.iloc[:, np.r_[0:12]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('11_Role_Volante_Equilibrado.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:29, 6, 29, 31]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==7)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:12, 13]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos', 
                                                    'Passes_Longos_Certos', 'Passes_Frontais_Certos', 'Passes_Progressivos_Certos', 
                                                    'Ações_Ofensivas_BemSucedidas', 'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos', 
                                                    'Corridas_Progressivas', 'Passes_TerçoFinal_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_11.csv')
            tabela_d = tabela_d.iloc[:, np.r_[60:71, 13, 18, 30, 32]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==7)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:12]]
            tabela_d = tabela_d.rename(columns={'Ações_Defensivas_BemSucedidas_Percentil':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_Percentil':'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos_Percentil':'Duelos_Aéreos_Ganhos',
                                                'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 'Passes_Frontais_Certos_Percentil':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_Percentil':'Passes_Progressivos_Certos',
                                                'Ações_Ofensivas_BemSucedidas_Percentil':'Ações_Ofensivas_BemSucedidas', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos',
                                                'Corridas_Progressivas_Percentil':'Corridas_Progressivas', 'Passes_TerçoFinal_Certos_Percentil':'Passes_TerçoFinal_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################

            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_11_Mean_Charts = pd.read_csv('11_Role_Volante_Equilibrado.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_11_Mean_Charts.iloc[:, np.r_[1, 3, 29, 31, 18:29]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Defensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Defensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Duelos_Aéreos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Aéreos_Ganhos'].mean()
            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Frontais_Certos_LM'] = Role_x_Mean_Charts['Passes_Frontais_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Ações_Ofensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Ofensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Corridas_Progressivas_LM'] = Role_x_Mean_Charts['Corridas_Progressivas'].mean()
            Role_x_Mean_Charts['Passes_TerçoFinal_Certos_LM'] = Role_x_Mean_Charts['Passes_TerçoFinal_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)

            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_11_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:15]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[15:26]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Ações_Defensivas_BemSucedidas_LM':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_LM':'Duelos_Defensivos_Ganhos', 'Duelos_Aéreos_Ganhos_LM':'Duelos_Aéreos_Ganhos',
                                                'Passes_Longos_Certos_LM':'Passes_Longos_Certos', 'Passes_Frontais_Certos_LM':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_LM':'Passes_Progressivos_Certos', 
                                                'Ações_Ofensivas_BemSucedidas_LM':'Ações_Ofensivas_BemSucedidas', 'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 
                                                'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 'Corridas_Progressivas_LM':'Corridas_Progressivas', 'Passes_TerçoFinal_Certos_LM':'Passes_TerçoFinal_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_11_Mean_Charts = pd.concat([Role_11_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_11_Mean_Charts = Role_11_Mean_Charts.append(League_Mean).reset_index()

            #Splitting Columns
            Role_11_Mean_Charts_1 = Role_11_Mean_Charts.iloc[:, np.r_[0, 1:7]]
            Role_11_Mean_Charts_2 = Role_11_Mean_Charts.iloc[:, np.r_[0, 7:12]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_11_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_11_Mean_Charts_1['Atleta'])):
                if Role_11_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_11_Mean_Charts_1.iloc[x].values.tolist()
                if Role_11_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_11_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_11_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_11_Mean_Charts_2['Atleta'])):
                if Role_11_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_11_Mean_Charts_2.iloc[x].values.tolist()
                if Role_11_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_11_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            ##########################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:15]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

                #####################################################################################################################
                #####################################################################################################################
                ##################################################################################################################### 
                #####################################################################################################################
        elif posição == ("Segundo Volante"):
            ##################################################################################################################### 
            #####################################################################################################################
            # SEGUNDO VOLANTE BOX TO BOX
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_12.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[15, 20, 32, 36:40, 34, 17]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==8)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            #####################################################################################################################
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_12.csv")
            tabela_a = tabela_a.iloc[:, np.r_[15, 17, 21:27, 28:31, 20, 32, 34]]
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==8)&(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                formatter = {"Idade": "{:.0f}"}
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format(formatter).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            #####################################################################################################################
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'>SEGUNDO VOLANTE BOX TO BOX</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # SEGUNDO VOLANTE ORGANIZADOR
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_13.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[12, 17, 29, 33:37, 31, 14]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==8)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>SEGUNDO VOLANTE ORGANIZADOR</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # SEGUNDO VOLANTE EQUILIBRADO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_14.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[15, 20, 32, 36:40, 34, 17]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==8)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>SEGUNDO VOLANTE EQUILIBRADO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('14_Role_Segundo_Volante_Equilibrado.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==8)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2  = tabela_2.iloc[:, np.r_[0:14]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('14_Role_Segundo_Volante_Equilibrado.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==8)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:14, 15]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos', 'Passes_Longos_Certos', 'Passes_Progressivos_Certos', 'Pisadas_Área',
                                                    'Dribles_BemSucedidos', 'Corridas_Progressivas', 'xG', 'xA', 'Assistência_Finalização', 'Passes_TerçoFinal_Certos',
                                                    'Deep_Completions', 'Passes_ÁreaPênalti_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_14.csv')
            tabela_d = tabela_d.iloc[:, np.r_[66:79, 15, 20, 32, 34]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==8)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:13]]
            tabela_d = tabela_d.rename(columns={'Ações_Defensivas_BemSucedidas_Percentil':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_Percentil':'Duelos_Defensivos_Ganhos', 
                                                'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 'Passes_Progressivos_Certos_Percentil':'Passes_Progressivos_Certos',
                                                'Pisadas_Área_Percentil':'Pisadas_Área', 'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 
                                                'Corridas_Progressivas_Percentil':'Corridas_Progressivas', 'xG_Percentil':'xG', 'xA_Percentil':'xA', 
                                                'Assistência_Finalização_Percentil':'Assistência_Finalização', 'Passes_TerçoFinal_Certos_Percentil':'Passes_TerçoFinal_Certos',
                                                'Deep_Completions_Percentil':'Deep_Completions', 'Passes_ÁreaPênalti_Certos_Percentil':'Passes_ÁreaPênalti_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()
            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
    
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering
                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_14_Mean_Charts = pd.read_csv('14_Role_Segundo_Volante_Equilibrado.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_14_Mean_Charts.iloc[:, np.r_[1, 3, 31, 33, 18:31]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Defensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Defensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Pisadas_Área_LM'] = Role_x_Mean_Charts['Pisadas_Área'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Corridas_Progressivas_LM'] = Role_x_Mean_Charts['Corridas_Progressivas'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Passes_TerçoFinal_Certos_LM'] = Role_x_Mean_Charts['Passes_TerçoFinal_Certos'].mean()
            Role_x_Mean_Charts['Deep_Completions_LM'] = Role_x_Mean_Charts['Deep_Completions'].mean()
            Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos_LM'] = Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)

            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_14_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:17]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[17:30]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Ações_Defensivas_BemSucedidas_LM':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_LM':'Duelos_Defensivos_Ganhos',
                                                'Passes_Longos_Certos_LM':'Passes_Longos_Certos', 'Passes_Progressivos_Certos_LM':'Passes_Progressivos_Certos', 
                                                'Pisadas_Área_LM':'Pisadas_Área', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 'Corridas_Progressivas_LM':'Corridas_Progressivas', 
                                                'xA_LM':'xA', 'xG_LM':'xG','Assistência_Finalização_LM':'Assistência_Finalização', 'Passes_TerçoFinal_Certos_LM':'Passes_TerçoFinal_Certos', 
                                                'Deep_Completions_LM':'Deep_Completions', 'Passes_ÁreaPênalti_Certos_LM':'Passes_ÁreaPênalti_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_14_Mean_Charts = pd.concat([Role_14_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_14_Mean_Charts = Role_14_Mean_Charts.append(League_Mean).reset_index()

            #Splitting Columns
            Role_14_Mean_Charts_1 = Role_14_Mean_Charts.iloc[:, np.r_[0, 1:8]]
            Role_14_Mean_Charts_2 = Role_14_Mean_Charts.iloc[:, np.r_[0, 8:14]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_14_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_14_Mean_Charts_1['Atleta'])):
                if Role_14_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_14_Mean_Charts_1.iloc[x].values.tolist()
                if Role_14_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_14_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_14_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_14_Mean_Charts_2['Atleta'])):
                if Role_14_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_14_Mean_Charts_2.iloc[x].values.tolist()
                if Role_14_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_14_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_2.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_2.png', dpi=600, bbox_inches="tight")

            ##########################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:17]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

                #####################################################################################################################
                #####################################################################################################################
                ##################################################################################################################### 
                #####################################################################################################################
        elif posição == ("Meia"):
            #####################################################################################################################
            #####################################################################################################################
            # MEIA ORGANIZADOR
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_15.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[12, 17, 29, 33:37, 31, 14]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==9)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            #####################################################################################################################
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_15.csv")
            tabela_a = tabela_a.iloc[:, np.r_[12, 14, 19:24, 25:28, 17, 29, 31]]
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==9)&(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)
            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                formatter = {"Idade": "{:.0f}"}
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format(formatter).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            #####################################################################################################################
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'>MEIA ORGANIZADOR</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('15_Role_Meia_Organizador.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:28, 6, 28, 30]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==9)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2  = tabela_2.iloc[:, np.r_[0:11]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('15_Role_Meia_Organizador.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:28, 6, 28, 30]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==9)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[0:11, 12]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Passes_Longos_Certos', 'Passes_Frontais_Certos', 'Passes_Progressivos_Certos',
                                                    'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos', 'xA', 'Assistência_Finalização',
                                                    'Passes_TerçoFinal_Certos', 'Passes_EntreLinhas_Certos', 'Passes_Chave',]].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_15.csv')
            tabela_d = tabela_d.iloc[:, np.r_[57:67, 12, 17, 29, 31]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==9)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:10]]
            tabela_d = tabela_d.rename(columns={'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 'Passes_Frontais_Certos_Percentil':'Passes_Frontais_Certos',
                                                'Passes_Progressivos_Certos_Percentil': 'Passes_Progressivos_Certos', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 
                                                'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 'xA_Percentil':'xA', 'Assistência_Finalização_Percentil':'Assistência_Finalização',
                                                'Passes_TerçoFinal_Certos_Percentil':'Passes_TerçoFinal_Certos', 'Passes_EntreLinhas_Certos_Percentil':'Passes_EntreLinhas_Certos',
                                                'Passes_Chave_Percentil':'Passes_Chave'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'


            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}

                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_15_Mean_Charts = pd.read_csv('15_Role_Meia_Organizador.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_15_Mean_Charts.iloc[:, np.r_[1, 3, 28, 30, 18:28]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Frontais_Certos_LM'] = Role_x_Mean_Charts['Passes_Frontais_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Passes_TerçoFinal_Certos_LM'] = Role_x_Mean_Charts['Passes_TerçoFinal_Certos'].mean()
            Role_x_Mean_Charts['Passes_EntreLinhas_Certos_LM'] = Role_x_Mean_Charts['Passes_EntreLinhas_Certos'].mean()
            Role_x_Mean_Charts['Passes_Chave_LM'] = Role_x_Mean_Charts['Passes_Chave'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)

            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_15_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:14]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[14:24]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Passes_Longos_Certos_LM':'Passes_Longos_Certos', 'Passes_Frontais_Certos_LM':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_LM':'Passes_Progressivos_Certos', 
                                                'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 'xA_LM':'xA', 
                                                'Assistência_Finalização_LM':'Assistência_Finalização', 'Passes_TerçoFinal_Certos_LM':'Passes_TerçoFinal_Certos', 
                                                'Passes_EntreLinhas_Certos_LM':'Passes_EntreLinhas_Certos', 'Passes_Chave_LM':'Passes_Chave'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_15_Mean_Charts = pd.concat([Role_15_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_15_Mean_Charts = Role_15_Mean_Charts.append(League_Mean).reset_index()

            #Splitting Columns
            Role_15_Mean_Charts_1 = Role_15_Mean_Charts.iloc[:, np.r_[0, 1:6]]
            Role_15_Mean_Charts_2 = Role_15_Mean_Charts.iloc[:, np.r_[0, 6:11]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_15_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_15_Mean_Charts_1['Atleta'])):
                if Role_15_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_15_Mean_Charts_1.iloc[x].values.tolist()
                if Role_15_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_15_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_15_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_15_Mean_Charts_2['Atleta'])):
                if Role_15_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_15_Mean_Charts_2.iloc[x].values.tolist()
                if Role_15_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_15_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_2.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_2.png', dpi=600, bbox_inches="tight")

####################################################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:14]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

            #####################################################################################################################
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################
            # MEIA ATACANTE
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_16.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[19, 24, 36, 40:44, 38, 21]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==9)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>MEIA ATACANTE</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('16_Role_Meia_Atacante.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:35, 6, 35, 37]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==9)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2 = tabela_2.iloc[:, np.r_[0:18]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('16_Role_Meia_Atacante.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:35, 6, 35, 37]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==9)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[0:18, 19]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Passes_Longos_Certos', 'Passes_Frontais_Certos', 'Passes_Progressivos_Certos',
                                                    'Duelos_Ofensivos_Ganhos', 'Pisadas_Área', 'Dribles_BemSucedidos', 'xG', 'Finalizações_NoAlvo',
                                                    'Ameaça_Ofensiva', 'xA', 'Assistência_Finalização', 'Passes_TerçoFinal_Certos', 
                                                    'Passes_Inteligentes_Certos', 'Passes_EntreLinhas_Certos', 'Deep_Completions', 'Passes_Chave',
                                                    'Passes_ÁreaPênalti_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_16.csv')
            tabela_d = tabela_d.iloc[:, np.r_[78:95, 19, 24, 36, 38]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==9)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:17]]
            tabela_d = tabela_d.rename(columns={'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 'Passes_Frontais_Certos_Percentil':'Passes_Frontais_Certos',
                                                'Passes_Progressivos_Certos_Percentil': 'Passes_Progressivos_Certos', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 
                                                'Pisadas_Área_Percentil':'Pisadas_Área', 'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 'xG_Percentil':'xG', 
                                                'Finalizações_NoAlvo_Percentil':'Finalizações_NoAlvo', 'Ameaça_Ofensiva_Percentil':'Ameaça_Ofensiva', 'xA_Percentil':'xA',
                                                'Assistência_Finalização_Percentil':'Assistência_Finalização', 'Passes_TerçoFinal_Certos_Percentil':'Passes_TerçoFinal_Certos', 
                                                'Passes_Inteligentes_Certos_Percentil':'Passes_Inteligentes_Certos', 'Passes_EntreLinhas_Certos_Percentil':'Passes_EntreLinhas_Certos',
                                                'Deep_Completions_Percentil':'Deep_Completions', 'Passes_Chave_Percentil':'Passes_Chave', 'Passes_ÁreaPênalti_Certos_Percentil':'Passes_ÁreaPênalti_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'


            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}

    
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering
            
                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_16_Mean_Charts = pd.read_csv('16_Role_Meia_Atacante.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_16_Mean_Charts.iloc[:, np.r_[1, 3, 35, 37, 18:35]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Frontais_Certos_LM'] = Role_x_Mean_Charts['Passes_Frontais_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Pisadas_Área_LM'] = Role_x_Mean_Charts['Pisadas_Área'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['Finalizações_NoAlvo_LM'] = Role_x_Mean_Charts['Finalizações_NoAlvo'].mean()
            Role_x_Mean_Charts['Ameaça_Ofensiva_LM'] = Role_x_Mean_Charts['Ameaça_Ofensiva'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Passes_TerçoFinal_Certos_LM'] = Role_x_Mean_Charts['Passes_TerçoFinal_Certos'].mean()
            Role_x_Mean_Charts['Passes_Inteligentes_Certos_LM'] = Role_x_Mean_Charts['Passes_Inteligentes_Certos'].mean()
            Role_x_Mean_Charts['Passes_EntreLinhas_Certos_LM'] = Role_x_Mean_Charts['Passes_EntreLinhas_Certos'].mean()
            Role_x_Mean_Charts['Deep_Completions_LM'] = Role_x_Mean_Charts['Deep_Completions'].mean()
            Role_x_Mean_Charts['Passes_Chave_LM'] = Role_x_Mean_Charts['Passes_Chave'].mean()
            Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos_LM'] = Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_16_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:21]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[21:38]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Passes_Longos_Certos_LM':'Passes_Longos_Certos', 'Passes_Frontais_Certos_LM':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_LM':'Passes_Progressivos_Certos', 
                                                'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'Pisadas_Área_LM':'Pisadas_Área', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 'xG_LM':'xG',  
                                                'Finalizações_NoAlvo_LM':'Finalizações_NoAlvo', 'Ameaça_Ofensiva_LM':'Ameaça_Ofensiva', 'xA_LM':'xA', 'Assistência_Finalização_LM':'Assistência_Finalização', 'Passes_TerçoFinal_Certos_LM':'Passes_TerçoFinal_Certos', 
                                                'Passes_Inteligentes_Certos_LM':'Passes_Inteligentes_Certos', 'Passes_EntreLinhas_Certos_LM':'Passes_EntreLinhas_Certos', 'Deep_Completions_LM':'Deep_Completions', 
                                                'Passes_Chave_LM':'Passes_Chave', 'Passes_ÁreaPênalti_Certos_LM':'Passes_ÁreaPênalti_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_16_Mean_Charts = pd.concat([Role_16_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_16_Mean_Charts = Role_16_Mean_Charts.append(League_Mean).reset_index()
            #Role_16_Mean_Charts = Role_16_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    

            #Splitting Columns
            Role_16_Mean_Charts_1 = Role_16_Mean_Charts.iloc[:, np.r_[0, 1:10]]
            Role_16_Mean_Charts_2 = Role_16_Mean_Charts.iloc[:, np.r_[0, 10:18]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_16_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_16_Mean_Charts_1['Atleta'])):
                if Role_16_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_16_Mean_Charts_1.iloc[x].values.tolist()
                if Role_16_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_16_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_16_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_16_Mean_Charts_2['Atleta'])):
                if Role_16_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_16_Mean_Charts_2.iloc[x].values.tolist()
                if Role_16_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_16_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_2.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_2.png', dpi=600, bbox_inches="tight")

            ##########################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique", key="mais_graficos_key")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:21]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)



            #####################################################################################################################
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################
        elif posição == ("Extremo"):
            ##################################################################################################################### 
            #####################################################################################################################
            # EXTREMO ORGANIZADOR
            # Texto de Abertura
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_17.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[15, 20, 32, 36:40, 34, 17]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&((tabela_1['Código_Posição_Wyscout']==10)|(tabela_1['Código_Posição_Wyscout']==11))&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            ##################################################################################################################### 
            #####################################################################################################################
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_17.csv")
            tabela_a = tabela_a.iloc[:, np.r_[15, 17, 21:27, 28:31, 20, 32, 34]]
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&((tabela_a['Código_Posição_Wyscout']==10)|(tabela_a['Código_Posição_Wyscout']==11))&(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                formatter = {"Idade": "{:.0f}"}
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format(formatter).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            ##################################################################################################################### 
            #####################################################################################################################
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>EXTREMO ORGANIZADOR</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('17_Role_Extremo_Organizador.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&((tabela_2['Código_Posição_Wyscout']==10)|(tabela_2['Código_Posição_Wyscout']==11))&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2 = tabela_2.iloc[:, np.r_[0:14]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('17_Role_Extremo_Organizador.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_b = tabela_b[((tabela_b['Código_Posição_Wyscout']==10)|(tabela_b['Código_Posição_Wyscout']==11))&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:14, 15]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Passes_Longos_Certos', 'Passes_Frontais_Certos', 'Passes_Progressivos_Certos',
                                                    'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos', 'xG', 'Finalizações_NoAlvo',
                                                    'Conversão_Gols', 'xA', 'Assistência_Finalização', 'Passes_Inteligentes_Certos', 
                                                    'Passes_EntreLinhas_Certos', 'Passes_Chave']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_17.csv')
            tabela_d = tabela_d.iloc[:, np.r_[66:79, 15, 20, 32, 34]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&((tabela_d['Código_Posição_Wyscout']==10)|(tabela_d['Código_Posição_Wyscout']==11))&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:14]]
            tabela_d = tabela_d.rename(columns={'Passes_Longos_Certos_Percentil':'Passes_Longos_Certos', 'Passes_Frontais_Certos_Percentil':'Passes_Frontais_Certos',
                                                'Passes_Progressivos_Certos_Percentil': 'Passes_Progressivos_Certos', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 
                                                'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 'xG_Percentil':'xG', 'Finalizações_NoAlvo_Percentil':'Finalizações_NoAlvo', 
                                                'Conversão_Gols_Percentil':'Conversão_Gols', 'xA_Percentil':'xA', 'Assistência_Finalização_Percentil':'Assistência_Finalização', 
                                                'Passes_Inteligentes_Certos_Percentil':'Passes_Inteligentes_Certos', 'Passes_EntreLinhas_Certos_Percentil':'Passes_EntreLinhas_Certos',
                                                'Passes_Chave_Percentil':'Passes_Chave'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering
                return styled_df
            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_17_Mean_Charts = pd.read_csv('17_Role_Extremo_Organizador.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_17_Mean_Charts.iloc[:, np.r_[1, 3, 31, 33, 18:31]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Passes_Longos_Certos_LM'] = Role_x_Mean_Charts['Passes_Longos_Certos'].mean()
            Role_x_Mean_Charts['Passes_Frontais_Certos_LM'] = Role_x_Mean_Charts['Passes_Frontais_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['Finalizações_NoAlvo_LM'] = Role_x_Mean_Charts['Finalizações_NoAlvo'].mean()
            Role_x_Mean_Charts['Conversão_Gols_LM'] = Role_x_Mean_Charts['Conversão_Gols'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Passes_Inteligentes_Certos_LM'] = Role_x_Mean_Charts['Passes_Inteligentes_Certos'].mean()
            Role_x_Mean_Charts['Passes_EntreLinhas_Certos_LM'] = Role_x_Mean_Charts['Passes_EntreLinhas_Certos'].mean()
            Role_x_Mean_Charts['Passes_Chave_LM'] = Role_x_Mean_Charts['Passes_Chave'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_17_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:17]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[17:30]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Passes_Longos_Certos_LM':'Passes_Longos_Certos', 'Passes_Frontais_Certos_LM':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_LM':'Passes_Progressivos_Certos', 
                                                'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 'xG_LM':'xG',  
                                                'Finalizações_NoAlvo_LM':'Finalizações_NoAlvo', 'Conversão_Gols_LM':'Conversão_Gols', 'xA_LM':'xA', 'Assistência_Finalização_LM':'Assistência_Finalização', 
                                                'Passes_Inteligentes_Certos_LM':'Passes_Inteligentes_Certos', 'Passes_EntreLinhas_Certos_LM':'Passes_EntreLinhas_Certos', 
                                                'Passes_Chave_LM':'Passes_Chave'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_17_Mean_Charts = pd.concat([Role_17_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_17_Mean_Charts = Role_17_Mean_Charts.append(League_Mean).reset_index()
            #Role_17_Mean_Charts = Role_17_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    

            #Splitting Columns
            Role_17_Mean_Charts_1 = Role_17_Mean_Charts.iloc[:, np.r_[0, 1:8]]
            Role_17_Mean_Charts_2 = Role_17_Mean_Charts.iloc[:, np.r_[0, 8:14]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_17_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_17_Mean_Charts_1['Atleta'])):
                if Role_17_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_17_Mean_Charts_1.iloc[x].values.tolist()
                if Role_17_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_17_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_17_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_17_Mean_Charts_2['Atleta'])):
                if Role_17_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_17_Mean_Charts_2.iloc[x].values.tolist()
                if Role_17_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_17_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_2.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_2.png', dpi=600, bbox_inches="tight")

            ######################################################################################################################################
            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:17]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

            ##################################################################################################################### 
            #####################################################################################################################
            # EXTREMO TÁTICO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_18.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[9, 14, 26, 30:34, 28, 11]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&((tabela_1['Código_Posição_Wyscout']==10)|(tabela_1['Código_Posição_Wyscout']==11))&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>EXTREMO TÁTICO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('18_Role_Extremo_Tático.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:25, 6, 25, 27]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&((tabela_2['Código_Posição_Wyscout']==10)|(tabela_2['Código_Posição_Wyscout']==11))&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2 = tabela_2.iloc[:, np.r_[0:8]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('18_Role_Extremo_Tático.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:25, 6, 25, 27]]
            tabela_b = tabela_b[((tabela_b['Código_Posição_Wyscout']==10)|(tabela_b['Código_Posição_Wyscout']==11))&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:8, 9]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos', 'Passes_Frontais_Certos',
                                                    'Passes_Progressivos_Certos', 'Duelos_Ofensivos_Ganhos', 'xG', 'xA']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_18.csv')
            tabela_d = tabela_d.iloc[:, np.r_[48:55, 9, 14, 26, 28]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&((tabela_d['Código_Posição_Wyscout']==10)|(tabela_d['Código_Posição_Wyscout']==11))&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:7]]
            tabela_d = tabela_d.rename(columns={'Ações_Defensivas_BemSucedidas_Percentil':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_Percentil':'Duelos_Defensivos_Ganhos', 
                                                'Passes_Frontais_Certos_Percentil':'Passes_Frontais_Certos', 'Passes_Progressivos_Certos_Percentil': 'Passes_Progressivos_Certos', 
                                                'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 'xG_Percentil':'xG', 'xA_Percentil':'xA'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'


            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}

                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_18_Mean_Charts = pd.read_csv('18_Role_Extremo_Tático.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_18_Mean_Charts.iloc[:, np.r_[1, 3, 25, 27, 18:25]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas_LM'] = Role_x_Mean_Charts['Ações_Defensivas_BemSucedidas'].mean()
            Role_x_Mean_Charts['Duelos_Defensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Defensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Passes_Frontais_Certos_LM'] = Role_x_Mean_Charts['Passes_Frontais_Certos'].mean()
            Role_x_Mean_Charts['Passes_Progressivos_Certos_LM'] = Role_x_Mean_Charts['Passes_Progressivos_Certos'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_18_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:11]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[11:18]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Ações_Defensivas_BemSucedidas_LM':'Ações_Defensivas_BemSucedidas', 'Duelos_Defensivos_Ganhos_LM':'Duelos_Defensivos_Ganhos', 'Passes_Frontais_Certos_LM':'Passes_Frontais_Certos', 
                                                'Passes_Progressivos_Certos_LM':'Passes_Progressivos_Certos', 'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'xG_LM':'xG', 'xA_LM':'xA'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_18_Mean_Charts = pd.concat([Role_18_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_18_Mean_Charts = Role_18_Mean_Charts.append(League_Mean).reset_index()

            #Splitting Columns
            Role_18_Mean_Charts_1 = Role_18_Mean_Charts.iloc[:, np.r_[0, 1:8]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_18_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_18_Mean_Charts_1['Atleta'])):
                if Role_18_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_18_Mean_Charts_1.iloc[x].values.tolist()
                if Role_18_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_18_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                #subtitle_name = clube,
                #subtitle_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                #subtitle_name_2 = liga,
                #subtitle_color_2 = '#344D94',
                title_fontsize = 18,
                #subtitle_fontsize = 15,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            #####################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique", key="mais_graficos_key")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:11]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)


            #####################################################################################################################
            #####################################################################################################################
            # EXTREMO AGUDO
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_19.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[15, 20, 32, 36:40, 34, 17]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&((tabela_1['Código_Posição_Wyscout']==10)|(tabela_1['Código_Posição_Wyscout']==11))&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>EXTREMO AGUDO</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('19_Role_Extremo_Agudo.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&((tabela_2['Código_Posição_Wyscout']==10)|(tabela_2['Código_Posição_Wyscout']==11))&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2 = tabela_2.iloc[:, np.r_[0:14]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('19_Role_Extremo_Agudo.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_b = tabela_b[((tabela_b['Código_Posição_Wyscout']==10)|(tabela_b['Código_Posição_Wyscout']==11))&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[0:14, 15]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Duelos_Ofensivos_Ganhos', 'Pisadas_Área', 'Dribles_BemSucedidos', 'Acelerações', 
                                                    'Passes_Longos_Recebidos', 'xG', 'Finalizações_NoAlvo', 'Conversão_Gols', 'xA', 
                                                    'Assistência_Finalização', 'Deep_Completions', 'Deep_Completed_Crosses', 'Passes_Chave']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_19.csv')
            tabela_d = tabela_d.iloc[:, np.r_[66:79, 15, 20, 32, 34]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&((tabela_d['Código_Posição_Wyscout']==10)|(tabela_d['Código_Posição_Wyscout']==11))&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:13]]
            tabela_d = tabela_d.rename(columns={'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 'Pisadas_Área_Percentil':'Pisadas_Área', 
                                                'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 'Acelerações_Percentil':'Acelerações', 
                                                'Passes_Longos_Recebidos_Percentil':'Passes_Longos_Recebidos', 'xG_Percentil':'xG', 'Finalizações_NoAlvo_Percentil':'Finalizações_NoAlvo', 
                                                'Conversão_Gols_Percentil':'Conversão_Gols', 'xA_Percentil':'xA', 'Assistência_Finalização_Percentil':'Assistência_Finalização', 
                                                'Deep_Completions_Percentil':'Deep_Completions', 'Deep_Completed_Crosses_Percentil':'Deep_Completed_Crosses', 
                                                'Passes_Chave_Percentil':'Passes_Chave'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df
        
            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            #####################################################################################################################
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_19_Mean_Charts = pd.read_csv('19_Role_Extremo_Agudo.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_19_Mean_Charts.iloc[:, np.r_[1, 3, 31, 33, 18:31]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Pisadas_Área_LM'] = Role_x_Mean_Charts['Pisadas_Área'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Acelerações_LM'] = Role_x_Mean_Charts['Acelerações'].mean()
            Role_x_Mean_Charts['Passes_Longos_Recebidos_LM'] = Role_x_Mean_Charts['Passes_Longos_Recebidos'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['Finalizações_NoAlvo_LM'] = Role_x_Mean_Charts['Finalizações_NoAlvo'].mean()
            Role_x_Mean_Charts['Conversão_Gols_LM'] = Role_x_Mean_Charts['Conversão_Gols'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Deep_Completions_LM'] = Role_x_Mean_Charts['Deep_Completions'].mean()
            Role_x_Mean_Charts['Deep_Completed_Crosses_LM'] = Role_x_Mean_Charts['Deep_Completed_Crosses'].mean()
            Role_x_Mean_Charts['Passes_Chave_LM'] = Role_x_Mean_Charts['Passes_Chave'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_19_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:17]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[17:30]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'Pisadas_Área_LM':'Pisadas_Área', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 
                                                    'Acelerações_LM':'Acelerações', 'Passes_Longos_Recebidos_LM':'Passes_Longos_Recebidos', 'xG_LM':'xG', 'Finalizações_NoAlvo_LM':'Finalizações_NoAlvo', 'Conversão_Gols_LM':'Conversão_Gols', 
                                                    'xA_LM':'xA', 'Assistência_Finalização_LM':'Assistência_Finalização', 'Deep_Completions_LM':'Deep_Completions', 'Deep_Completed_Crosses_LM':'Deep_Completed_Crosses', 
                                                    'Passes_Chave_LM':'Passes_Chave'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_19_Mean_Charts = pd.concat([Role_19_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_19_Mean_Charts = Role_19_Mean_Charts.append(League_Mean).reset_index()
            #Role_19_Mean_Charts = Role_19_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    

            #Splitting Columns
            Role_19_Mean_Charts_1 = Role_19_Mean_Charts.iloc[:, np.r_[0, 1:8]]
            Role_19_Mean_Charts_2 = Role_19_Mean_Charts.iloc[:, np.r_[0, 8:14]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_19_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_19_Mean_Charts_1['Atleta'])):
                if Role_19_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_19_Mean_Charts_1.iloc[x].values.tolist()
                if Role_19_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_19_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_19_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_19_Mean_Charts_2['Atleta'])):
                if Role_19_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_19_Mean_Charts_2.iloc[x].values.tolist()
                if Role_19_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_19_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_2.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_2.png', dpi=600, bbox_inches="tight")

            ##########################################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique", key="2_mais_graficos_key")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:17]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)



                #####################################################################################################################
                #####################################################################################################################
                #####################################################################################################################
                ##################################################################################################################### 
        elif posição == ("Atacante"):
            ##################################################################################################################### 
            #####################################################################################################################
            # ATACANTE REFERÊNCIA
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_20.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[12, 17, 29, 33:37, 31, 14]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==12)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            ##################################################################################################################### 
            #####################################################################################################################
            # Texto de Abertura
            markdown_amount_1 = f"<div style='text-align:center; font-size:{fontsize}px'>{jogadores:}</div>"
            markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>{clube:}</div>"
            st.markdown("<h4 style='text-align: center;'>Jogador Selecionado</b></h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_1, unsafe_allow_html=True)
            st.markdown(markdown_amount_2, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # Dados Básicos do Jogador
            tabela_a  = pd.read_csv("PlayerAnalysis_Role_20.csv")
            tabela_a = tabela_a.iloc[:, np.r_[12, 14, 19:24, 25:28, 17, 29, 31]]
            tabela_a = tabela_a[(tabela_a['Atleta']==jogadores)&(tabela_a['Código_Posição_Wyscout']==12)&(tabela_a['Versão_Temporada']==temporada)&(tabela_a['Liga']==liga)]
            tabela_a  = tabela_a.iloc[:, np.r_[0:3, 4:10]]
            st.markdown("<h4 style='text-align: center;'>Dados Básicos</b></h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_a, use_container_width=True, hide_index=True)

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index(drop=True)
                df = df.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Valor_Mercado': 'Valor', 'Nacionalidade': 'Nacional'})
                formatter = {"Idade": "{:.0f}"}
                # Ensure 'Rating' is rounded and formatted to 3 decimal places during styling
                return df.style.format(formatter).set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px',
                                    'font-size': '15px'})

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML without the index and display it
                styled_html = style_table(tabela_a).to_html(escape=False, index=False, hide_index=True)
                st.markdown(styled_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()

            #####################################################################################################################
            #####################################################################################################################
            st.markdown("<h3 style='text-align: center;'><br>ATACANTE REFERÊNCIA</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################

            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('20_Role_Atacante_Referência.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:28, 6, 28, 30]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==12)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2 = tabela_2.iloc[:, np.r_[0:12]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('20_Role_Atacante_Referência.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:28, 6, 28, 30]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==12)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:12, 12]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Duelos_Aéreos_Ganhos', 'Duelos_Ofensivos_Ganhos', 'xG', 'Conversão_Gols', 
                                                  'Conversão_xG', 'Ameaça_Ofensiva', 'xA', 'Deep_Completions', 'Passes_Chave', 
                                                  'Passes_ÁreaPênalti_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_20.csv')
            tabela_d = tabela_d.iloc[:, np.r_[57:67, 12, 17, 29, 31]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==12)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:10]]
            tabela_d = tabela_d.rename(columns={'Duelos_Aéreos_Ganhos_Percentil':'Duelos_Aéreos_Ganhos', 'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 
                                                'xG_Percentil':'xG', 'Conversão_Gols_Percentil':'Conversão_Gols', 'Conversão_xG_Percentil':'Conversão_xG', 
                                                'Ameaça_Ofensiva_Percentil':'Ameaça_Ofensiva', 'xA_Percentil':'xA',  
                                                'Deep_Completions_Percentil':'Deep_Completions', 'Passes_Chave_Percentil':'Passes_Chave', 
                                                'Passes_ÁreaPênalti_Certos_Percentil':'Passes_ÁreaPênalti_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()
            tabela_2 = tabela_2.drop(tabela_2.index[-1])

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            #st.dataframe(tabela_2, use_container_width=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
    
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering

                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################

            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_20_Mean_Charts = pd.read_csv('20_Role_Atacante_Referência.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_20_Mean_Charts.iloc[:, np.r_[1, 3, 28, 30, 18:28]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Duelos_Aéreos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Aéreos_Ganhos'].mean()
            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['Conversão_Gols_LM'] = Role_x_Mean_Charts['Conversão_Gols'].mean()
            Role_x_Mean_Charts['Conversão_xG_LM'] = Role_x_Mean_Charts['Conversão_xG'].mean()
            Role_x_Mean_Charts['Ameaça_Ofensiva_LM'] = Role_x_Mean_Charts['Ameaça_Ofensiva'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Deep_Completions_LM'] = Role_x_Mean_Charts['Deep_Completions'].mean()
            Role_x_Mean_Charts['Passes_Chave_LM'] = Role_x_Mean_Charts['Passes_Chave'].mean()
            Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos_LM'] = Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_20_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:14]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[14:24]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Duelos_Aéreos_Ganhos_LM':'Duelos_Aéreos_Ganhos', 'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'xG_LM':'xG', 'Conversão_Gols_LM':'Conversão_Gols', 
                                                    'Conversão_xG_LM':'Conversão_xG', 'Ameaça_Ofensiva_LM':'Ameaça_Ofensiva', 'xA_LM':'xA', 'Deep_Completions_LM':'Deep_Completions',  
                                                    'Passes_Chave_LM':'Passes_Chave', 'Passes_ÁreaPênalti_Certos_LM':'Passes_ÁreaPênalti_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_20_Mean_Charts = pd.concat([Role_20_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_20_Mean_Charts = Role_20_Mean_Charts.append(League_Mean).reset_index()
            #Role_20_Mean_Charts = Role_20_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    

            #Splitting Columns
            Role_20_Mean_Charts_1 = Role_20_Mean_Charts.iloc[:, np.r_[0, 1:11]]
            #Role_20_Mean_Charts_2 = Role_20_Mean_Charts.iloc[:, np.r_[1, 9:15]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_20_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_20_Mean_Charts_1['Atleta'])):
                if Role_20_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_20_Mean_Charts_1.iloc[x].values.tolist()
                if Role_20_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_20_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            #####################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:14]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)

            ##################################################################################################################### 
            #####################################################################################################################
            ##################################################################################################################### 
            #####################################################################################################################
            # SEGUNDO ATACANTE
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_22.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[15, 20, 32, 36:40, 34, 17]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==12)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>SEGUNDO ATACANTE</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('22_Role_Segundo_Atacante.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==12)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2 = tabela_2.iloc[:, np.r_[0:14]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('22_Role_Segundo_Atacante.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:31, 6, 31, 33]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==12)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:14, 15]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos', 'Acelerações', 'xG', 
                                                    'Finalizações_NoAlvo', 'Conversão_Gols', 'Conversão_xG', 'Ameaça_Ofensiva', 'xA', 
                                                    'Assistência_Finalização', 'Deep_Completions', 'Passes_Chave', 'Passes_ÁreaPênalti_Certos']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_22.csv')
            tabela_d = tabela_d.iloc[:, np.r_[66:79, 15, 20, 32, 34]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==12)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:13]]
            tabela_d = tabela_d.rename(columns={'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 
                                                'Acelerações_Percentil':'Acelerações', 'xG_Percentil':'xG', 'Finalizações_NoAlvo_Percentil':'Finalizações_NoAlvo', 
                                                'Conversão_Gols_Percentil':'Conversão_Gols', 'Conversão_xG_Percentil':'Conversão_xG', 
                                                'Ameaça_Ofensiva_Percentil':'Ameaça_Ofensiva', 'xA_Percentil':'xA', 'Assistência_Finalização_Percentil':'Assistência_Finalização', 
                                                'Deep_Completions_Percentil':'Deep_Completions', 'Passes_Chave_Percentil':'Passes_Chave', 
                                                'Passes_ÁreaPênalti_Certos_Percentil':'Passes_ÁreaPênalti_Certos'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering
                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False, hide_index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_22_Mean_Charts = pd.read_csv('22_Role_Segundo_Atacante.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_22_Mean_Charts.iloc[:, np.r_[1, 3, 31, 33, 18:31]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Acelerações_LM'] = Role_x_Mean_Charts['Acelerações'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['Finalizações_NoAlvo_LM'] = Role_x_Mean_Charts['Finalizações_NoAlvo'].mean()
            Role_x_Mean_Charts['Conversão_Gols_LM'] = Role_x_Mean_Charts['Conversão_Gols'].mean()
            Role_x_Mean_Charts['Conversão_xG_LM'] = Role_x_Mean_Charts['Conversão_xG'].mean()
            Role_x_Mean_Charts['Ameaça_Ofensiva_LM'] = Role_x_Mean_Charts['Ameaça_Ofensiva'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            Role_x_Mean_Charts['Deep_Completions_LM'] = Role_x_Mean_Charts['Deep_Completions'].mean()
            Role_x_Mean_Charts['Passes_Chave_LM'] = Role_x_Mean_Charts['Passes_Chave'].mean()
            Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos_LM'] = Role_x_Mean_Charts['Passes_ÁreaPênalti_Certos'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_22_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:17]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[17:30]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 
                                                    'Acelerações_LM':'Acelerações', 'xG_LM':'xG', 'Finalizações_NoAlvo_LM':'Finalizações_NoAlvo', 'Conversão_Gols_LM':'Conversão_Gols', 
                                                    'Conversão_xG_LM':'Conversão_xG', 'Ameaça_Ofensiva_LM':'Ameaça_Ofensiva', 'xA_LM':'xA', 'Assistência_Finalização_LM':'Assistência_Finalização', 
                                                    'Deep_Completions_LM':'Deep_Completions', 'Passes_Chave_LM':'Passes_Chave', 'Passes_ÁreaPênalti_Certos_LM':'Passes_ÁreaPênalti_Certos'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_22_Mean_Charts = pd.concat([Role_22_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_22_Mean_Charts = Role_22_Mean_Charts.append(League_Mean).reset_index()
            #Role_22_Mean_Charts = Role_22_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    

            #Splitting Columns
            Role_22_Mean_Charts_1 = Role_22_Mean_Charts.iloc[:, np.r_[0, 1:8]]
            Role_22_Mean_Charts_2 = Role_22_Mean_Charts.iloc[:, np.r_[0, 8:14]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_22_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_22_Mean_Charts_1['Atleta'])):
                if Role_22_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_22_Mean_Charts_1.iloc[x].values.tolist()
                if Role_22_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_22_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            # Preparing Graph 2
            # Get Parameters

            params = list(Role_22_Mean_Charts_2.columns)
            params = params[1:]
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_22_Mean_Charts_2['Atleta'])):
                if Role_22_Mean_Charts_2['Atleta'][x] == jogadores:
                    a_values = Role_22_Mean_Charts_2.iloc[x].values.tolist()
                if Role_22_Mean_Charts_2['Atleta'][x] == 'Média da Liga':
                    b_values = Role_22_Mean_Charts_2.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_2.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_2.png', dpi=600, bbox_inches="tight")

            #####################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique", key="mais_graficos_key")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:17]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)


            ##################################################################################################################### 
            #####################################################################################################################

            # ATACANTE MÓVEL
            # Elaborar Tabela de Abertura com Rating, Ranking, Percentil
            tabela_1 = pd.read_csv('PlayerAnalysis_Role_21.csv')
            tabela_1  = tabela_1.iloc[:, np.r_[11, 16, 28, 32:36, 30, 13]]
            tabela_1 = tabela_1[(tabela_1['Atleta']==jogadores)&(tabela_1['Código_Posição_Wyscout']==12)&(tabela_1['Versão_Temporada']==temporada)&(tabela_1['Liga']==liga)]
            clube = tabela_1.iat[0, 8]
            rating = tabela_1.iat[0, 3]
            ranking = tabela_1.iat[0,4]
            percentil = tabela_1.iat[0,6]
            size = tabela_1.iat[0,5]
            fontsize = 20
            # Texto de Abertura
            st.markdown("<h3 style='text-align: center;'>ATACANTE MÓVEL</b></h3>", unsafe_allow_html=True)
            # Rating/Ranking/Percentil
            markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>{rating:}</div>"
            markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>{ranking:}</div>"
            markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>{percentil:}</div>"
            markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>(Total de {size:} jogadores na Liga)</div>"
            st.markdown("<h4 style='text-align: center;'>Rating/Ranking/Percentil do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)
            st.markdown(markdown_amount_6, unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<h4 style='text-align: center;'>Rating</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_3, unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center;'>Ranking</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_4, unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center;'>Percentil</b></h4>", unsafe_allow_html=True)
                st.markdown(markdown_amount_5, unsafe_allow_html=True)
            st.markdown("---")
            ##################################################################################################################### 
            #####################################################################################################################
            # #Elaborar Tabela com Métricas do Atleta
            tabela_2 = pd.read_csv('21_Role_Atacante_Móvel.csv')
            tabela_2 = tabela_2.iloc[:, np.r_[1, 18:27, 6, 27, 29]]
            tabela_2 = tabela_2[(tabela_2['Atleta']==jogadores)&(tabela_2['Código_Posição_Wyscout']==12)&(tabela_2['Versão_Temporada']==temporada)&(tabela_2['Liga']==liga)]
            tabela_2 = tabela_2.iloc[:, np.r_[0:10]]
            tabela_2  = pd.DataFrame(tabela_2)
            tabela_2 = tabela_2.round(decimals=2)
            # Média da Liga
            tabela_b = pd.read_csv('21_Role_Atacante_Móvel.csv')
            tabela_b = tabela_b.iloc[:, np.r_[1, 18:27, 6, 27, 29]]
            tabela_b = tabela_b[(tabela_b['Código_Posição_Wyscout']==12)&(tabela_b['Versão_Temporada']==temporada)&(tabela_b['Liga']==liga)]
            tabela_b = tabela_b.iloc[:, np.r_[1:10, 11]]
            tabela_b = tabela_b.round(decimals=2)
            tabela_c = (tabela_b.groupby('Liga')[['Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos', 'Acelerações', 'xG', 
                                                    'Conversão_Gols', 'Conversão_xG', 'Ameaça_Ofensiva', 'xA', 
                                                    'Assistência_Finalização']].mean())
            tabela_c = tabela_c.round(decimals=2)
            Atleta = ['Média da Liga']
            tabela_c['Atleta'] = Atleta 
            tabela_c.insert(0, 'Atleta', tabela_c.pop('Atleta'))
            # Percentil na Liga
            tabela_d = pd.read_csv('PlayerAnalysis_Role_21.csv')
            tabela_d = tabela_d.iloc[:, np.r_[54:63, 11, 16, 28, 30]]
            tabela_d = tabela_d[(tabela_d['Atleta']==jogadores)&(tabela_d['Código_Posição_Wyscout']==12)&(tabela_d['Versão_Temporada']==temporada)&(tabela_d['Liga']==liga)]
            tabela_d = tabela_d.iloc[:, np.r_[0:9]]
            tabela_d = tabela_d.rename(columns={'Duelos_Ofensivos_Ganhos_Percentil':'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos_Percentil':'Dribles_BemSucedidos', 
                                                'Acelerações_Percentil':'Acelerações', 'xG_Percentil':'xG', 'Conversão_Gols_Percentil':'Conversão_Gols', 
                                                'Conversão_xG_Percentil':'Conversão_xG', 'Ameaça_Ofensiva_Percentil':'Ameaça_Ofensiva', 'xA_Percentil':'xA', 
                                                'Assistência_Finalização_Percentil':'Assistência_Finalização'})
            Atleta = ['Percentil na Liga']
            tabela_d['Atleta'] = Atleta 
            tabela_d.insert(0, 'Atleta', tabela_d.pop('Atleta'))
            tabela_2 = pd.concat([tabela_2, tabela_c, tabela_d]).reset_index(drop=True)
            tabela_2.rename(columns={'Atleta': 'Métricas'}, inplace=True)
            tabela_2 = tabela_2.transpose()

            st.markdown("<h4 style='text-align: center;'>Desempenho do Jogador na Liga/Temporada</h4>", unsafe_allow_html=True)

            # Define function to color and label cells in the "Percentil na Liga" column
            def color_percentil(val):
                # Color map for "Blues" from Matplotlib
                cmap = plt.get_cmap('Blues')

                # Define categories and corresponding thresholds
                if val >= 90:
                    color = cmap(0.8)  # "Elite"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 75 <= val < 90:
                    color = cmap(0.65)  # "Destaque"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 60 <= val < 75:
                    color = cmap(0.5)  # "Razoável"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                elif 40 <= val < 60:
                    color = cmap(0.35)  # "Mediano"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'
                else:
                    color = cmap(0.2)  # "Fraco"
                    return f'background-color: rgba({color[0]*255}, {color[1]*255}, {color[2]*255}, 0.8); color: black'

            # Styling DataFrame using Pandas
            def style_table(df):
                df = df.reset_index()  # If you want the index to be a visible column
                new_header = df.iloc[0]  # Capture the first row to use as column headers
                df = df[1:]  # Remove the first row from the data
                df.columns = new_header  # Set the new column headers
                first_column_name = df.columns[1]  # Adjusted for the added index column
                # Ensure 'Rating' is rounded and formatted to 2 decimal places during styling
                formatter = {first_column_name: "{:.2f}", "Média da Liga": "{:.2f}", "Percentil na Liga": "{:.0f}"}
    
                # Apply the color formatting to "Percentil na Liga" column
                styled_df = df.style.format(formatter).applymap(color_percentil, subset=["Percentil na Liga"])

                # Additional table styles
                styled_df = styled_df.set_table_styles(
                    [{
                        'selector': 'thead th',
                        'props': [('font-weight', 'bold'),
                                ('border-style', 'solid'),
                                ('border-width', '0px 0px 2px 0px'),
                                ('border-color', 'black')]
                    }, {
                        'selector': 'thead th:not(:first-child)',
                        'props': [('text-align', 'center')]  # Centering all headers except the first
                    }, {
                        'selector': 'thead th:last-child',
                        'props': [('color', 'black')]  # Make last column header black
                    }, {
                        'selector': 'td',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'center')]
                    }, {
                        'selector': 'th',
                        'props': [('border-style', 'solid'),
                                ('border-width', '0px 0px 1px 0px'),
                                ('border-color', 'black'),
                                ('text-align', 'left')]
                    }]
                ).set_properties(**{'padding': '2px', 'font-size': '15px', 'margin': 'auto'})  # Adjust this for centering
                return styled_df

            # Displaying in Streamlit
            def main():
                #st.title("Your DataFrame")

                # Convert the styled DataFrame to HTML, ensure the index is shown and wrapped in a center-aligned div
                styled_html = style_table(tabela_2).to_html(escape=False, index=False)
                center_html = f"<div style='margin-left: auto; margin-right: auto; width: fit-content;'>{styled_html}</div>"
                st.markdown(center_html, unsafe_allow_html=True)

            if __name__ == '__main__':
                main()


            # Function to plot the legend for the 5 colors from the Blues colormap
            def plot_color_legend():
                # Create a list of 5 normalized values (from lowest to highest)
                values = np.linspace(0, 0.5, 5)  # Normalized between 0 and 0.5 to cover half of the Blues colormap
                
                # Generate corresponding colors using the 'Blues' colormap
                colors = plt.cm.Blues(values)
                
                # Labels for the legend (highest to lowest)
                labels = ['Elite (>90)', 'Destaque (75-90)', 'Razoável (60-75)', 'Mediano (40-60)', 'Frágil (<40)']
                
                # Plot the legend horizontally with a smaller size
                fig, ax = plt.subplots(figsize=(6, 0.2))  # Smaller layout
                for i, (label, color) in enumerate(zip(labels[::-1], colors)):  # Reverse labels for display
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black'))  # Draw rectangle
                    ax.text(i + 0.5, 0.5, label, ha='center', va='center', fontsize=7)  # Add text inside the rectangles
                
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 1)
                ax.axis('off')  # Remove axes
                
                # Add an arrow pointing from "Highest" to "Lowest"
                ax.annotate('', xy=(5, 1), xytext=(0, 1),
                            arrowprops=dict(facecolor='black', shrink=0.04, width=1.3, headwidth=5))

                return fig

            # Call the function to plot the legend and display it in Streamlit
            legend_fig = plot_color_legend()
            st.pyplot(legend_fig)

            ##################################################################################################################### 
            #####################################################################################################################
            #Plotar Gráfico Alternativo
            # Player Comparison Data
            st.markdown("<h4 style='text-align: center;'><br>Comparativo do Jogador com a Média da Liga</h4>", unsafe_allow_html=True)
            Role_21_Mean_Charts = pd.read_csv('21_Role_Atacante_Móvel.csv')
            #PLOTTING COMPARISON BETWEEN 1 PLAYER AND LEAGUE MEAN
            #Determining Club and League 
            Role_x_Mean_Charts  = Role_21_Mean_Charts.iloc[:, np.r_[1, 3, 27, 29, 18:27]]
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Versão_Temporada']==temporada)&(Role_x_Mean_Charts['Liga']==liga)]

            Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos_LM'] = Role_x_Mean_Charts['Duelos_Ofensivos_Ganhos'].mean()
            Role_x_Mean_Charts['Dribles_BemSucedidos_LM'] = Role_x_Mean_Charts['Dribles_BemSucedidos'].mean()
            Role_x_Mean_Charts['Acelerações_LM'] = Role_x_Mean_Charts['Acelerações'].mean()
            Role_x_Mean_Charts['xG_LM'] = Role_x_Mean_Charts['xG'].mean()
            Role_x_Mean_Charts['Conversão_Gols_LM'] = Role_x_Mean_Charts['Conversão_Gols'].mean()
            Role_x_Mean_Charts['Conversão_xG_LM'] = Role_x_Mean_Charts['Conversão_xG'].mean()
            Role_x_Mean_Charts['Ameaça_Ofensiva_LM'] = Role_x_Mean_Charts['Ameaça_Ofensiva'].mean()
            Role_x_Mean_Charts['xA_LM'] = Role_x_Mean_Charts['xA'].mean()
            Role_x_Mean_Charts['Assistência_Finalização_LM'] = Role_x_Mean_Charts['Assistência_Finalização'].mean()
            
            Role_x_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            Role_y_Mean_Charts  = pd.DataFrame(Role_x_Mean_Charts)
            
            Role_x_Mean_Charts = Role_x_Mean_Charts[(Role_x_Mean_Charts['Atleta']==jogadores)]
            
            #Selecting data to compare 1 player and league mean
            Role_21_Mean_Charts  = Role_x_Mean_Charts.iloc[:, np.r_[0, 4:13]]

            #Preparing League Mean Data
            League_Mean = Role_x_Mean_Charts.iloc[:, np.r_[13:22]]
            League_Mean['Atleta'] = 'Média da Liga' 
            League_Mean.insert(0, 'Atleta', League_Mean.pop('Atleta'))
            League_Mean = League_Mean.rename(columns={'Duelos_Ofensivos_Ganhos_LM':'Duelos_Ofensivos_Ganhos', 'Dribles_BemSucedidos_LM':'Dribles_BemSucedidos', 
                                                    'Acelerações_LM':'Acelerações', 'xG_LM':'xG', 'Conversão_Gols_LM':'Conversão_Gols', 
                                                    'Conversão_xG_LM':'Conversão_xG', 'Ameaça_Ofensiva_LM':'Ameaça_Ofensiva', 'xA_LM':'xA', 'Assistência_Finalização_LM':'Assistência_Finalização'})
            #Merging Dataframes
            #Adjusting Player Dataframe
            #Concatenating Dataframes
            Role_21_Mean_Charts = pd.concat([Role_21_Mean_Charts, League_Mean]).reset_index(drop=True)
            #Role_21_Mean_Charts = Role_21_Mean_Charts.append(League_Mean).reset_index()
            #Role_21_Mean_Charts = Role_21_Mean_Charts.rename(columns={'Interceptações.1': 'Interceptações'})    

            #Splitting Columns
            Role_21_Mean_Charts_1 = Role_21_Mean_Charts.iloc[:, np.r_[0, 1:10]]
            #Role_21_Mean_Charts_2 = Role_21_Mean_Charts.iloc[:, np.r_[1, 9:15]]


            # Preparing Graph 1
            # Get Parameters

            params = list(Role_21_Mean_Charts_1.columns)
            params = params[1:]
            
            #Preparing Data
            ranges = []
            a_values = []
            b_values = []

            for x in params:
                a = min(Role_y_Mean_Charts[params][x])
                a = a
                b = max(Role_y_Mean_Charts[params][x])
                b = b
                ranges.append((a, b))

            for x in range(len(Role_21_Mean_Charts_1['Atleta'])):
                if Role_21_Mean_Charts_1['Atleta'][x] == jogadores:
                    a_values = Role_21_Mean_Charts_1.iloc[x].values.tolist()
                if Role_21_Mean_Charts_1['Atleta'][x] == 'Média da Liga':
                    b_values = Role_21_Mean_Charts_1.iloc[x].values.tolist()
                        
            a_values = a_values[1:]
            b_values = b_values[1:]

            values = [a_values, b_values]

            #Plotting Data
            title = dict(
                title_name = jogadores,
                title_color = '#B6282F',
                title_name_2 = 'Média da Liga',
                title_color_2 = '#344D94',
                title_fontsize = 18,
            ) 

            endnote = 'Viz by@JAmerico1898\ Data from Wyscout\nAll features are per90'

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,radar_color=['#B6282F', '#344D94'], dpi=600, alphas=[.8,.6], title=title, endnote=endnote, compare=True)
            plt.savefig('Player&League_Comparison_1.png')
            st.pyplot(fig)
            fig.savefig('Player&League_Comparison_1.png', dpi=600, bbox_inches="tight")

            #####################################################################################################################

            # Plotting KDE Comparison Graphs
            mais_gráficos = st.button("Para gráficos adicionais por métrica, clique", key="2_mais_graficos_key")
            if mais_gráficos:
                st.markdown("<h4 style='text-align: center;'><br>Posição Relativa do Jogador na Liga<br></h4>", unsafe_allow_html=True)
                # Select columns from 4 to 10 (7 columns in total)
                selected_columns = Role_y_Mean_Charts.iloc[:, 4:13]

                # Plot KDE for each selected column in pairs
                for i in range(0, len(selected_columns.columns), 2):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))  # Always create two subplots

                    # Plot first column in the pair
                    density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='blue', bw_adjust=0.5)
                    sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i], ax=ax1, color='red', height=0.05)  # Adding rug plot
                    x_vals = density.get_lines()[0].get_xdata()
                    y_vals = density.get_lines()[0].get_ydata()
                    ax1.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
                    player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i]].values[0]
                    ax1.axvline(x=player_value, color='red', linewidth=2)
                    ax1.text(player_value + 0.01 * (ax1.get_xlim()[1] - ax1.get_xlim()[0]), ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                    ax1.set_title(f'{selected_columns.columns[i]}', fontsize=18, fontweight='bold')
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['left'].set_visible(False)
                    ax1.set_xlabel('')
                    ax1.set_ylabel('')
                    ax1.tick_params(axis='x', labelsize=14)
                    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)


                    if i + 1 < len(selected_columns.columns):  # Check if there is a second plot to render
                        # Plot second column in the pair
                        density = sns.kdeplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='blue', bw_adjust=0.5)
                        sns.rugplot(data=Role_y_Mean_Charts, x=selected_columns.columns[i+1], ax=ax2, color='red', height=0.05)  # Adding rug plot
                        x_vals = density.get_lines()[0].get_xdata()
                        y_vals = density.get_lines()[0].get_ydata()
                        ax2.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)                                
                        player_value = Role_y_Mean_Charts.loc[Role_y_Mean_Charts['Atleta'] == jogadores, selected_columns.columns[i+1]].values[0]
                        ax2.axvline(x=player_value, color='red', linewidth=2)
                        ax2.text(player_value + 0.01 * (ax2.get_xlim()[1] - ax2.get_xlim()[0]), ax2.get_ylim()[0] + (ax2.get_ylim()[1] - ax2.get_ylim()[0]) * 0.1, jogadores, color='red', fontsize=17, verticalalignment='bottom')
                        ax2.set_title(f'{selected_columns.columns[i+1]}', fontsize=18, fontweight='bold')
                        ax2.spines['top'].set_visible(False)
                        ax2.spines['right'].set_visible(False)
                        ax2.spines['left'].set_visible(False)
                        ax2.set_xlabel('')
                        ax2.set_ylabel('')
                        ax2.tick_params(axis='x', labelsize=14)
                        ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

                    else:
                        # Instead of hiding the second axis, we simply clear it
                        ax2.clear()
                        ax2.axis('off')  # Turn off the axis if not used

                    plt.tight_layout()  # Adjust layout to prevent overlap
                    st.pyplot(fig)



                        #####################################################################################################################
                        #####################################################################################################################
                        #####################################################################################################################
                        #####################################################################################################################

if choose == "Compare Jogadores":
    
    #CABEÇALHO DO FORM
    st.markdown("<h1 style='text-align: center;'>Melhores do Brasileirão até a Rodada 25</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>app by @JAmerico1898</h6>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<h2 style='text-align: center;'>Compare Jogadores</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Série A - 2024</h3>", unsafe_allow_html=True)
    st.markdown("---")

    
    jogador_1 = st.selectbox("Escolha o primeiro Jogador!", options=jogadores, index=None, placeholder="Escolha o primeiro Jogador!")

    if jogador_1:
        #Determinar Equipe e Posição
        df20 = df.loc[(df['Atleta']==jogador_1)]
        equipes = df20['Equipe'].unique()
        equipe_1 = st.selectbox("Escolha o Clube do primeiro Jogador!", options=equipes)
        posições = df20['Posição2'].unique()
        posição_1 = st.selectbox("Escolha a Posição do primeiro Jogador!", options=posições)

    jogador_2 = st.selectbox("Escolha o segundo Jogador!", options=jogadores, index=None, placeholder="Escolha o segundo Jogador!")

    if jogador_2:
        #Determinar Equipe e Posição
        df20 = df.loc[(df['Atleta']==jogador_2)]
        equipes = df20['Equipe'].unique()
        equipe_2 = st.selectbox("Escolha o Clube do segundo Jogador!", options=equipes)
        posições = df20['Posição2'].unique()
        posição_2 = st.selectbox("Escolha a Posição do segundo Jogador!", options=posições)

        if (posição_1 == posição_2 == ("Goleiro")):
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Goleiro Clássico</h3>", unsafe_allow_html=True)
            Goleiro_Charts = pd.read_csv('PlayerAnalysis_Role_1.csv')

            Goleiro_Charts_1 = Goleiro_Charts[
            ((Goleiro_Charts['Atleta'] == jogador_1) & (Goleiro_Charts['Equipe'] == equipe_1)) |
            ((Goleiro_Charts['Atleta'] == jogador_2) & (Goleiro_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Goleiro_Charts_1 = Goleiro_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Goleiro_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics = Goleiro_Charts_1.iloc[:, np.r_[0, 48:55]].reset_index(drop=True)
            metrics.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

######################################################################################################################################
######################################################################################################################################

        elif (posição_1 == posição_2 == ("Lateral")):
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Lateral Equilibrado</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_5.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 81:90]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 90:99]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

######################################################################################################################################
######################################################################################################################################

        elif (posição_1 == posição_2 == ("Zagueiro")):
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Zagueiro Equilibrado</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_8.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 66:73]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 73:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################
######################################################################################################################################

        elif (posição_1 == posição_2 == ("Primeiro Volante")):
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Primeiro Volante Equilibrado</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_11.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 60:66]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 66:71]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

######################################################################################################################################
######################################################################################################################################

        elif (posição_1 == posição_2 == ("Segundo Volante")):
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Segundo Volante Equilibrado</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_14.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 66:72]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 72:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################
######################################################################################################################################

        elif (posição_1 == posição_2 == ("Meia")):
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Meia Organizador</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_15.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 57:67]].reset_index(drop=True)
            #metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 72:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)
            
######################################################################################################################################

            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Meia Atacante</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_16.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 78:87]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 87:95]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################
######################################################################################################################################

        elif (posição_1 == posição_2 == ("Extremo")):
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Extremo Organizador</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_17.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 66:73]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 73:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################

            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Extremo Tático</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_18.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 48:55]].reset_index(drop=True)
            #metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 72:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

######################################################################################################################################

            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Extremo Agudo</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_19.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 66:73]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 73:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################
######################################################################################################################################

        elif (posição_1 == posição_2 == ("Atacante")):

            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Atacante Referência</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_20.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 57:67]].reset_index(drop=True)
            #metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 72:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################
            
            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Atacante Móvel</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_21.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 54:63]].reset_index(drop=True)
            #metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 73:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################

            #Plotar Primeiro Gráfico - Radar de Percentis do Jogador na liga:
            st.markdown("<h3 style='text-align: center; color: blue; '>Comparação do Desempenho dos Jogadores em 2024<br><br>Perfil: Segundo Atacante</h3>", unsafe_allow_html=True)
            Lateral_Charts = pd.read_csv('PlayerAnalysis_Role_22.csv')

            Lateral_Charts_1 = Lateral_Charts[
            ((Lateral_Charts['Atleta'] == jogador_1) & (Lateral_Charts['Equipe'] == equipe_1)) |
            ((Lateral_Charts['Atleta'] == jogador_2) & (Lateral_Charts['Equipe'] == equipe_2))
            ]

            # Reindex to ensure the correct order
            Lateral_Charts_1 = Lateral_Charts_1.set_index('Atleta').loc[[jogador_1, jogador_2]].reset_index()

            # Create a dictionary of columns to rename by removing the '_percentil' suffix
            columns_to_rename = {
                col: col.replace('_Percentil', '') for col in Lateral_Charts_1.columns if '_Percentil' in col
            }            

            #Collecting data to plot
            metrics_1 = Lateral_Charts_1.iloc[:, np.r_[0, 66:73]].reset_index(drop=True)
            metrics_2 = Lateral_Charts_1.iloc[:, np.r_[0, 73:79]].reset_index(drop=True)
            
            #Plotting the first graph
            metrics_1.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_1.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_1['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_1.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_1.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)

            #Plotting the second graph
            metrics_2.rename(columns=columns_to_rename, inplace=True)
            ## parameter names
            params = list(metrics_2.columns[1:])

            ## range values
            ranges = [(0, 100), (0, 100), (0, 100), (0, 100), (0, 100), (0, 100)]
            a_values = []
            b_values = []

            # Check each entry in 'Atleta' column to find match for jogador_1 and jogador_2
            for i, atleta in enumerate(metrics_2['Atleta']):
                if atleta == jogador_1:
                    a_values = metrics_2.iloc[i, 1:].tolist()  # Skip 'Atleta' column
                elif atleta == jogador_2:
                    b_values = metrics_2.iloc[i, 1:].tolist()

            values = [a_values, b_values]

            ## title values
            title = dict(
                title_name=jogador_1,
                title_color = '#B6282F',
                subtitle_name= equipe_1,
                subtitle_color='#B6282F',
                title_name_2=jogador_2,
                title_color_2 = '#344D94',
                subtitle_name_2=equipe_2,
                subtitle_color_2='#344D94',
                title_fontsize=20,
                subtitle_fontsize=18,
            )            

            ## endnote 
            endnote = "Gráfico: @JAmerico1898\nTodos os dados em percentil"

            ## instantiate object
            #radar = Radar()

            radar=Radar(fontfamily='Cursive', range_fontsize=8)
            fig, ax = radar.plot_radar(
                ranges=ranges,
                params=params,
                values=values,
                radar_color=['#B6282F', '#344D94'],
                dpi=600,
                alphas=[.8, .6],
                title=title,
                endnote=endnote,
                compare=True
            )
            st.pyplot(fig)


######################################################################################################################################
######################################################################################################################################

        else:
            
            st.markdown("<h3 style='text-align: center; color: red; '><br><br>A comparação não é possível, pois os jogadores são de posições diferentes.</h3>", unsafe_allow_html=True)
