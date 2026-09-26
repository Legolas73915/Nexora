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
    assert producto['precio'] == 5.5

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

def test_actualizar_producto(monkeypatch):
    inventario.inventario.clear()
    inventario.inventario.append({"nombre": "Lapiz", "cantidad": 10, "precio": 5.5})

    inputs = iter(["Lapiz", "c", "20"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    inventario.actualizar_producto()
    producto = inventario.inventario[0]
    assert producto["cantidad"] == 20

    inputs = iter(["Lapiz", "p", "7.0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    inventario.actualizar_producto()
    producto = inventario.inventario[0]
    assert producto["precio"] == 7.0

def test_eliminar_producto(monkeypatch):
    inventario.inventario.clear()
    inventario.inventario.append({"nombre": "Lapiz", "cantidad": 10, "precio": 5.5})

    inputs = iter(["Lapiz"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    inventario.eliminar_producto()
    assert len(inventario.inventario) == 0

