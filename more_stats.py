from data_cleaning import *
import streamlit as st
import numpy as np
import pandas as pd


def get_more_stats(p_id, player_name):
    #regular_season_stats, regular_season_tot_stats, playoff_stats, playoff_stats_tot, allstar_stats, allstar_stats_tot = get_career_stats(p_id)
    season = ['Regular Season', 'PlayOff', 'All-Start']

    selection = st.selectbox(label="Select the season", options=season)
    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    # select the type of season
    if selection == 'Regular Season':
        regular_details = get_career_stats(p_id)[0]
        #st.dataframe(regular_details)

        # get the stats in details and total
        reg_tot = get_career_stats(p_id)[1]
        # format the percentage columns
        reg_tot = formatage_pct(reg_tot)
        # reset the index columns
        #reg_tot = reg_tot.drop('Unnamed:0', axis=1)
        reg_tot = reg_tot.reset_index(drop=True)
        # replace na/nan by '-'
        reg_tot = reg_tot.replace(pd.NA, '-')

        #reg_tot.iloc[0:n]['PLAYER_AGE']
        #reg_tot.iloc[0:n]['PLAYER_AGE'] = reg_tot.iloc[0:n]['PLAYER_AGE'].astype(int)

        st.dataframe(reg_tot)
        #st.write(reg_tot['PLAYER_AGE'].dtype)
        #st.write(reg_tot['SEASON_ID'].dtype)
        # st.dataframe(regular_season_stats.style.highlight_max(axis=0, color='red'))

    elif selection == 'PlayOff':
        playoff_stats = get_career_stats(p_id)[2]
        #playoff_stats = formatage_pct(playoff_stats)

        # get the stats in details and total
        playoff_stats_tot = get_career_stats(p_id)[3]
        # format the percentage columns
        playoff_stats_tot = formatage_pct(playoff_stats_tot)
        # reset the index columns
        playoff_stats_tot = playoff_stats_tot.reset_index(drop=True)
        # replace na/nan by '-'
        playoff_stats_tot = playoff_stats_tot.replace(pd.NA, '-')
        st.dataframe(playoff_stats_tot)
    else:
        allstar_stats = get_career_stats(p_id)[4]
        #allstar_stats = formatage_pct(allstar_stats)

        # get the stats in details and total
        allstar_stats_tot = get_career_stats(p_id)[5]
        # format the percentage columns
        allstar_stats_tot = formatage_pct(allstar_stats_tot)
        # reset the index columns
        allstar_stats_tot = allstar_stats_tot.reset_index(drop=True)
        # replace na/nan by '-'
        allstar_stats_tot = allstar_stats_tot.replace(pd.NA, '-')
        st.dataframe(allstar_stats_tot)

