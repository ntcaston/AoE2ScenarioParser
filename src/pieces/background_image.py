from src.pieces.scenario_piece import *
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class BackgroundImagePiece(ScenarioPiece):
    def __init__(self, parser):
        retrievers = [
            Retriever("ASCII, Background filename", DataType("str16")),
            Retriever("Picture Version", DataType("u32")),
            Retriever("Bitmap width", DataType("u32")),
            Retriever("Bitmap height", DataType("s32")),
            Retriever("Picture Orientation", DataType("s16")),
            # Retriever("	BITMAPINFOHEADER", DataType("u32")),
        ]

        super().__init__(parser, "Background Image", retrievers)
