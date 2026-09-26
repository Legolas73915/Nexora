import builtins
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import src.inventario as inventario

def test_agregar_producto(monkeypatch):
    inputs = iter(["Lapiz", "10", "5.5"])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    inventario.agregar_producto()

    assert len(inventario.inventario) == 1
    producto = inventario.inventario[0]
    assert producto['nombre'] == 'Lapiz'
    assert producto['cantidad'] == 10
    assert producto['presio'] == 5.5

def test_buscar_produto_existente(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", lambda _: "Lapiz")

    inventario.buscar_producto()

    captured = capsys.readouterr()

    assert "Lapiz" in captured.out

def test_buscar_producto_inexistente(monkeypatch, capsys):

    monkeypatch.setattr(builtins, "input", lambda _: "Borrador")

    inventario.buscar_producto()

    captured = capsys.readouterr()

    assert "no existe" in captured.out or "esta vacio" in captured.out

