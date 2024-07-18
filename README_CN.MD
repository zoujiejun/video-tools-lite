# video-tools-lite

## 简介

**video-tools-lite** 是一个轻量级的工具集，旨在简化常见的视频处理任务。如果你在处理视频编辑，这个工具可以通过处理切割、合并和批量重命名等任务来为你节省时间。

- **依赖**：主要依赖 `ffmpeg`，因此需要确保其已安装并且环境变量已配置。

## 功能

- 视频切割
- 视频合并
- 文件批量重命名

## 使用方法

### 配置文件

为了简化操作，所有参数都通过 JSON 文件配置。以下是配置文件的示例：

```json
{
    "ffmpeg_path": "ffmpeg",
    "cutting": {
        "duration": 10,
        "output_path": "./output/"
    },
    "merge": {
        "extname": "mp4",
        "output_path": "./output2/"
    }
}
```

- `ffmpeg_path`：`ffmpeg` 的路径。确保它在你的 PATH 中，或者指定完整的路径。
- `cutting`：视频切割的配置
  - `duration`：每次切割的时长，单位为秒。
  - `output_path`：输出文件的保存目录。
- `merge`：视频合并的配置
  - `extname`：输入文件的扩展名。
  - `output_path`：合并后视频的保存目录。

### 安装

克隆仓库并进入项目目录：

```powershell
git clone https://github.com/zoujiejun/video-tools-lite.git
cd video-tools-lite
```

### 视频切割

要切割视频，运行以下命令：

```powershell
python3 .\video_cutting.py .\config.json .\input\demo.mp4
```

- **参数**：
  - `config.json`：配置文件的路径。
  - `demo.mp4`：输入视频文件的路径。

### 视频合并

要合并视频，执行：

```powershell
python3 .\video_merge.py .\config.json .\output\demo\
```

- **参数**：
  - `config.json`：配置文件的路径。
  - `demo/`：包含要合并的视频文件的目录。

### 文件批量重命名

要重命名目录中的文件，使用：

```powershell
python3 .\batch_rename.py .\output\demo\
```

- **参数**：
  - `demo/`：包含要重命名的文件的目录。

## 许可证

本项目采用 MIT 许可证。
