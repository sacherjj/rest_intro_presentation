from typing import Optional, List
import requests
import attr


URL = 'http://localhost:5000/api/v1/meetings'


@attr.s
class Meeting:
    meeting_date: str = attr.ib()
    theme: str = attr.ib()
    pbj_topic: Optional[str] = attr.ib(None)
    right_brain_topic: Optional[str] = attr.ib(None)
    pro_talk_topic: Optional[str] = attr.ib(None)

    @classmethod
    def from_dict(cls, meeting_dict: dict) -> "Meeting":
        return Meeting(**meeting_dict)

    def to_dict(self) -> dict:
        return {"meeting_date": self.meeting_date,
                "theme": self.theme,
                "pbj_topic": self.pbj_topic,
                "right_brain_topic": self.right_brain_topic,
                "pro_talk_topic": self.pro_talk_topic}


def get_meeting(meeting_date: str) -> Optional[Meeting]:
    response = requests.get(f'{URL}/{meeting_date}')
    if response.status_code == 404:
        return None
    return Meeting.from_dict(response.json())


def get_meetings() -> List[Meeting]:
    response = requests.get(URL)
    body = response.json()
    return [Meeting.from_dict(mtg) for mtg in body['meetings']]


def post_meeting(meeting: Meeting):
    response = requests.post(URL, json=meeting.to_dict())
    body = response.json()
    if response.status_code == 400:
        raise Exception(body["message"])


def put_meeting(meeting: Meeting):
    response = requests.put(f'{URL}/{meeting.meeting_date}',
                            json=meeting.to_dict())
    if response.status_code == 404:
        raise Exception(response.json()['message'])


def delete_meeting(meeting_date: str):
    response = requests.delete(f'{URL}/{meeting_date}')
    if response.status_code == 404:
        raise Exception(response.json()['message'])


if __name__ == "__main__":
    print("\nGET /meetings")
    print(get_meetings())

    mtg = Meeting("2019-02-12", "Share the (Python) Love")
    print(f"\nCreated meeting for {mtg.meeting_date}")
    print("POST /meetings")
    post_meeting(mtg)

    print("\nGET /meetings")
    print(get_meetings())

    print("\nGET /meetings/2019-02-12")
    mtg2 = get_meeting('2019-02-12')
    print(mtg2)

    print(f'\nMeetings equal?  {mtg == mtg2}')

    print("\nAdding pbj_topic")
    mtg.pbj_topic = "REST APIs in Python"
    print("PUT /meetings/2019-02-12")
    put_meeting(mtg)

    print("\nGET /meetings/2019-02-12")
    print(get_meeting('2019-02-12'))

    mtg2 = Meeting('2019-03-12', 'Python Madness')
    print(f"\nCreated meeting for {mtg2.meeting_date}")
    print("POST /meetings")
    post_meeting(mtg2)

    print("\nGET /meetings")
    print(get_meetings())

    print("\nDELETE /meetings/2019-02-12")
    delete_meeting("2019-02-12")

    print("\nGET /meetings")
    print(get_meetings())

    print("\nDELETE /meetings/2019-03-12")
    delete_meeting("2019-03-12")

    print("\nGET /meetings")
    print(get_meetings())

