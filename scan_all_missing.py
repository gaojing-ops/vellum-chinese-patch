# -*- coding: utf-8 -*-
"""Comprehensive scan for missing combat/UI texts in resources.assets."""
import struct, re, sys

sys.path.insert(0, r'D:\Desktop-Projects\汉化\Vellum汉化补丁')

# Load ALL known translations
known = set()
with open(r'D:\Desktop-Projects\汉化\Vellum汉化补丁\BepInEx\Translation\zh-CN\Text\_VellumChinese.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('//') and '=' in line:
            known.add(line.split('=', 1)[0])

from patch_assets import TRANSLATIONS
known.update(TRANSLATIONS.keys())
from translations_extended import TRANSLATIONS_EXTENDED
known.update(TRANSLATIONS_EXTENDED.keys())
for i in range(1, 7):
    mod = __import__(f'translations_batch{i}')
    d = getattr(mod, f'TRANSLATIONS_BATCH{i}')
    known.update(d.keys())
print(f'Total known: {len(known)}')

data = open(r'A:\SteamLibrary\steamapps\common\Vellum Study Hall\Vellum Study Hall_Data\resources.assets.bak', 'rb').read()

combat_words = [
    'Kill', 'Soak', 'SOAK', 'Dodge', 'DODGE', 'Interrupt', 'lust', 'Lust',
    'Invulnerable', 'Spread', 'Stack', 'STACK', 'Phase', 'Intermission',
    'incoming', 'Warning', 'Avoid', 'careful', 'Stand', 'Hide',
    'Break', 'Move to', 'Get to', 'Run to', "Don't", "DON'T",
    'Watch out', 'Killable', 'transforms', 'before it', 'Shade',
    'Manifestation', 'Note:', 'Mechanics', 'Study',
    'during', 'During', 'lava', 'Lava',
]

skip_words = ['.dll', '.cs', 'Unity', 'System.', 'Debug', 'MeshFX', 'Aura_',
              'Prime_', '_Kill', 'Apply', 'GameObject', 'Transform', 'Animation',
              'Material', 'Shader', 'Texture', 'prefab', 'Component', 'Manager',
              'Controller', 'Handler', 'Renderer', 'Buffer', 'Config']

missing = set()
offset = 0
while offset < len(data) - 8:
    slen = struct.unpack('<I', data[offset:offset+4])[0]
    if 12 <= slen <= 500:
        s = offset + 4
        e = s + slen
        if e <= len(data):
            try:
                txt = data[s:e].decode('utf-8')
                if txt not in known and any(w in txt for w in combat_words):
                    clean = re.sub(r'<[^>]+>', '', txt)
                    if clean.isprintable() and len(clean) > 10:
                        if not any(x in txt for x in skip_words):
                            missing.add(txt)
            except:
                pass
    offset += 4

print(f'\nMissing combat-related: {len(missing)}')
for m in sorted(missing, key=len):
    short = m[:140].replace('\n', '\\n').replace('\r', '')
    print(f'  {short}')
