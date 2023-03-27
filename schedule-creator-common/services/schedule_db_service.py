from models.schedule import Schedule
from bson import ObjectId

class ScheduleDBService:

    def __init__(self):
        self.db = Schedule
    
    async def get_schedule_by_id(self, schedule_id: str) -> Schedule:
        return await self.db.get(ObjectId(schedule_id))
    
    async def get_schedule_by_name(self, schedule_name: str) -> Schedule:
        return await self.db.find_one(Schedule.name == schedule_name)
    
    @staticmethod
    async def create_schedule(schedule: Schedule) -> Schedule:
        return await schedule.save()
    
    @staticmethod
    async def update_schedule(schedule: Schedule, schedule_id: str) -> Schedule:
        schedule.id = ObjectId(schedule_id)
        return await schedule.replace()
    
    async def delete_schedule(self, schedule_id: str) -> None:
        schedule = await self.get_schedule_by_id(schedule_id)
        await schedule.delete()