# Dominic DiPuma

class EventRecord:
    def __init__(self, event_list=None):
        self._event_list = event_list

        if self._event_list == None:
            self._event_list = []

    def add_event(self, event):
        self._event_list.append(event)

    def get_event_list(self):
        return self._event_list

    def filter_by_type(self, type_of_event):
        return EventRecord(
                [e for e in self._event_list if type(e) is type_of_event])
