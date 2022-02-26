class Seat:
    def __init__(self, attr) -> None:
        self.attr = attr
        # 바람이 불지 않는 상태 default
        self.status = 0
        self.pass_dir = 'none'
        self.input_dir = 'none'
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def submit_xy(self, y_co, x_co, y_limit, x_limit,):
        self.y_co = y_co
        self.x_co = x_co
        
        if self.x_co != 0:
            self.up = [self.x_co - 1, self.y_co]

        if self.x_co < x_limit:
            self.down = [self.x_co + 1, self.y_co]

        if self.y_co != 0:
            self.left = [self.x_co, self.y_co - 1]

        if self.y_co < y_limit:
            self.right = [self.x_co, self.y_co + 1]

    #def change_status(self, map):
        

    def set_attr(self, value):
        self.attr = value

    def get_attr(self):
        return self.attr

    def get_xy(self):
        return self.x_co, self.y_co

    def get_around(self):
        return self.up, self.down, self.left, self.right
    
def input_2d(x_amount, y_amount):
    map = [[Seat(0) for y in range(y_amount)] for x in range(x_amount)]
    
    for i in range(len(map)):
        for j in range((len(map[i]))):
            map[i][j].submit_xy(j, i, (y_amount - 1), (x_amount - 1))

    return map

def print_map(map):
    for i in range(len(map)):
        for j in range((len(map[i]))):
            attr_digit = map[i][j].get_attr()
            x_co, y_co = map[i][j].get_xy()
            print('{0}{1} : {2}'.format(x_co, y_co, attr_digit), end=' ')
        print('\n')
    
def print_status(map):
    for i in range(len(map)):
        for j in range((len(map[i]))):
            x_co, y_co = map[i][j].get_xy()
            up, down, left, right = map[i][j].get_around()
            print('{0}{1} : up {2} down {3} left {4} right {5}'.format(x_co, y_co, up, down, left, right), end='\t')
        print('\n')

def ask_ac(map, x_co, y_co):
    map[x_co][y_co].set_attr(9)

def ask_tool(map, amount):
    for i in range(amount):
        attr, x, y = input('{0}번째의 물건번호과 좌표를 입력해주세요 : '.format(i + 1)).split(' ')
        map[x][y].set_attr(attr)

def cal_map(map):
    for i in range(len(map)):
        for j in range((len(map[i]))):
            attr_digit = map[i][j].get_attr()

if __name__ == '__main__':
    map = input_2d(2, 3)
    print_map(map)
    print_status(map)
    #ask_ac(map, 0, 1)
    #print_map(map)

