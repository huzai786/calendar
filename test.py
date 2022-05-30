import dataclasses
import datetime
import functools

import tabulate

alices_free_times = [
    (datetime.datetime(2022, 6, 2, 9, 0), datetime.datetime(2022, 6, 2, 9, 30)),
    (datetime.datetime(2022, 6, 2, 11, 0), datetime.datetime(2022, 6, 2, 12, 10)),
]

bobs_free_times = [
    (datetime.datetime(2022, 6, 2, 5, 9), datetime.datetime(2022, 6, 2, 6, 56)),
    (datetime.datetime(2022, 6, 2, 15, 37), datetime.datetime(2022, 6, 2, 17, 24)),
    (datetime.datetime(2022, 6, 2, 9, 5), datetime.datetime(2022, 6, 2, 9, 25)),
]


@functools.total_ordering
@dataclasses.dataclass
class Timespan:
    start: datetime.datetime
    stop: datetime.datetime
    owner: str

    @property
    def duration(self):
        return self.stop - self.start

    @property
    def fields(self):
        return [self.owner, self.start, self.stop, self.duration]

    def __str__(self):
        return (
            f"{self.owner} is free for {self.duration} from {self.start} to {self.stop}"
        )

    def __lt__(self, other):
        if self.start < other.start:
            return True
        elif self.start > other.start:
            return False
        return self.stop < other.stop


free_times = []
for p in alices_free_times:
    p = sorted(p)
    free_times.append(Timespan(*p, owner="Alice"))

for p in bobs_free_times:
    p = sorted(p)
    free_times.append(Timespan(*p, owner="Bob"))

free_times = list(sorted(free_times))
print(tabulate.tabulate([e.fields for e in free_times]))


@functools.total_ordering
@dataclasses.dataclass
class Transition:
    owner: str
    when: datetime.datetime
    is_start: bool

    def __lt__(self, other):
        return self.when < other.when


transitions = []
for ft in free_times:
    transitions.append(Transition(owner=ft.owner, when=ft.start, is_start=True))
    transitions.append(Transition(owner=ft.owner, when=ft.stop, is_start=False))
transitions = list(sorted(transitions))
print(
    tabulate.tabulate(
        [(t.owner, t.when, "is free" if t.is_start else "is busy") for t in transitions]
    )
)

who_is_free_when = []

currently_free = set()
for index, tr in enumerate(transitions):
    if tr.is_start:
        currently_free.add(tr.owner)
    else:
        if tr.owner in currently_free:
            currently_free.remove(tr.owner)
    datum = [
        transitions[index + 1].when - tr.when
        if index < len(transitions) - 1
        else "----"
    ]
    datum.append(tr.when)
    datum.append(currently_free.copy())

    who_is_free_when.append(datum)
print(tabulate.tabulate(who_is_free_when, headers=["Duration", "when", "who's free"]))


def find_free_time(duration_minutes, num_required_attendees):
    for t in who_is_free_when:
        if (
            isinstance(t[0], datetime.timedelta)
            and t[0].total_seconds() >= duration_minutes * 60
        ):
            if len(t[2]) >= num_required_attendees:
                print(f"Hey at {t[1]} {t[2]} are free for {t[0]}")


find_free_time(20, 2)