class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class Not:
    def __init__(self,term):
        self._term = term
    
    def test(self, player):
        return not self._term.test(player)

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
    
    def test(self,player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Or:
    def __init__(self, *matcher):
        self.matcher = matcher

    def test(self, player):
        for i in self.matcher:
            if i.test(player):
                return True
        return False

class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query
    
    def build(self):
        return self._query

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query,HasFewerThan(value,attr)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))
    
    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))