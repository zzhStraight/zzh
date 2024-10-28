import streamlit as st

from header import header
from footer import footer
from helpers import delete_old_files


def body():
    with st.columns([2, 3, 2])[1]:
        st.markdown(
            """
        <center>

        ## 欢迎使用 Moseca，您的个人网页应用，旨在重塑您的音乐体验。
        <font size="3"> 无论您是想要重新混音自己最喜欢的歌曲的音乐人，还是热衷于卡拉 OK 的爱好者，或者是想更深入了解自己喜欢的曲目的音乐爱好者，Moseca 都适合您。 </font>

        <br>

        ### 高质量的音轨分离

        <center><img title="高质量的音轨分离" src="https://i.imgur.com/l7H8YWL.png" width="60%" ></img></center>

        <br>

        <font size="3"> 可以分离多达 6 个音轨，包括 🗣人声、🥁鼓、🔉贝斯、🎸吉他、🎹钢琴（测试版）和 🎶 其他音轨。 </font>

        <br>

        ### 先进的 AI 算法

        <center><img title="先进的 AI 算法" src="https://i.imgur.com/I8Pvdav.png" width="60%" ></img></center>

        <br>

        <font size="3"> Moseca 利用最先进的 AI 技术，准确提取您原始歌曲中的人声或音乐。 </font>

        <br>

        ### 卡拉 OK 乐趣

        <center><img title="卡拉 OK 乐趣" src="https://i.imgur.com/nsn3JGV.png" width="60%" ></img></center>

        <br>

        <font size="3"> 以全新的方式与您最喜欢的曲目互动！ </font>

        <font size="3"> Moseca 提供身临其境的在线卡拉 OK 体验，允许您搜索 YouTube 上的任何歌曲并在线去除人声。 </font>

        <font size="3"> 享受高质量伴奏，尽情在家唱歌。</font>

        <br>

        ### 轻松部署

        <font size="3"> 使用 Moseca，您可以在
        <a href="https://huggingface.co/spaces/fabiogra/moseca?duplicate=true">
        <img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue"
        alt="Hugging Face Spaces"></a> 部署个人 Moseca 应用，或者通过 </font>
        [![Docker Call](https://img.shields.io/badge/-Docker%20Image-blue?logo=docker&labelColor=white)](https://huggingface.co/spaces/fabiogra/moseca/discussions?docker=true)
        <font size="3"> 一键在本地部署。

        使用现成的 [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ODoK3VXajprNbskqy7G8P1h-Zom92TMA?usp=sharing) 提高音乐分离的速度，支持 GPU。</font>

        <br>

        ### 开源且免费

        <font size="3"> Moseca 是 lalal.ai、splitter.ai 或 media.io 人声去除工具的免费开源替代方案。

        您可以自由修改、分发和使用它。我相信社区协作的力量，鼓励用户为我们的源代码贡献力量，让 Moseca 在每次更新中变得更好。
        </font>

        <br>

        ### 支持

        - <font size="3"> 通过为 GitHub 仓库点赞来支持我们</font> [![GitHub stars](https://img.shields.io/github/stars/fabiogra/moseca.svg?style=social&label=Star)](https://github.com/fabiogra/moseca)。
        - <font size="3"> 如果您发现问题或有改进 Moseca 的建议，可以提交一个</font> [![GitHub issues](https://img.shields.io/github/issues/fabiogra/moseca.svg)](https://github.com/fabiogra/moseca/issues/new)
        - <font size="3"> 喜欢 Moseca 吗？</font> [![Buymeacoffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/fabiogra)

        ------

        ## 常见问题

        ### 什么是 Moseca？

        <font size="3"> Moseca 是一个开源的网页应用，利用先进的 AI 技术分离音乐轨道中的人声和乐器。它还提供在线卡拉 OK 体验，允许您搜索 YouTube 上的任何歌曲并去除人声。</font>

        ### 是否有任何限制？
        <font size="3">是的，在这个环境中，处理长度和 CPU 使用方面存在一些限制，以确保所有用户的流畅体验。
        <b>如果您希望去除这些限制，可以在个人环境中部署 Moseca 应用，例如在 <a href="https://huggingface.co/spaces/fabiogra/moseca?duplicate=true"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue" alt="Hugging Face Spaces"></a> 或通过 [![Docker Call](https://img.shields.io/badge/-Docker%20Image-blue?logo=docker&labelColor=white)](https://huggingface.co/spaces/fabiogra/moseca/discussions?docker=true)。

        您还可以通过 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ODoK3VXajprNbskqy7G8P1h-Zom92TMA?usp=sharing) 以 GPU 支持加速音乐分离过程。</b>
        </font>


        ### Moseca 如何工作？
        <font size="3"> Moseca 利用 Facebook 的混合谱图和波形源分离模型（[DEMUCS](https://github.com/facebookresearch/demucs)）。为了快速去除卡拉 OK 人声，Moseca 使用由 [tsurumeso](https://github.com/tsurumeso/vocal-remover) 开发的 AI 人声去除器。
        </font>
        ### 如何使用 Moseca？
        <font size="3">1. 上传您的文件：选择您的歌曲并将其上传到 Moseca。它支持多种音乐格式，方便您使用。</font>

        <font size="3">2. 选择分离模式：根据您的需求选择仅人声、4 音轨或 6 音轨分离。</font>

        <font size="3">3. 让 AI 展现魔力：Moseca 的先进 AI 将在几分钟内完成音轨分离，为您提供高质量的分离音频轨道。</font>

        <font size="3">4. 下载并享受：预览并下载您分离的音轨。 </font>


        ------
        ## 免责声明

        <font size="3">Moseca 旨在从受版权保护的音乐中分离人声和乐器，以便进行法律允许的用途，如学习、练习、研究或其他不涉及商业活动的用途，这些用途符合合理使用或版权例外的范围。作为用户，您有责任确保您使用分离的音频轨道符合您所在司法管辖区的法律要求。
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
