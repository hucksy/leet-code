from collections import deque
from typing import List
import logging

class Que:
    """
    Implement a que that models parties waiting in line at a restaurant. People can enque to get in line,
    join to add more people to a party, or deque when they're table is called
    Enque([Bob, Alice]) - Bob and Alice join the line
    Join("Alice", "Chris") - Chris joins Alice's party in line
    Deque() - Removes the first party in the que and returns it
    """
    logging.basicConfig(filename='que_test.log', filemode='a', level=logging.DEBUG)

    def __init__(self) -> None:
        self.q = deque()
        self.peeps = {}

    def enque(self, party: List[str]) -> None:
        self.q.appendleft(party)
        for peep in party:
            self.peeps[peep] = self.q[0]

    def join(self, line_person: str, join_person: str) -> None:
        self.peeps[line_person].append(join_person)
        self.peeps[join_person] = self.peeps[line_person]

    def deque(self):
        try:
            popped = self.q.popleft()
        except IndexError as ie:
            msg = "yo this queue is empty player, we can't pop nothing"
            logging.exception(msg)
        else:
            return popped


q = Que()
q.enque(['moffs', 'huck'])
q.enque(['trixie', 'foxy'])
q.enque(['grandpa'])
print(q.q)
print(q.peeps)
q.join('grandpa', 'santa')
print(q.q)
