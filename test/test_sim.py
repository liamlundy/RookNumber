from rook_number.sim import Simulation


def test_sim_small(capfd):
    sim = Simulation()
    sim.run(3, 3)
    out, err = capfd.readouterr()
    print(out)

    assert out == """Now Running Rook Number Simulation for K Rooks
Rows: 3, Cols: 3

The Rook Number for a 3 x 3 board is 34
"""