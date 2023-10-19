from sc2.ids.unit_typeid import UnitTypeId
from sharpy.knowledges import KnowledgeBot
from sharpy.plans import BuildOrder, BuildId


class SC2PlannerBot(KnowledgeBot):
    def __init__(self, build_str):
        super().__init__("SC2PlannerBot")
        self.build_str = build_str

    async def create_plan(self) -> BuildOrder:
        return BuildOrder(eval(self.build_str))