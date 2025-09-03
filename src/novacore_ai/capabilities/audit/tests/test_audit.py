from importlib import import_module


def test_smoke():
    mod = import_module(
        __name__.replace(".tests", ".contracts").replace("test_", "") + "_capability"
    )
    impl = mod.Impl()
    assert impl.supports("ping")
    assert impl.run("ping", {"x": 1})["ok"] is True
