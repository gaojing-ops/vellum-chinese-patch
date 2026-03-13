# -*- coding: utf-8 -*-
"""
Vellum Study Hall - Asset Bundle 文本补丁工具
直接修改 resources.assets 中嵌入的英文文本为中文。

用法: python patch_assets.py
会自动在 Steam 默认路径查找游戏，也可以手动输入路径。
"""
import os
import sys
import shutil
import struct

# ============================================================
#  翻译字典：原文 → 中文
#  注意：中文 UTF-8 字节数必须 ≤ 原文字节数，否则跳过
# ============================================================
TRANSLATIONS = {
    # ---- H1: 元首阿福扎恩 (General Aversion) ----
    '<b>General Aversion</b>, a ruthless fan of board games, deploys his ultimate stratagem: tic-tac-toe. \n\nPerhaps the greatest strategic mind of the null forces, only the best heroes can put an end to the General\'s pursuit of total victory.   ':
        '<b>\u5143\u9996\u963f\u798f\u624e\u6069</b>\uff0c\u4e00\u4e2a\u6b8b\u9177\u7684\u68cb\u76d8\u6e38\u620f\u7231\u597d\u8005\uff0c\u90e8\u7f72\u4e86\u4ed6\u7684\u7ec8\u6781\u6218\u672f\uff1a\u4e5d\u5bab\u683c\u8fde\u7ebf\u3002\n\n\u4f5c\u4e3a\u865a\u7a7a\u52bf\u529b\u4e2d\u6700\u5f3a\u7684\u6218\u7565\u5929\u624d\uff0c\u53ea\u6709\u6700\u4f18\u79c0\u7684\u82f1\u96c4\u624d\u80fd\u7ec8\u7ed3\u5143\u9996\u5bf9\u5168\u9762\u80dc\u5229\u7684\u8ffd\u6c42\u3002',

    'Tanks drive the tic-tac-toe positions':
        '\u5766\u514b\u4e3b\u5bfc\u4e5d\u5bab\u683c\u7ad9\u4f4d',

    'During Tic Tac Toe, Follow the <b>Tank</b> and help <pos>Soak</pos> the attack \nto clear a Tic Tac Toe space.\n\n<i>Soak means to be in the area of an attack, usually to spread the attack\'s effect across multiple players.</i>':
        '\u4e5d\u5bab\u683c\u9636\u6bb5\uff0c\u8ddf\u968f<b>\u5766\u514b</b>\u5e76\u5e2e\u5fd9<pos>\u5206\u644a</pos>\u653b\u51fb\n\u6765\u6e05\u9664\u4e00\u4e2a\u4e5d\u5bab\u683c\u683c\u5b50\u3002\n\n<i>\u5206\u644a\uff1a\u7ad9\u5728\u653b\u51fb\u8303\u56f4\u5185\uff0c\u5c06\u653b\u51fb\u6548\u679c\u5206\u644a\u7ed9\u591a\u540d\u73a9\u5bb6\u3002</i>',

    '<b>General Aversion</b> will summon <neg>additional creatures</neg> to fight you. Clear these Adds quickly. (your <pos>\'Q\' ability</pos> is great at this.)\n\n<i>Adds are additional enemies that will perform a variety of attacks.</i> ':
        '<b>\u5143\u9996</b>\u4f1a\u53ec\u5524<neg>\u989d\u5916\u7684\u5c0f\u602a</neg>\u6765\u653b\u51fb\u4f60\u3002\u5feb\u901f\u6e05\u7406\u8fd9\u4e9b\u5c0f\u602a\u3002\uff08<pos>Q\u6280\u80fd</pos>\u975e\u5e38\u9002\u5408\uff09\n\n<i>\u5c0f\u602a\u662f\u989d\u5916\u7684\u654c\u4eba\uff0c\u4f1a\u8fdb\u884c\u5404\u79cd\u653b\u51fb\u3002</i>',

    # ---- H2: 弗拉希乌斯 (The Volorax) ----
    'From the depths of the Nullnado, <b>The Volorax</b> crawled its way to any and every nearby food source. \n\nDespite its insatiable hunger, the Volorax has taken great strides to ensure its food supply is sourced in an ethical manner.':
        '\u4ece\u865a\u7a7a\u98ce\u66b4\u7684\u6df1\u5904\uff0c<b>\u5f17\u62c9\u5e0c\u4e4c\u65af</b>\u722c\u5411\u4e00\u5207\u80fd\u627e\u5230\u7684\u98df\u7269\u6765\u6e90\u3002\n\n\u5c3d\u7ba1\u5b83\u6709\u7740\u65e0\u5c3d\u7684\u9965\u997f\uff0c\u5f17\u62c9\u5e0c\u4e4c\u65af\u4ecd\u5728\u52aa\u529b\u786e\u4fdd\u5176\u98df\u7269\u6765\u6e90\u5408\u4e4e\u9053\u5fb7\u3002',

    'Kill adds to break walls or get zapped':
        '\u6740\u5c0f\u602a\u7834\u58c1\uff0c\u5426\u5219\u88ab\u79d2',

    '<neg>Bursters</neg> will fixate you and chase you. They will explode on death.\n\n<b>Lead them to a wall</b> and kill two near each other to bring the wall down!':
        '<neg>\u7206\u722c\u866b</neg>\u4f1a\u9501\u5b9a\u5e76\u8ffd\u51fb\u4f60\u3002\u5b83\u4eec\u6b7b\u4ea1\u65f6\u4f1a\u7206\u70b8\u3002\n\n<b>\u5c06\u5b83\u4eec\u5f15\u5230\u5899\u8fb9</b>\uff0c\u5728\u5899\u65c1\u8fde\u6740\u4e24\u53ea\u5373\u53ef\u7834\u58c1\uff01',

    '<b>The Volorax</b> will fire a <neg>deadly beam</neg> and sweep most of the \narena with it. Get to the <pos>safe spot!</pos> \n\n<i>If you didn\'t bring down the walls, you won\'t be able to \nget there.</i>':
        '<b>\u5f17\u62c9\u5e0c\u4e4c\u65af</b>\u4f1a\u53d1\u5c04<neg>\u81f4\u547d\u5c04\u7ebf</neg>\u626b\u5c04\u5927\u90e8\u5206\n\u573a\u5730\u3002\u8d76\u5feb\u53bb<pos>\u5b89\u5168\u533a\uff01</pos>\n\n<i>\u5982\u679c\u4f60\u6ca1\u6709\u7834\u574f\u6c34\u6676\u58c1\uff0c\u5c31\u65e0\u6cd5\u5230\u8fbe\u5b89\u5168\u533a\u3002</i>',

    # ---- H3: 陨落之王萨哈达尔 (Former Hegemonarch Sal) ----
    'Having made risky political moves from the shadows, <b>Former Hegemonarch Sal</b> now sits captive among his own machinations. \n\nOvercome by boredom, Sal bides his time... waiting for the perfect opportunity to re-write his story. ':
        '\u5728\u6697\u4e2d\u8fdb\u884c\u4e86\u5192\u9669\u7684\u653f\u6cbb\u64cd\u4f5c\u540e\uff0c<b>\u9668\u843d\u4e4b\u738b\u8428\u54c8\u8fbe\u5c14</b>\u5982\u4eca\u88ab\u56f0\u5728\u81ea\u5df1\u7684\u9634\u8c0b\u4e4b\u4e2d\u3002\n\n\u88ab\u65e0\u804a\u6240\u56f0\uff0c\u8428\u5c14\u9759\u5f85\u65f6\u673a\u2026\u7b49\u5f85\u91cd\u5199\u81ea\u5df1\u6545\u4e8b\u7684\u5b8c\u7f8e\u65f6\u523b\u3002',

    'Stop him from eating orbs!':
        '\u522b\u8ba9\u4ed6\u5403\u865a\u7a7a\u7403!',

    '<b>Sal</b> will summon <neg>orbs</neg> that need to be killed before they reach him.\n\nKilling an <neg>orb</neg> deals damage and causes you to take more \ndamage from other <neg>orbs</neg> for a short time. \n<b>Wait for that debuff to fall off!</b>':
        '<b>\u8428\u5c14</b>\u4f1a\u53ec\u5524<neg>\u865a\u7a7a\u7403</neg>\uff0c\u5fc5\u987b\u5728\u5230\u8fbe\u4ed6\u4e4b\u524d\u51fb\u6740\u3002\n\n\u51fb\u6740<neg>\u7403</neg>\u4f1a\u9020\u6210\u4f24\u5bb3\uff0c\u5e76\u4f7f\u4f60\u77ed\u65f6\u95f4\u5185\u53d7\u5230\n\u5176\u4ed6<neg>\u7403</neg>\u7684\u66f4\u591a\u4f24\u5bb3\u3002\n<b>\u7b49\u51cf\u76ca\u6d88\u5931\u518d\u7ee7\u7eed\uff01</b>',

    '<b>Sal</b> will summon an add that casts for a short time. If the cast goes off, it leaves a pool behind.\n\n<pos>Interrupt</pos> the spell by moving through the add.':
        '<b>\u8428\u5c14</b>\u4f1a\u53ec\u5524\u4e00\u4e2a\u65bd\u6cd5\u7684\u5c0f\u602a\u3002\u5982\u679c\u8bfb\u6761\u5b8c\u6210\u4f1a\u7559\u4e0b\u706b\u6d77\u3002\n\n\u7a7f\u8fc7\u5c0f\u602a\u6765<pos>\u6253\u65ad</pos>\u65bd\u6cd5\u3002',

    '<b>Sal</b> will target you with a debuff that will spawn 5 lines of spikes\n after it expires.\n\nMove so that these spikes won\'t hit your teammates.':
        '<b>\u8428\u5c14</b>\u4f1a\u7ed9\u4f60\u65bd\u52a0\u51cf\u76ca\uff0c\u5230\u671f\u540e\u4ea7\u751f5\u6761\u5c16\u5cf0\u7ebf\u3002\n\n\u79fb\u52a8\u8ba9\u5c16\u5cf0\u4e0d\u8981\u6253\u5230\u961f\u53cb\u3002',

    '<b>Sal</b> will summon rotating beams that deal massive damage. \nCircle around him to dodge these. He will drop a pool at the end.\n\n<b>Sal</b> takes <pos>increased damage</pos> during this.':
        '<b>\u8428\u5c14</b>\u4f1a\u53ec\u5524\u65cb\u8f6c\u5c04\u7ebf\u9020\u6210\u5de8\u5927\u4f24\u5bb3\u3002\n\u7ed5\u7740\u4ed6\u8f6c\u6765\u8eb2\u907f\u3002\u7ed3\u675f\u65f6\u4f1a\u7559\u4e0b\u706b\u6d77\u3002\n\n\u6b64\u671f\u95f4<b>\u8428\u5c14</b>\u53d7\u5230<pos>\u989d\u5916\u4f24\u5bb3</pos>\u3002',

    # ---- H4: 双龙 ----
    'At <b>50% Health</b>, <b>Prequel and Sequel</b> will fly up and create a circle of fire. \n\nGet to the center of the arena and kill the add that spawns.':
        '<b>50%\u8840\u91cf</b>\u65f6\uff0c<b>\u5a01\u5384\u9ad8\u5c14\u548c\u827e\u4f50\u62c9\u514b</b>\u4f1a\u98de\u8d77\u5e76\u5236\u9020\u706b\u5708\u3002\n\n\u8d76\u5feb\u53bb\u573a\u5730\u4e2d\u5fc3\uff0c\u51fb\u6740\u5237\u65b0\u7684\u5c0f\u602a\u3002',

    '<b>Sequel</b> will target all players with an AoE that summons <neg>Orbs</neg> after the AoE detonates.\n\n<pos>Loosely stack</pos> so the AoEs don\'t overlap, but close enough that you can AoE the orbs afterwards.':
        '<b>\u827e\u4f50\u62c9\u514b</b>\u4f1a\u5bf9\u6240\u6709\u73a9\u5bb6\u65bd\u653eAOE\uff0c\u5f15\u7206\u540e\u53ec\u5524<neg>\u865a\u7a7a\u7403</neg>\u3002\n\n<pos>\u677e\u6563\u96c6\u5408</pos>\u907f\u514dAOE\u91cd\u53e0\uff0c\u4f46\u8981\u8db3\u591f\u8fd1\u4ee5\u4fbfAOE\u6740\u7403\u3002',

    '<b>Sequel</b> fires a slow moving orb at the Tank. \nThe Orb will leave behind a pool when it hits a wall or another pool.\n\n<pos>Soak</pos> the orb before it hits a wall to make the pool smaller.':
        '<b>\u827e\u4f50\u62c9\u514b</b>\u5411\u5766\u514b\u53d1\u5c04\u6162\u901f\u7403\u3002\n\u7403\u78b0\u5899\u6216\u5176\u4ed6\u6c60\u5b50\u65f6\u7559\u4e0b\u706b\u6d77\u3002\n\n\u5728\u7403\u78b0\u5899\u524d<pos>\u5206\u644a</pos>\u5b83\u53ef\u7f29\u5c0f\u706b\u6d77\u3002',

    # ---- H5: 光盲先锋军 ----
    '<b>Awkward Andy</b> will toss a <neg>shield</neg> at you that deals area damage. \n\nDon\'t stand near anyone else!':
        '<b>\u8d1d\u83b1\u6885\u5c06\u519b</b>\u4f1a\u5411\u4f60\u6295\u63b7<neg>\u76fe\u724c</neg>\uff0c\u9020\u6210\u8303\u56f4\u4f24\u5bb3\u3002\n\n\u4e0d\u8981\u7ad9\u5728\u522b\u4eba\u65c1\u8fb9\uff01',

    'Each member of <b>The Light-Enthused Fanbase</b> will create \nan Aura around them. <pos>Get out of it.</pos>\n\nOnce they\'re done, they\'ll leave behind a <neg>damaging pool.</neg>':
        '<b>\u5149\u76f2\u5148\u950b\u519b</b>\u7684\u6bcf\u4e2a\u6210\u5458\u4f1a\u5728\u8eab\u8fb9\u521b\u5efa\n\u5149\u73af\u3002<pos>\u8d76\u7d27\u79bb\u5f00\u3002</pos>\n\n\u5149\u73af\u7ed3\u675f\u540e\u4f1a\u7559\u4e0b<neg>\u6c38\u4e45\u706b\u6d77\u3002</neg>',

    '2 members of <b>The Light-Enthused Fanbase</b> will <neg>shield themselves</neg> when you pop cooldowns. \n\n<pos>Damage</pos> the one that\'s unshielded.':
        '<b>\u5149\u76f2\u5148\u950b\u519b</b>\u7684 2 \u540d\u6210\u5458\u4f1a\u5728\u4f60\u5f00\u7206\u53d1\u65f6<neg>\u5f00\u76fe</neg>\u3002\n\n<pos>\u653b\u51fb</pos>\u6ca1\u6709\u62a4\u76fe\u7684\u90a3\u4e2a\u3002',

    'Kill them evenly':
        '\u5e73\u8861\u51fb\u6740',

    '<b>Awkward Andy</b> will drop a <neg>hammer</neg> on an <pos>ally</pos>, help <pos>soak</pos> it to \nreduce damage and then dodge <neg>hammers.</neg>':
        '<b>\u8d1d\u83b1\u6885\u5c06\u519b</b>\u4f1a\u5411<pos>\u961f\u53cb</pos>\u7835\u4e0b<neg>\u5723\u9524</neg>\uff0c\u5e2e\u5fd9<pos>\u5206\u644a</pos>\n\u51cf\u4f24\uff0c\u7136\u540e\u8eb2\u907f<neg>\u65cb\u8f6c\u98de\u9524\u3002</neg>',

    '<b>Para-social Svenn</b> will <neg>charge forward</neg> and damage anyone in his path. \n\nAfter charging, he will begin casting. <pos>Break his shield</pos> to interrupt him.':
        '<b>\u6218\u4e89\u7267\u5e08\u745f\u6069</b>\u4f1a<neg>\u5411\u524d\u51b2\u950b</neg>\uff0c\u4f24\u5bb3\u8def\u5f84\u4e0a\u7684\u6240\u6709\u4eba\u3002\n\n\u51b2\u950b\u540e\u5979\u4f1a\u5f00\u59cb\u65bd\u6cd5\u3002<pos>\u6253\u7834\u62a4\u76fe</pos>\u6765\u6253\u65ad\u5979\u3002',

    # ---- 坎比纳隆 (Combineron) ----
    'Feasting on the celestial cookie jar, <b>Combineron, the Unkempt Fraud</b> has grown so large in its painful assimilation of mass. \n\nUnchecked growth and a continuous hunger make the Gleamdrift a woeful place. Danger and sorrow await.':
        '\u8d2a\u5a6a\u5730\u541e\u566c\u5929\u5802\u7684\u997c\u5e72\u7f50\uff0c<b>\u574e\u6bd4\u7eb3\u9686\uff0c\u84ec\u5934\u9a97\u5b50</b>\u5728\u75db\u82e6\u7684\u8d28\u91cf\u540c\u5316\u4e2d\u53d8\u5f97\u65e0\u6bd4\u5de8\u5927\u3002\n\n\u5931\u63a7\u7684\u751f\u957f\u548c\u6c38\u4e0d\u505c\u6b47\u7684\u9965\u997f\u8ba9\u5fae\u5149\u6f02\u6d41\u6210\u4e3a\u4e86\u60b2\u60e8\u4e4b\u5730\u3002',

    'Soak to realm-hop, then kill kill kill!':
        '\u5206\u644a\u5207\u6362\u4f4d\u9762\uff0c\u7136\u540e\u72e0\u72e0\u6740\uff01',

    'Dodge breaths and focus adds!':
        '\u8eb2\u5410\u606f,\u96c6\u706b\u5c0f\u602a!',

    '<b>Combineron</b> will target the tank with an AoE.\n\nHelp <pos>Soak</pos> it <b>Every Other</b> time. This will send you to a different \n\'realm\'.':
        '<b>\u574e\u6bd4\u7eb3\u9686</b>\u4f1a\u5bf9\u5766\u514b\u65bd\u653e\u8303\u56f4\u6280\u80fd\u3002\n\n<b>\u6bcf\u9694\u4e00\u6b21</b><pos>\u5206\u644a</pos>\u5b83\u3002\u8fd9\u4f1a\u5c06\u4f60\u9001\u5230\u53e6\u4e00\u4e2a\n\u201c\u4f4d\u9762\u201d\u3002',

    '<b>Combineron</b> will summon adds in the other realm. \nKill them quickly if you see them.\n\nOnce killed in the other realm, they\'ll respawn in the main realm and run to the boss. Kill them before they reach <b>Combineron</b>!':
        '<b>\u574e\u6bd4\u7eb3\u9686</b>\u4f1a\u5728\u53e6\u4e00\u4e2a\u4f4d\u9762\u53ec\u5524\u5c0f\u602a\u3002\n\u770b\u5230\u5c31\u5feb\u901f\u51fb\u6740\u3002\n\n\u5728\u53e6\u4e00\u4f4d\u9762\u88ab\u6740\u540e\uff0c\u5b83\u4eec\u4f1a\u5728\u4e3b\u4f4d\u9762\u91cd\u751f\u5e76\u8dd1\u5411BOSS\u3002\u5728\u5b83\u4eec\u8d70\u5230<b>\u574e\u6bd4\u7eb3\u9686</b>\u8eab\u8fb9\u524d\u51fb\u6740\uff01',

    '<b>Combineron</b> will fly through the arena, breathing fire in a line. Dodge the fire!':
        '<b>\u574e\u6bd4\u7eb3\u9686</b>\u4f1a\u98de\u8fc7\u573a\u5730\uff0c\u6cbf\u76f4\u7ebf\u55b7\u706b\u3002\u8eb2\u907f\u706b\u7130\uff01',

    '<b>Combineron</b>\'s adds will spawn pools when they die in the other \nrealm and <b>Combineron</b>\'s breath will leave behind pools.':
        '<b>\u574e\u6bd4\u7eb3\u9686</b>\u7684\u5c0f\u602a\u5728\u53e6\u4e00\u4f4d\u9762\u6b7b\u4ea1\u65f6\u4f1a\u751f\u6210\u6c60\u5b50\uff0c\n<b>\u574e\u6bd4\u7eb3\u9686</b>\u7684\u5410\u606f\u4e5f\u4f1a\u7559\u4e0b\u6c60\u5b50\u3002',

    '<b>Combineron</b> will target you with an AoE ring. Bring that ring \nto the <b>Pools</b> to clear them when the AoE ring finishes.':
        '<b>\u574e\u6bd4\u7eb3\u9686</b>\u4f1a\u7528\u8303\u56f4\u5708\u70b9\u540d\u4f60\u3002\u628a\u5708\u5e26\u5230\n<b>\u6c60\u5b50</b>\u65c1\uff0c\u5708\u7ed3\u675f\u65f6\u53ef\u4ee5\u6e05\u9664\u6c60\u5b50\u3002',

    # ---- 大母鸡比格 (Bigol'Hen) ----
    '<b>Bigol\'Hen</b> will make you either <pos>Light or Void</pos>. \n\nYou will need to interact with all other mechanics based on this.':
        '<b>\u5927\u6bcd\u9e21\u6bd4\u683c</b>\u4f1a\u8ba9\u4f60\u53d8\u6210<pos>\u5723\u5149\u6216\u865a\u7a7a</pos>\u5c5e\u6027\u3002\n\n\u4f60\u9700\u8981\u6839\u636e\u8fd9\u4e2a\u5c5e\u6027\u6765\u5e94\u5bf9\u6240\u6709\u5176\u4ed6\u673a\u5236\u3002',

    '<b>Bigol\'Hen</b> will summon adds that will dive bomb players. \nKilling them summons an <neg>egg</neg>. <pos>Kill that egg quickly</pos> or the add will respawn.':
        '<b>\u5927\u6bcd\u9e21\u6bd4\u683c</b>\u4f1a\u53ec\u5524\u4fef\u51b2\u73a9\u5bb6\u7684\u5c0f\u602a\u3002\n\u51fb\u6740\u540e\u4f1a\u751f\u6210<neg>\u86cb</neg>\u3002<pos>\u5feb\u901f\u6253\u6389\u86cb</pos>\uff0c\u5426\u5219\u5c0f\u602a\u4f1a\u91cd\u751f\u3002',

    'When reaching 0 health, <b>Bigol\'Hen</b> will turn into an egg. \nDamage this egg to fully kill <b>Bigol\'Hen</b>. After some time,\n <b>Bigol\'Hen</b> will respawn, but the Egg\'s health will persist \nto the next Egg Phase.':
        '<b>\u5927\u6bcd\u9e21\u6bd4\u683c</b>\u8840\u91cf\u5f52\u96f6\u65f6\u4f1a\u53d8\u6210\u86cb\u3002\n\u6253\u7834\u86cb\u624d\u80fd\u5f7b\u5e95\u51fb\u6740<b>\u5927\u6bcd\u9e21\u6bd4\u683c</b>\u3002\u8fc7\u6bb5\u65f6\u95f4\u540e\n<b>\u5927\u6bcd\u9e21\u6bd4\u683c</b>\u4f1a\u91cd\u751f\uff0c\u4f46\u86cb\u7684\u8840\u91cf\u4f1a\u4fdd\u7559\n\u5230\u4e0b\u4e00\u6b21\u86cb\u9636\u6bb5\u3002',

    'The <b>Adds</b> dive bomb will target players with an AoE. Help <pos>soak</pos> these AoEs if you\'re the <b>matching color.</b>\n\nIf you\'re targeted, move to a player that matches the AoE\'s color to get their help soaking.':
        '<b>\u5c0f\u602a</b>\u4fef\u51b2\u70b8\u5f39\u4f1a\u5bf9\u73a9\u5bb6\u65bd\u653eAOE\u3002\u5982\u679c\u4f60\u662f<b>\u5339\u914d\u989c\u8272</b>\u5c31\u5e2e\u5fd9<pos>\u5206\u644a</pos>\u3002\n\n\u5982\u679c\u4f60\u88ab\u70b9\u540d\uff0c\u79fb\u5230\u989c\u8272\u5339\u914d\u7684\u73a9\u5bb6\u65c1\u8fb9\u8ba9\u4ed6\u4eec\u5e2e\u4f60\u5206\u644a\u3002',

    'Deal with your matching color mechanics!  ':
        '\u5904\u7406\u4e0e\u4f60\u989c\u8272\u5339\u914d\u7684\u673a\u5236\uff01',

    'Stay aware of your color!':
        '\u6ce8\u610f\u4f60\u7684\u989c\u8272\uff01',

    # ---- 阿拉希奥姆 (Araxiom) ----
    'No longer itsy-bitsy, <b>Araxiom</b> communicates with her fellow Torn via complex, large patterning of decaying plot threads.':
        '<b>\u963f\u62c9\u5e0c\u5965\u59c6</b>\u5df2\u4e0d\u518d\u5fae\u5c0f\uff0c\u5979\u901a\u8fc7\u8150\u673d\u60c5\u8282\u7ebf\u7684\u590d\u6742\u5927\u578b\u56fe\u6848\u4e0e\u540c\u4f34\u7684\u6495\u88c2\u8005\u4ea4\u6d41\u3002',

    'Bombardiers are <neg>immune</neg> to damage until \nhit by Araxiom\'s Fissure.':
        '\u8f70\u70b8\u866b<neg>\u514d\u4f24</neg>,\u88ab\u88c2\u7f1d\u547d\u4e2d\n\u540e\u624d\u53ef\u653b\u51fb\u3002',

    'A medium-sized <b>Broodling</b>, the Guardian continuously <neg>protects</neg> <b>Araxiom</b>.':
        '\u4e2d\u578b<b>\u5e7c\u866b</b>\uff0c\u5b88\u62a4\u8005\u4f1a\u6301\u7eed<neg>\u4fdd\u62a4</neg><b>\u963f\u62c9\u5e0c\u5965\u59c6</b>\u3002',

}


