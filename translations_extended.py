# -*- coding: utf-8 -*-
"""
Vellum Study Hall - 扩展翻译字典
包含页面效果、能力描述、系统文本等的中文翻译。
所有翻译已验证：中文UTF-8字节数 ≤ 英文UTF-8字节数。
"""

TRANSLATIONS_EXTENDED = {
    # ================================================================
    #  页面效果 — 通用/防御
    # ================================================================
    '$enemy-ravings$ are <neg>immune</neg> to $ability-primary$ damage.':
        '$enemy-ravings$对$ability-primary$伤害<neg>免疫</neg>。',

    'Your $ability-movement$ now <pos>resets</pos> when your $barrier$ breaks.':
        '$barrier$被破时$ability-movement$会<pos>重置</pos>。',

    'Reduced $ability-utility$ cooldown by $+||2|s$ per stack.':
        '每层减少$ability-utility$冷却$+||2|s$。',

    'Heal for $+|+|1|HP$/<b>s</b> while within <b>10m</b> of an enemy.':
        '在敌人<b>10m</b>内每<b>s</b>恢复$+|+|1|HP$。',

    '<b>Worthy</b> - $+|5|BAR$ for each $ability-utility$ cast.':
        '<b>英勇</b> - 每次$ability-utility$获得$+|5|BAR$。',

    'Casting $ability-primary$ grants subsequent casts $+|+|5|%|DMG$, up to $+|+|50|%$, then resets.':
        '连续$ability-primary$每次$+|+|5|%|DMG$，至$+|+|50|%$后重置。',

    '$keyword-leech$ <pos>reduces</pos> $ability-movement$ cooldown.':
        '$keyword-leech$<pos>减少</pos>$ability-movement$冷却。',

    'Continuing to cast $ability-primary$ will cause you to go <neg>overboard</neg>.':
        '持续施放$ability-primary$会导致<neg>过载</neg>。',

    'Using $ability-movement$ within <b>1s</b> of taking damage will restore $+|25|HP$.':
        '受伤<b>1s</b>内使用$ability-movement$恢复$+|25|HP$。',

    'Gain $+|+|40|%|DMG$ while your $Barrier$ is recharging.':
        '$Barrier$充能时获得$+|+|40|%|DMG$。',

    'Gain 1 <pos>Signature</pos> $mana-temp-neutral$ every 5s.':
        '每5s获得1个<pos>签名</pos>$mana-temp-neutral$。',

    'Damage taken increased by $-|+|25|%$.':
        '受到伤害提高$-|+|25|%$。',

    '$+|+|15|%|DMG$ dealt, and $-|+|15|%|DMG$ taken for each stack.':
        '每层$+|+|15|%|DMG$输出，$-|+|15|%|DMG$承伤。',

    '$ability-secondary$ gains $+|+|25|%|DMG$ and $+|+|15|%| Size$ per stack.':
        '$ability-secondary$每层$+|+|25|%|DMG$和$+|+|15|%| Size$。',

    '$ability-secondary$ can now <pos>pass through</pos> the environment, gaining <pos>size and damage</pos> the further it travels.':
        '$ability-secondary$可<pos>穿透</pos>地形，飞行越远<pos>体积和伤害</pos>越高。',

    '$Boss$ $Torn$ <neg>count</neg> as $enemy-splice$, $enemy-tangent$, and $enemy-raving$.':
        '$Boss$ $Torn$<neg>视为</neg>$enemy-splice$、$enemy-tangent$和$enemy-raving$。',

    'When you are slain, this page is <neg>consumed</neg> to <pos>revive</pos> you and <shake><b>Erase</b></shake> the offending foe.':
        '你死亡时此页面被<neg>消耗</neg>来<pos>复活</pos>你并<shake><b>抹杀</b></shake>凶手。',

    '$ability-primary$ can be channeled <pos>indefinitely</pos>.':
        '$ability-primary$可<pos>无限</pos>引导。',

    # ================================================================
    #  页面效果 — 攻击/伤害
    # ================================================================
    'Deal $+|+|30|%|DMG$ while standing in your $keyword-pool$.':
        '站在$keyword-pool$中时$+|+|30|%|DMG$。',

    'Using $ability-primary$ has a 20% chance to cast $ability-secondary$. (2s CD)':
        '$ability-primary$有20%几率触发$ability-secondary$。(2s冷却)',

    '$ability-secondary$ increases $ability-primary$ damage by $+|+|50|%$ for <b>3s</b>.':
        '$ability-secondary$使$ability-primary$伤害$+|+|50|%$持续<b>3s</b>。',

    'Grants all Scribes a <b>Defense Page</b> choice.':
        '全队获得<b>防御页面</b>选择。',

    'Grants all Scribes a <b>Keyword Page</b> choice.':
        '全队获得<b>词缀页面</b>选择。',

    'Grants all Scribes a <b>Movement Page</b> choice.':
        '全队获得<b>位移页面</b>选择。',

    'Grants all Scribes an <b>Offense Page</b> choice.':
        '全队获得<b>攻击页面</b>选择。',

    'Gravity is <neg>greatly increased</neg>.':
        '重力<neg>大幅增加</neg>。',

    'Bring it to the <b>Font</b> to complete the <b>Bonus Objective</b>!':
        '带到<b>圣泉</b>完成<b>额外目标</b>！',

    'The next time <neg>die</neg>, you will automatically <pos>revive</pos>.':
        '下次<neg>死亡</neg>时自动<pos>复活</pos>。',

    '$ability-movement$ now has <pos>No Cooldown</pos> but costs <neg>1</neg> $mana-neutral$.':
        '$ability-movement$<pos>无冷却</pos>但消耗<neg>1</neg>$mana-neutral$。',

    'Taking damage has a $Chance|+|30$ to fire your $ability-primary$ at the attacker.':
        '受伤有$Chance|+|30$向攻击者发射$ability-primary$。',

    'Ink Launchers grant $+|+|100|%| Air Control$ until landing.':
        '墨水发射器给予$+|+|100|%| Air Control$至落地。',

    '<b>Lava</b> <neg>slows</neg> $scribes$ by $-|-|50|%$.':
        '<b>熔岩</b><neg>减速</neg>$scribes$ $-|-|50|%$。',

    'Gained for each slain $torn$ during the tome.':
        '在卷册中每击杀$torn$获得一层。',

    'Damaged $enemy-ravings$ <neg>pulse</neg> $keyword-stain$.':
        '受伤$enemy-ravings$<neg>脉冲</neg>$keyword-stain$。',

    '$ability-secondary$ launches <pos>2 additional</pos> projectiles.':
        '$ability-secondary$发射<pos>额外2枚</pos>弹射物。',

    'The <b>Zombie Furnace</b> has been activated!':
        '<b>僵尸熔炉</b>已启动！',

    '<neg>Fog</neg> now reduces visibility <neg>tremendously</neg>.':
        '<neg>迷雾</neg>现在<neg>大幅</neg>降低能见度。',

    'Deal $+|500|%$ of damage taken back to attacker.':
        '将受到伤害的$+|500|%$反弹给攻击者。',

    'Taking damage applies $keyword-marked$ to the attacker.':
        '受伤时对攻击者施加$keyword-marked$。',

    'Store all damage taken. When your $barrier$ is broken, explode for $+|500|%$ of stored damage.\n(Does not proc additional effects.)':
        '蓄积所有受到的伤害。$barrier$被破时爆炸造成$+|500|%$蓄积伤害。\n（不触发额外效果。）',

    'Deal $+|+|50|%|DMG$ while at full $barrier$.':
        '$barrier$满时$+|+|50|%|DMG$。',

    '$+|3|%|DMG$ is converted to $Barrier$.':
        '$+|3|%|DMG$转化为$Barrier$。',

    'Generating $Barrier$ restores partial $mana-neutral$.':
        '生成$Barrier$时恢复部分$mana-neutral$。',

    '$ability-utility$ grants $+|+5|%|DMG$ per stack of $keyword-tension$ consumed for <b>5s.</b>':
        '$ability-utility$每消耗一层$keyword-tension$获得$+|+5|%|DMG$持续<b>5s。</b>',

    'Gain $keyword-tension$ twice as fast.':
        '双倍速获得$keyword-tension$。',

    '$keyword-tension$ has a $+|50|%$ Chance to persist through $ability-utility$.':
        '$keyword-tension$有$+|50|%$几率在$ability-utility$后保留。',

    'Taking damage now generates $keyword-tension$.':
        '受伤时生成$keyword-tension$。',

    'Gain $keyword-tension$ when casting with $ability-primary$ or $ability-secondary$.':
        '施放$ability-primary$或$ability-secondary$时获得$keyword-tension$。',

    '$keyword-plotarmor$ $Barrier$ and <b>Damage Reduction</b> persist during $keyword-resolved$.':
        '$keyword-plotarmor$的$Barrier$和<b>减伤</b>在$keyword-resolved$期间保留。',

    'You now direct $keyword-twists$, and they <neg>no longer</neg> seek foes.':
        '你现在手动引导$keyword-twists$，不再<neg>自动</neg>追敌。',

    'Every time you fire $keyword-twists$, they gain $+|+|25|%|DMG$ for <b>3s</b>.':
        '每次发射$keyword-twists$，获得$+|+|25|%|DMG$持续<b>3s</b>。',

    '$keyword-twists$ lodge into enemies applying $keyword-weakened$ and dealing $+|45|DMG$ per $keyword-twist$ over <b>3s</b>.':
        '$keyword-twists$嵌入敌人施加$keyword-weakened$，每个$keyword-twist$造成$+|45|DMG$/<b>3s</b>。',

    '<b>Slowed</b>, and taking <neg>increasing damage<neg> the longer you remain affected.':
        '<b>减速</b>，持续时间越长受到的<neg>伤害越高<neg>。',

    'Killing an enemy has a $Chance|+|30$ to recharge a spent $mana-any$.':
        '击杀敌人有$Chance|+|30$恢复一个$mana-any$。',

    'Continue taking damage to complete the <b>Bonus Objective</b>!':
        '继续承受伤害以完成<b>额外目标</b>！',

    '$explosive-orb$<b>s</b> now move toward the nearest $Scribe$.':
        '$explosive-orb$现在会向最近的$Scribe$移动。',

    '$+|-|30|%$ damage taken.':
        '承伤$+|-|30|%$。',

    '$ability-utility$ cooldown is <pos>reduced</pos> by $+|-|20|%$.':
        '$ability-utility$冷却<pos>减少</pos>$+|-|20|%$。',

    '<b>Obelisks</b> must be <b>fueled</b> <neg>twice</neg> before they are vulnerable.':
        '<b>方尖碑</b>需要<b>充能</b><neg>两次</neg>才会变得可攻击。',

    # ================================================================
    #  页面效果 — 主要技能
    # ================================================================
    '$ability-primary$ gains $+|1| Bounce$. Each Bounce gains $+|33|%| Size$.':
        '$ability-primary$获得$+|1| Bounce$。每次弹射$+|33|%| Size$。',

    '$ability-primary$ has a chance to split every time it bounces.':
        '$ability-primary$每次弹射有几率分裂。',

    '$ability-primary$ gains $+|50|%| damage and size$.':
        '$ability-primary$$+|50|%| damage and size$。',

    '$ability-primary$ gains $+|100|%| Damage$ on direct hit.':
        '$ability-primary$直接命中时$+|100|%| Damage$。',

    '$ability-primary$ gains up to $+|100|%| damage$ and $+|50|%| size$ increasing the longer it takes before exploding.':
        '$ability-primary$爆炸前飞行越久，$+|100|%| damage$和$+|50|%| size$越高。',

    '$ability-primary$ detonates when close to a $Torn$. $ability-primary$ also gains $+|15|%|DMG$.':
        '$ability-primary$靠近$Torn$时引爆。$ability-primary$$+|15|%|DMG$。',

    '$ability-primary$ gains $+|2| Bounces$. Each Bounce gains $+|33|%| Damage$.':
        '$ability-primary$获得$+|2| Bounces$。每次弹射$+|33|%| Damage$。',

    '$ability-primary$ gains $+|+|40|%|DMG$, <pos>Size</pos>, and pushes $Torn$ backwards.':
        '$ability-primary$$+|+|40|%|DMG$、<pos>体积</pos>增大并击退$Torn$。',

    '$ability-primary$ and $ability-secondary$ knock the $Scribe$ back.':
        '$ability-primary$和$ability-secondary$会击退$Scribe$。',

    '$ability-primary$ explodes a <pos>second time</pos> after <b>0.5s</b>.':
        '$ability-primary$在<b>0.5s</b>后<pos>二次</pos>爆炸。',

    '$ability-primary$ deals $+|+|35|%|DMG$ to distant foes.':
        '$ability-primary$对远处敌人$+|+|35|%|DMG$。',

    '$ability-primary$ damage has a $Chance|+|30$ to apply $keyword-blot$.':
        '$ability-primary$伤害有$Chance|+|30$施加$keyword-blot$。',

    '$ability-primary$ coats $Torn$ in an adhesive mixture that increases $+|+|50|%|DMG$ taken from $ability-primary$ for <b>3s</b>.':
        '$ability-primary$涂$Torn$粘液，受$ability-primary$$+|+|50|%|DMG$持续<b>3s</b>。',

    '$ability-primary$ has a $Chance|+|50$ to fire a <pos>second time</pos>. $Chance|+|100$ at Full Charge.':
        '$ability-primary$有$Chance|+|50$<pos>二次</pos>发射。满蓄力时$Chance|+|100$。',

    '$ability-primary$ and $ability-secondary$ $keyword-flourish$ hits grant $+|+|20|BAR$.':
        '$ability-primary$和$ability-secondary$$keyword-flourish$命中得$+|+|20|BAR$。',

    'Correctly timing the second attack of $ability-primary$ deals $+|+|200|%|DMG$.':
        '精准把握$ability-primary$第二击时机可造成$+|+|200|%|DMG$。',

    '$ability-primary$ deals $+|100|%|DMG$ at full charge, but charges <neg>slightly slower</neg>.':
        '$ability-primary$满蓄力时$+|100|%|DMG$，但蓄力<neg>略慢</neg>。',

    '$ability-primary$ attacks $+|20|%$ <pos>faster</pos>.':
        '$ability-primary$攻速<pos>加快</pos>$+|20|%$。',

    '$ability-primary$ projectiles <pos>seek targets</pos> much more aggressively.':
        '$ability-primary$弹射物更强力地<pos>追踪目标</pos>。',

    '$ability-primary$ can deflect your $ability-secondary$ <b>shields</b>.':
        '$ability-primary$可以弹射$ability-secondary$的<b>盾</b>。',

    # ================================================================
    #  页面效果 — 副技能
    # ================================================================
    '$ability-secondary$ gains $+|+|135|%|DMG$, but costs $-|+|1$ mana.':
        '$ability-secondary$$+|+|135|%|DMG$，但消耗$-|+|1$法力。',

    '$ability-secondary$ gains $+|+|80|%|DMG$, but forfeits $-|40|% Size$.':
        '$ability-secondary$$+|+|80|%|DMG$，但体积$-|40|% Size$。',

    '$ability-secondary$ casts from Multi-Purpose Tool are <pos>infused</pos> with your <b>Signature Ink</b>.':
        '万能工具的$ability-secondary$会被<b>签名墨水</b><pos>灌注</pos>。',

    '$ability-secondary$ deals $+|+|40|%|DMG$ while within 10m of <pos>Dusk</pos>.':
        '在<pos>黄昏</pos>10m内时$ability-secondary$$+|+|40|%|DMG$。',

    '$ability-secondary$ casts an <pos>additional time</pos> at your location after <b>2s</b>.':
        '$ability-secondary$在<b>2s</b>后在你的位置<pos>再次</pos>施放。',

    '$ability-secondary$ triggers a <pos>second burst</pos> after a short delay.':
        '$ability-secondary$短暂延迟后触发<pos>二次爆发</pos>。',

    '$ability-secondary$ gains $+|75|%| Size$, $+|50|%|DMG$, and now <pos>roots</pos> foes for <b>0.5s</b> instead of knocking back.':
        '$ability-secondary$$+|75|%| Size$、$+|50|%|DMG$，并<pos>定身</pos>敌人<b>0.5s</b>而非击退。',

    '$ability-secondary$ gains <pos>25 base damage.</pos>':
        '$ability-secondary$<pos>25基础伤害。</pos>',

    '$ability-secondary$ gains $+|+|25|%|DMG$ and knocks $Torn$ back further. <i>(Roots longer with Albatross)</i>':
        '$ability-secondary$$+|+|25|%|DMG$并增加$Torn$击退距离。<i>(信天翁下定身更久)</i>',

    # ================================================================
    #  页面效果 — 位移/大招
    # ================================================================
    '$ability-movement$ cooldown reset.':
        '$ability-movement$冷却重置。',

    'Your $ability-movement$ casts $ability-primary$ at the nearest enemy.':
        '$ability-movement$会向最近敌人发射$ability-primary$。',

    'When cast without a target, $ability-movement$ blinks further and in <i>any</i> direction.':
        '无目标时$ability-movement$闪现更远且可向<i>任意</i>方向。',

    # Removed: text not found in assets

    '$ability-utility$ grants $+|+|100|%|DMG$, <pos>Speed</pos>, and $keyword-leech$ <pos>Healing</pos> for <b>5s</b>.':
        '$ability-utility$给予$+|+|100|%|DMG$、<pos>速度</pos>和$keyword-leech$<pos>治疗</pos>持续<b>5s</b>。',

    '$ability-utility$ detonates already $keyword-tether$<b>ed</b> $Torn$ for $+|125|DMG$.':
        '$ability-utility$引爆已$keyword-tether$的$Torn$造成$+|125|DMG$。',

    'Your $ability-utility$ duration is <pos>increased</pos> by $+|2|s$.':
        '$ability-utility$持续时间<pos>延长</pos>$+|2|s$。',

    '$ability-utility$ restores <pos>4</pos> $mana-neutral$ over <pos>4s</pos> for all $Scribes$.':
        '$ability-utility$为所有$Scribes$在<pos>4s</pos>内恢复<pos>4</pos>$mana-neutral$。',

    # ================================================================
    #  页面效果 — 签名/核心技能
    # ================================================================
    '$ability-signature$ applies an <pos>additional stack</pos> of $keyword-blot$.':
        '$ability-signature$施加<pos>额外一层</pos>$keyword-blot$。',

    'Gain another Signature Ink. Infuses your $ability-signature$ with that Ink.':
        '获得额外签名墨水。为$ability-signature$灌注该墨水。',

    '$ability-core$ applies $keyword-tether$ to <pos>all</pos> foes affected by $keyword-blot$.':
        '$ability-core$对<pos>全部</pos>$keyword-blot$敌人施加$keyword-tether$。',

    'Convert $mana-neutral$ to $mana-core$ when you use your $ability-signature$.':
        '使用$ability-signature$时将$mana-neutral$转化为$mana-core$。',

    'Unlock a new Signature Ink.':
        '解锁新的签名墨水。',

    # ================================================================
    #  页面效果 — 关键词/墨渍
    # ================================================================
    '$keyword-blot$ causes affected $torn$ to take $+|+|10|%|DMG$ from <pos>any sources</pos>.':
        '$keyword-blot$使$torn$受到<pos>所有来源</pos>$+|+|10|%|DMG$。',

    'Each time $keyword-blot$ deals damage, it also deals $+|5|DMG$ to your current target.':
        '$keyword-blot$每次造成伤害时也对当前目标造成$+|5|DMG$。',

    '$+|2|%|$ of $keyword-blot$ damage is granted as $Barrier$.':
        '$keyword-blot$伤害的$+|2|%|$转化为$Barrier$。',

    '$keyword-blot$ lasts an <pos>additional 2s</pos>.':
        '$keyword-blot$持续时间<pos>延长2s</pos>。',

    '$keyword-blot$ lasts an <pos>additional 3s</pos> when applied to $keyword-weakened$ enemies.':
        '$keyword-blot$对$keyword-weakened$的敌人持续时间<pos>延长3s</pos>。',

    '$keyword-infuse$ damage <pos>increases</pos> to <pos>50%</pos> from <b>33%</b>.':
        '$keyword-infuse$伤害从<b>33%</b><pos>提升</pos>至<pos>50%</pos>。',

    '$keyword-leech$ healing <pos>increases</pos> by <pos>+10%</pos>.':
        '$keyword-leech$治疗量<pos>提升</pos><pos>+10%</pos>。',

    '$keyword-flourish$<b>es</b> deal $+|+|50|%|DMG$ during $ability-utility$.':
        '$ability-utility$期间$keyword-flourish$造成$+|+|50|%|DMG$。',

    '$keyword-flourish$<b>es</b> deal $+|+|250|%|DMG$ during $ability-utility$.':
        '$ability-utility$期间$keyword-flourish$造成$+|+|250|%|DMG$。',

    'Your general damage bonuses <pos>also increase</pos> your $keyword-flourish$ damage bonus.':
        '你的通用伤害加成也会<pos>增加</pos>$keyword-flourish$伤害加成。',

    'Damage from your $ability-movement$ applies $keyword-draft$ to enemies.':
        '$ability-movement$伤害对敌人施加$keyword-draft$。',

    '$keyword-pool$ gains an additional $+|100|% Size$.\n\n$Torn$ in $keyword-pool$<B>s</b> take $+|50|%$ more damage.':
        '$keyword-pool$体积额外$+|100|% Size$。\n\n$keyword-pool$中的$Torn$受到$+|50|%$更多伤害。',

    # ================================================================
    #  页面效果 — 屏障/生存
    # ================================================================
    'Your $barrier$ starts recharging faster.':
        '$barrier$开始更快充能。',

    '$+|30|%|SPD$ while your $barrier$ is empty.':
        '$barrier$为空时$+|30|%|SPD$。',

    'Gain $+|+|75|%|HP$ and  $+|-|50|%$ Knockback taken. \nGrow in size by $-|+|20|%$.':
        '获得$+|+|75|%|HP$和$+|-|50|%$击退。\n体型增大$-|+|20|%$。',

    'Next damage taken <pos>reduced to 0</pos> and attacker takes $+|100|DMG$.':
        '下次受伤<pos>降为0</pos>并对攻击者造成$+|100|DMG$。',

    'Gain $+|25|%|DMG$ per stack, but <neg>lose</neg> stacks when taking damage.':
        '每层$+|25|%|DMG$，但受伤时<neg>失去</neg>层数。',

    'Gain $+|+|20|HP$ at the start of each <b>Chapter</b> (Max 240).':
        '每<b>章节</b>开始时获得$+|+|20|HP$(上限240)。',

    'You can now <b>Glide</b> while falling.':
        '下落时可以<b>滑翔</b>。',

    'Gain <pos>damage</pos> based on your current <pos>speed</pos> (Max $+|+|50|%|DMG$).':
        '基于当前<pos>速度</pos>获得<pos>伤害</pos>加成(上限$+|+|50|%|DMG$)。',

    'Killing an enemy has a $Chance|+|50$ to grant $+|+|1| Max HP$.':
        '击杀敌人有$Chance|+|50$获得$+|+|1| Max HP$。',

    'Gain $keyword-invulnerable$ every <b>5s</b>.':
        '每<b>5s</b>获得$keyword-invulnerable$。',

    '$ability-primary$ damage increased by $+|+|2|%$ per stack. <neg>All lost</neg> upon casting $ability-secondary$.':
        '$ability-primary$每层$+|+|2|%$伤害。施放$ability-secondary$时<neg>全部失去</neg>。',

    # ================================================================
    #  页面效果 — 速度/移动
    # ================================================================
    '$+|+|1|%|SPD$ per stack.':
        '每层$+|+|1|%|SPD$。',

    '$+|+|50|%|SPD$ and immune to Reversion Hourglasses.':
        '$+|+|50|%|SPD$且免疫逆转沙漏。',

    '$+|+|25|%|DMG$ per stack.':
        '每层$+|+|25|%|DMG$。',

    '$+|+10|%$ <pos>Speed</pos> and <pos>Damage</pos>.':
        '$+|+10|%$<pos>速度</pos>和<pos>伤害</pos>。',

    'Reduced Speed and Increased Gravity.':
        '速度降低，重力增加。',

    # ================================================================
    #  页面效果 — 掉落物/拾取
    # ================================================================
    '<pos>Barrier Motes</pos> have a $Chance|+|20$ to drop from slain foes.':
        '<pos>屏障微粒</pos>有$Chance|+|20$从击杀的敌人掉落。',

    'When collected, restore $+|10|BAR$.':
        '拾取后恢复$+|10|BAR$。',

    # ================================================================
    #  Boss/战斗机制
    # ================================================================
    '<neg>Lava</neg> now <neg>rises</neg> over time.':
        '<neg>熔岩</neg>随时间<neg>上涨</neg>。',

    '$enemy-splices$ are <neg>Immune</neg> to push and pull effects.':
        '$enemy-splices$对推拉效果<neg>免疫</neg>。',

    'Mechanics will <neg>overlap!</neg> Keep dodging and don\'t kill your <pos>teammates!</pos>':
        '机制会<neg>重叠！</neg>持续躲避，别误杀<pos>队友！</pos>',

    '<pos>Loosely</pos> stack! Don\'t <neg>overlap</neg> allies.':
        '<pos>松散</pos>集合！不要<neg>重叠</neg>队友。',

    'While <pos>dusted</pos> you  must <b>kill</b> the <neg>manifestations!</neg>':
        '<pos>被尘化</pos>时必须<b>击杀</b><neg>具象！</neg>',

    '$+|+|10|%|DMG$ per stack for <b>Syncing</b>!':
        '每层$+|+|10|%|DMG$用于<b>同步</b>！',

    'Destroy the <b>Eye of the Storm</b>!':
        '摧毁<b>风暴之眼</b>！',

    'All foes are $keyword-embossed$ while near the Fountain.':
        '靠近喷泉时所有敌人获得$keyword-embossed$。',

    'Can see and attack <neg>Manifestations</neg>.':
        '可以看到并攻击<neg>具象</neg>。',

    '$enemy-tangent$ attacks <neg>add $-|+|3| Seconds$</neg> to $Scribe$ Movement Ability cooldown.':
        '$enemy-tangent$攻击<neg>增加$-|+|3| Seconds$</neg>$Scribe$位移冷却。',

    # ================================================================
    #  页面效果 — 清漆/护甲
    # ================================================================
    'Gain $+|5$ $keyword-varnish$ for $+|5|s$ whenever $ability-primary$ deals damage.':
        '$ability-primary$造成伤害时获得$+|5$$keyword-varnish$持续$+|5|s$。',

    'While charging $ability-primary$, gain 20 $keyword-varnish$ and summon a <pos>shield</pos>, blocking projectiles.':
        '蓄力$ability-primary$时获得20$keyword-varnish$并召唤<pos>盾</pos>，格挡弹射物。',

    '$torn$ damaged by $keyword-twists$ gain 3 $keyword-varnish$.':
        '被$keyword-twists$伤害$torn$得3$keyword-varnish$。',

    # ================================================================
    #  页面效果 — 墨灵
    # ================================================================
    'Your $keyword-inkling$ has recently come to your aid and cannot do so again for a time.':
        '$keyword-inkling$刚刚援助过你，暂时无法再次出手。',

    'Your $keyword-inkling$<b>\'s</b> $keyword-inkcast$ deals $+|+|200|%|DMG$ to its target.':
        '$keyword-inkling$的$keyword-inkcast$对目标$+|+|200|%|DMG$。',

    'Your $keyword-inkling$ kills <pos>reduce</pos> your $ability-signature$ cooldown by $+|0.5|s$.':
        '$keyword-inkling$击杀<pos>减少</pos>$ability-signature$冷却$+|0.5|s$。',

    # ================================================================
    #  任务文本
    # ================================================================
    'You may <pos>Reroll</pos> a <b>Page Choice</b> once in each <b>Tome</b>.':
        '每本<b>卷册</b>中可<pos>重骰</pos>一次<b>页面选择</b>。',

    'Gain $keyword-impervious$ for <b>3s</b> after being revived.':
        '复活后获得$keyword-impervious$持续<b>3s</b>。',

    'Regain $+|1|HP$ every <b>3s</b>.':
        '每<b>3s</b>恢复$+|1|HP$。',

    'Gain 1 level when killing a foe. The Ink Font will imbue extra power.':
        '击杀敌人升1级。墨泉会灌注额外力量。',

    'Acrobatically <pos>flip</pos> backwards, becoming $keyword-impervious$ for $+|0.3|s$.':
        '杂技般<pos>后空翻</pos>，获得$keyword-impervious$持续$+|0.3|s$。',

    # ================================================================
    #  能力描述（核心技能说明）
    # ================================================================
    'Lash out in close-quarters with an inky whip, cracking an area for $+|20|DMG$.':
        '近距离挥出墨鞭，对区域造成$+|20|DMG$。',

    '<b>Hold & Release:</b> Conjure a <b>Twilight Lance</b> to <pos>recolor</pos> corrupted lanterns.':
        '<b>蓄力释放:</b>召唤<b>暮光长矛</b><pos>重染</pos>腐化灯笼。',

    'Lash out with a close-ranged <pos>Splash</pos>, <b>impacting</b> an area of several foes.':
        '近距离释放<pos>溅射</pos>，<b>冲击</b>多个敌人区域。',

    'Quickly fling condensed <b>Ink</b> to <pos>pummel</pos> foes.':
        '快速甩出浓缩<b>墨水</b><pos>痛击</pos>敌人。',

    'Quickly fling condensed <pos>Ink</pos> to <b>pummel</b> foes.':
        '快速甩出浓缩<pos>墨水</pos><b>痛击</b>敌人。',

    'Sends out a vengeful, seeking raven that deals $+|50|DMG$ and knocks enemies away.':
        '放出复仇追踪乌鸦，造成$+|50|DMG$并击退敌人。',

    'Summon a <pos>Raven</pos> to <b>seek out</b> and <pos>knock away</pos> enemies.':
        '召唤<pos>乌鸦</pos><b>追踪</b>并<pos>击退</pos>敌人。',

    'Hurl an <b>Anvil</b> to <pos>bludgeon</pos> all enemies <pos>along its path</pos>.':
        '投掷<b>铁砧</b><pos>碾压</pos>路径上<pos>所有敌人</pos>。',

    'Hurl an <pos>Anvil</pos> to <b>bludgeon</b> all enemies <pos>along its path</pos>.':
        '投掷<pos>铁砧</pos><b>碾压</b>路径上<pos>所有敌人</pos>。',

    'Take on a <b>Spectral Form</b> for <pos>0.85s</pos>, gaining <pos>increased mobility</pos> and <pos>immunity</pos> to damage and knockback effects.':
        '化为<b>幽灵形态</b><pos>0.85s</pos>，获得<pos>高机动</pos>和伤害击退<pos>免疫</pos>。',

    'Toss an inky <pos>Potion</pos> that <pos>bounces</pos>, then shatters to <b>envelop</b> nearby foes.':
        '投掷墨水<pos>药剂</pos>，<pos>弹跳</pos>后碎裂<b>笼罩</b>附近敌人。',

    'Toss an inky <b>Potion</b> that <pos>bounces</pos>, then shatters to <pos>envelop</pos> nearby foes.':
        '投掷墨水<b>药剂</b>，<pos>弹跳</pos>后碎裂<pos>笼罩</pos>附近敌人。',

    'Sling a <pos>Spoiled Apple</pos> that <pos>sticks</pos> to foes and <pos>bursts</pos> after a short delay.':
        '弹射<pos>烂苹果</pos>，<pos>粘</pos>在敌人身上并延迟<pos>爆炸</pos>。',

    # ================================================================
    #  状态效果
    # ================================================================
    'A <b>Zombie</b> has slowed you by $-|-|40|%$.':
        '<b>僵尸</b>减速了你$-|-|40|%$。',

    '<neg>Slowed</neg> $-|20|%$ by a <b>Zombie</b>.':
        '被<b>僵尸</b><neg>减速</neg>$-|20|%$。',

    '<b>Slowed</b> while in <neg>Lava</neg>':
        '在<neg>熔岩</neg>中<b>减速</b>',

    'Slowed by a $enemy-raving$ attack.':
        '被$enemy-raving$攻击减速。',

    '<neg>Rooted</neg> by a Mine.':
        '地雷<neg>定身</neg>。',

    # ================================================================
    #  撕裂者修正页面（敌人增强效果）
    # ================================================================
    '$torn$ have a $Chance|-|15$ to <neg>arrive</neg> $keyword-embossed$.':
        '$torn$有$Chance|-|15$<neg>出现</neg>时带$keyword-embossed$。',

    '$torn$ <b>Pages</b> are more <neg>dangerous</neg>.':
        '$torn$<b>页面</b>更加<neg>危险</neg>。',

    '$torn$ <b>Pages</b> are <neg>devastating</neg>.':
        '$torn$<b>页面</b><neg>毁灭性</neg>的。',

    '$Torn$ deal $+|-|75|%|DMG$, but their attacks <neg>apply</neg> $keyword-poison$.':
        '$Torn$造成$+|-|75|%|DMG$，但攻击<neg>施加</neg>$keyword-poison$。',

    '$torn$ <neg>always</neg> $keyword-bolster$ their nearby allies when slain.':
        '$torn$被杀时<neg>总是</neg>$keyword-bolster$附近友军。',

    '$enemy-ravings$ gain a <neg>burst of speed</neg> when nearby $Scribes$ use Movement Abilities.':
        '附近$Scribes$使用位移时$enemy-ravings$<neg>爆发加速</neg>。',

    '$enemy-ravings$ <neg>move faster</neg> based on their target\'s missing Health.':
        '$enemy-ravings$基于目标已损生命值<neg>加速移动</neg>。',

    '$enemy-ravings$ grant a large burst of <neg>speed</neg> to nearby $Torn$ on death.':
        '$enemy-ravings$死亡时给予附近$Torn$大量<neg>速度</neg>。',

    '$enemy-ravings$ gain <neg>Size</neg> and <neg>Speed</neg> every second.':
        '$enemy-ravings$每秒增加<neg>体型</neg>和<neg>速度</neg>。',

    '$enemy-splice$ attacks have a $chance|-|50$ to <neg>drain</neg> a $mana-neutral$.':
        '$enemy-splice$攻击有$chance|-|50$<neg>汲取</neg>$mana-neutral$。',

    '$Torn$ attacks <neg>root</neg> $Scribes$ with a full $barrier$.':
        '$Torn$攻击会<neg>定身</neg>$barrier$满的$Scribes$。',

    '$torn$ gain $-|+|100|%|SPD$ while in <neg>Lava</neg>.':
        '$torn$在<neg>熔岩</neg>中获得$-|+|100|%|SPD$。',

    '$torn$ drop $keyword-gold$ when slain. All Vignettes are <b>Markets</b>.':
        '$torn$被杀时掉落$keyword-gold$。所有插画为<b>市场</b>。',

    '$Scribes$ grant $keyword-embossed$ to the <neg>first</neg> $Torn$ they <i>dare</i> to damage each Chapter.':
        '$Scribes$每章<neg>第一个</neg><i>敢</i>攻击的$Torn$获$keyword-embossed$。',

    'Damaging $torn$ <neg>shrinks</neg> $scribe$ spells and projectiles by $-|-|10|%$. (Max <neg>5</neg> stacks)':
        '伤害$torn$时$scribe$技能和弹射物<neg>缩小</neg>$-|-|10|%$。(最多<neg>5</neg>层)',

    'The <b>second</b> $torn$ <b>Page</b> choice is always <neg>hidden</neg>.':
        '<b>第二</b>个$torn$<b>页面</b>选择总是<neg>隐藏</neg>的。',

    # ================================================================
    #  圣泉（Font）能力
    # ================================================================
    '<b>The Font</b> <pos>applies</pos> $keyword-marked$ to a nearby foe every <b>5s</b>.':
        '<b>圣泉</b>每<b>5s</b><pos>施加</pos>$keyword-marked$给附近敌人。',

    '<b>The Font</b> summons a <pos>Bell</pos> that $keyword-silences$ all foes for <pos>5s</pos> when rung.\n\n<b>Interact</b> to ring the bell. (30s CD)':
        '<b>圣泉</b>召唤<pos>钟</pos>，敲响后$keyword-silences$所有敌人<pos>5s</pos>。\n\n<b>交互</b>敲钟。(30s冷却)',

    'Complete a <sprite name=bookclub><b>Book Club</b> challenge.':
        '完成一个<sprite name=bookclub><b>读书会</b>挑战。',

    # ================================================================
    #  通用游戏文本
    # ================================================================
    'Your $ability-signature$ cleanses any $keyword-poison$ on you.':
        '$ability-signature$清除你身上的$keyword-poison$。',

    'Diamonds rain from the sky, granting $+|15$ $keyword-gold$ if caught.':
        '钻石从天而降，接住获得$+|15$$keyword-gold$。',

    '$boss$ gains <neg>Attack Speed</neg> based on missing health.':
        '$boss$基于已损生命值获得<neg>攻击速度</neg>。',

    'When consuming $keyword-stain$, $enemy-tangent$ attacks <neg>reduce</neg> $Scribe$ <neg>Health</neg> by $-|-|50|%$ for <b>5s</b>.':
        '消耗$keyword-stain$时，$enemy-tangent$攻击<neg>降低</neg>$Scribe$<neg>生命</neg>$-|-|50|%$持续<b>5s</b>。',

    '$ability-movement$ causes your target to deal $+|-|25|%|DMG$ for <b>3s</b>.':
        '$ability-movement$使目标造成$+|-|25|%|DMG$持续<b>3s</b>。',

    '$ability-movement$ causes you to generate $+|+|50|%$ more $mana-neutral$ for <b>5s</b> when teleporting to a $torn$.':
        '传送到$torn$时$ability-movement$使你$+|+|50|%$$mana-neutral$生成持续<b>5s</b>。',

    'Killing your $ability-movement$ target within <b>2s</b> of warping refunds the cooldown.':
        '传送后<b>2s</b>内击杀$ability-movement$目标退还冷却。',

    'Increase <pos>Maximum Health</pos>, forfeit <neg>All Barrier</neg>.\n$ability-primary$ applies $keyword-tether$.\nCan generate $mana-red$.':
        '增加<pos>最大生命</pos>，失去<neg>全部屏障</neg>。\n$ability-primary$施加$keyword-tether$。\n可生成$mana-red$。',

    'Damage from <b>Spells</b> generates $keyword-survey$.\nCan generate $mana-orange$.':
        '<b>法术</b>伤害生成$keyword-survey$。\n可生成$mana-orange$。',

    'Foes hit by $ability-primary$ take $+|+|12|%|DMG$ from $ability-primary$ for <b>2s</b> (Max $+|450|%$).':
        '$ability-primary$命中的敌人受$ability-primary$$+|+|12|%|DMG$<b>2s</b>(上限$+|450|%$)。',

    'Every <b>15th</b> mana spent casts a <pos>free</pos> $ability-utility$.':
        '每消耗<b>15</b>法力<pos>免费</pos>施放$ability-utility$。',

    'Using $ability-utility$ grants up to 5 <pos>Signature</pos> $temp-mana-neutral$. (1 Mana per 5s between uses.)':
        '$ability-utility$给予至多5个<pos>签名</pos>$temp-mana-neutral$。(每5s间隔1法力。)',

    'Gain <pos>+3 Rewrites</pos>.\n\n<i>As you wish.</i>':
        '<pos>+3改写</pos>。\n\n<i>如你所愿。</i>',

    '<neg>Instant Death</neg> at <b>10</b> stacks.':
        '<b>10</b>层时<neg>即死</neg>。',

    'Negative effects from $enemy-ravings$ last $-|+|30|%| longer$.':
        '$enemy-ravings$的负面效果持续$-|+|30|%| longer$。',

    '$Scribes$ who move during <neg>Red Light</neg> will be $keyword-silenced$ for <neg>3s</neg> by the court.':
        '在<neg>红灯</neg>期间移动的$Scribes$会被$keyword-silenced$<neg>3s</neg>。',

    'The $Torn$ drain a $mana-neutral$ from $Scribes$ who move during <neg>Red Light</neg>.':
        '$Torn$会从<neg>红灯</neg>期间移动的$Scribes$汲取$mana-neutral$。',

    'There must <neg>always</neg> be a $keyword-chosen$, infused with <neg>powers</neg> from the $boss$.':
        '必须<neg>始终</neg>有一名$keyword-chosen$，被$boss$灌注<neg>力量</neg>。',

    'Stay near the <b>Center</b> until <neg>Crystal Walls</neg> spawn!':
        '在<neg>水晶墙</neg>出现前待在<b>中心</b>附近！',

    '<b>Resonant Shards</b> will be more <neg>numerous</neg> and <neg>widespread</neg>.':
        '<b>共鸣碎片</b>会更加<neg>密集</neg>和<neg>分散</neg>。',

    'Enemies killed by $keyword-flourish$ have a $Chance|+|50$ to spawn a black hole, <pos>pulling in</pos> nearby foes.':
        '$keyword-flourish$击杀的敌人有$Chance|+|50$生成黑洞，<pos>吸引</pos>附近敌人。',

    # System texts with different newline format - handled by _VellumChinese.txt

    'Your <b>Tranquility</b> regeneration is <pos>3x</pos> as strong.':
        '<b>宁静</b>恢复效果<pos>3倍</pos>增强。',

    '$boss$ summons a <neg>Hailstorm</neg> that travels the arena, $keyword-freezing$ $scribes$ that remain within.':
        '$boss$召唤<neg>冰雹风暴</neg>穿越场地，$keyword-freezing$留在其中的$scribes$。',

    '<b>Araxiom</b>\'s cry <neg>slows</neg> $scribes$ for <b>3s</b>.':
        '<b>Araxiom</b>嚎叫<neg>减速</neg>$scribes$<b>3s</b>。',

    '<b>Inkways</b> grant $+|+|100|%| Jump Height$.':
        '<b>墨道</b>给予$+|+|100|%| Jump Height$。',

    'Carrying your <b>Obelisk</b>, which will be placed with your next $ability-secondary$.':
        '携带<b>方尖碑</b>，将在下次$ability-secondary$时放置。',

    'The <b>Atlas</b> continually expels destructive <neg>energy sparks</neg>.':
        '<b>图鉴</b>持续喷发破坏性<neg>能量火花</neg>。',

    'The <b>Atlas</b> continually <neg>slows</neg> visible scribes.':
        '<b>图鉴</b>持续<neg>减速</neg>可见的书记官。',

    'A <pos>Seasonal</pos> effect constantly follows you, <pos>cycling</pos> after each $ability-signature$.':
        '<pos>季节</pos>效果持续跟随你，每次$ability-signature$后<pos>轮换</pos>。',

    'Gain $+|+|15|%|DMG$ for each stack of $keyword-gloom$ on you.':
        '每层$keyword-gloom$获得$+|+|15|%|DMG$。',

    'Gain $+|+|10|%|DMG$ for all abilities per stack.':
        '每层所有技能$+|+|10|%|DMG$。',

    'When $ability-secondary$ hits the environment, it <b>clangs</b> ($+|15|DMG$/s) for <b>5s</b>.':
        '$ability-secondary$命中环境时<b>铿锵</b>($+|15|DMG$/s)持续<b>5s</b>。',

    'While $ability-primary$ is fully charged, you may gallop and trample ($+|15|DMG$) your foes.':
        '$ability-primary$满蓄力时可冲锋践踏($+|15|DMG$)敌人。',

    # Removed: text not found in assets (whitespace difference)

    '$ability-secondary$ deals <pos>increased damage</pos> based on <b>drop height</b>. (Up to $+|+|150|DMG$.)':
        '$ability-secondary$基于<b>落高</b>造成<pos>更多伤害</pos>。(至$+|+|150|DMG$。)',

    '$ability-secondary$ can be charged for <b>1s</b> longer to deal $+|+|250|%|DMG$.':
        '$ability-secondary$可多蓄力<b>1s</b>造成$+|+|250|%|DMG$。',

    '$ability-secondary$ now uses <b>ALL</b> $mana-neutral$, gaining $+|+|60$ <pos>Base Damage</pos> and $+|+|25|%$ <pos>Size</pos> per extra $mana-neutral$ spent.':
        '$ability-secondary$消耗<b>全部</b>$mana-neutral$，每额外$mana-neutral$获得$+|+|60$<pos>基础伤害</pos>和$+|+|25|%$<pos>体积</pos>。',

    'Every <b>4th</b> cast of $ability-secondary$ or the cast after $ability-utility$ will throw <pos>3</pos> Apples.':
        '每第<b>4</b>次$ability-secondary$或$ability-utility$后施放投掷<pos>3</pos>个苹果。',

    'Generating $keyword-plotarmor$ fires off $keyword-twists$.':
        '生成$keyword-plotarmor$时发射$keyword-twists$。',

    'Creating $keyword-plotthreads$ now restores an additional $+|5|BAR$.':
        '创建$keyword-plotthreads$时额外恢复$+|5|BAR$。',

    'You fire 3 additional $keyword-twists$.':
        '额外发射3个$keyword-twists$。',

    'The first $keyword-twist$ from each set is larger and deals $+|+|250|%|DMG$.':
        '每组第一个$keyword-twist$更大且造成$+|+|250|%|DMG$。',

    'Your $ability-movement$ now <pos>resets</pos> the cooldown of all other <b>Scribes\'</b> Movement Abilities.':
        '$ability-movement$<pos>重置</pos>所有其他<b>书记官</b>的位移冷却。',

    'Fully Charged $ability-primary$ lodges into $Torn$ dealing $+|50|DMG$ over <b>2s</b> and causing them to take $+|+|20|%|DMG$ from $ability-primary$.':
        '满蓄力$ability-primary$嵌入$Torn$造成$+|50|DMG$/<b>2s</b>，并使其受$ability-primary$$+|+|20|%|DMG$。',

    '$+|+|25|%|DMG$ for each <b>Bonus Objective</b> and $enemy-elite$.':
        '每完成<b>额外目标</b>和$enemy-elite$$+|+|25|%|DMG$。',

    '$Torn$ you damage take  $+|2|%$ of their <b>current health</b> as damage per second for <b>5s</b>.':
        '被你伤害的$Torn$每秒受到<b>当前生命</b>$+|2|%$伤害持续<b>5s</b>。',

    'Increased $ability-primary$ values by <b>1</b> each stack, resetting when a <pos>20</pos> is rolled.':
        '每层$ability-primary$数值+<b>1</b>，骰出<pos>20</pos>时重置。',

    'Each $ability-primary$ <b>anchor</b> increases the <pos>size</pos> and <pos>damage</pos> of your next $ability-secondary$ by $+|3|%$.':
        '$ability-primary$每个<b>锚点</b>使下次$ability-secondary$<pos>体积</pos>和<pos>伤害</pos>$+|3|%$。',

    '$explosive-orb$ detonations will now <neg>blast</neg> $Scribes$ within line of sight, <neg>regardless</neg> of distance.':
        '$explosive-orb$爆炸会<neg>波及</neg>视线内的$Scribes$，<neg>无视</neg>距离。',

    'Gain $+|+|30|%|DMG$ to foes whose heads are above yours.':
        '对头部高于你的敌人$+|+|30|%|DMG$。',

    '$ability-primary$ has a <b>15%</pos> chance to trigger Dawn\'s <pos> Sunbeam</pos> or Dusk\'s <pos>Sundown</pos>.':
        '$ability-primary$有<b>15%</pos>几率触发黎明<pos>日光</pos>或黄昏<pos>日落</pos>。',

    '<pos>Immune</pos> to the <b>Metaphorest</b>\'s <neg>Gloom</neg> while within the light.':
        '在光明中<pos>免疫</pos><b>隐喻森林</b>的<neg>阴郁</neg>。',

    # Removed: texts not found in assets (whitespace/truncation difference)

    '<b>Quest:</b> Fully spend your mana <b>10</b> times. \n\n<b>Reward:</b> $ability-primary$ gains $+|+|50|%$ $mana-neutral$ generation.':
        '<b>任务:</b>完全消耗法力<b>10</b>次。\n\n<b>奖励:</b>$ability-primary$$mana-neutral$生成$+|+|50|%$。',

    '<b>Quest:</b> Have your $barrier$ broken 15 times.\n\n<b>Reward:</b> Gain $+|75|BAR$.':
        '<b>任务:</b>$barrier$被破坏15次。\n\n<b>奖励:</b>获得$+|75|BAR$。',

    '<b>Reward:</b> Gain $+|+|25|HP$ and $+|+|25|BAR$ every <b>10s</b>.':
        '<b>奖励:</b>每<b>10s</b>获得$+|+|25|HP$和$+|+|25|BAR$。',

    '$ability-signature$ summons a <pos>shield</pos>, making you $keyword-impervious$ and knocking away foes. ($+|25|DMG$)':
        '$ability-signature$召唤<pos>盾</pos>，使你$keyword-impervious$并击退敌人。($+|25|DMG$)',

    # ================================================================
    #  Boss选择界面 — H1 元首阿福扎恩 机制描述
    # ================================================================
    "Don't get overwhelmed with adds!":
        '别被小怪淹没！',

    '<b>General Aversion</b> will play a game of tic tac toe. \nClear Adds so that there are <neg>never 3 in a row.</neg>':
        '<b>元首</b>将进行九宫格连线。\n清理小怪，<neg>绝不能三连。</neg>',

    '<b>General Aversion</b> and the <b>Portals</b> will summon AoEs that \n<neg>detonate</neg> after a brief delay.\n\n<i>AoE means Area of Effect. These attacks will cover an area \ninstead of just focusing on an individual.</i>':
        '<b>元首</b>和<b>传送门</b>会召唤\n短暂延迟后<neg>引爆</neg>的AoE。\n\n<i>AoE即范围攻击。这些攻击会覆盖一片区域\n而非只针对个体。</i>',

    'Watch your feet!':
        '小心脚下！',

    # ================================================================
    #  Boss选择界面 — H2 弗拉希乌斯 机制描述
    # ================================================================
    '<b>The Volorax</b> summons a set of expanding ring AoEs near the \ntank that <neg>detonate</neg> after a delay.\n\n<i>Stand on the edge of one ring</i> and wait for it to detonate. Then <b>immediately move forward</b> to avoid the next one. ':
        '<b>弗拉希乌斯</b>在坦克附近召唤扩散环形AoE，\n延迟后<neg>引爆</neg>。\n\n<i>站在环的边缘</i>等它爆炸。然后<b>立刻向前走</b>躲避下一个。',

    '<b>The Volorax</b> summons two walls that section the arena. Stay in the <b>center</b> of the map!':
        '<b>弗拉希乌斯</b>召唤两面墙分割场地。待在地图<b>中心</b>！',

    # ================================================================
    #  Boss选择界面 — H3 萨哈达尔 机制描述
    # ================================================================
    'Dodge and avoid hitting your team!':
        '躲避，别打到队友！',

    '<b>Sal</b> will occasionally target you to drop a pool.\n\nMove to edge of the arena so the pool is not in your way.':
        '<b>萨尔</b>会不时选你放置水池。\n\n移到场地边缘使水池不挡路。',

    # ================================================================
    #  Boss选择界面 — H4 双龙 机制描述
    # ================================================================
    'The twin red dragons, <b>Prequel</b> and <b>Sequel</b>, have maintained their ability to put on a dazzlingly dangerous two-drake show - despite the corrupting influence of their new management. \n\nWhile a few glimpses of their original act remain, the grand finale would overshadow all. ':
        '这对红色双龙，<b>前传</b>与<b>续集</b>，依然能上演令人目眩的危险双龙秀——尽管受到新管理者的堕落影响。\n\n虽然原有演出的痕迹犹存，但压轴大戏将盖过一切。',

    'Keep your allies safe when you get targeted by abilities!':
        '被技能瞄准时保护好队友！',

    'Soak to shrink the deathball!':
        '分摊以缩小死亡球！',

    'When they fly, stay safe and survive the adds!':
        '飞行阶段，注意安全并清小怪！',

    "<b>Prequel</b> will target you with a breath attack.\n\n<pos>Aim</pos> the breath so it doesn't hit your DPS or Healers!":
        '<b>前传</b>会用吐息攻击你。\n\n<pos>引导</pos>吐息避开输出和治疗！',

    '<b>Prequel</b> will tether you to an energy ball, damaging you over time.\n\n<pos>Get far away</pos> to break the tether!':
        '<b>前传</b>会用能量球连接你，持续造成伤害。\n\n<pos>远离</pos>以拉断连接！',

    "During intermission, if you're targeted with an AoE, move to the edge and avoid hitting your teammates with it.":
        '转场期间如果你被AoE瞄准，移到边缘，别打到队友。',

    # ================================================================
    #  Boss选择界面 — H5 光盲先锋军 机制描述
    # ================================================================
    '<b>The Light-Enthused Fanbase</b> were once normal followers of the light - engaging appropriately with the altruistic tenets of hope, justice, and kindness. The trio, however, have fallen into extreme zealousness. \n\nFew can withstand the over-familiar auras of <b>Vain Verus</b>, <b>Para-social Svenn</b>, and <b>Awkward Andy</b>.':
        '<b>光盲先锋军</b>曾是正常的圣光追随者——恪守希望、正义与仁慈的教义。然而这三人已坠入极端狂热。\n\n鲜有人能抵挡<b>维纳尔</b>、<b>瑟恩</b>和<b>贝莱梅</b>过分亲密的光环。',

    'Dodge, duck, dip, dive, and interrupt':
        '闪、蹲、侧、俯冲并打断',

    # ================================================================
    #  Boss选择界面 — 贝洛朗,奥的子嗣 机制描述
    # ================================================================
    "Kill the boss... a lot":
        '反复击杀BOSS…',

    "<b>Bigol'Hen</b> will summon two different <neg>walls of orbs</neg> that slowly \nmove across the arena.\n\n<b>Move through orbs of the color that matches yours</b> \nto <pos>destroy them.</pos>\n\nLet allies of the opposite color destroy those orbs to get safely through.":
        "<b>贝洛朗</b>会召唤两面不同的<neg>球墙</neg>\n缓慢横穿场地。\n\n<b>穿过与你颜色匹配的球</b>\n来<pos>消灭它们。</pos>\n\n让相反颜色的队友消灭那些球安全通过。",

    "<b>Bigol'Hen</b> will summon Quills that fire at players. \n\nIf targeted, <pos>hide behind</pos> a player of the <i>opposite color</i> to <b>absorb the quill.</b>\n\nIf an ally is targeted by a quill <i>matching your color</i>, <b>stand in its way</b> to <pos>protect your friend.</pos>":
        "<b>贝洛朗</b>会召唤飞羽射向玩家。\n\n被瞄准时，<pos>躲到</pos><i>反色</i>玩家身后<b>吸收飞羽。</b>\n\n若队友被<i>与你同色</i>的飞羽瞄准，<b>挡在前面</b><pos>保护队友。</pos>",

    "<b>Bigol'Hen</b>'s egg will summon conal AoEs. Stand in the cones that <i>match your color</i> to avoid damage.":
        "<b>贝洛朗</b>的蛋会召唤锥形AoE。站在<i>与你颜色匹配</i>的锥形区域中免伤。",

    # ================================================================
    #  Boss选择界面 — 阿拉希奥姆 机制描述
    # ================================================================
    'No longer itsy-bitsy, <b>Araxiom</b> communicates with her fellow Torn via complex, large patterning of decaying plot threads.':
        '不再是小蜘蛛了，<b>阿拉希奥姆</b>通过复杂的大型衰败故事线与撕裂者同伴交流。',

    'Try to apply <pos>Lanterns</pos> generously!':
        '尽量多使用<pos>灯笼</pos>！',

    'Araxiom cannot be harmed while Guardians live!':
        '守护者活着时无法伤害Araxiom！',

    "<b>Araxiom's</b> den is populated by dormant <b>Broodling Eggs</b>. Periodically, <b>Araxiom</b> scatters fresh <b>Broodling Eggs</b> across the arena.":
        "<b>阿拉希奥姆</b>的巢穴中散布休眠<b>虫卵</b>。<b>阿拉希奥姆</b>会定期撒下新<b>虫卵</b>。",

    'An extra Guardian and pair of Bursting Eggs appear.':
        '额外出现一个守护者和一对爆裂虫卵。',

    '<b>Araxiom</b> shrieks, knocking away Scribes and dropping a <pos>Fiery Lantern</pos> from above, capable of waking Eggs <pos>early</pos> and <pos>half health</pos>.':
        '<b>阿拉希奥姆</b>尖啸击退书记官，从上方掉落<pos>火焰灯笼</pos>，可<pos>提前</pos>唤醒虫卵且<pos>半血</pos>。',

    '<b>Araxiom</b>  awakens any remaining Eggs in her den. <b>Broodlings</b> hatched in this way are <neg>Empowered</neg>.':
        '<b>阿拉希奥姆</b>唤醒巢中所有剩余虫卵。如此孵化的<b>幼虫</b>会被<neg>强化</neg>。',

    '<b>Araxiom</b> scours the ground with webbed blades, erupting a line \nof spikes at her target.':
        '<b>阿拉希奥姆</b>用蛛网利刃扫地，向目标\n喷射一排尖刺。',

    'A second pair of angled fissures appears after a short delay.':
        '短暂延迟后出现第二对斜向裂缝。',

    '<b>Araxiom</b> roars, crumbling the ceiling and causing rockfall around Scribes.':
        '<b>Araxiom</b>咆哮，震碎天花板，在书记官周围落石。',

    '<b>Araxiom</b> hungrily leaps toward her target.':
        '<b>阿拉希奥姆</b>饥饿地扑向目标。',

    'Leap also creates a damaging Quake \nwhere Araxiom lands.':
        '飞扑还会在落点\n制造伤害性地震。',

    '<b>Araxiom</b> rampages, continuously raining debris down from above around all Scribes.':
        '<b>阿拉希奥姆</b>暴走，持续从上方在所有书记官周围降下碎石。',

    'Getting hit by debris slows Scribes for 2s.':
        '被碎石击中会减速书记官2s。',

    'Broodling (Bombardier)':
        '幼虫（轰炸者）',

    'A large <b>Broodling</b>, the Bombardier constantly attacks Scribes \nfrom afar.':
        '大型<b>幼虫</b>，轰炸者会持续\n远程攻击书记官。',

    'Bombardiers are <neg>immune</neg> to damage until \nhit by Araxiom\'s Fissure.':
        '轰炸者对伤害<neg>免疫</neg>\n直到被Araxiom裂缝击中。',

    'Broodling (Guardian)':
        '幼虫(守护者)',

    'A medium-sized <b>Broodling</b>, the Guardian continuously <neg>protects</neg> <b>Araxiom</b>.':
        '中型<b>幼虫</b>，守护者持续<neg>保护</neg><b>阿拉希奥姆</b>。',

    'Broodling (Burstling)':
        '幼虫（爆裂者）',

    'A small <b>Broodling</b>, the Burstling swiftly sacrifices itself in a <b>ghastly explosion</b>.':
        '小型<b>幼虫</b>，爆裂者迅速自爆产生<b>恐怖爆炸</b>。',

    'Awaken, Legions!':
        '醒来!军团!',

    'The Dormant Brood':
        '休眠的虫族',

    # ================================================================
    #  Boss语录/风味文字
    # ================================================================
    "He'll eat the whole Salad Bar!":
        '他要吃掉整个沙拉吧！',

    'He sweeps with such Ease!':
        '扫荡如此轻松！',

    'Beware the middle overlaps!':
        '小心中间的重叠！',

    "Stop their Aura Farming...":
        '阻止他们刷光环…',

    'Araxiom, Legionweaver Stirs':
        'Araxiom织网者苏醒',

    'In The Metaphorest':
        '在隐喻森林中',

    'Baffling Darkness Grows...':
        '困惑黑暗蔓延…',

    'Umbral Courtyard':
        '暗影庭院',

    'On Branching Paths':
        '在分岔路上',

    "At The Raving Lord's Invitation":
        '应狂言之主的邀请',

    'The Proverbial Quarry':
        '谚语采石场',

    'The Binding Workshop':
        '装订工坊',

    'With Dark Purpose':
        '黑暗目的',

    'The Machines Rumble':
        '机器隆隆作响',

    'Charting the Throughline':
        '描绘主线',

    'On The Throughline':
        '在主线上',

    'The Facade Strengthens':
        '幻象加固',

    'The Grand Forgery':
        '伟大的赝品',

    'The Splice Lord Refines His Duty':
        '接合之主精炼职责',

    'Chronomalus, Darkest Hour':
        '时空兽，至暗时刻',

    'In the Fullness of Time...':
        '在时间的尽头…',

    'Perplexicon, The Sealed Archive':
        '困惑典籍，封印档案馆',

    'The Sealed Archive':
        '封印档案馆',

    'Under Lock and Key...':
        '重重锁闭…',

    'The Brainstorm, Plotting a Course':
        '脑暴，谋划路线',

    'Weathering the Plot':
        '经受故事考验',

    'Amidst The Brainstorm':
        '脑暴之中',

    'Rocky Shores, Seas of Tumult':
        '岩岸，翻涌之海',

    'Horizon, The Tangent Lord':
        '地平线，离题之主',

    'Last Work of a Studious Pupil':
        '勤学弟子的遗作',

    'Intermission AoE':
        '转场AoE',

    # ================================================================
    #  战斗中提示（带富文本标签）— 二进制补丁
    # ================================================================
    '<pos>Kill the Manifestation</pos> to prevent <neg>extra damage</neg>...':
        '<pos>击杀具象</pos>以避免<neg>额外伤害</neg>…',

    "Get to the <pos>center</pos>...\nIt's <b>intermission</b> time!":
        '去<pos>中心</pos>…\n<b>转场</b>时间！',

    'Standing in an <b>Essence Pool</b> and taking <neg>increasing damage</neg>!':
        '站在<b>精华池</b>中承受<neg>递增伤害</neg>！',

    '<pos>The Tank</pos> will be playing <b>Tic-Tac-Toe</b> with the <neg>Boss.</neg>':
        '<pos>坦克</pos>将和<neg>首领</neg>下<b>九宫格</b>。',

    "If the boss gets <b>3 in a row</b>, it's a <neg>Wipe!</neg>":
        '首领<b>三连线</b>就<neg>灭团！</neg>',

    '<pos>Kill</pos> the <neg>Manifestations</neg> before they reach the <neg>Boss!</neg>':
        '在<neg>具象</neg>到达<neg>首领</neg>前<pos>击杀</pos>它们！',

    'Kill the Dragons <pos>evenly!</pos> They <neg>don\'t</neg> share health.':
        '平衡击杀双龙<pos>！</pos>它们<neg>不</neg>共享血量。',

    '<pos>Stay on your color</pos> and hit the egg - now we just game!':
        '<pos>待在你的颜色</pos>上打蛋——开战！',

    'Destroy the Obelisks':
        '摧毁方尖碑',

    'You can open <b>eggs</b> <pos>prematurely</pos>, sapping them of strength.':
        '你可以<pos>提前</pos>打开<b>蛋</b>，削弱它们。',

    'Destroy the Lava Furnace!':
        '摧毁熔岩炉！',

    '<pos>Kill</pos> the <neg>Adds</neg> before they reach the <neg>Boss!</neg>':
        '在<neg>小怪</neg>到达<neg>首领</neg>前<pos>击杀</pos>！',

    '<neg>DON\'T SOAK!</neg> \n\n<b>On Heroic</b> you have to <i>alternate soaks</i>.':
        '<neg>别分摊！</neg>\n\n<b>英雄难度</b>需要<i>交替分摊</i>。',

    '<pos>SOAK</pos> with the <sprite name="sym_bar">Tank to get phased!':
        '<pos>分摊</pos><sprite name="sym_bar">坦克的圈进入内场！',

    '<pos>Destroy the Orb</pos> before it <neg>reaches</neg> the boss!':
        '<pos>摧毁宝珠</pos>在它<neg>到达</neg>首领之前！',

    '<pos>SOAK</pos> on <sprite name="sym_bar">Tank to clear a space!':
        '<pos>分摊</pos><sprite name="sym_bar">坦克位清格子！',

    '<pos>Soak</pos> the <neg>Hammer</neg>, then <pos>dodge</pos> the spinning projectiles!':
        '<pos>分摊</pos><neg>圣锤</neg>，然后<pos>躲</pos>旋转飞盾！',

    '<neg>Run away</neg> to <pos>break</pos> the tether!':
        '<neg>跑开</neg>来<pos>拉断</pos>连接！',

    'Kill the <b>egg</b> before the bird <neg>respawns</neg>!':
        '在鸟<neg>重生</neg>前击杀<b>蛋</b>！',

    '<b>Get to</b> the <pos>Safe Spot!</pos>':
        '<b>去</b><pos>安全区！</pos>',

    'Stay out of the <neg>Charge Path</neg>!':
        '远离<neg>冲锋路径</neg>！',

    'Play Tic-Tac-Toe with the boss!\nHere is some more info!':
        '和首领下九宫格！\n更多详细信息！',

    'Break the <neg>Shield</neg> before the cast completes!':
        '在施法完成前打破<neg>护盾</neg>！',

    'An <neg>Orb</neg> will fire soon! Get ready to <pos>SOAK</pos> it.':
        '<neg>宝珠</neg>即将发射！准备<pos>分摊</pos>。',

    'Get to the edge of the safe zone to avoid allies!':
        '去安全区边缘以避开队友！',

    # ================================================================
    #  Horizon 机制描述（离题之主）
    # ================================================================
    '<b>Horizon</b> launches 3 <neg>concoctions</neg> toward his target, and another at a random Scribe, which bounce once before exploding.':
        '<b>地平线</b>向目标发射3个<neg>药剂</neg>，另一个射向随机书记官，弹跳一次后爆炸。',

    'Explosions release 3 <neg>Dice</neg> in random directions.':
        '爆炸向随机方向释放3个<neg>骰子</neg>。',

    '<b>Horizon</b> buckles the ground, unfolding a <neg>randomly-arcing</neg> \nline toward the targeted $scribe$, which erupts after <b>0.66s</b>.':
        '<b>地平线</b>震裂地面，向目标$scribe$展开<neg>随机弧形</neg>\n裂纹，<b>0.66s</b>后喷发。',

    'An additional crease line is released.':
        '释放额外一条裂纹。',

    'Semiotic Deconstruction':
        '符号解构',

    '<b>Horizon</b> will periodically activate <b>eyes</b> around him, bringing \n<neg>new destructive power</neg> to bear.':
        '<b>地平线</b>会定期激活周围的<b>眼</b>，\n释放<neg>新的破坏力</neg>。',

    'The <b>Bubbling Eye</b> will periodically throw <neg>Concoctions</neg> at \nrandom $scribe$.':
        '<b>沸腾之眼</b>会定期向\n随机$scribe$投掷<neg>药剂</neg>。',

    'The <b>Shifting Eye</b> will periodically form <neg>Creases</neg> at random $scribes$.':
        '<b>移形之眼</b>会定期在随机$scribes$处形成<neg>裂纹</neg>。',

    'The <b>Lucky Eye</b> will periodically roll <neg>Clatters</neg> at random points in the arena, which will release <b>Dice</b> based on the rolled value.':
        '<b>幸运之眼</b>会定期向场地随机点投<neg>骰响</neg>，根据骰值释放<b>骰子</b>。',

    'The <b>Discoidal Eye</b> will periodically discharge <b>energetic \npulsations</b> that <neg>expand</neg> through the entire arena.':
        '<b>碟形之眼</b>会定期释放<b>能量\n脉冲</b>，<neg>扩散</neg>至整个场地。',

    'The ring expands faster, then <neg>returns</neg>.':
        '环扩散更快，然后<neg>回收</neg>。',

    'The <b>Celestial Eye</b> will occasionally warp in new dark <neg>Eclipses</neg> \nto rain chaos over the arena.':
        '<b>天界之眼</b>会不时召唤黑暗<neg>日蚀</neg>\n在场地中降下混沌。',

    # ================================================================
    #  额外游戏文本
    # ================================================================
    '$ability-movement$ leaves behind an $keyword-pool$.':
        '$ability-movement$留下$keyword-pool$。',

    '$ability-secondary$ leaves behind an <pos>Imprint</pos> that grants $Scribes$ $+|1$ $mana-neutral$ and reduces their $ability-utility$ cooldowns by $+|1|s$ each second for <b>4s</b>.':
        '$ability-secondary$留下<pos>印记</pos>，每秒给予$Scribes$$+|1$$mana-neutral$并减少$ability-utility$冷却$+|1|s$，持续<b>4s</b>。',

    '$ability-movement$ leaves behind an area that launches $Scribes$ into the air.':
        '$ability-movement$留下一个将$Scribes$弹射到空中的区域。',

    'Tower and Underground Area of Effect attacks <neg>deal increasing damage</neg>.':
        '塔和地下范围攻击<neg>造成递增伤害</neg>。',

    "<b>Styxen</b>'s Shield Bash leaves behind a <neg>molten trail.</neg>":
        '<b>斯提克森</b>的盾击留下<neg>熔岩轨迹。</neg>',

    "<b>Myriad's Swoop</b> leaves behind <neg>flaming feathers</neg>.":
        '<b>万象俯冲</b>留下<neg>燃烧羽毛</neg>。',

    'Overgrown Towers whose Chains hold up the <b>The Taking Tree</b>.':
        '高耸之塔，锁链撑起<b>攫取之树</b>。',

    'Swipe leaves behind a fiery patch.':
        '横扫留下一片火焰。',

    '<b>Crombul</b> becomes overwhelmed with fury, gaining enhanced Damage, Size, and Speed.':
        '<b>克隆布尔</b>被狂怒吞没，获得增强的伤害、体型和速度。',

    '<b>Lingering Blast</b> travels faster, <neg>seeks</neg> Scribes, and leaves behind a slowing area when expiring.':
        '<b>余爆</b>飞行更快，<neg>追踪</neg>书记官，消失时留下减速区域。',

    'After $ability-utility$ expires, your $keyword-inkling$ leaves behind a healing area for <b>3s</b>. ($+|30|HP$)':
        '$ability-utility$结束后，$keyword-inkling$留下治疗区域<b>3s</b>。($+|30|HP$)',

    # ================================================================
    #  Horizon 额外技能描述
    # ================================================================
    '<b>Horizon</b> <neg>tears away</neg> the $mana-neutral$ of all $scribes$. The $mana-neutral$ can be <pos>collected</pos> from the ground.':
        '<b>地平线</b><neg>夺走</neg>所有$scribes$的$mana-neutral$。$mana-neutral$可从地面<pos>拾取</pos>。',

    'After a short delay, <b>Horizon</b> <neg>annihilates</neg> all $scribes$ within \na narrow view in front of him.':
        '短暂延迟后，<b>地平线</b><neg>湮灭</neg>前方\n狭窄视野内的所有$scribes$。',

    'The field of view is increased by $-|10| degrees$.':
        '视野范围增加$-|10| degrees$。',

    '<b>Horizon</b> charges up a massive, destructive beam that <neg>follows</neg> his target for <b>1.5s</b>.':
        '<b>地平线</b>蓄力一道巨大破坏光束，<neg>跟踪</neg>目标<b>1.5s</b>。',

    'Planets releas a <neg>destructive beam</neg> straight down.':
        '行星向下释放<neg>毁灭光束</neg>。',
}
