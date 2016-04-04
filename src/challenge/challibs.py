
# External Packages
from collections import namedtuple, defaultdict
from datetime import datetime, timedelta
import json
from time import strptime


def _split_filter(li, cond):
    """
      takes in list and conditional
      returns [[False], [True]] split list in O(n) time
    """
    retval = [[],[]]
    for elm in li:
        index = cond(elm)
        retval[index].append(elm if index else elm)
    return retval


def clean_tweets(instream):
    """
    INPUT: iterable of raw tweets

    generator that takes in a iterable for raw formed tweets as json, and
      cleans them into a simple dict, only containing
      'hashtags' and 'created_at'

    Only yields correctly formated tweets
    """
    def datetimeify(datestr):
        tstamp = strptime(datestr, '%a %b %d %H:%M:%S %z %Y')
        simple = tstamp.tm_year, \
                 tstamp.tm_mon, \
                 tstamp.tm_mday, \
                 tstamp.tm_hour, \
                 tstamp.tm_min, \
                 tstamp.tm_sec
        return datetime(*simple)

    def clean(line):
        raw = json.loads(line)

        ret = dict()
        if raw and \
           'created_at' in raw.keys() and \
           'entities'   in raw.keys() and \
           'hashtags'   in raw['entities'].keys():
            ret['created_at'] = datetimeify(raw['created_at'])
            _ = [hashs['text'] for hashs in raw['entities']['hashtags']]
            tags = sorted(set(_))
            ret['hashtags'] = tags
        return ret

    for line in instream:
        cleaned = clean(line)
        if cleaned:
            yield cleaned


_Edge = namedtuple('Edge', ['timestamp', 'dst'])

class TimeGraph(defaultdict):
    """
    TimeGraph implements a collections.defaultdict(list)
      of namedtuple('Edge', ['timestamp', 'dst'])

    Only the most recent Edge is kept in the list

    TimeGraph only mantains a 'delta' seconds window of Edge. If an entry is
      added, whose 'timestamp' is greater than 'delta' seconds from
      'self.__start', then self.__start is updated to 'timestamp' - 'delta'
      and any Edge violating the window contract is purged.
    """
    def __init__(self, delta):
        """
        delta is defined in seconds
        """
        start = lambda:datetime.utcfromtimestamp(0)

        self.__delta = timedelta(seconds=delta)
        self.__start = start()
        defaultdict.__init__(self, list)

    def addEdges(self, timestamp, *pairs):
        """
        Update timestamp and insert edges into our TimeGraph
        """
        for src, dst in pairs:
            self._addEdge(timestamp, src, dst)

        if (timestamp - self.__start) > self.__delta:
            self._retime(timestamp)

    def _addEdge(self, timestamp, src, dst):
        edge = _Edge(timestamp, dst)

        if self.__start < edge.timestamp:
            [f, t] = _split_filter(self[src], lambda x: x.dst == edge.dst)
            t.append(edge)
            new = max(t, key=lambda x: x.timestamp)
            f.append(new)
            self[src] = f

    def averate_degree(self):
        """
        returns degree of graph
        """
        degrees = [len(self[key]) for key in self if self[key]]
        return 0 if len(degrees) == 0 else sum(degrees)/len(degrees)

    def _retime(self, timestamp):
        """
        updates time information and cleans old edges
        """
        self.__start = timestamp - self.__delta
        fnc = lambda x: x.timestamp >= self.__start
        remove = []

        for key in self:
            self[key] = list(filter(fnc, self[key]))
            if not self[key]:
                remove.append(key)

        for key in remove:
            self.pop(key, None)
