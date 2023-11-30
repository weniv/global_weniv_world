import js

from pyodide.ffi import create_once_callable
from coordinate import character_data, map_data,running_speed, mob_data, item_data, _available_items, error_message
from item import Item

command_count = 0 # 명령어 줄 수

def get_running_speed():
    # spped value
    a = 0.00020004
    b = -0.0408163393
    c = 2.5411162993

    # speed slide bar
    slider = js.document.getElementById("speed-range")
    slider_output = js.document.getElementById("speed-text")
    slider_output.innerHTML = slider.value
    running_speed = a * int(slider.value)**2 + b * int(slider.value) + c
    return running_speed

def mission_end():
    """
    미션 클리어
    """
    global command_count
    command_count = 0

def mission_start():
    """
    미션 시작
    """
    global command_count
    command_count = 0

def print(*texts, type="normal"):
    """
    html 문서 내 출력
    """
    def main():
        output = js.document.getElementById("output")
        result = ""
        for text in texts:
            result += str(text)

        if output:
            paragraph = js.document.createElement("p")
            paragraph.innerText = result
            paragraph.classList.add("output-item")
            if type == "error":
                paragraph.setAttribute("data-error", "true")
            output.appendChild(paragraph)
        else:
            js.console.log(result)
    running_speed = get_running_speed()
    wait_time = command_count*1000*running_speed
    js.setTimeout(create_once_callable(lambda: (main())), wait_time)

def say(text="", character=None, speech_time=5000):
    """
    charecter의 말풍선에 출력
    """
    def main():
        if character != None:
            character.say(text)
        else:
            if character_data[0]["character_obj"] != None:
                character_data[0]["character_obj"].say(text, speech_time)
            else:
                print("캐릭터가 없습니다.")

    running_speed = get_running_speed()
    wait_time = command_count*1000*running_speed
    js.setTimeout(create_once_callable(lambda: (main())), wait_time)
    
def directions(character=None):
    """
    character의 방향을 right, left, top, bottom으로 반환
    """
    global command_count
    command_count += 1
    
    d = {0: "right", 1: "top", 2: "left", 3: "bottom"}
    if character != None:
        return d[character._get_character_data("directions")]
    else:
        if character_data[0]["character_obj"] != None:
            return d[character_data[0]["directions"]]
        else:
            print("캐릭터가 없습니다.")
            return None


def item(character=None):
    """
    character가 가지고 있는 아이템을 보여주는 함수
    """
    if character != None:
        return character._get_character_data("items")
    else:
        if character_data[0]["character_obj"] != None:
            return character_data[0]["items"]
        else:
            print("캐릭터가 없습니다.")
            return None
    wait_time = 1000 * command_count

def set_item(x, y, name, count=1, description={}, character=None):
    if not (isinstance(x, int) and isinstance(y, int)):
        alert_error('ArgumentsError')
        print("error.ArgumentsError: arguments is wrong." , type="error")
        raise Exception('ArgumentsError')

    if not (0 <= x < map_data["height"] and 0 <= y < map_data["width"]):
        alert_error('OutOfWorld')
        print("error.OutOfWorld: out of world", type="error")
        raise Exception('OutOfWorld')
    
    if name not in _available_items:
        alert_error('InvalidItem')
        print("error.InvalidItem: Invalid item", type="error")
        raise Exception('InvalidItem')

    item = Item(x, y, name, count, description)
    item.draw()


def move(character=None):
    global command_count
    command_count += 1
    if character != None:
        character.move()
    else:
        if character_data[0]["character_obj"] != None:
            character_data[0]["character_obj"].move()
        else:
            print("캐릭터가 없습니다.")


def turn_left(character=None):
    global command_count
    command_count += 1

    if character != None:
        character.turn_left()
    else:
        if character_data[0]["character_obj"] != None:
            character_data[0]["character_obj"].turn_left()
        else:
            print("캐릭터가 없습니다.")


def pick(character=None):
    global command_count
    command_count += 1
    
    if character != None:
        character.pick()
    else:
        if character_data[0]["character_obj"] != None:
            character_data[0]["character_obj"].pick()
        else:
            print("캐릭터가 없습니다.")


def put(item_name, character=None):
    global command_count
    command_count += 1
    
    if character != None:
        character.put(item_name)
    else:
        if character_data[0]["character_obj"] != None:
            character_data[0]["character_obj"].put(item_name)
        else:
            print("캐릭터가 없습니다.")


def repeat(count, f):
    if isinstance(count, int) == True:
        for i in range(0, count):
            f()
    elif isinstance(f, int) == True:
        for i in range(0, f):
            count()


