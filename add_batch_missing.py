# -*- coding: utf-8 -*-
"""Batch add all missing game-visible translations."""

fp = r'D:\Desktop-Projects\汉化\Vellum汉化补丁\BepInEx\Translation\zh-CN\Text\_VellumChinese.txt'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# All missing game-visible texts from the scan (excluding code/shader/debug)
new_entries = [
    # === 战斗提示 (富文本标签版) ===
    'During <pos>lust</pos> two of the three are <neg>Invulnerable</neg>!=<pos>色欲</pos>阶段三个中有两个<neg>无敌</neg>！',
    'Stacking <neg>sensory overload</neg>.=叠加<neg>感官过载</neg>。',
    'Stacking <neg>vision impairment</neg>.=叠加<neg>视觉损伤</neg>。',
    'Focus on safety during <b>Golgor\'s</b> grand attacks!=<b>高尔戈</b>大招期间注意安全！',
    'Look for <pos>Dispelling Gusts</pos> during <b>Death Winds</b>.=在<b>死亡之风</b>中寻找<pos>驱散之风</pos>。',
    '<b>Note:</b> Mechanics may appear differently in other Worlds.=<b>注意：</b>不同世界中机制可能有所不同。',
    'Absorb beams that match your shield. Dodge the others.=吸收与你盾牌匹配的光束。躲开其他的。',
    # === Boss机制/页面效果 ===
    '$Scribes$ damaged by <b>Verse</b> drop a <neg>lava pool</neg>.=$Scribes$被<b>Verse</b>伤害时掉落<neg>熔岩池</neg>。',
    '<neg>Lava</neg> starts to pool throughout the <b>Tome</b>, <neg>burning</neg> everyone it touches.=<neg>熔岩</neg>开始在<b>卷册</b>中蔓延，<neg>灼烧</neg>接触者。',
    '<b>Color-infused Lanterns</b> only provide <neg>partial immunity</neg> during <b>Myriad\'s Ritual</b>.=<b>浸色灯笼</b>在<b>Myriad仪式</b>期间只提供<neg>部分免疫</neg>。',
    'Don\'t let the decaying <b>Chromatic Orbs</b> explode at the same time.=别让衰变的<b>色彩宝珠</b>同时爆炸。',
    'The $boss$ drops bananas. If $Scribes$ touch them, <neg>bananas</neg> heal ($-|10|%|HP$) the $boss$. <i>Don\'t touch bananas.</i>=$boss$扔香蕉。$Scribes$碰到会<neg>治疗</neg>($-|10|%|HP$)$boss$。<i>别碰香蕉。</i>',
    'Soak Mana Orbs while flying around.=飞行时分摊法力宝珠。',
    'Dodge Verse\'s attacks to gain bonus currency.=躲避Verse的攻击获取额外货币。',
    'Next incoming damage increased by $-|+|50|%$.=下次受到伤害增加$-|+|50|%$。',
    'Slowed $-|5|%$ and receives more damage $-|5|%$. Stacks up to <b>5</b> times.=减速$-|5|%$并受到更多伤害$-|5|%$。最多叠<b>5</b>层。',
    # === 页面效果/技能 ===
    'During $keyword-hare$, $Scribes$ leave behind a <pos>Speed Boost</pos> path.=$keyword-hare$期间$Scribes$留下<pos>加速</pos>路径。',
    'During $keyword-hare$, gain $+|+|25|%|DMG$ but also $-|+|15|%| Damage Taken$.=$keyword-hare$期间$+|+|25|%|DMG$但$-|+|15|%| Damage Taken$。',
    '$Scribes$ may <pos>triple jump</pos> during <pos>Winter</pos> and <pos>Summer</pos>.=$Scribes$在<pos>冬季</pos>和<pos>夏季</pos>可<pos>三段跳</pos>。',
    '<b>Temporary</b> $mana-neutral$ generated during <pos>Spring</pos> and <pos>Summer</pos> is converted to Signature Color Mana.=<pos>春季</pos>和<pos>夏季</pos>生成的<b>临时</b>$mana-neutral$转化为签名颜色法力。',
    # 注意这里有一个<b>标签没闭合，原文就是这样
    '$Scribes$ in $ability-secondary$ <b>rings</b> will gain $+|+5|%$ <pos>Damage and  Attack Speed.</pos> <i>(Stacks up to 15%)</i>.=$ability-secondary$<b>环</b>中的$Scribes$$+|+5|%$<pos>伤害和攻速。</pos><i>(最多15%)</i>。',
    'Killing $Torn$ will <pos>afflict</pos> nearby $enemy-elites$ with $keyword-weakened$ for <pos>5s</pos>.=击杀$Torn$对附近$enemy-elites$<pos>施加</pos>$keyword-weakened$<pos>5s</pos>。',
    'Kills during $ability-utility$ <pos>extend</pos> your $keyword-inkling$\'s transformation by <b>0.5s</b>.=$ability-utility$期间击杀<pos>延长</pos>$keyword-inkling$变身<b>0.5s</b>。',
    'Your $keyword-inkling$ gains $+|+|75|%|DMG$, <pos>Speed</pos>, and <pos>Size</pos> during your $ability-utility$.=$ability-utility$期间$keyword-inkling$$+|+|75|%|DMG$、<pos>速度</pos>和<pos>体型</pos>。',
    '$Scribes$ who do not move during a <pos>Green Light</pos> will be <neg>rear-ended</neg> by other traffic.=<pos>绿灯</pos>期间不移动的$Scribes$会被<neg>追尾</neg>。',
    '$Scribes$ who move during <neg>Red Light</neg> will be <neg>Rooted</neg> for <neg>3s</neg> instead of slowed.=<neg>红灯</neg>期间移动的$Scribes$会被<neg>定身</neg><neg>3s</neg>而非减速。',
    '<neg>Minor</neg> $Torn$ have a $-|20|%| Chance$ to respawn as a <neg>Standard</neg> $Torn$.=<neg>小型</neg>$Torn$有$-|20|%| Chance$重生为<neg>标准</neg>$Torn$。',
    '<b>Standard</b> $Torn$ <neg>count</neg> as $enemy-splice$, $enemy-tangent$, and $enemy-raving$.=<b>标准</b>$Torn$<neg>视为</neg>$enemy-splice$、$enemy-tangent$和$enemy-raving$。',
    '$ability-secondary$ grants affected $Scribes$ a level of $keyword-Invulnerable$.=$ability-secondary$给予受影响$Scribes$一层$keyword-Invulnerable$。',
    '$Torn$ gain 1 Stack of $keyword-quarry$ per Page affecting them.=$Torn$每受一个页面影响获得1层$keyword-quarry$。',
    'Gain a stacking $+|+|1|%|DMG$ every second during a Chapter. (Max $+|+|250|%$)  Resets on Chapter end.=每章每秒$+|+|1|%|DMG$叠加(上限$+|+|250|%$)。章节结束重置。',
    'Killing an $enemy-elite$ or completing a <b>Bonus Objective</b> <b>permanently</b> <pos>reduces</pos> the cooldown of $ability-core$.=击杀$enemy-elite$或完成<b>额外目标</b><b>永久</b><pos>降低</pos>$ability-core$冷却。',
    'Every <b>15 Stacks</b> of $keyword-unrivaled$ fire off projectiles at all visible $Torn$ that deal $+|10|%$ of their health as damage.=每<b>15层</b>$keyword-unrivaled$向所有可见$Torn$发射弹射物，造成其$+|10|%$生命值伤害。',
    '$keyword-unrivaled$ reduces $ability-signature$ <b>Cooldown</b> by $+|-|25|%$ when above <b>50 Stacks</b>=$keyword-unrivaled$超过<b>50层</b>时$ability-signature$<b>冷却</b>$+|-|25|%$',
    'Consecutive thrown $ability-secondary$ hits gain $+|+|25|%|DMG$ and $+|+|15|%| Size$. (Max 5 Stacks, resets on miss.)=连续$ability-secondary$命中$+|+|25|%|DMG$和$+|+|15|%| Size$。(上限5层，未命中重置。)',
    'Flourish $+|20$ times during a <pos>single</pos> <b>Yellow Signature Ability</b>=单次<b>黄色签名技能</b>中$keyword-flourish$$+|20$次',
    'Every $keyword-flourish$ during $ability-signature$ gains $+|+|5|%|DMG$ (Max 250%)=$ability-signature$期间每次$keyword-flourish$$+|+|5|%|DMG$(上限250%)',
    'Break down 1 $keyword-plotarmor$ into $keyword-twists$ and gain 1 stack of $keyword-resolved$.=分解1个$keyword-plotarmor$为$keyword-twists$并获得1层$keyword-resolved$。',
    'Reach $+|60$ $keyword-blot$ Stacks on an enemy.=对一个敌人叠加$+|60$层$keyword-blot$。',
    'Killing enemies applies $keyword-marked$ to one nearby foe.=击杀敌人对附近一敌施加$keyword-marked$。',
    # === 挑战/成就 ===
    'Kill $+|200$ Minor $torn$.=击杀$+|200$个小型$torn$。',
    'Kill $+|2$ $boss$<b>es</b>.=击杀$+|2$个$boss$。',
    'Kill $+|10$ $boss$<b>es</b>.=击杀$+|10$个$boss$。',
    'Kill $+|125$ Standard $torn$.=击杀$+|125$个标准$torn$。',
    'Kill $+|100$ $enemy-ravings$.=击杀$+|100$个$enemy-ravings$。',
    'Kill $+|100$ $enemy-splices$.=击杀$+|100$个$enemy-splices$。',
    'Kill $+|100$ $enemy-tangents$.=击杀$+|100$个$enemy-tangents$。',
    'Kill $+|10$ $enemy-elite$ $torn$.=击杀$+|10$个$enemy-elite$$torn$。',
    'Kill 12 $Torn$ with a single use of $ability-signature$.=单次$ability-signature$击杀12个$Torn$。',
    'Defeat a Torn Boss at Appendix 3 during an Endless Run.=无尽模式中在附录3击败一个Torn Boss。',
    'Defeat a Torn Boss at Appendix 1 during an Endless Run.=无尽模式中在附录1击败一个Torn Boss。',
    '<pos>Spread</pos> $keyword-blot$ <pos>25,000</pos> times.=<pos>扩散</pos>$keyword-blot$<pos>25,000</pos>次。',
    # === 设置/UI ===
    'Sets the center-of-screen crosshair displayed during gameplay.=设置游戏中屏幕中心准星。',
    'Enables visual indicators around the Scribe to let you know of immediate incoming danger.=启用书记官周围的视觉提示以警示即刻到来的危险。',
    # === 最后一波Boss描述 ===
    'Found after mending The Last Stand of Pen and Ink=修复"笔墨最后阵地"后发现',
    'The Last Stand of Pen and Ink=笔墨最后阵地',
    'Standing in a <style=ability>Passage</style> grants <pos>+3</pos> to $ability-primary$ rolls. (Does not affect Natural 1s.)=站在<style=ability>通道</style>中$ability-primary$掷骰<pos>+3</pos>。(不影响天然1。)',
]

# Add all entries at end of file before the last section
marker = '# 带富文本标签的战斗提示'
pos = content.find(marker)
if pos == -1:
    # Fallback: add before the batch translations section
    marker = '// ========== Batch translations'
    pos = content.find(marker)

if pos != -1:
    insert = '\r\n# 补充翻译 — 扫描二进制发现的遗漏\r\n'
    insert += '\r\n'.join(new_entries) + '\r\n\r\n'
    content = content[:pos] + insert + content[pos:]
else:
    # Append to end
    insert = '\r\n# 补充翻译 — 扫描二进制发现的遗漏\r\n'
    insert += '\r\n'.join(new_entries) + '\r\n'
    content += insert

with open(fp, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Added {len(new_entries)} missing translations')
