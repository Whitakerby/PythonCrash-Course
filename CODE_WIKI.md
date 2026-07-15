# PythonCrash-Course Code Wiki

> 本文档是对 `PythonCrash-Course` 仓库的完整结构化说明，涵盖项目整体架构、各模块职责、关键类与函数说明、依赖关系以及运行方式等关键信息。
>
> 仓库本质上是《Python 编程：从入门到实践》（Python Crash Course）一书的配套学习项目，包含三个循序渐进的部分：基础语法练习（demo01）、Pygame 入门练习（demo02）、以及一个完整的「外星人入侵」游戏项目（alien_invasion）。

---

## 目录

- [一、项目概览](#一项目概览)
- [二、项目整体架构](#二项目整体架构)
- [三、目录结构](#三目录结构)
- [四、模块详解](#四模块详解)
  - [4.1 demo01 —— Python 基础语法练习](#41-demo01--python-基础语法练习)
  - [4.2 demo02 —— Pygame 入门练习](#42-demo02--pygame-入门练习)
  - [4.3 alien_invasion —— 外星人入侵游戏（核心项目）](#43-alien_invasion--外星人入侵游戏核心项目)
- [五、关键类与函数说明](#五关键类与函数说明)
- [六、依赖关系](#六依赖关系)
- [七、项目运行方式](#七项目运行方式)
- [八、游戏核心流程图](#八游戏核心流程图)
- [九、设计说明与扩展点](#九设计说明与扩展点)

---

## 一、项目概览

| 项目属性 | 说明 |
|---------|------|
| 项目名称 | PythonCrash-Course |
| 项目类型 | Python 学习实践仓库 |
| 主要语言 | Python 3 |
| 核心依赖 | pygame、tkinter（标准库） |
| 学习教材 | 《Python 编程：从入门到实践》 |
| 项目目标 | 通过三个递进式子项目，掌握 Python 基础语法、Pygame 游戏开发、面向对象设计 |

仓库共包含三个子目录，分别对应学习的不同阶段：

1. **demo01**：Python 基础语法练习（变量、字符串、数值运算等）。
2. **demo02**：第 12 章习题，涵盖 Pygame 窗口、按键检测、星空生成、以及一个使用 tkinter 实现的侧面射击小游戏。
3. **alien_invasion**：完整的「外星人入侵」游戏项目，是整个仓库的核心成果。

---

## 二、项目整体架构

```
PythonCrash-Course/
│
├── demo01/                    # 基础语法练习（脚本式，无类封装）
│   ├── hellopython.py
│   ├── name.py
│   ├── full_name.py
│   ├── simple_message.py
│   ├── simple_messages.py
│   ├── 2.3单元小测.py
│   ├── add blank.py
│   ├── delete blank.py
│   ├── apostrophe2.3.5.py
│   ├── 加减乘除.py
│   └── 浮点数.py
│
├── demo02/                    # Pygame 入门练习（含 tkinter 版小游戏）
│   ├── settings.py            # 设置类
│   ├── ship.py                # 飞船类（支持四向移动）
│   ├── star.py                # 星星精灵类
│   ├── stars_game.py          # 随机星空主程序
│   ├── 练习12-1-2.py          # 蓝色背景窗口
│   ├── 练习12-4.py            # 四向移动飞船
│   ├── 练习12-5.py            # 按键检测
│   ├── 练习12-6.py            # tkinter 侧面射击游戏
│   └── images/
│       └── ship.bmp
│
├── alien_invasion/            # 核心项目：外星人入侵游戏
│   ├── alien_invasion.py      # 主程序（AlienInvasion 控制类）
│   ├── settings.py            # Settings 设置类
│   ├── ship.py                # Ship 飞船类
│   ├── alien.py               # Alien 外星人类
│   ├── bullet.py              # Bullet 子弹类
│   ├── button.py              # Button 按钮类
│   ├── game_stats.py          # GameStats 统计信息类
│   ├── scoreboard.py          # Scoreboard 记分牌类
│   └── images/
│       ├── ship.bmp
│       └── alien.bmp
│
├── .gitignore                 # 忽略 __pycache__、.idea、venv 等
└── README.md                  # 仓库说明（仅标题）
```

整体架构特点：

- **递进式学习结构**：从无封装的脚本 → 单文件 Pygame 程序 → 多类协作的完整游戏项目。
- **面向对象设计**：`alien_invasion` 项目采用经典的「主控类 + 资源类」模式，每个游戏实体（飞船、外星人、子弹、按钮、记分牌）均独立成类，由主控类 `AlienInvasion` 统一调度。
- **pygame.sprite 协作**：游戏中的可动实体均继承自 `pygame.sprite.Sprite`，通过 `pygame.sprite.Group` 进行统一管理与碰撞检测。

---

## 三、目录结构

### 3.1 顶层目录

| 路径 | 类型 | 说明 |
|------|------|------|
| `demo01/` | 目录 | 第 2 章基础语法练习脚本集合 |
| `demo02/` | 目录 | 第 12 章 Pygame 入门练习 |
| `alien_invasion/` | 目录 | 完整的「外星人入侵」游戏项目 |
| `.gitignore` | 文件 | Git 忽略规则 |
| `README.md` | 文件 | 仓库标题说明 |

### 3.2 资源文件

| 路径 | 说明 |
|------|------|
| `alien_invasion/images/ship.bmp` | 外星人入侵项目的飞船位图 |
| `alien_invasion/images/alien.bmp` | 外星人位图 |
| `demo02/images/ship.bmp` | demo02 练习使用的飞船位图 |

> 注意：各游戏脚本通过相对路径 `images/ship.bmp` 加载图像，因此必须在对应的子目录下运行脚本，否则会出现文件找不到的错误。

---

## 四、模块详解

### 4.1 demo01 —— Python 基础语法练习

本目录是第 2 章「变量和简单数据类型」的练习脚本集合，全部以脚本形式编写，无类封装，直接通过 `print()` 输出结果。主要练习主题如下：

| 文件 | 练习主题 |
|------|---------|
| [hellopython.py](file:///workspace/demo01/hellopython.py) | 变量赋值与打印输出 |
| [name.py](file:///workspace/demo01/name.py) | 字符串方法 `title()`、`upper()`、`lower()` |
| [full_name.py](file:///workspace/demo01/full_name.py) | f-string 格式化字符串 |
| [simple_message.py](file:///workspace/demo01/simple_message.py) | 变量赋值与多重赋值 |
| [simple_messages.py](file:///workspace/demo01/simple_messages.py) | 变量重新赋值、字符串字面量 |
| [2.3单元小测.py](file:///workspace/demo01/2.3单元小测.py) | 综合练习：名言拼接、空白字符处理、大小写转换 |
| [add blank.py](file:///workspace/demo01/add%20blank.py) | 制表符 `\t` 与换行符 `\n` |
| [delete blank.py](file:///workspace/demo01/delete%20blank.py) | `rstrip()`、`lstrip()`、`strip()` 剔除空白 |
| [apostrophe2.3.5.py](file:///workspace/demo01/apostrophe2.3.5.py) | 字符串中单引号的使用 |
| [加减乘除.py](file:///workspace/demo01/加减乘除.py) | 整数四则运算 |
| [浮点数.py](file:///workspace/demo01/浮点数.py) | 浮点数运算、大数字下划线分隔、多重赋值 |

### 4.2 demo02 —— Pygame 入门练习

本目录是第 12 章「武装飞船」相关习题，包含几个可独立运行的练习以及一个主程序 `stars_game.py`。

#### 4.2.1 共享模块

- [settings.py](file:///workspace/demo02/settings.py)：`Settings` 类，仅包含屏幕尺寸、背景色和飞船速度的基础配置（精简版，与 alien_invasion 中的版本不同）。
- [ship.py](file:///workspace/demo02/ship.py)：`Ship` 类，支持上下左右四向移动的飞船（比 alien_invasion 版多了 `moving_up`/`moving_down` 标志与 y 坐标更新）。
- [star.py](file:///workspace/demo02/star.py)：`Star` 精灵类，复用 `images/ship.bmp` 作为星星图像，仅用于星空练习。

#### 4.2.2 练习脚本

| 文件 | 练习内容 |
|------|---------|
| [练习12-1-2.py](file:///workspace/demo02/练习12-1-2.py) | `blue` 类：创建蓝色背景窗口并绘制飞船 |
| [练习12-4.py](file:///workspace/demo02/练习12-4.py) | `AlienInvasion` 类（简化版）：支持方向键四向移动飞船 |
| [练习12-5.py](file:///workspace/demo02/练习12-5.py) | 按键检测：打印 `KEYDOWN` 事件的 `event.key` 值 |
| [练习12-6.py](file:///workspace/demo02/练习12-6.py) | `SideShooter` 类：基于 **tkinter** 的侧面射击小游戏 |
| [stars_game.py](file:///workspace/demo02/stars_game.py) | `StarsGame` 类：随机偏移的星空网格生成主程序 |

#### 4.2.3 tkinter 侧面射击游戏（练习12-6）

这是一个独立的小游戏，使用 Python 标准库 `tkinter` 而非 pygame 实现：

- 玩家用 ↑/↓ 或 W/S 控制飞船上下移动，按空格发射子弹。
- 子弹从飞船右侧水平射出，飞出屏幕后自动销毁。
- 通过 `root.after(16, self.game_loop)` 实现约 60 FPS 的游戏循环。

### 4.3 alien_invasion —— 外星人入侵游戏（核心项目）

这是仓库的核心项目，实现了《Python 编程：从入门到实践》第 12~14 章的完整游戏。游戏采用经典的「主控类统一调度 + 实体类各司其职」架构。

#### 4.3.1 模块组成

| 文件 | 类 | 职责 |
|------|----|------|
| [alien_invasion.py](file:///workspace/alien_invasion/alien_invasion.py) | `AlienInvasion` | 主控类：管理游戏资源、主循环、事件响应、碰撞检测、流程控制 |
| [settings.py](file:///workspace/alien_invasion/settings.py) | `Settings` | 存储所有游戏配置参数（屏幕、飞船、子弹、外星人、节奏加速） |
| [ship.py](file:///workspace/alien_invasion/ship.py) | `Ship` | 玩家飞船：左右移动、边界限制、绘制、居中重置 |
| [alien.py](file:///workspace/alien_invasion/alien.py) | `Alien` | 单个外星人：水平移动、边缘检测 |
| [bullet.py](file:///workspace/alien_invasion/bullet.py) | `Bullet` | 子弹：向上移动、绘制 |
| [button.py](file:///workspace/alien_invasion/button.py) | `Button` | Play 按钮：渲染文本并居中绘制 |
| [game_stats.py](file:///workspace/alien_invasion/game_stats.py) | `GameStats` | 游戏统计：剩余飞船数、得分、等级、最高分、活动状态 |
| [scoreboard.py](file:///workspace/alien_invasion/scoreboard.py) | `Scoreboard` | 记分牌：渲染当前分、最高分、等级、剩余飞船图像 |

#### 4.3.2 游戏玩法

- 点击 **Play** 按钮或游戏开始后，玩家使用 **←/→** 键控制飞船左右移动，按 **空格** 发射子弹。
- 子弹击中外星人后双方消失并得分；消灭全部外星人后进入下一关，难度提升。
- 外星人触底或撞到飞船时，玩家损失一艘飞船；飞船耗尽则游戏结束。
- 按 **Q** 键随时退出游戏。

---

## 五、关键类与函数说明

### 5.1 AlienInvasion（主控类）

定义于 [alien_invasion.py](file:///workspace/alien_invasion/alien_invasion.py)，是整个游戏的中枢。

| 方法 | 说明 |
|------|------|
| `__init__(self)` | 初始化 pygame、创建设置对象、全屏窗口、统计对象、记分牌、飞船、子弹与外星人编组、Play 按钮，并调用 `_create_fleet()` 生成初始外星人群 |
| `run_game(self)` | 游戏主循环：依次调用 `_check_events()`，在游戏活动状态下更新飞船/子弹/外星人，最后调用 `_update_screen()` 刷新画面 |
| `_create_fleet(self)` | 计算屏幕可容纳的外星人行列数，双层循环生成外星人群 |
| `_create_alien(self, alien_number, row_number)` | 在指定行列坐标创建单个外星人并加入编组 |
| `_check_fleet_edges(self)` | 检测是否有外星人触达屏幕边缘 |
| `_check_fleet_direction(self)` | 整群外星人下移并反转水平移动方向 |
| `_check_events(self)` | 监听键盘/鼠标事件并分发处理 |
| `_check_play_button(self, mouse_pos)` | 响应点击 Play 按钮：重置设置、隐藏鼠标、重置统计、重建外星人群、飞船居中 |
| `_check_keydown_events(self, event)` | 响应按下方向键（移动）、空格（开火）、Q（退出） |
| `_check_keyup_events(self, event)` | 响应松开方向键，停止移动 |
| `_fire_bullet(self)` | 在子弹数未超上限时创建新子弹并加入编组 |
| `_update_bullets(self)` | 更新子弹位置、删除飞出屏幕的子弹、检测子弹与外星人碰撞 |
| `_check_bullet_alien_collisions(self)` | 处理碰撞：得分、检查最高分、外星人全灭则清空子弹、新建外星人群、提速并升级 |
| `_update_aliens(self)` | 检测边缘后更新外星人位置，检测与飞船碰撞及触底 |
| `_check_aliens_bottom(self)` | 检测是否有外星人到达屏幕底端 |
| `_ship_hit(self)` | 飞船被撞处理：剩余飞船 -1、清空外星人与子弹、重建外星人群、飞船居中、暂停 0.5 秒；飞船耗尽则结束游戏并恢复鼠标 |
| `_update_screen(self)` | 绘制背景、飞船、子弹、外星人、记分牌；非活动状态下绘制 Play 按钮并翻转显示 |

### 5.2 Settings（设置类）

定义于 [settings.py](file:///workspace/alien_invasion/settings.py)，集中管理所有可调参数。

| 成员 | 说明 |
|------|------|
| `screen_width / screen_height` | 屏幕宽高（默认 1200×800，全屏时被实际尺寸覆盖） |
| `bg_color` | 背景色 `(230, 230, 230)` |
| `bullet_speed / bullet_width / bullet_height / bullet_color / bullets_allowed` | 子弹速度、尺寸、颜色、同时存在上限（3） |
| `ship_speed / ship_limit` | 飞船速度、初始飞船数（3） |
| `alien_speed / fleet_drop_speed / fleet_direction` | 外星人速度、下移速度、移动方向（1 右 / -1 左） |
| `speedup_scale / score_scale` | 升级时的提速倍率（1.1）、分数提升倍率（1.5） |
| `initialize_dynamic_settings()` | 重置随游戏进程变化的动态参数（速度、方向、积分 `alien_points=50`） |
| `increase_speed()` | 通关后按倍率提升飞船/子弹/外星人速度并提高外星人积分 |

### 5.3 Ship（飞船类）

定义于 [ship.py](file:///workspace/alien_invasion/ship.py)，继承 `pygame.sprite.Sprite`。

| 方法 | 说明 |
|------|------|
| `__init__(self, ai_game)` | 加载飞船图像、放置于屏幕底部中央、初始化移动标志 |
| `update(self)` | 根据 `moving_right`/`moving_left` 标志更新 x 坐标（带屏幕边界限制） |
| `blitme(self)` | 在当前位置绘制飞船 |
| `center_ship(self)` | 将飞船重新居中于屏幕底部（用于复活与重开） |

### 5.4 Alien（外星人类）

定义于 [alien.py](file:///workspace/alien_invasion/alien.py)，继承 `pygame.sprite.Sprite`。

| 方法 | 说明 |
|------|------|
| `__init__(self, ai_game)` | 加载外星人图像、初始位置置于屏幕左上角附近、存储精确 x 坐标 |
| `check_edges(self)` | 检测外星人是否触及屏幕左右边缘，返回布尔值 |
| `update(self)` | 按 `alien_speed * fleet_direction` 水平移动外星人 |

### 5.5 Bullet（子弹类）

定义于 [bullet.py](file:///workspace/alien_invasion/bullet.py)，继承 `pygame.sprite.Sprite`。

| 方法 | 说明 |
|------|------|
| `__init__(self, ai_game)` | 在飞船顶部创建子弹矩形，存储小数 y 坐标 |
| `update(self)` | 子弹向上移动（y 递减） |
| `draw_bullet(self)` | 在屏幕上绘制子弹矩形 |

### 5.6 Button（按钮类）

定义于 [button.py](file:///workspace/alien_invasion/button.py)，用于游戏开始前的 Play 按钮。

| 方法 | 说明 |
|------|------|
| `__init__(self, ai_game, msg)` | 设置按钮尺寸（200×50）、绿色背景、白色文字，并居中于屏幕 |
| `_prep_msg(self, msg)` | 将文本渲染为图像并居中于按钮 |
| `draw_button(self)` | 绘制按钮背景与文本 |

### 5.7 GameStats（统计信息类）

定义于 [game_stats.py](file:///workspace/alien_invasion/game_stats.py)，跟踪游戏运行时状态。

| 成员 | 说明 |
|------|------|
| `high_score` | 历史最高分（跨局保留） |
| `game_active` | 游戏是否处于活动状态（初始为 False，点击 Play 后为 True） |
| `reset_stats()` | 重置运行期统计：`ships_left`（飞船数）、`score`（得分）、`level`（等级，初始 1） |

### 5.8 Scoreboard（记分牌类）

定义于 [scoreboard.py](file:///workspace/alien_invasion/scoreboard.py)，负责将统计信息渲染为屏幕图像。

| 方法 | 说明 |
|------|------|
| `prep_score()` | 将当前得分渲染为图像，置于屏幕右上角 |
| `prep_high_score()` | 将最高分渲染为图像，置于屏幕顶部中央 |
| `prep_level()` | 将等级渲染为图像，置于得分下方 |
| `prep_ships()` | 用飞船图像编组表示剩余飞船数，置于屏幕左上角 |
| `check_high_score()` | 比较当前分与最高分，更新最高分并重新渲染 |
| `show_score()` | 在屏幕上绘制得分、最高分、等级和剩余飞船 |

---

## 六、依赖关系

### 6.1 外部依赖

| 依赖 | 用途 | 适用模块 |
|------|------|---------|
| `pygame` | 游戏开发库：窗口、事件、绘图、精灵、碰撞 | demo02、alien_invasion |
| `tkinter` | GUI 标准库（Python 自带） | demo02/练习12-6.py |

### 6.2 标准库依赖

| 依赖 | 用途 |
|------|------|
| `sys` | 调用 `sys.exit()` 退出游戏 |
| `time.sleep` | 飞船被撞后暂停 0.5 秒 |
| `random` | 星空练习中生成随机偏移 |

### 6.3 模块内依赖关系（alien_invasion）

```
alien_invasion.py
 ├── settings.Settings
 ├── game_stats.GameStats
 ├── ship.Ship
 ├── bullet.Bullet
 ├── alien.Alien
 ├── button.Button
 └── scoreboard.Scoreboard
        └── ship.Ship   （用于显示剩余飞船图像）
```

依赖注入方式：所有实体类在构造时接收主控类 `AlienInvasion` 实例 `ai_game`（或 `self`），通过它访问共享的 `screen`、`settings`、`stats` 等资源。这是一种简化的「上下文对象」依赖注入模式。

### 6.4 安装依赖

```bash
# pygame 需要单独安装
pip install pygame

# tkinter 通常随 Python 安装，若缺失可在系统层面安装：
# Debian/Ubuntu: sudo apt-get install python3-tk
```

---

## 七、项目运行方式

### 7.1 环境要求

- Python 3.x
- pygame（运行 demo02 与 alien_invasion）
- tkinter（仅运行 demo02/练习12-6.py）

### 7.2 运行外星人入侵游戏（核心项目）

由于脚本通过相对路径 `images/ship.bmp` 加载图像，**必须在 `alien_invasion` 目录下执行**：

```bash
cd alien_invasion
python alien_invasion.py
```

游戏将以**全屏模式**启动（代码中使用了 `pygame.FULLSCREEN`）。如需窗口模式，可取消注释 [alien_invasion.py](file:///workspace/alien_invasion/alien_invasion.py#L25-L26) 中的窗口设置代码。

### 7.3 运行 demo02 练习

```bash
cd demo02

# 随机星空主程序
python stars_game.py

# 蓝色背景窗口
python 练习12-1-2.py

# 四向移动飞船
python 练习12-4.py

# 按键检测
python 练习12-5.py

# tkinter 侧面射击游戏（无需 pygame）
python 练习12-6.py
```

### 7.4 运行 demo01 基础练习

```bash
cd demo01
python hellopython.py
# 其他脚本同理，直接运行即可查看输出
```

### 7.5 操作说明（alien_invasion）

| 按键 | 功能 |
|------|------|
| ← / → | 控制飞船左右移动 |
| 空格 | 发射子弹（最多同时 3 发） |
| Q | 退出游戏 |
| 鼠标点击 Play | 开始/重新开始游戏 |

---

## 八、游戏核心流程图

### 8.1 主循环流程

```
run_game()
   │
   ▼
┌─────────────────┐
│  _check_events  │ ◄── 处理键盘/鼠标事件
└────────┬────────┘
         │
         ▼
    game_active?
    ┌────┴────┐
   是         否
    │         │
    ▼         │
┌─────────────┤
│ ship.update │
│_update_bullets│
│_update_aliens │
└─────┬───────┘
      │         │
      ▼         ▼
┌─────────────────┐
│ _update_screen  │ ◄── 绘制并刷新画面
└────────┬────────┘
         │
         └──► 回到循环顶部
```

### 8.2 碰撞与升级流程

```
_update_bullets
   │
   ▼
子弹 vs 外星人碰撞 (groupcollide)
   │
   ├─ 命中 → 得分增加 → 更新记分牌 → 检查最高分
   │
   └─ 外星人全灭?
         ├─ 是 → 清空子弹 → 新建外星人群 → increase_speed → 等级 +1
         └─ 否 → 继续
```

### 8.3 飞船损失流程

```
外星人撞飞船 / 外星人触底
        │
        ▼
   _ship_hit()
        │
   ships_left > 0 ?
   ├─ 是 → ships_left-1 → 清空外星人/子弹 → 重建 → 飞船居中 → 暂停0.5s
   └─ 否 → game_active=False → 显示鼠标 → 显示Play按钮
```

---

## 九、设计说明与扩展点

### 9.1 架构设计特点

1. **主控类集中调度**：`AlienInvasion` 持有所有资源对象的引用，统一驱动更新与渲染，避免了实体类之间的直接耦合。
2. **上下文对象注入**：实体类通过构造参数接收主控类实例，按需访问 `screen`、`settings`、`stats`，减少全局变量。
3. **精灵与编组协作**：飞船、外星人、子弹均继承 `Sprite`，使用 `Group` 统一管理，便于批量更新与碰撞检测（`groupcollide`、`spritecollideany`）。
4. **设置与状态分离**：`Settings` 管理静态/动态参数，`GameStats` 管理运行时状态，职责清晰。
5. **动态难度**：通过 `increase_speed()` 在通关后按倍率提升速度与积分，实现递进式挑战。

### 9.2 已知的小问题

- [ship.py](file:///workspace/alien_invasion/ship.py#L35) 的 `update()` 方法中，移动逻辑里同时存在 `self.rect.x += 1` 和基于 `self.x` 的更新，存在冗余的整数位移代码（不影响功能但不够简洁）。
- [scoreboard.py](file:///workspace/alien_invasion/scoreboard.py#L28-L30) 的 `prep_score()` 中先对分数做了 `round(..., -1)` 取整，随后又被 `str(self.stats.score)` 覆盖，四舍五入逻辑实际未生效。
- [settings.py](file:///workspace/alien_invasion/settings.py#L47) 的 `increase_speed()` 中包含 `print(self.alien_points)` 调试输出。

### 9.3 可扩展方向

- 增加音效与背景音乐。
- 引入不同类型的外星人（不同外观、分值、移动模式）。
- 持久化最高分到文件，避免关闭游戏后丢失。
- 增加暂停功能（如按 P 键暂停）。
- 重构为包结构，添加 `__init__.py` 与统一入口，解决相对路径依赖问题。

---

> 本 Code Wiki 基于仓库当前快照生成，如代码后续变更，请同步更新本文档。