def front_is_clear(character=None):
    '''
    캐릭터의 앞이 비어있는지 확인하는 함수
    동기로 실행되면 이 함수가 먼저 실행되어 앞에 벽을 체크하지 못합니다.
    '''
    if character != None:
        print(f"character not none")
        return character.front_is_clear()
    else:
        if character_data[0]["character_obj"] != None:
            return character_data[0]["character_obj"].front_is_clear()
        else:
            print("캐릭터가 없습니다.")

def left_is_clear(character=None):
    '''
    캐릭터의 왼쪽이 비어있는지 확인하는 함수
    동기로 실행되면 이 함수가 먼저 실행되어 앞에 벽을 체크하지 못합니다.
    '''
    if character != None:
        return character.left_is_clear()
    else:
        if character_data[0]["character_obj"] != None:
            return character_data[0]["character_obj"].left_is_clear()
        else:
            print("캐릭터가 없습니다.")

def right_is_clear(character=None):
    '''
    캐릭터의 오른쪽이 비어있는지 확인하는 함수
    동기로 실행되면 이 함수가 먼저 실행되어 앞에 벽을 체크하지 못합니다.
    '''
    if character != None:
        return character.right_is_clear()
    else:
        if character_data[0]["character_obj"] != None:
            return character_data[0]["character_obj"].right_is_clear()
        else:
            print("캐릭터가 없습니다.")
  
def back_is_clear(character=None):
    '''
    캐릭터의 뒤가 비어있는지 확인하는 함수
    동기로 실행되면 이 함수가 먼저 실행되어 앞에 벽을 체크하지 못합니다.
    '''
    if character != None:
        return character.back_is_clear()
    else:
        if character_data[0]["character_obj"] != None:
            return character_data[0]["character_obj"].back_is_clear()
        else:
            print("캐릭터가 없습니다.")
  
def attack(character=None):
    global command_count
    command_count += 1
    
    if character != None:
        character.attack()
    else:
        if character_data[0]["character_obj"] != None:
            character_data[0]["character_obj"].attack()
        else:
            print("캐릭터가 없습니다.")


def open_door(character=None):
    
    global command_count
    command_count += 1
    
    if character != None:
        character.open_door()
    else:
        if character_data[0]["character_obj"] != None:
            character_data[0]["character_obj"].open_door()
        else:
            print("캐릭터가 없습니다.")

def typeof_wall(character=None):
    if character != None:
        return character.typeof_wall()
    else:
        if character_data[0]["character_obj"] != None:
            return character_data[0]["character_obj"].typeof_wall()
        else:
            print("캐릭터가 없습니다.")
            return None
        
def on_item(character=None):
    '''
    발 아래 아이템이 있는지 확인하는 함수
    '''
    if character != None:
        x, y = character._get_character_data("x"), character._get_character_data("y")
        if (x, y) in item_data:
            return True
        return False
    else: 
        if character_data[0]["character_obj"] != None:
            if (character_data[0]['x'], character_data[0]['y']) in item_data:
                return True
            return False
        else:
            print("캐릭터가 없습니다.")
            return None

# 작동하지만 시기상조로 인해 주석처리  
# def change_img():
#     '''
#     주인공 캐릭터의 이미지를 바꾸는 함수
#     '''
#     character = js.document.querySelector(".character")
#     character.style.backgroundImage = f'url("assets/img/characters/lion.png")'

# def add_ch():
#     '''
#     캐릭터를 추가하는 함수
#     순환 참조로 인해 이 함수만 index.html에 있음
#     '''
#     pass

def submit():
    '''
    통계보고서 처리를 위한 정답 확인용 함수
    캐릭터의 위치, 프린트된 결과, 말한 결과 등을 수집하여 정답 여부 확인
    '''
    pass

def mob_exist(x, y):
    for m in mob_data:
        if m['x'] == x and m['y'] == y:
            return True
    return False

def character_exist(x, y):
    for c in character_data:
        if c['x'] == x and c['y'] == y:
            return True
    return False


def eat(item, character=None):
    global command_count
    command_count += 1
    
    if character != None:
        character.eat(item)
    else:
        if character_data[0]["character_obj"] != None:
            character_data[0]["character_obj"].eat(item)
        else:
            print("캐릭터가 없습니다.")
            
            
# utility function
def _show_modal(message):
    toast = js.document.querySelector('.toast')
    
    text = toast.querySelector('.text')
    text.innerText = message
    toast.classList.add('show')
    
    button = toast.querySelector('.confirm')
    button.addEventListener('click', create_once_callable( lambda e:hiddenToast()))
    js.setTimeout(create_once_callable(lambda: (hiddenToast())), 2000)
    
def hiddenToast():
    js.document.querySelector('.toast').classList.remove('show')

def alert_error(error_type):
    # 순환참조로 인하여 built_in_functions에서 발생하는 오류는 따로 관리
    if error_type not in error_message.keys():
        _show_modal("알 수 없는 에러가 발생했습니다.")
    else:
        _show_modal(error_message[error_type])