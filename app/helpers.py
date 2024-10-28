import json
import os
import random
from base64 import b64encode
from io import BytesIO
from pathlib import Path
from loguru import logger as log
import time

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
from pydub import AudioSegment
from streamlit.runtime.scriptrunner import RerunData, RerunException
from streamlit.source_util import get_pages
from streamlit_player import st_player

extensions = ["mp3", "wav", "ogg", "flac"]  # we will look for all those file types.


def check_file_availability(url):
    exit_status = os.system(f"wget -o --spider {url}")
    return exit_status == 0


@st.cache_data(show_spinner=False)
def url_is_valid(url):
    if url.startswith("http") is False:
        st.error("URL 应以 http 或 https 开头。")
        return False
    if url.split(".")[-1] not in extensions:
        st.error("扩展名不支持")
        return False
    return True


@st.cache_data(show_spinner=False)
def load_audio_segment(path: str, format: str) -> AudioSegment:
    try:
        return AudioSegment.from_file(path, format=format)
    except Exception as e:
        st.error("音频文件无效")
        log.warning(e)
        st.stop()


@st.cache_data(show_spinner=False)
def plot_audio(_audio_segment: AudioSegment, max_y: float, *args, **kwargs) -> Image.Image:
    samples = _audio_segment.get_array_of_samples()
    arr = np.array(samples)

    fig, ax = plt.subplots(figsize=(10, 2))
    ax.plot(arr, linewidth=0.04)
    ax.set_axis_off()

    # Scale the plot based on max Y value
    ax.set_ylim(bottom=-max_y, top=max_y)

    # Set the background color to transparent
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)

    buf = BytesIO()
    plt.savefig(buf, format="png", dpi=100, bbox_inches="tight")
    buf.seek(0)
    image = Image.open(buf)

    plt.close(fig)
    return image


@st.cache_data(show_spinner=False)
def load_list_of_songs(path="sample_songs.json"):
    if os.environ.get("PREPARE_SAMPLES"):
        return json.load(open(path))
    else:
        st.error(
            "没有可用的示例。"
        )


def get_random_song():
    sample_songs = load_list_of_songs()
    if sample_songs is None:
        return None, None
    name, url = random.choice(list(sample_songs.items()))
    return name, url


def streamlit_player(
    player,
    url,
    height,
    is_active,
    muted,
    start,
    key,
    playback_rate=1,
    events=None,
    play_inline=False,
    light=False,
):
    with player:
        options = {
            "progress_interval": 1000,
            "playing": is_active,  # st.checkbox("Playing", False),
            "muted": muted,
            "light": light,
            "play_inline": play_inline,
            "playback_rate": playback_rate,
            "height": height,
            "config": {"start": start},
            "events": events,
        }
        if url != "":
            events = st_player(url, **options, key=key)
    return events


@st.cache_data(show_spinner=False)
def local_audio(path, mime="audio/mp3"):
    data = b64encode(Path(path).read_bytes()).decode()
    return [{"type": mime, "src": f"data:{mime};base64,{data}"}]


def _standardize_name(name: str) -> str:
    return name.lower().replace("_", " ").strip()


@st.cache_data(show_spinner=False)
def switch_page(page_name: str):
    st.session_state.executed = False
    st.session_state.page = page_name

    page_name = _standardize_name(page_name)

    pages = get_pages("header.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if _standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [_standardize_name(config["page_name"]) for config in pages.values()]
    raise ValueError(f"找不到页面 {page_name}。必须是 {page_names} 中的一个。")


def st_local_audio(pathname, key):
    st_player(
        local_audio(pathname),
        **{
            "progress_interval": 1000,
            "playing": False,
            "muted": False,
            "light": False,
            "play_inline": True,
            "playback_rate": 1,
            "height": 40,
            "config": {"start": 0, "forceAudio": True, "forceHLS": True, "forceSafariHLS": True},
        },
        key=key,
    )


def file_size_is_valid(file_size):
    if file_size is not None:
        file_size = int(file_size)
        max_size_mb = int(os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"])
        if max_size_mb and file_size > max_size_mb * 1024 * 1024:
            st.error(
                f"文件太大。 最大文件大小: {max_size_mb}MB."
            )
            return False
    return True


def _get_files_to_not_delete():
    not_delete = []
    if os.environ.get("PREPARE_SAMPLES"):
        for filename in ["sample_songs.json", "separate_songs.json"]:
            try:
                with open(filename) as f:
                    not_delete += list(json.load(f).keys())
            except Exception as e:
                log.warning(e)
    return not_delete


def _remove_file_older_than(file_path: str, max_age_limit: float):
    # If the file is older than the age limit, delete it
    if os.path.getmtime(file_path) < max_age_limit:
        try:
            log.info(f"Deleting {file_path}")
            os.remove(file_path)
        # except OSError as e:
        #     log.warning(f"Error: Could not delete {file_path}. Reason: {e.strerror}")


def delete_old_files(directory: str, age_limit_seconds: int):
    files_to_not_delete = _get_files_to_not_delete()
    age_limit = time.time() - age_limit_seconds

    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(directory):
        if dirpath.split("/")[-1] not in files_to_not_delete:
            for filename in filenames:
                if filename.split(".")[0] not in files_to_not_delete:
                    file_path = os.path.join(dirpath, filename)
                    _remove_file_older_than(file_path, age_limit)
