import ttkbootstrap as tk


class Layout(object):
    #i-Frame
    def _Frame(
        _name,
        _root,
        _width: int,
        _height: int,
        _side: str,
        _fill: str,
        _padx: int,
        _pady: int,
        _expand: bool,
        _showinfo: bool,
    ):
        _name = tk.Frame(_root, width=_width, height=_height)
        _name.pack(side=str(_side),
                   fill=str(_fill),
                   padx=_padx,
                   pady=_pady,
                   expand=_expand)
        if _showinfo is True:
            _name.config(bootstyle='success')
        return _name

    #i-LabelFrame
    def _LableFrame(_name, _root, _text: str, _width: int, _hight: int,
                    _side: str, _fill: str, _padx: int, _pady: int,
                    _expend: bool):
        _name = tk.LabelFrame(_root,
                              text=str(_text),
                              width=_width,
                              height=_hight,
                              bootstyle='info')
        _name.pack(side=str(_side),
                   fill=str(_fill),
                   padx=_padx,
                   pady=_pady,
                   expand=_expend)
        return _name

    #i-Button
    def _Button(
        _name,
        _root,
        _text: str,
        _width: int,
        _side: str,
        _padx: int,
        _pady: int,
        *_command,
    ):
        _name = tk.Button(
            _root,
            text=str(_text),
            command=_command[0],
            width=_width,
        )
        _name.pack(side=str(_side), padx=_padx, pady=_pady)
        return _name

    #i-Entry
    def _Entry(_name,
               _root,
               _width: int,
               _side: str,
               _padx: int,
               _pady: int,
               _fontsize: int = 8):
        _name = tk.Entry(_root, width=_width, justify='center',font=(_fontsize))
        _name.pack(side=str(_side), padx=_padx, pady=_pady)
        return _name
