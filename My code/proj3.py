#everything in this is stupid but our teacher wanted this.


from random import randint
from random import shuffle

class Person:
    def __init__(self, name, lastname):
        self.name=name
        self.lastname=lastname
    
    def get_name(self):
        return self.name+" "+self.lastname
    
    def __str__(self):
        return self.name+" "+self.lastname
    
    def __lt__(self, other):
        return self.lastname<other.lastname if self.lastname!=other.lastname else self.name<other.name
    
class Player(Person):
    uid=0
    def __init__(self, name, lastname):
        self.name=name
        self.lastname=lastname
        self.power=randint(4, 8)
        Player.uid+=1
        self.id=Player.uid
        self.points=[]
        self.temp=[]
        
    def reset(self):
        self.points=[]
        self.temp=[]
        Player.uid=0

    
    def get_id(self):
        return self.id
    
    def get_power(self):
        return self.power
    
    def set_team(self, team):
        self.team=team
        team.players.append(self)
        
    def get_team(self):
        return self.team
    
    def add_to_points(self, point):
        self.points.append(point)
        
    def get_points_detailed(self):
        return self.points
    
    def get_points(self):
        return sum(self.points)
    
    def round_points(self, point):
        self.temp.append(point)
        
    def round_clear(self):
        self.temp=[]
        
    def apply_points(self):
        self.add_to_points(sum(self.temp))
    
    def __lt__(self, other):
        if self.get_points()!=other.get_points(): return self.get_points()<other.get_points()  
        elif self.lastname==other.lastname: return self.lastname<other.lastname  
        else: return self.name<other.name
    
class Manager(Person):
    mid=0
    def __init__(self, name, lastname):
        self.name=name
        self.lastname=lastname
        self.influence=[]
        Manager.mid+=1
        self.id=Manager.mid
        
    def reset(self):
        self.influence=[]
        Manager.mid=0
    
    def get_id(self):
        return self.id
    
    def set_team(self, t):
        t.manager=self
        self.team=t
        
    def get_team(self):
        return self.team
    
    def get_influence_detailed(self):
        return self.influence
    
    def get_influence(self):
        return sum(self.influence)
    
    def __lt__(self, other):
        if self.get_influence()!=other.get_influence(): return self.get_influence()<other.get_influence()
        elif self.lastname==other.lastname: return self.lastname<other.lastname  
        else: return self.name<other.name
        
        
    
class Team:
    tid=0
    def __init__(self, teamname, manager, players):
        self.teamname=teamname
        self.manager=manager
        self.players=players[:]
        Team.tid+=1 
        self.id=Team.tid
        self.fixture=[]
        self.wins=0
        self.conceded=0
        self.scored=0
        self.losses=0
        
        
    def reset(self):
        self.fixture=[]
        self.wins=0
        self.conceded=0
        self.scored=0
        self.losses=0
        self.manager.reset()
        for i in self.players:
            i.reset()
        Team.tid=0
        
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.teamname
    
    def get_roster(self):
        return self.players
    
    def get_manager(self):
        return self.manager
    
    def add_to_fixture(self, m):
        self.fixture.append(m)
        
    def get_fixture(self):
        return self.fixture
    
    def add_results(self, s):
        self.scored+=s[0]
        self.conceded+=[1]
        if s[0]>s[1]: self.wins+=1 
        else: self.losses+=1
        
    def get_scored(self):
        return self.scored
    
    def get_conceded(self):
        return self.conceded
    
    def get_wins(self):
        return self.wins
    
    def get_losses(self):
        return self.losses
    
    def __str__(self):
        return self.teamname

    def __lt__(self, other):
        return self.get_scored()<other.get_scored() if self.get_scored()!=other.get_scored() else (self.get_scored() - self.get_conceded()) <(other.get_scored() - other.get_conceded())
    
    def __gt__(self, other):
        return self.get_scored()>other.get_scored() if self.get_scored()!=other.get_scored() else (self.get_scored() - self.get_conceded()) >(other.get_scored() - other.get_conceded())

    def __le__(self, other):
        return self.get_scored()<=other.get_scored()
    
    def __ge__(self, other):
        return self.get_scored()>=other.get_scored()
    
    def __eq__(self, other):
        return self.get_scored()==other.get_scored()
    
