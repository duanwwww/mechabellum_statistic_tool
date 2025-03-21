UnitDict = {
    'Crawler': {
        'cost': 100,
        'unlock cost': 0
    },
    'Fang': {
        'cost': 100,
        'unlock cost': 0
    },
    'Hound': {
        'cost': 100,
        'unlock cost': 0
    },
    'Arclight': {
        'cost': 100,
        'unlock cost': 0
    },
    'Marksman': {
        'cost': 100,
        'unlock cost': 0
    },
    'Mustang': {
        'cost': 200,
        'unlock cost': 0
    },
    'Sledgehammer': {
        'cost': 200,
        'unlock cost': 0
    },
    'Stormcaller': {
        'cost': 200,
        'unlock cost': 0
    },
    'SteelBall': {
        'cost': 200,
        'unlock cost': 0
    },
    'Tarantula': {
        'cost': 200,
        'unlock cost': 0
    },
    'Sabertooth': {
        'cost': 200,
        'unlock cost': 0
    },
    'Rhino': {
        'cost': 200,
        'unlock cost': 50
    },
    'Hacker': {
        'cost': 200,
        'unlock cost': 100
    },
    'Wasp': {
        'cost': 200,
        'unlock cost': 50
    },
    'Phoenix': {
        'cost': 200,
        'unlock cost': 50
    },
    'PhantomRay': {
        'cost': 200,
        'unlock cost': 50
    },
    'Wraith': {
        'cost': 300,
        'unlock cost': 50
    },
    'Scorpion': {
        'cost': 300,
        'unlock cost': 50
    },
    'Vulcan' : {
        'cost': 400,
        'unlock cost': 200
    },
    'MeltingPoint': {
        'cost': 400,
        'unlock cost': 200
    },
    'Fortress': {
        'cost': 400,
        'unlock cost': 200
    },
    'Sandworm': {
        'cost': 400,
        'unlock cost': 200
    },
    'Raiden': {
        'cost': 400,
        'unlock cost': 200
    },
    'Overlord': {
        'cost': 500,
        'unlock cost': 200
    },
    'WarFactory': {
        'cost': 800,
        'unlock cost': 200
    },
    'FireBadger': {
        'cost': 200,
        'unlock cost': 0
    },
    'Typhoon': {
        'cost': 300,
        'unlock cost': 50
    },
    'Farseer': {
        'cost': 300,
        'unlock cost': 50
    },
}

def base_supply_cost(round):
    assert round >= 2
    if round <= 4:
        return 200 * (round - 1)
    elif round <= 7:
        return 100 * (round + 1)
    else: 
        return 100 * round

def unit_cost(name, level, num):
    return UnitDict[name]['cost'] * (level + 1) / 2 * num + (num - 1) * 50 + UnitDict[name]['unlock cost']

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    
    return dp[m][n]

def check_name(name):
    if name in UnitDict:
        return True
    else:
        print(f'Invalid name, do you mean:{min(UnitDict, key=lambda x: edit_distance(name, x))}?')
        return False

class Data:
    def __init__(self, round, name, level, num, cost):
        self.round = round
        self.name = name
        self.level = level
        self.num = num
        self.cost = cost
        self.bias = base_supply_cost(round) + cost - unit_cost(name, level, num)

    def __str__(self):
        return f'Round{self.round}, {self.name} lv.{self.level} * {self.num}, cost: {self.cost} bias: {self.bias}'