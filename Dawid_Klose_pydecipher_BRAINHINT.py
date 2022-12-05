#!/usr/bin/python3
import logging
from typing import Tuple, Dict

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
logger = logging.getLogger()


class OfficeCode:
    """Recruitment task for BRAINHINT.
    The most interesting type of setting the office key I have ever seen C:
    """

    def __init__(self, input_code: str = ""):
        """Constructing main attributes.

        :param input_code: String with given input. e.g.: LRLDU\nLDLRL\n
        """
        if input_code:
            self.input_code: str = input_code
        else:
            raise ValueError("Not any input_code provided!")
        self.index_right_left: int = 1
        self.index_up_down: int = 1
        self.keyboard: Tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        self.update_up_down: Dict = {}
        self.update_right_left: Dict = {}

    def read_the_code(self) -> str:
        """Inform about the decrypting input and start private parsing methods."""
        logger.info(f"Starting reading the code from given text: {self.input_code}")
        self._prepare_input_for_parsing()
        return self._start_decrypting_loop()

    def _prepare_input_for_parsing(self):
        """Get rid of unnecessary white-marks from the input."""
        self.input_code = (
            repr(self.input_code.lstrip()).replace("'", "").replace(r"\n", "-")
        )
        logger.debug(f"Prepared input: {self.input_code}")

    def _start_decrypting_loop(self) -> str:
        """Iterate through the input."""
        ret_code = ""
        for element in self.input_code:
            self.update_up_down: Dict = {
                "U": self.index_up_down - 1,
                "D": self.index_up_down + 1,
            }
            self.update_right_left: Dict = {
                "L": self.index_right_left - 1,
                "R": self.index_right_left + 1,
            }
            if element == "-":
                self.point = self.keyboard[self.index_up_down][self.index_right_left]
                ret_code += str(self.point)
                continue
            elif element in ("U", "D"):
                self.index_up_down = self.update_up_down[element]
            elif element in ("R", "L"):
                self.index_right_left = self.update_right_left[element]
            else:
                logger.error(
                    r"Unsupported code combination! Required letters are: 'U D R L \n'!!!"
                )
                raise ValueError
            self._set_proper_indexes()
            self.point = self.keyboard[self.index_up_down][self.index_right_left]
        return ret_code

    def _set_proper_indexes(self):
        self.index_up_down = 2 if self.index_up_down > 2 else self.index_up_down
        self.index_right_left = (
            2 if self.index_right_left > 2 else self.index_right_left
        )
        self.index_up_down = 0 if self.index_up_down < 0 else self.index_up_down
        self.index_right_left = (
            0 if self.index_right_left < 0 else self.index_right_left
        )


inside_input = """ULL
RRDDD
LURDL
UUUUD
"""
test = OfficeCode(input_code=inside_input)
output = test.read_the_code()
logger.critical(f"RETURNED CODE: {output}\n\n")

