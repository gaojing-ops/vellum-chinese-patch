# Vellum: Raid Night Study Hall 汉化补丁

非官方中文汉化补丁，让你和朋友更方便地学习团本机制。

## 安装方法

### 方法一：自动安装（推荐）

> 需要 Python 3.8+（[下载 Python](https://www.python.org/downloads/)）

1. 确保已从 Steam 安装 **Vellum: Raid Night Study Hall**
2. 双击运行 `install_chinese_patch.py`
3. 选择 **1. 安装汉化补丁**
4. 脚本会自动完成以下操作：
   - 复制 BepInEx 框架和翻译文件
   - 复制中文字体文件
   - 修补游戏资源文件中的嵌入文本
5. 启动游戏即可

### 方法二：手动安装

1. 找到游戏安装目录（Steam > 右键游戏 > 管理 > 浏览本地文件）
2. 将以下文件/文件夹复制到**游戏根目录**，覆盖同名文件：
   - `BepInEx/` 文件夹（整个复制）
   - `winhttp.dll`
   - `doorstop_config.ini`
   - `arialuni_sdf_u2021`（中文字体文件）
3. 运行 `patch_assets.py` 修补嵌入文本（选择 **1. 应用中文补丁**）
4. 启动游戏即可

## 卸载方法

- **自动卸载**：运行 `install_chinese_patch.py`，选择 **2. 卸载汉化补丁**
- **手动卸载**：
  1. 用 `resources.assets.bak` 还原 `resources.assets`（位于 `Vellum Study Hall_Data/` 下）
  2. 删除游戏目录下的 `BepInEx/`、`winhttp.dll`、`doorstop_config.ini`、`arialuni_sdf_u2021`

## 汉化范围

| 类别 | 状态 |
|------|------|
| 主菜单 / 设置界面 / 按钮 | ✅ 已汉化 |
| Boss 名称 | ✅ 已汉化 |
| 技能名称 | ✅ 已汉化 |
| 图鉴分类标题 | ✅ 已汉化 |
| 战斗指令（分摊/躲避/集合等） | ✅ 已汉化 |
| Boss 描述正文 | ✅ 已汉化（资源补丁） |
| Boss 战斗提示详情 | ✅ 大部分已汉化 |
| 「独特机制」页面描述 | ⚠ 部分未汉化 |
| 含精灵图标的战斗文本 | ⚠ 部分未汉化 |

## 已知问题

- 图鉴「独特机制」（Unique）页面的部分文本因嵌入方式特殊，暂未翻译
- 含精灵图标（如坦克图标 ★）的战斗提示文本难以通过文本钩子匹配
- 战斗提示列表中的 `- Don't get overwhelmed with adds!` 等条目属于嵌入资源文本
- 游戏更新后需重新运行 `patch_assets.py`（BepInEx 部分不受影响）

## 自定义翻译

翻译文件位于 `BepInEx/Translation/zh-CN/Text/_VellumChinese.txt`

格式为 `英文原文=中文翻译`，每行一条，`#` 开头为注释。可用记事本编辑。

## 翻译术语来源

- Boss 及技能译名参考：WoW 12.0 团本开荒速查手册
- 游戏原创 Boss（坎比纳隆、大母鸡比格、阿拉希奥姆）采用音译 + 意译

## 技术信息

- 基于 [BepInEx](https://github.com/BepInEx/BepInEx) 5.4.23.2 + [XUnity.AutoTranslator](https://github.com/bbepis/XUnity.AutoTranslator) 5.3.0
- UI 文本通过 XUnity 文本钩子实时替换（不修改游戏文件）
- Boss 描述等嵌入文本通过 `patch_assets.py` 直接修补 `resources.assets`（会自动创建 `.bak` 备份）

## 免责声明

本项目为非官方的社区汉化补丁，仅供学习和个人使用。

- 本补丁与 Vellum 游戏开发者无关，不代表官方立场
- 所有游戏内容的版权归原开发者所有
- 本项目不包含任何游戏原始资产，仅包含翻译文本和开源工具
- BepInEx 和 XUnity.AutoTranslator 遵循各自的开源许可证

**如有侵权，请联系我删除。**

## 致谢

- [BepInEx](https://github.com/BepInEx/BepInEx) 团队
- [XUnity.AutoTranslator](https://github.com/bbepis/XUnity.AutoTranslator) 作者 bbepis
- WoW 12.0 团本攻略社区
