from collections import namedtuple
import csv
import os

if __name__ == '__main__':
    userid = raw_input("Enter user ID: ")
    foldername = 'data/%s' % userid
    filename_timestamps= '{foldername}/timed_decisions.csv'
    decision_events = []

    DecisionEvent = namedtuple('DecisionEvent', ['event_type', 'timestamp', 'decision'])

    if not os.path.exists(foldername):
        os.makedirs(foldername)

    filename_timestamps = filename_timestamps.format(foldername=foldername)

    with open(filename_timestamps, 'w') as f:
        writer = csv.DictWriter(f, DecisionEvent._fields, delimiter=';')
        writer.writeheader()
        writer.writerows([evt._asdict() for evt in decision_events])
        decision_events = []


    while True:
        print "Enter next event: (event_type, timestamp, decision)\n"
        event_type = raw_input("event_type: ")
        if event_type == 'no':
            break
        timestamp = raw_input("timestamp: ")
        decision = raw_input("decision: ")
        event = DecisionEvent(event_type, timestamp, decision)
        decision_events.append(event)
        with open(filename_timestamps, 'a') as f:
            writer = csv.DictWriter(f, DecisionEvent._fields, delimiter=';')
            writer.writerows([evt._asdict() for evt in decision_events])
            decision_events = []
