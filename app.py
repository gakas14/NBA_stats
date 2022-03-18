from data_cleaning import get_current_season
import streamlit as st
from data_cleaning import get_player_id
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




player_list = players.get_players()
player_list = pd.DataFrame(player_list)
player_list.to_csv('player_list.csv', index=False)


p_id, player_name = get_basic_stats()


#player_info = commonplayerinfo.CommonPlayerInfo(player_id=p_id)
#df_player_info = player_info.get_data_frames()
#df_player_info.to_csv('df_player_info.csv')

#a_player_gamelog = playergamelog.PlayerGameLog(player_id=p_id)
#df_player_gamelog = a_player_gamelog.get_data_frames()
#player_gamelog = df_player_gamelog[0]
#player_gamelog.to_csv('player_gamelog.csv')

#p = playerprofilev2.PlayerProfileV2(player_id=p_id)
#df_p = p.get_data_frames()
#df_p.to_csv('df_p.csv')

#p_d = playerdashboardbyshootingsplits.PlayerDashboardByShootingSplits(player_id=p_id)
#df_shoot = p_d.get_data_frames()
#df_shoot.to_csv('df_shoot.csv')

bar_chart(p_id, player_name)
#pie_chart(p_id, player_name)

#if st.button('Get more Stats'):
get_more_stats(p_id, player_name)


#if __name__ == '__name__':
    #get_basic_stats(sys.argv[1])






