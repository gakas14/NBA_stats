from data_cleaning import get_current_season
import streamlit as st
from data_cleaning import get_palyer_id
from data_cleaning import formatage_data_set
from data_cleaning import get_career_stats
from basic_stats import *
from more_stats import *
# Import sys dependency to extract command line arguments
import sys


st.set_page_config('wide')
# Create sidebar
st.sidebar.markdown("<div> <img src='https://content.sportslogos.net/news/2021/07/nba-75th-anniversary-2021-2022-wilt-kareem-jordan-kobe-sportslogosnet-logo-1170x807.png' width=300/>  <h1 style='display:inline-block'> NBA Players Stats Dash </h1> </div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to search for a particular NBA player.")
st.sidebar.markdown("You GET <ol><li>You can search a particular player.</li> <li>You can see the current season stats of the player.</li> "
                    "<li>A chart of the players shooting Area, different area shots attempted and made.</li>"
                    "<li>A chart of th player average PTS,AST and REB over years.</li>"
                    "<li>The player total numbers in the Regular Season, PlayOff and All-Star game.</li>"
                    "</ol>", unsafe_allow_html=True)


p_id, player_name = get_basic_stats()

bar_chart(p_id, player_name)

#pie_chart(p_id, player_name)

#if st.button('Get more Stats'):
get_more_stats(p_id, player_name)


#if __name__ == '__name__':
    #get_basic_stats(sys.argv[1])