inside_input2 = """
RDRRDLRRUDRUUUULDDRDUULLDUULDURDDUDRULDLUDDRLRDUDDURRRRURDURLLRDRUUULDLLLURDRLLULLUULULLLDLLLRRURRLRDUULRURRUDRRDRLURLRURLLULRUURRUURDDLDRDLDLLUDUULLLUUUUDULLDRRUURLDURDDDDDRLLRRURDLUDRRUUDLRRLLRDURDUDDDLRDDRDLRULLUULRULRLLULDDRURUUDLDDULDRLLURDDUDDUDRDUDLDRRRDURRLDRDRLDLLDUDDDULULRRULRLLURDRRDDUUUUUULRUDLRRDURDLRDLUDLDURUDDUUURUDLUUULDLRDURDLDUUDLDDDURUUDUUDRLRDULLDUULUDRUDRLRRRDLLDRUDULRRUDDURLDRURRLLRRRDRLLDLULULRRUURRURLLUDRRLRULURLDDDDDURUDRRRRULLUUDLDDLUUL
ULURUDLULDULDLLDDLLLDRRLLUDRRDRDUDURUDLRRRRUDRDDURLRRULLDLURLDULLUDDLUDURDUURRRRLDLRLDDULLRURLULLDDRUDLRRRLDRRRDLDRLLDDRRDDLUUDRUDDLULRURLDURRLLDLRUDLLRRUULUDRLLLRLDULURRRRRDDUURDRRUUDULRUULDDULRLUDLUDDULLRLRDDLRLLURRRULDLRRRUURRLDDRDLRDLRRDRDLDRDUDRDURUUDRLRRULRDLLDLLRRRDRLDRLRLRLLLURURDULUUDDRLLDDDRURRURLRDDULLRURUDRRDRLRRRLDLRLRULDRLUURRUUULRLDLLURLLLDLLLDRRDULRURRRRLUDLLRRUDLRUDRURDRRDLUUURRDLRLRUUUDURDLUDURRUUDURLUDDDULLDRDLLDDDRLDDDRLDLDDDDUDUUDURUUDULRDDLULDRDRLURLUDRDLUULLULRLULRDDRULDUDDURUURULUDLUURLURU
URLURDDRLLURRRLDLDLUDUURDRUDLLLRRDLUUULRRLURRRLUDUDLRLDDRUDLRRRULUDUDLLLULULLLRUDULDDDLLLRRRLRURDULUDDDULDLULURRRDLURDLRLLDUDRUDURDRRURULDRDUDLLRDDDUDDURLUULLULRDRRLDDLDURLRRRLDRDLDULRULRRRLRLLDULRDLURLRUUDURRUUDLLUDRUDLRLDUUDLURRRDDUUDUDRLDLDDRURDDLLDDRDLRLRDLLLUDLUUDRLRLRDDRDLRDLLUULLLLUULLDLLDLRDLRLRRLUUDLLRLRUDRURULRLRLULUDRLLUDDUDDULRLDDRUUUURULDRRULLLDUURULUDRLLURLRRLDLRRLDDRRRDUDDUDLDDLULUDDUURDLLLRLDLRDRUUUUUDDDLDRDDRRRLRURRRRDURDRURUDLURRURDRLRUUDDLDRRULLDURDRLRRDURURUULRDUDLDRDDLULULRDRRUDDRLLRLULRLLUUDRDUUDDUDLRUUDLLUULLRUULUDDLURRRLLDRLRRLLRULLDUULURLLLLUUULDR
LDUURULLRLDRRUUDUUUURUUUDDDURRDDLRDLLRDDRULDDUURUDDURLLUDRDUDRDULDRRRLULUDRULLLLDRLLDRDLDLLRURULUDDDDURDDDRLLUDLDRULRDLDUDDDUUDLLRLLLDLRLRLRRUDDULDDDUDLDDLUDDULDLLLLULLLLDDURDDURRRDDRLRLLUDLLUDDDUDURUDRLRDRULULDDRULDLULULLRUULRLDULUURRDRDRRDLDDDRRLUULDLUDRDDUDLRURULLDDURLDDRULUDLDDDRDRLLRDLLUURRRURDRLRURLDDLURDRURDDURLLRLRUDUUDLDUDURRDDURDRDDUDDDUDUURURDDLLRUUDDRRDULDDLLDLRULUULRUUDLLDRLULDULDDUDLULRULDRLLDUULDDDLRLLRLULDDULDDRRRLDRRLURULRDDRDLRRDUDDRDRRRRUDUDLLRRDRRURRUURDRULDDUDURLUDDURDUDRDUULLDRURUURURDRRLDDLDLUURLULRUDURDRUUURRURRDRUDRUURDURLRULULLLULDLLDLRRLDRDLUULUDDDLRDRLRLDRUDUDRLLRL
LURLUURLURDUUDRUDLDLLURRRDLDRRRULDDRRDRDUUDRUDURDDDURLUDDLULUULRRLLRULUDRDDRRRLDURDUDDURDDDLRLDDLULLDRDDLUUDUURRRLULRUURRRRLLULDUDRDUURRRURRDRDUDUDLUDULLDLDDRLUDRURDULURLURRLLURLLLRLUURLRUDLUDDRLURRUULULRLURRURUDURDLDLDDUDDRDLLRLLRRULDDRUDURUDDDUDLLRDLRUDULLLRRRUURUDUUULLRDUDRURUDULLDLLUUUDRULRLLRRDDDDUDULDRDRLLDDLLDDDURRUDURLDLRDRUURDDURLRDRURLRRLLRLULDRRLRUDURDUURRLUUULUDDDLRLULRDRLLURRRDLURDUUDRRRLUURRLLUDLUDLUULLRRDLLRDDRURRUURLDDLRLRLRUDLDLRLRDRRDLLLRDLRDUDLLDDDRD
"""

test2 = OfficeCode(input_code=inside_input2)
output = test2.read_the_code()
logger.critical(f"RETURNED CODE: {output}")
