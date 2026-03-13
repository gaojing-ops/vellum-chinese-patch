# 开发交接文档

## 项目结构

```
Vellum汉化补丁/
├── arialuni_sdf_u2021          # TMP 中文字体 AssetBundle (22MB)
├── winhttp.dll                 # BepInEx 引导文件
├── doorstop_config.ini         # BepInEx 引导配置
├── install_chinese_patch.py    # 一键安装脚本
├── patch_assets.py             # 资源文件二进制补丁脚本
├── README.md                   # 用户说明
├── DEV_NOTES.md                # 本文档
├── .gitignore
└── BepInEx/
    ├── config/
    │   └── AutoTranslatorConfig.ini   # XUnity 配置
    ├── core/                          # BepInEx 核心 DLL
    ├── plugins/
    │   ├── XUnity.AutoTranslator/     # 文本钩子插件
    │   └── XUnity.ResourceRedirector/ # 资源重定向插件
    └── Translation/zh-CN/Text/
        └── _VellumChinese.txt         # 翻译文件 (~800条)
```

## 技术架构

### 两层翻译机制

1. **XUnity.AutoTranslator 文本钩子**（`_VellumChinese.txt`）
   - 拦截 Unity TextMeshPro 的 text setter
   - 实时替换 UI 文本：菜单、按钮、Boss 名称、技能名、战斗指令等
   - 不修改游戏文件，完全运行时替换

2. **二进制资源补丁**（`patch_assets.py`）
   - 直接修改 `resources.assets`（176MB）中的嵌入文本
   - Boss 描述正文、战斗提示详情等 ScriptableObject 内嵌文本
   - XUnity 无法钩取这些文本（不经过标准 TMP text setter）

### 二进制补丁原理

Unity 字符串序列化格式：
```
[4字节 小端 uint32 长度] [N字节 UTF-8 字符串数据] [对齐填充到4字节]
```

补丁方式：
- 在文件中查找英文 UTF-8 字节序列
- 替换为中文 UTF-8 字节 + `\x00` 空字节填充
- **不修改长度前缀！** 修改会导致后续字段偏移错位，游戏黑屏
- 中文字节数必须 ≤ 英文字节数，否则跳过

### 字体方案

- 游戏使用 TMP 1.4.0，字体 AssetBundle 版本 1.1.0（有不匹配警告但可用）
- `arialuni_sdf_u2021` 放在游戏根目录
- 通过 `AutoTranslatorConfig.ini` 配置：
  ```ini
  OverrideFontTextMeshPro=arialuni_sdf_u2021
  FallbackFontTextMeshPro=arialuni_sdf_u2021
  ```

## 截图分析 — 剩余未汉化内容

### 图鉴页面（截图 1）
- ✅ Boss 名称、描述正文、「战斗提示」标题、「独特机制」标题已汉化
- ❌ 战斗提示列表项 `- Don't get overwhelmed with adds!`、`- Dodge damage!`
  - 这些在 `_VellumChinese.txt` 中有翻译，但实际是嵌入在资源中的
  - 需要加入 `patch_assets.py` 的 TRANSLATIONS 字典
- ❌ 底部 `Note: Mechanics may appear differently in other Worlds.`
  - 同上，嵌入在资源中，XUnity 无法钩取

### 独特机制页面（截图 2）
- ❌ `AoE Dodge` 标题及描述段落
- 这些文本在 `vellum_text_extracted.json` 中存在，但部分带有二进制前缀
  无法用简单的 `data.find()` 匹配
- 需要更复杂的偏移定位方式（按已知 offset 直接修补）

### 战斗场景（截图 3）
- ❌ `SOAK on ★Tank to clear a space!` — 含 `<sprite name="sym_bar">` 精灵图标
  - XUnity 看到的文本包含精灵标记，与翻译文件中的纯文本不匹配
  - 解决方案：在翻译文件中添加含精灵标记的完整变体

## 待办事项

### 高优先级
- [ ] 将截图中可见的未翻译文本加入 `patch_assets.py`
  - `Don't get overwhelmed with adds!` 和 `Dodge damage!` 在资源中的变体
  - 各 Boss 的 Unique 页面描述文本
- [ ] 处理含 `<sprite>` 标记的战斗文本匹配

### 中优先级
- [ ] H6（宇宙之冕/奥蕾莉亚）的嵌入文本补丁 — 需要在提取的 JSON 中定位
- [ ] 奇美鲁斯 (Chimaerus) 的嵌入文本补丁
- [ ] 更多战斗场景中的提示文本

### 低优先级
- [ ] 图鉴中的怪物描述（Skeleton Crews、Imps、Wranglers 等小怪）
- [ ] 剧情/背景文本（Lore entries）
- [ ] 道具/技能描述文本

## 配置注意事项

### 会导致游戏卡死的配置（不要开启！）
```ini
TextGetterCompatibilityMode=True    # 导致游戏冻结
ForceMonoModHooks=True              # 导致游戏冻结
IgnoreVirtualTextSetterCallingRules=True  # 导致游戏冻结
```

### 调试用配置（发布时关闭）
```ini
EnableTextPathLogging=False         # 开启会生成大量日志
OutputUntranslatableText=False      # 开启会输出未翻译文本
LogAllLoadedResources=False         # 开启会记录所有加载的资源
EnableDumping=False                 # 开启会导出资源（与 CacheMetadataForAllFiles 冲突）
```

## 相关文件位置（开发环境）

- 游戏目录：`D:\SteamLibrary\steamapps\common\Vellum Study Hall\`
- 补丁源码：`C:\Users\rsb\Desktop\222\Vellum汉化补丁\`
- 提取的文本 JSON：`C:\Users\rsb\Desktop\222\vellum_text_extracted.json`
- 攻略参考：`C:\Users\rsb\Desktop\222\魔兽世界12.0团本前瞻攻略\`