def find_game_path():
    """尝试自动查找游戏路径"""
    common_paths = [
        r"D:\SteamLibrary\steamapps\common\Vellum Study Hall",
        r"C:\Program Files (x86)\Steam\steamapps\common\Vellum Study Hall",
        r"C:\Program Files\Steam\steamapps\common\Vellum Study Hall",
        r"E:\SteamLibrary\steamapps\common\Vellum Study Hall",
    ]
    for p in common_paths:
        assets = os.path.join(p, "Vellum Study Hall_Data", "resources.assets")
        if os.path.isfile(assets):
            return p
    return None


def patch_assets(game_path):
    assets_path = os.path.join(game_path, "Vellum Study Hall_Data", "resources.assets")
    backup_path = assets_path + ".bak"

    if not os.path.isfile(assets_path):
        print(f"[ERROR] 找不到资源文件: {assets_path}")
        return False

    # 创建备份
    if not os.path.isfile(backup_path):
        print(f"[备份] 创建备份: {backup_path}")
        shutil.copy2(assets_path, backup_path)
    else:
        print(f"[备份] 备份已存在，跳过")

    # 读取整个文件
    print(f"[读取] 加载 resources.assets ({os.path.getsize(assets_path) / 1024 / 1024:.1f} MB)...")
    with open(assets_path, "rb") as f:
        data = bytearray(f.read())

    patched = 0
    skipped_size = 0
    skipped_notfound = 0

    for eng_text, chn_text in TRANSLATIONS.items():
        eng_bytes = eng_text.encode("utf-8")
        chn_bytes = chn_text.encode("utf-8")

        if len(chn_bytes) > len(eng_bytes):
            print(f"  [跳过] 中文({len(chn_bytes)}B) > 英文({len(eng_bytes)}B): {eng_text[:40]}...")
            skipped_size += 1
            continue

        # 在文件中查找英文文本
        pos = data.find(eng_bytes)
        if pos == -1:
            print(f"  [未找到] {eng_text[:50]}...")
            skipped_notfound += 1
            continue

        # 不修改长度前缀！修改会导致 Unity 反序列化偏移错位，游戏黑屏。
        # 保持原始长度，用空字节填充剩余部分。
        padding_len = len(eng_bytes) - len(chn_bytes)
        replacement = chn_bytes + b"\x00" * padding_len
        data[pos:pos + len(eng_bytes)] = replacement

        patched += 1
        short_eng = eng_text[:40].replace("\n", "\\n")
        short_chn = chn_text[:30].replace("\n", "\\n")
        print(f"  [OK] {short_eng}... => {short_chn}...")

    # 写回文件
    print(f"\n[写入] 保存修改后的 resources.assets...")
    with open(assets_path, "wb") as f:
        f.write(data)

    print(f"\n========== 完成 ==========")
    print(f"  成功替换: {patched} 条")
    print(f"  长度超限: {skipped_size} 条")
    print(f"  未找到:   {skipped_notfound} 条")
    print(f"  备份位置: {backup_path}")
    return True


