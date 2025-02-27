import os
import cv2
import random

# 获取当前目录
current_directory = os.path.dirname(os.path.abspath(__file__))

# 支持的视频文件扩展名
video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.flv']

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 检查文件是否是视频文件
    if any(filename.lower().endswith(ext) for ext in video_extensions):
        # 构建完整的文件路径
        filepath = os.path.join(current_directory, filename)
        
        # 打开视频文件
        cap = cv2.VideoCapture(filepath)
        
        # 获取视频的总帧数
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # 随机选择一个帧号
        random_frame_number = random.randint(0, total_frames - 1)
        
        # 设置视频的当前帧位置
        cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)
        
        # 读取随机帧
        ret, frame = cap.read()
        if not ret:
            print("无法读取帧")
            cap.release()
        
        else:
            # 构建输出文件名
            base_name = os.path.basename(filename)
            video_name, _ = os.path.splitext(base_name)
            image_filename = f"{video_name}_frame_{random_frame_number}.jpg"
            output_path = os.path.join(current_directory, image_filename)
            
            # 保存截取的帧为图片文件
            cv2.imencode('.jpg', frame)[1].tofile(output_path)
            print(f"Saved random frame from {filename} as {image_filename}")
        
        # 释放视频对象
        cap.release()

print("Finished processing all video files.")