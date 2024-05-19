#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

# for name in ["ccc", "cube", "box", "king", "cow"]:
tk = TkDrawer()
try:
    for name in ["test1", "test2", "test3", "test4", "test5"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        f = Polyedr(f"data/{name}.geom")
        f.draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print(f"Сумма длин рёбер с двумя «хорошими» точками - {f.g()}")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