def restore_backup(game_path):
    assets_path = os.path.join(game_path, "Vellum Study Hall_Data", "resources.assets")
    backup_path = assets_path + ".bak"
    if os.path.isfile(backup_path):
        shutil.copy2(backup_path, assets_path)
        print(f"[还原] 已从备份还原: {assets_path}")
        return True
    else:
        print(f"[ERROR] 找不到备份文件: {backup_path}")
        return False


def main():
    print("=" * 50)
    print("  Vellum Study Hall Asset 文本补丁工具 v1.0")
    print("=" * 50)

    game_path = find_game_path()
    if game_path:
        print(f"\n[自动检测] 游戏路径: {game_path}")
    else:
        game_path = input("\n请输入游戏安装路径: ").strip().strip('"')

    if not os.path.isdir(game_path):
        print(f"[ERROR] 路径不存在: {game_path}")
        input("按回车退出...")
        return

    print("\n请选择操作:")
    print("  1. 应用中文补丁")
    print("  2. 还原原始文件")
    choice = input("\n输入选项 (1/2): ").strip()

    if choice == "1":
        print()
        patch_assets(game_path)
    elif choice == "2":
        restore_backup(game_path)
    else:
        print("无效选项")

    input("\n按回车退出...")


if __name__ == "__main__":
    main()