class Match:
    def __init__(self, home_team, away_team, week_no):
        self.home_team=home_team
        self.away_team=away_team
        self.week=week_no
        self.score=[0,0]
        self.played=False
        self.winner=None
        
        
    def is_played(self):
        return self.played
    
    def play(self):
        if not self.played:
            pass
        
        manager_ps=[randint(-10, 10), randint(-10,10)]
        self.home_team.manager.influence.append(manager_ps[0])
        self.away_team.manager.influence.append(manager_ps[1])
        
        scores=manager_ps
        
        def play_round():
            for i in self.home_team.players:
                poi=i.power + randint(-5,5)
                i.round_points(poi)
                scores[0]+=poi
                
            for i in self.away_team.players:
                poi=i.power + randint(-5,5)
                i.round_points(poi)
                scores[1]+=poi
        
        for _ in range(4):
            play_round()                
            
        while scores[0]==scores[1]:
            play_round()
            
        for i in range(5):
            self.home_team.get_roster()[i].apply_points()
            self.away_team.get_roster()[i].apply_points()
                
        if scores[0]>scores[1]: self.home_team.wins+=1 
        else: self.away_team.wins+=1 
        
        self.home_team.scored+=scores[0]
        self.home_team.conceded+=scores[1]
        self.away_team.scored+=scores[1]
        self.away_team.conceded+=scores[0]
        
        self.winner = (self.home_team if scores[0]>scores[1] else self.away_team)
        self.is_played=True
        
    def get_match_score(self):
        return self.score
    
    def get_week_no(self):
        return self.week
    
    def get_teams(self):
        return self.home_team, self.away_team
    
    def get_home_team(self):
        return self.home_team
    
    def get_away_team(self):
        return self.away_team
    
    def get_winner(self):
        return self.winner
    
    def swap(self, week_no):
        self.home_team, self.away_team=self.away_team, self.home_team
        self.week_no=week_no
        
    def swaped(self):
        home_team, away_team=self.away_team, self.home_team
        return home_team, away_team, self.week
        
    def __str__(self):
        return (self.home_team.get_name()+" VS. "+self.away_team.get_name()) if self.score[0]!=0 else (self.home_team.get_name()+" " + str(self.score[0])+ " VS. "+str(self.score[1])+ " " +self.away_team.get_name())
    
    
class Season:
    def __init__(self, teams, managers, players):
        teams=open(teams)
        managers=open(managers)
        players=open(players)
        count=0
        mancount=0
        self.teams=[]
        self.managers=[]
        self.players=[]
        self.current_week=1
        self.fixture=[]

        for i in players:
            pi = i.strip("\n").split(" ")
            self.players.append(Player(pi[0], pi[1]))
        
        for i in managers:
            mi = i.strip("\n").split(" ")
            self.managers.append(Manager(mi[0], mi[1]))
            
        for i in teams:
            ti = [i.strip("\n")]
            ti.append(self.managers[mancount])
            ti.append([])
            for j in self.players[count: count+5]:
                ti[-1].append(j)
            self.teams.append(Team(ti[0], ti[1], ti[2]))
            count+=5
            mancount+=1
            
        shuffle(self.teams)
        
        self.build_fixture()
        
        teams.close()
        managers.close()
        players.close()        
        
    def reset(self):
        for i in self.teams:
            i.reset()
        for i in self.players:
            i.reset()
        for i in self.managers:
            i.reset()
        self.fixture=[]
        self.build_fixture()
        self.current_week=1
            
    def build_fixture(self):
        fixture_ring=[self.teams[0:int(len(self.teams)/2)] , list(reversed(self.teams[int(len(self.teams)/2) : len(self.teams)]))]
        match=[]
        matchrev=[]
        week_no=1
        
        if len(self.teams)%2!=0:
            fixture_ring[0].insert(0, "dum")
        
        for i in (range(int(len(self.teams)-1)) if len(self.teams)%2==0 else range(len(self.teams))):
            for j in range(len(fixture_ring[0])):
                match.append(Match(fixture_ring[0][j], fixture_ring[1][j], week_no))
            
            fixture_ring[0].insert(1, fixture_ring[1].pop(0))
            fixture_ring[1].append(fixture_ring[0].pop())
            week_no+=1
        for j in match:
            matchrev.append(Match(j.swaped()[0], j.swaped()[1], (j.swaped()[2]+week_no)))
            
        match.extend(matchrev)

        for i in match:
            if "dum"!=i.home_team.get_name():
                self.fixture.append(i)
                self.fixture[-1].home_team.add_to_fixture(self.fixture[-1])
                self.fixture[-1].away_team.add_to_fixture(self.fixture[-1])
            
        
            
    
    def get_season_length(self):
        return (len(self.teams)-1)*2
            
    def get_week_fixture(self, week_no):
        lst=[]
        for i in self.fixture:
            if i.get_week_no()==week_no:
              lst.append(i)  
        return lst
    
    def get_week_no(self):
        return self.current_week
    
    def play_week(self):
        for i in self.get_week_fixture(self.get_week_no()):
            i.play()
        if self.current_week<len(self.fixture):
            self.current_week+=1
    
    def get_players(self):
        return self.players
    
    def get_managers(self):
        return self.managers
    
    def get_teams(self):
        return self.teams
    
    def get_best_player(self):
        bp=self.players[0]
        
        for i in self.players:
            if bp<i:
                bp=i
                
        return bp
    
    def get_best_manager(self):
        bm=self.managers[0]
        
        for i in self.managers:
            if bm<i:
                bm=i
                
        return bm
    
    def get_most_scoring_team(self):
        bt=self.teams[0]
        
        for i in self.teams:
            if bt<i:
                bt=i
                
        return bt
    
    def get_champion(self):
        if self.current_week-1!=self.fixture[-1].get_week_no():
            pass
        
        a=sorted(self.teams)
        
        return a[-1]
    
    
    
if __name__ == "__main__":

    teams_file = 'teams.txt'
    managers_file = 'managers.txt'
    players_file = 'players.txt'

    # Create a season
    season21 = Season(teams_file, managers_file, players_file)

    # Play the matches
    for i in range(season21.get_season_length()):
        season21.play_week()

    # Get season statistics
    print("Champion is:", season21.get_champion() )
    print("Most scoring team is:", season21.get_most_scoring_team() )
    print("Best player is:", season21.get_best_player() )
    print("Best manager is:", season21.get_best_manager() )

    
    
    
