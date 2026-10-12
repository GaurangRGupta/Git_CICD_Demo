def predict_label(value):
    """A tiny example function for CI testing."""
    return "positive" if value >= 0.5 else "negative"


if __name__ == "__main__":
    print("MLOps Git/CI demo")
    print("Prediction:", predict_label(0.8))
    print("Prediction:", predict_label(0.2))
