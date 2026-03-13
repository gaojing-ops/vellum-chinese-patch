"""
Vellum: Raid Night Study Hall 汉化补丁安装器
===========================================
使用方法：
1. 确保你已经从 Steam 安装了 Vellum: Raid Night Study Hall
2. 双击运行本脚本（或命令行运行 python install_chinese_patch.py）
3. 脚本会自动查找游戏安装位置并安装汉化补丁
4. 启动游戏即可看到中文界面

注意：汉化补丁不会修改任何原始游戏文件，完全通过 BepInEx 插件系统实现。
卸载方法：删除游戏目录下的 BepInEx 文件夹、winhttp.dll 和 doorstop_config.ini 即可。
"""

import os
import sys
import zipfile
import shutil

def find_game():
    """Try to find the game installation directory"""
    common_paths = [
        r"A:\SteamLibrary\steamapps\common\Vellum Study Hall",
        r"D:\SteamLibrary\steamapps\common\Vellum Study Hall",
        r"C:\Program Files (x86)\Steam\steamapps\common\Vellum Study Hall",
        r"C:\Program Files\Steam\steamapps\common\Vellum Study Hall",
        r"E:\SteamLibrary\steamapps\common\Vellum Study Hall",
        r"F:\SteamLibrary\steamapps\common\Vellum Study Hall",
    ]
    
    for path in common_paths:
        if os.path.exists(os.path.join(path, "Vellum Study Hall.exe")):
            return path
    
    return None

def install_patch(game_dir):
    """Install the Chinese patch to the game directory"""
    patch_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"游戏目录: {game_dir}")
    print(f"补丁目录: {patch_dir}")
    
    # Step 1: Copy BepInEx files
    bep_src = os.path.join(patch_dir, "BepInEx")
    bep_dst = os.path.join(game_dir, "BepInEx")
    
    if os.path.exists(bep_dst):
        print("\n⚠ 检测到已安装 BepInEx，将更新汉化文件...")
    else:
        print("\n📦 安装 BepInEx 框架...")
        
    # Copy BepInEx folder
    if os.path.exists(bep_src):
        shutil.copytree(bep_src, bep_dst, dirs_exist_ok=True)
        print("  ✅ BepInEx 框架已安装")
    
    # Step 2: Copy doorstop files and font
    for fname in ["winhttp.dll", "doorstop_config.ini", "arialuni_sdf_u2021"]:
        src = os.path.join(patch_dir, fname)
        dst = os.path.join(game_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  ✅ {fname} 已复制")
    
    # Step 3: Apply binary asset patch for embedded text
    patch_script = os.path.join(patch_dir, "patch_assets.py")
    if os.path.exists(patch_script):
        print("\n📝 应用资源文件文本补丁...")
        try:
            sys.path.insert(0, patch_dir)
            from patch_assets import patch_assets as do_patch
            do_patch(game_dir)
        except Exception as e:
            print(f"  ⚠ 资源补丁出错: {e}")
            print("  游戏仍可运行，但部分描述文本将保持英文")

    # Step 4: Verify installation
    print("\n🔍 验证安装...")
    checks = {
        "BepInEx 目录": os.path.exists(os.path.join(game_dir, "BepInEx")),
        "winhttp.dll": os.path.exists(os.path.join(game_dir, "winhttp.dll")),
        "doorstop_config.ini": os.path.exists(os.path.join(game_dir, "doorstop_config.ini")),
        "XUnity.AutoTranslator": os.path.exists(os.path.join(game_dir, "BepInEx", "plugins", "XUnity.AutoTranslator")),
        "汉化文件": os.path.exists(os.path.join(game_dir, "BepInEx", "Translation", "zh-CN", "Text", "_VellumChinese.txt")),
        "配置文件": os.path.exists(os.path.join(game_dir, "BepInEx", "config", "AutoTranslatorConfig.ini")),
    }
    
    all_ok = True
    for name, ok in checks.items():
        status = "✅" if ok else "❌"
        print(f"  {status} {name}")
        if not ok:
            all_ok = False
    
    if all_ok:
        print("\n🎉 汉化补丁安装成功！")
        print("   现在可以启动游戏了，文本将自动显示为中文。")
        print("\n💡 提示：")
        print("   - 首次启动可能需要等几秒钟加载插件")
        print("   - 游戏中按 ALT+0 可打开翻译设置面板")
        print("   - 部分文本可能仍为英文（需要后续补充翻译）")
    else:
        print("\n⚠ 部分文件安装失败，请检查上方标记为 ❌ 的项目")
    
    return all_ok

def uninstall_patch(game_dir):
    """Remove the Chinese patch"""
    print(f"正在卸载汉化补丁...")

    # Restore resources.assets backup if exists
    assets_bak = os.path.join(game_dir, "Vellum Study Hall_Data", "resources.assets.bak")
    assets_file = os.path.join(game_dir, "Vellum Study Hall_Data", "resources.assets")
    if os.path.exists(assets_bak):
        shutil.copy2(assets_bak, assets_file)
        os.remove(assets_bak)
        print("  ✅ 已还原 resources.assets")

    for item in ["BepInEx", "winhttp.dll", "doorstop_config.ini", "arialuni_sdf_u2021"]:
        path = os.path.join(game_dir, item)
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            print(f"  ✅ 已删除 {item}")

    print("\n🎉 汉化补丁已完全卸载！游戏已恢复原始状态。")

def main():
    print("=" * 50)
    print("  Vellum: Raid Night Study Hall")
    print("  汉化补丁安装器 v1.0")
    print("  基于 BepInEx + XUnity.AutoTranslator")
    print("=" * 50)
    
    # Find game
    game_dir = find_game()
    
    if not game_dir:
        print("\n❌ 未找到游戏安装目录！")
        print("请手动输入游戏安装路径")
        print("（包含 'Vellum Study Hall.exe' 的文件夹）")
        game_dir = input("\n路径: ").strip().strip('"')
        
        if not os.path.exists(os.path.join(game_dir, "Vellum Study Hall.exe")):
            print("❌ 该路径下未找到 Vellum Study Hall.exe")
            input("按回车退出...")
            return
    
    print(f"\n✅ 找到游戏: {game_dir}")
    
    # Menu
    print("\n请选择操作：")
    print("  1. 安装汉化补丁")
    print("  2. 卸载汉化补丁")
    print("  3. 退出")
    
    choice = input("\n选择 (1/2/3): ").strip()
    
    if choice == "1":
        install_patch(game_dir)
    elif choice == "2":
        uninstall_patch(game_dir)
    else:
        print("退出")
    
    input("\n按回车退出...")

if __name__ == "__main__":
    main()
