from main import run_experiment

def test_reproducibility_same_seed_same_output():
    m1, v1 = run_experiment(seed=42, n=10_000)
    m2, v2 = run_experiment(seed=42, n=10_000)

    assert m1 == m2
    assert v1 == v2

def test_different_seed_changes_output():
    m1, v1 = run_experiment(seed=1, n=10_000)
    m2, v2 = run_experiment(seed=2, n=10_000)

    assert (m1, v1) != (m2, v2)
