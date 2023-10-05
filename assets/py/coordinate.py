# 캐릭터 좌표
# 0번째는 default 캐릭터
character_data = [
    {
        "character": "licat",
        "character_obj": None,
        "x": 0,
        "y": 0,
        "directions": 0,  # 0(동, 오른쪽), 1(북), 2(서, 왼쪽), 3(남)
        "items": {},
    }
]

# 맵 전역에 있는 아이템 데이터
# (x, y): {item: 'beeper', count: 1}
item_data = {}

# 맵 크기
map_data = {"height": 5, "width": 5}


# 한 변 길이
map_size = 100
border_size = 1

running_speed = 1

# 맵에 있는 벽 데이터
wall_data = {"world": {}}
blockingWallType = ["wall", "fence"]  # 이동 불가한 벽 종류
wall_type = "wall"  # 현재 선택되어 있는 벽 종류

story_wall = {
    # 1번 스토리
    1:{"map_width":5, "map_height":5, "wall":{(0, 0.5): '', (0, 1.5): '', (0, 2.5): '', (0, 3.5): '', (0.5, 0): 'fence', (0.5, 1): '', (0.5, 2): '', (0.5, 3): '', (0.5, 4): '', (1.0, 0.5): '', (1.0, 1.5): '', (1.0, 2.5): '', (1.0, 3.5): '', (1.5, 0): '', (1.5, 1): '', (1.5, 2): 'wall', (1.5, 3): '', (1.5, 4): '', (2.0, 0.5): 'wall', (2.0, 1.5): 'wall', (2.0, 2.5): 'door', (2.0, 3.5): 'door', (2.5, 0): '', (2.5, 1): 'wall', (2.5, 2): '', (2.5, 3): 'door', (2.5, 4): '', (3.0, 0.5): '', (3.0, 1.5): '', (3.0, 2.5): '', (3.0, 3.5): '', (3.5, 0): '', (3.5, 1): '', (3.5, 2): '', (3.5, 3): '', (3.5, 4): '', (4.0, 0.5): '', (4.0, 1.5): '', (4.0, 2.5): '', (4.0, 3.5): ''}, "item":{(2, 2): {'item': 'diamond', 'count': 1}}},
    # 2번 스토리
    2:{"map_width":5, "map_height":5, "wall":{(0, 0.5): '', (0, 1.5): '', (0, 2.5): '', (0, 3.5): '', (0.5, 0): 'fence', (0.5, 1): '', (0.5, 2): '', (0.5, 3): '', (0.5, 4): '', (1.0, 0.5): '', (1.0, 1.5): '', (1.0, 2.5): '', (1.0, 3.5): '', (1.5, 0): '', (1.5, 1): '', (1.5, 2): 'wall', (1.5, 3): '', (1.5, 4): '', (2.0, 0.5): 'wall', (2.0, 1.5): 'wall', (2.0, 2.5): 'door', (2.0, 3.5): 'door', (2.5, 0): '', (2.5, 1): 'wall', (2.5, 2): '', (2.5, 3): 'door', (2.5, 4): '', (3.0, 0.5): '', (3.0, 1.5): '', (3.0, 2.5): '', (3.0, 3.5): '', (3.5, 0): '', (3.5, 1): '', (3.5, 2): '', (3.5, 3): '', (3.5, 4): '', (4.0, 0.5): '', (4.0, 1.5): '', (4.0, 2.5): '', (4.0, 3.5): ''}, "item":{(2, 2): {'item': 'diamond', 'count': 1}}},
    }