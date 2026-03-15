# -*- coding: utf-8 -*-
fp = r'D:\Desktop-Projects\汉化\Vellum汉化补丁\BepInEx\Translation\zh-CN\Text\_VellumChinese.txt'
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()

marker = 'Raid Night Study Hall=团本研习厅'
pos = c.find(marker)
if pos == -1:
    print('Marker not found!')
    exit(1)

end = c.find('\n', pos) + 1

new_entries = [
    'Study Hall: Wordcraft=研习厅：文字工艺',
    'Wordcraft=文字工艺',
    'Study hard - learn the basics of beating these Bosses of upcoming non-Vellum Raids!=努力学习——掌握击败即将到来的非Vellum团本Boss的基础！',
    'Check out the Codex for a deeper look at mechanics. Good luck!=查看图鉴深入了解机制。祝好运！',
    'Note: Some of these encounters may appear differently in other Worlds=注意：部分遭遇战在其他世界中可能表现不同',
]

insert = '\r\n'.join(new_entries) + '\r\n'
c = c[:end] + insert + c[end:]

with open(fp, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'Added {len(new_entries)} Wordcraft translations')
