from ml_project.main import greet_ml_world


def test_greet_ml_world():
    """
    Test that the ML engine placeholder runs successfully.
    """
    message = greet_ml_world()
    assert message == "Hello World from ML Engine!"
    assert isinstance(message, str)
