from src.objects.aoe2_object import AoE2Object


class TerrainObject(AoE2Object):
    def __init__(self,
                 terrain_id,
                 elevation
                 ):

        super().__init__(locals())
