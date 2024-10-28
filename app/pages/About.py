import streamlit as st

from header import header
from footer import footer
from helpers import delete_old_files


def body():
    with st.columns([2, 3, 2])[1]:
        st.markdown(
            """
        <center>

        ## 欢迎使用 zzsepa，您的个人网页应用，旨在重塑您的音乐体验。
        <font size="3"> 无论您是想要重新混音自己最喜欢的歌曲的音乐人，还是热衷于卡拉 OK 的爱好者，或者是想更深入了解自己喜欢的曲目的音乐爱好者，zzsepa 都适合您。 </font>

        <br>

        ### 高质量的音轨分离

        <center><img title="高质量的音轨分离" src="https://i.imgur.com/l7H8YWL.png" width="60%" ></img></center>

        <br>

        <font size="3"> 可以分离多达 6 个音轨，包括 🗣人声、🥁鼓、🔉贝斯、🎸吉他、🎹钢琴（测试版）和 🎶 其他音轨。 </font>

        <br>

        ### 先进的 AI 算法

        <center><img title="先进的 AI 算法" src="https://i.imgur.com/I8Pvdav.png" width="60%" ></img></center>

        <br>

        <font size="3"> zzsepa 利用最先进的 AI 技术，准确提取您原始歌曲中的人声或音乐。 </font>

        <br>

        ### 卡拉 OK 乐趣

        <center><img title="卡拉 OK 乐趣" src="https://i.imgur.com/nsn3JGV.png" width="60%" ></img></center>

        <br>

        <font size="3"> 以全新的方式与您最喜欢的曲目互动！ </font>

        <font size="3"> zzsepa 提供身临其境的在线卡拉 OK 体验，允许您搜索 YouTube 上的任何歌曲并在线去除人声。 </font>

        <font size="3"> 享受高质量伴奏，尽情在家唱歌。</font>

        <br>

        ------
        ## 免责声明

        <font size="3">zzsepa 旨在从受版权保护的音乐中分离人声和乐器，以便进行法律允许的用途，如学习、练习、研究或其他不涉及商业活动的用途，这些用途符合合理使用或版权例外的范围。作为用户，您有责任确保您使用分离的音频轨道符合您所在司法管辖区的法律要求。
        </font>

        </center>
        """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    header(logo_and_title=False)
    body()
    footer()
    delete_old_files("/tmp", 60 * 30)
