
class StyleSimple:
    V = "|"
    H = "-"

    BORDER_H = H
    BORDER_V = V

    TL = "+"  # Top left
    TR = "+"  # Top right
    BL = "+"  # Bottom left
    BR = "+"  # Bottom right

    HB = "+"  # Horizontal bottom
    HT = "+"  # Horizontal top
    VL = "+"  # Vertical left
    VR = "+"  # Vertical right

    HV = "+"  # Horizontal vertical


class StyleBox:
    H = "─"
    V = "│"

    BORDER_H = H
    BORDER_V = V

    TL = "┌"  # Top left
    TR = "┐"  # Top right
    BL = "└"  # Bottom left
    BR = "┘"  # Bottom right

    HB = "┬"  # Horizontal bottom
    HT = "┴"  # Horizontal top
    VL = "┤"  # Vertical left
    VR = "├"  # Vertical right

    HV = "┼"  # Horizontal vertical


class StyleBoxBorder:
    H = "─"
    V = "│"

    BORDER_H = "═"
    BORDER_V = "║"

    TL = "╔"  # Top left
    TR = "╗"  # Top right
    BL = "╚"  # Bottom left
    BR = "╝"  # Bottom right

    HB = "╤"  # Horizontal bottom
    HT = "╧"  # Horizontal top
    VL = "╢"  # Vertical left
    VR = "╟"  # Vertical right

    HV = "┼"  # Horizontal vertical


_styles = {
    "simple": StyleSimple,
    "box": StyleBox,
    "box-border": StyleBoxBorder,
}


def show(table:list[list], style="simple"):
    """
    Show a list of list as a table.
    """

    style = _styles.get(style, StyleSimple)

    def show_row(row:list):
        sep = f" {style.V} "
        line = sep.join(f"{value:>{max_len[j]}}" for j, value in enumerate(row))
        print(f"{style.BORDER_V} {line} {style.BORDER_V}")

    def show_line(left:str, middle:str, right:str, fill:str=style.H):
        sep = f"{fill}{middle}{fill}"
        line = sep.join(f"{'':{fill}>{max_len[j]}}" for j in range(len(row)))
        print(f"{left}{fill}{line}{fill}{right}")

    max_len = [0 for _ in table[0]]
    for row in table:
        for j, value in enumerate(row):
            max_len[j] = max(max_len[j], len(str(value)))

    # Top border
    show_line(style.TL, style.HB, style.TR, style.BORDER_H)
    # Header
    show_row(table.pop(0))
    show_line(style.VR, style.HV, style.VL)
    # Fill with content
    for row in table:
        show_row(row)
    # Bottom border
    show_line(style.BL, style.HT, style.BR, style.BORDER_H)


if __name__ == '__main__':
    table = [
        ["Size", "Quantity", "ID"],
        [12, 1235, 15],
        [145, "h", "hahaha"]
    ]
    show(table, "box")
