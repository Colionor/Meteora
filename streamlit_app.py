import streamlit as st
import os
from PIL import Image
# import pillow_avif

st.set_page_config(
    page_title="Meteor-a", 
    page_icon="favicon_black_x128.ico", 
    initial_sidebar_state="expanded", 
    menu_items={
        'About': '「个人消费文明史」简单实例'
    }
    )

# 读取配置文件
def read_config_txt(config_path):
    config = {}
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    name, folder = parts
                    config[name] = folder
    except FileNotFoundError:
        print(f"未找到配置文件: {config_path}")
    return config
# 主函数
def main():
    st.title("「万物速朽」避难所")

    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 配置文件和图像文件夹路径
    img_folder = os.path.join(current_dir, 'Img')

    # 读取配置文件
    config = read_config_txt('config.txt')

    # 搜索框
    search_term = st.sidebar.text_input("搜索项目")
    if search_term:
        filtered_names = [name for name in config.keys() if search_term.lower() in name.lower()]
    else:
        filtered_names = list(config.keys())

    # 左侧下拉选择框
    selected_name = st.sidebar.selectbox("选择项目", filtered_names)

    # 获取对应的文件夹
    if selected_name in config:
        folder_name = config[selected_name]
        folder_path = os.path.join(img_folder, folder_name)

        if os.path.exists(folder_path):
            # 获取所有AVIF文件
            avif_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.avif')]
            avif_files.sort()

            # 右侧展示图像
            for file in avif_files:
                if os.path.exists(file):
                    try:
                        # 直接使用 Pillow 打开图像进行测试
                        img = Image.open(file)
                        st.image(img, use_container_width=True)
                    except Exception as e:
                        st.error(f"无法显示图像 {file}: {e}")
                else:
                    st.error(f"文件 {file} 不存在")
        else:
            st.error(f"未找到对应的文件夹: {folder_path}")
    else:
        st.error("未找到对应的配置信息")


if __name__ == "__main__":
    main()