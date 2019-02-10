from typing import Tuple, Optional
from flask_restful import Resource, reqparse
from rest_api.models.meeting import MeetingModel


class MeetingV1(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('meeting_date',
                        type=str,
                        required=True,
                        help='Date of meeting is required, format YYYY-MM-DD.')
    parser.add_argument('theme',
                        type=str,
                        required=True,
                        help='Theme is required.')
    parser.add_argument('pbj_topic',
                        type=str,
                        required=False,
                        help="Topic of the Python Beginner's Jam")
    parser.add_argument('right_brain_topic',
                        type=str,
                        required=False,
                        help='Topic of Right Brain Talk')
    parser.add_argument('pro_talk_topic',
                        type=str,
                        required=False,
                        help='Topic for Pro Talk')

    # By using optional meeting_date, we can handle URI that includes calls to
    # meetings or meetings/[meeting_date] with same methods.
    #
    # If we do not return a response code, 200 is defaulted.  I have typed the methods with
    # Tuple[dict, int] as I will explicitly return codes for every return path.
    #
    # flask_restful expects a dict as return type (or first argument of tuple if return code is specified)
    # and automatically does the JSON conversions.
    #
    # Response Codes used:
    # 200 - OK
    # 201 - Created
    # 202 - Accepted (Might be used if your API queues up an action, but doesn't complete immediately
    # 400 - Bad Request
    # 404 - Not Found

    def get(self, meeting_date: Optional[str] = None) -> Tuple[dict, int]:
        if meeting_date is None:
            # Requesting all meetings
            #
            # Note: for many records, you would need to paginate here and might have
            # a querystring arguments for page number and record counts.
            #
            # You could implement filters as querystring to make a targeted query.
            return {'meetings': [mtg.as_dict() for mtg in MeetingModel.all_meetings()]}, 200

        mm = MeetingModel.meeting_by_date(meeting_date)
        if mm:
            return mm.as_dict(), 200
        return {'message': 'Meeting not found'}, 404

    def post(self, meeting_date: Optional[str] = None) -> Tuple[dict, int]:
        if meeting_date is not None:
            return {'message': 'Do not provide meeting_date as URI path for POST.'}, 400

        data = MeetingV1.parser.parse_args()

        if MeetingModel.meeting_by_date(data['meeting_date']):
            return {'message': f'A meeting for date {data["meeting_date"]} already exists'}, 400

        # Because we have naming of resource and data model the same, we can use dictionary expansion
        # to offer the named arguments to the model creation.
        mm = MeetingModel(**data)
        mm.save_to_db()
        return {'message': 'Meeting created'}, 200

    def put(self, meeting_date: Optional[str] = None) -> Tuple[dict, int]:
        if meeting_date is None:
            # PUT requires item to update, so a non-meeting_date call isn't valid
            return {'message': 'Must specify the Meeting Date in URI to update.'}, 400

        mm = MeetingModel.meeting_by_date(meeting_date)
        if not mm:
            return {'message': 'Meeting not found.'}, 404

        data = MeetingV1.parser.parse_args()

        # We don't allow modifying the primary key of a meeting, so expect it to match the URI key.
        if meeting_date != data['meeting_date']:
            return {'meeting': 'meeting_date is not allowed to be updated.'}, 400

        # Again, since properties and resource fields are the same, we can setattr for each field.
        # This would still be possible if you needed a mapping for the value names to translate.
        for key in data:
            setattr(mm, key, data[key])
        mm.save_to_db()

    def delete(self, meeting_date: Optional[str] = None) -> Tuple[dict, int]:
        if meeting_date is None:
            # You could dangerously allow deleting all meetings, I don't
            return {'message': 'You cannot delete all meetings.'}, 400

        mm = MeetingModel.meeting_by_date(meeting_date)
        if not mm:
            return {'message': 'Meeting not found.'}, 404
        mm.delete_from_db()
        return {'message': f'Meeting {meeting_date} deleted'}, 200
